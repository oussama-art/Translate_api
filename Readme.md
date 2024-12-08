# FastAPI Translation Service

This is a simple translation API built using FastAPI and the Hugging Face Transformers library. It leverages the `facebook/mbart-large-50-many-to-many-mmt` model for multilingual translations.

## Features
- Translate text from one language to another using the mBART-50 model.
- Supports over 50 languages for translation.

---

## Requirements
- Python 3.8 or higher
- Required Python packages:
  - `fastapi`
  - `uvicorn`
  - `transformers`
  - `pydantic`

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/fastapi-translation-service.git
   cd fastapi-translation-service

2. **Set Up a Virtual Environment**
    ```bash 
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
3. **Install Dependencies**
    pip install -r requirements.txt

4. **Run the Server**
    uvicorn server:app --host 0.0.0.0 --port 8000

5. **Access the API**
    Go to http://127.0.0.1:8000/docs to explore the API documentation.

6. **Explanation of Dependencies:**
    fastapi: For building the REST API.
    uvicorn: ASGI server for running FastAPI.
    transformers: For loading the facebook/mbart-large-50-many-to-many-mmt model.
    pydantic: For data validation and parsing.
    torch: Required backend for running the mBART model. Ensure it is compatible with your environment.