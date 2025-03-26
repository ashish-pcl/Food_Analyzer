import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "../../static/uploads")
    EDAMAM_API_URL = "https://api.edamam.com/api/nutrition-analysis"
    EDAMAM_APP_ID = os.getenv("EDAMAM_APP_ID")
    EDAMAM_APP_KEY = os.getenv("EDAMAM_APP_KEY")
    GCP_CREDENTIALS = {
        # Your Google Cloud credentials dictionary here
    }
