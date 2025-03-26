from flask import request, jsonify, render_template
from src.services.nutrition_service import NutritionService
from src.utils.file_handler import save_uploaded_file
import logging

logger = logging.getLogger(__name__)

def init_routes(app):
    nutrition_service = NutritionService()

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["POST"])
    def upload():
        try:
            if "file" not in request.files:
                return jsonify({"error": "No file uploaded"}), 400
                
            file = request.files["file"]
            if file.filename == "":
                return jsonify({"error": "No selected file"}), 400
                
            file_path = save_uploaded_file(file, app.config["UPLOAD_FOLDER"])
            if not file.content_type.startswith('image'):
                return jsonify({"error": "Uploaded file is not an image"}), 400
                
            nutrition_info = nutrition_service.analyze_recipe(file_path)
            return jsonify(nutrition_info)
            
        except Exception as e:
            logger.error(f"Error in upload endpoint: {e}")
            return jsonify({"error": str(e)}), 500
