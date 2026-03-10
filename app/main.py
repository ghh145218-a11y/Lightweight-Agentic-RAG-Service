import os
import json
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from app.schemas import AnalyzeRequest, AnalyzeResponse 
from app.services.llm_service import generate_answer
from app.services.retrieval_service import RetrieverService
from app.services.search_service import SearchService 

# 1. Setup Logging (Must be BEFORE you use 'logger')
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# 2. Environment Validation
load_dotenv()
if not os.getenv("GROQ_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    logger.warning("CRITICAL: API keys missing. Check GROQ_API_KEY and TAVILY_API_KEY")

app = FastAPI(title="Agentic Lead RAG")

# 3. Services (KEEP COMMENTED FOR FIRST DEPLOY)
# retriever = RetrieverService()
web_search = SearchService()

@app.get("/")
def home():
    return {"message": "Agentic Lead Intelligence API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    logger.info("--- New Agentic Request Received ---")
    
    try:
        # These will fail if services are commented out, but we just need the app to START
        local_chunks = retriever.retrieve(request.text, k=3)
        web_chunks = web_search.search_leads(request.text)
        
        all_chunks = local_chunks + web_chunks
        context = "\n".join(all_chunks)

        raw_answer = await generate_answer(context, request.text)
        parsed_answer = json.loads(raw_answer)
        
        return {
            "question": request.text,
            "context_used": all_chunks,
            "analysis": parsed_answer
        }

    except Exception as e:
        logger.error(f"Agent Error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=422, detail=f"Data error: {str(e)}")
