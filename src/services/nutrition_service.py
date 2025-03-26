import requests
import logging
from src.config.base_config import Config
from src.services.vision_service import VisionService

logger = logging.getLogger(__name__)

class NutritionService:
    def __init__(self):
        self.api_url = Config.EDAMAM_API_URL
        self.app_id = Config.EDAMAM_APP_ID
        self.app_key = Config.EDAMAM_APP_KEY
        self.vision_service = VisionService()

    def analyze_recipe(self, file_path):
        try:
            ingredients = self.vision_service.detect_fruit(file_path)
            if "error" in ingredients:
                return ingredients

            valid_foods = ingredients["ingr"]
            if not valid_foods:
                return {"error": "No valid ingredients detected"}

            logger.info(f"?? Sending ingredients to Edamam API: {valid_foods}")
            
            params = {
                "app_id": self.app_id,
                "app_key": self.app_key,
                "ingr": valid_foods
            }

            response = requests.get(self.api_url, params=params)
            if response.status_code != 200:
                logger.error(f"? Edamam API Error {response.status_code}: {response.text}")
                return {"error": "Failed to fetch data from Edamam API"}

            result = response.json()
            nutrients = result.get("totalNutrients", {})

            return {
                "food_items": valid_foods,
                "calories(Kcal)": result.get("calories", 0),
                "carbs(g)": nutrients.get("CHOCDF", {}).get("quantity", 0),
                "protein(g)": nutrients.get("PROCNT", {}).get("quantity", 0),
                "fats(g)": nutrients.get("FAT", {}).get("quantity", 0)
            }
        except Exception as e:
            logger.error(f"?? Error in analyze_recipe: {e}")
            return {"error": str(e)}
