import os
import json
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from app.schemas import AnalyzeRequest, AnalyzeResponse 
from app.services.llm_service import generate_answer
from app.services.retrieval_service import RetrieverService
from app.services.search_service import SearchService  # 1. Import Search

# 1. Environment Validation
load_dotenv()
if not os.getenv("GROQ_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    raise RuntimeError("CRITICAL: API keys missing. Check GROQ_API_KEY and TAVILY_API_KEY")

# 2. Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Agentic Lead RAG")
retriever = RetrieverService()
web_search = SearchService()  # 2. Initialize Search Agent

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    logger.info("--- New Agentic Request Received ---")
    
    try:
        # 3. Step A: Local Retrieval (FAISS)
        local_chunks = retriever.retrieve(request.text, k=3)
        logger.info(f"FAISS found {len(local_chunks)} local leads")

        # 4. Step B: Live Web Search (Reddit/X/LinkedIn)
        logger.info("Searching live web for fresh signals...")
        web_chunks = web_search.search_leads(request.text)
        logger.info(f"Tavily found {len(web_chunks)} live web results")

        # 5. Combine Context
        all_chunks = local_chunks + web_chunks
        context = "\n".join(all_chunks)

        # 6. LLM Generation Step
        logger.info("Sending combined context to Groq...")
        raw_answer = await generate_answer(context, request.text)

        # 7. Parsing and Validation
        parsed_answer = json.loads(raw_answer)
        
        return {
            "question": request.text,
            "context_used": all_chunks,
            "analysis": parsed_answer
        }

    except json.JSONDecodeError:
        logger.error(f"Groq JSON Error: {raw_answer}")
        raise HTTPException(status_code=502, detail="AI returned invalid JSON format")
    except Exception as e:
        logger.error(f"Agent Error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=422, detail=f"Data error: {str(e)}")
