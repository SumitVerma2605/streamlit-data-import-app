from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse
import pandas as pd
import os
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/file")
async def upload_file(file: UploadFile = File(...)):
    """Upload CSV or Excel file"""
    try:
        # Validate file type
        allowed_extensions = ['.csv', '.xlsx', '.xls']
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File type not allowed. Allowed: {allowed_extensions}"
            )
        
        # Read file
        contents = await file.read()
        
        # Parse based on extension
        if file_ext == '.csv':
            df = pd.read_csv(pd.io.common.BytesIO(contents))
        else:
            df = pd.read_excel(pd.io.common.BytesIO(contents))
        
        # Generate unique ID
        file_id = str(uuid.uuid4())
        
        # Get data profile
        profile = {
            "file_id": file_id,
            "original_name": file.filename,
            "file_size": len(contents),
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "column_types": {col: str(dtype) for col, dtype in zip(df.columns, df.dtypes)},
            "missing_values": df.isnull().sum().to_dict(),
            "duplicates": int(df.duplicated().sum()),
            "uploaded_at": datetime.utcnow().isoformat()
        }
        
        logger.info(f"✅ File uploaded: {file_id} - {file.filename}")
        
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=profile
        )
        
    except Exception as e:
        logger.error(f"❌ Upload error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/status/{file_id}")
async def get_upload_status(file_id: str):
    """Get upload status"""
    return {
        "file_id": file_id,
        "status": "completed",
        "message": "File processed successfully"
    }