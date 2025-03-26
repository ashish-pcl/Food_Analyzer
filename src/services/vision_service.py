from collections import Counter
from google.cloud import vision
from google.oauth2 import service_account
import logging
from src.config.base_config import Config

logger = logging.getLogger(__name__)

class VisionService:
    def __init__(self):
        self.client = self._authenticate()

    def _authenticate(self):
        """Authenticate with Google Cloud Vision API."""
        credentials = service_account.Credentials.from_service_account_info(
            Config.GCP_CREDENTIALS
        )
        return vision.ImageAnnotatorClient(credentials=credentials)

    def detect_fruit(self, file_path):
        """Detects food items from an image using Google Vision API."""
        try:
            with open(file_path, 'rb') as image_file:
                content = image_file.read()
            
            image = vision.Image(content=content)
            response = self.client.object_localization(image=image)

            if response.error.message:
                logger.error(f"Google Vision API Error: {response.error.message}")
                return {"error": f"API Error: {response.error.message}"}

            food_items = [obj.name.lower() for obj in response.localized_object_annotations]
            food_count = Counter(food_items)

            ignored_items = {"tableware", "bowl", "plate", "dish"}
            filtered_items = {food: count for food, count in food_count.items() 
                           if food not in ignored_items}

            food_name_correction = {
                "french fries": "fries",
                "chips": "potato chips"
            }
            corrected_items = {food_name_correction.get(food, food): count 
                            for food, count in filtered_items.items()}

            if not corrected_items:
                return {"error": "No valid food items detected"}

            return {"ingr": [f"{count} {food}" for food, count in corrected_items.items()]}

        except Exception as e:
            logger.error(f"Error in detect_fruit: {e}")
            return {"error": str(e)}
