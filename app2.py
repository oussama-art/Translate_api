from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import MBartForConditionalGeneration, MBart50Tokenizer

app = FastAPI()

# Pydantic model for the request body
class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

# Load model and tokenizer
try:
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)
except Exception as e:
    raise RuntimeError(f"Error loading model or tokenizer: {e}")

@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        # Extract data from the request
        text = request.text
        source_lang = request.source_lang
        target_lang = request.target_lang

        # Validate input
        if not text or not source_lang or not target_lang:
            raise HTTPException(status_code=400, detail="Missing required fields: 'text', 'source_lang', or 'target_lang'.")

        # Set source language and tokenize input
        tokenizer.src_lang = source_lang
        inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

        # Generate translation
        translated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id[target_lang],
            max_length=512,
            num_beams=5
        )
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return {"translated_text": translated_text}

    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
