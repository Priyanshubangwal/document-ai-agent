from fastapi import FastAPI, UploadFile, File, HTTPException
from preprocessing import preprocess_image
from ocr_engine import extract_text

app = FastAPI(title="Document AI Agent - Phase 1")

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Only image files are supported in Phase 1.")
    
    try:
        # Read file bytes
        image_bytes = await file.read()
        
        # Step 1: Preprocess the image (OpenCV)
        cleaned_image = preprocess_image(image_bytes)
        
        # Step 2: Extract text (Tesseract OCR)
        text = extract_text(cleaned_image)
        
        # Step 3: Return structured JSON output
        return {
            "filename": file.filename,
            "status": "success",
            "extracted_text": text
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))