from flask import Blueprint, render_template, request
from app.services.prompt_lm_studio import (
    prompt_lm_studio_web_page,
    prompt_lm_studio_document,
)
from app.services.openai_api import getClient
from app.services.prompt_wrapper import get_web_page_prompt
import os
import time
import uuid


web_bp = Blueprint("web", __name__)


# Home
@web_bp.route("/")
def index():
    return render_template("index.html")


# =========================
# DOCUMENT
# =========================

# Document upload page
@web_bp.route("/file")
def file_page():
    return render_template(
        "file.html",
        models=getClient().models.list().data
    )


# Process uploaded PDF/image
@web_bp.route("/file", methods=["POST"])
def process_file():

    model = request.form.get("model")
    message = request.form.get("message")

    uploaded_file = request.files.get("file")

    if uploaded_file is None:
        return {
            "error": "No file was uploaded"
        }, 400

    if uploaded_file.filename == "":
        return {
            "error": "No file was selected"
        }, 400

    allowed_extensions = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
        ".tiff",
        ".bmp",
    }

    filename = uploaded_file.filename
    extension = os.path.splitext(filename)[1].lower()

    if extension not in allowed_extensions:
        return {
            "error": f"Unsupported file type: {extension}"
        }, 400

    upload_dir = "/tmp/ocr-mcp"
    os.makedirs(upload_dir, exist_ok=True)

    temp_filename = f"{uuid.uuid4()}{extension}"
    file_path = os.path.join(upload_dir, temp_filename)

    uploaded_file.save(file_path)

    try:

        start = time.perf_counter()

        choices = prompt_lm_studio_document(
            file_path=file_path,
            message=message,
            model=model,
        )

        return {
            "filename": filename,
            "choices": choices,
            "time": time.perf_counter() - start,
        }

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)


# =========================
# WEB
# =========================

# Web page
@web_bp.route("/web")
def web_page():
    return render_template(
        "web.html",
        models=getClient().models.list().data
    )


# Process web page
@web_bp.route("/web", methods=["POST"])
def scrape_web_page():

    model = request.form.get("model")
    message = request.form.get("message")
    url = request.form.get("url")

    start = time.perf_counter()

    choices = prompt_lm_studio_web_page(
        get_web_page_prompt(
            url=url,
            message=message,
        ),
        model=model,
    )

    return {
        "choices": choices,
        "time": time.perf_counter() - start,
    }