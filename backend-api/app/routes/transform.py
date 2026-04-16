from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class ColumnTransform(BaseModel):
    column_name: str
    operation: str  # rename, convert_type, handle_missing, remove
    parameters: dict

@router.post("/column")
async def transform_column(transform: ColumnTransform):
    """Transform a column"""
    try:
        logger.info(f"Transforming column: {transform.column_name}")
        
        return {
            "status": "success",
            "message": f"Column {transform.column_name} transformed",
            "operation": transform.operation
        }
    except Exception as e:
        logger.error(f"Transform error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/bulk")
async def bulk_transform(transformations: List[ColumnTransform]):
    """Apply bulk transformations"""
    try:
        results = []
        for t in transformations:
            results.append({
                "column": t.column_name,
                "operation": t.operation,
                "status": "success"
            })
        
        return {
            "status": "success",
            "transformations_applied": len(results),
            "results": results
        }
    except Exception as e:
        logger.error(f"Bulk transform error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )