from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import main
import os

app = FastAPI(
    title="Customer Support CrewAI API",
    description="API for processing customer support inquiries using CrewAI",
    version="1.0.0"
)

# Mount static files directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


class SupportInquiry(BaseModel):
    customer: str
    person: str
    inquiry: str


class SupportResponse(BaseModel):
    success: bool
    response: Optional[str] = None
    error: Optional[str] = None


@app.get("/")
async def root():
    """Serve the web UI."""
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {
        "message": "Customer Support CrewAI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "support": "/support/inquiry"
        }
    }


@app.get("/api")
async def api_info():
    """API information endpoint."""
    return {
        "message": "Customer Support CrewAI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "support": "/support/inquiry"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "customer-support-crewai"}


@app.post("/support/inquiry", response_model=SupportResponse)
async def process_inquiry(inquiry: SupportInquiry):
    """
    Process a customer support inquiry.
    
    - **customer**: Name of the customer company
    - **person**: Name of the person making the inquiry
    - **inquiry**: The customer's question or request
    """
    try:
        result = main.process_support_inquiry(
            customer=inquiry.customer,
            person=inquiry.person,
            inquiry=inquiry.inquiry
        )
        
        # Extract the response text from the result
        response_text = str(result)
        if hasattr(result, 'raw'):
            response_text = str(result.raw)
        elif hasattr(result, 'content'):
            response_text = str(result.content)
        
        return SupportResponse(
            success=True,
            response=response_text
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing inquiry: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

