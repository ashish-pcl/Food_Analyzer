import os
import logging

logger = logging.getLogger(__name__)

def save_uploaded_file(file, upload_folder):
    """Save uploaded file and return its path."""
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    logger.info(f"File saved to: {file_path}")
    return file_path
