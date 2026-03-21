import os
import json
from dotenv import load_dotenv  
from groq import AsyncGroq 

load_dotenv() 

client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    timeout=300.0, 
    max_retries=5
)

async def generate_answer(context, user_query):
    system_prompt = """
   You are a Lead Intelligence Specialist. Analyze the provided context and return structured JSON ONLY.

CRITICAL RULES:
- If data is older than 6 months or missing, set 'confidence_score' below 40.
- Extract the "Source" URL if it follows the ' | Source: ' tag; otherwise, return "Unknown".
- Ensure 'pitch_angle' is tailored specifically for a [User Niche] freelancer.
- No conversational text or markdown blocks (```). Return valid JSON only.

JSON SCHEMA:
{
  "startup_name": "string",
  "intent_score": 0-100,
  "hiring_signal": boolean,
  "funding_stage": "seed" | "series_a" | "series_b+" | "unknown",
  "remote_possible": boolean,
  "reasoning": "One verifiable fact supporting the score",
  "pitch_angle": "2 sentences max of outreach strategy",
  "source_url": "string",
  "confidence_score": 0-100
}

    """
    # sec prompt grk
# You are SignalScout Agent – an extremely honest, helpful research assistant for freelancers and small agencies.

# User niche: [insert user’s exact niche here]

# Task: Analyze the latest public data for this startup and decide if it is a REAL high-intent opportunity for the user.

# Rules you MUST follow:
# - ONLY use the data I give you right now (Crunchbase funding, job posts, website text, etc.). Never make anything up.
# - If data is missing or old, say “Low confidence – limited recent data” and give 0–30% score.
# - Always explain your reasoning in 3–4 short bullet points that a human can verify.
# - End with exact intent score (0–100%) and one-sentence “why this matters to the user”.
# - Never hype or use salesy language. Be direct and transparent.

# Data to analyze:
# [insert all fresh data here]

# Output format (exactly):
# Startup name:
# Intent score: XX%
# Reasoning:
# • bullet 1 (with source)
# • bullet 2
# • bullet 3
# Why this is a fit for [user niche]:
# Personalized outreach angle (2 sentences max):

    
     # old prompt here below
    # You are a startup lead intelligence AI agent.
    # Analyze the provided context and return structured JSON ONLY.

    # CRITICAL RULES:
    # - Focus ONLY on the company that matches the user's specific role request.
    # - Extract the "Source" URL if it exists in the context (it follows the ' | Source: ' tag).
    # - If no URL is found, return "Unknown".

    # You MUST include these exact keys in your JSON:
    # 1. "startup_name": (The name of the company or "Unknown")
    # 2. "hiring_signal": (true or false)
    # 3. "remote_possible": (true or false)
    # 4. "funding_stage": (e.g., "seed", "series_a", "unknown")
    # 5. "reasoning": (One sentence explaining why this company is the best lead)
    # 6. "source_url": (The URL found in the context for this specific lead)

    # Return valid JSON only.

    user_prompt = f"Context:\n{context}\n\nUser Query:\n{user_query}"

    response = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        # Try 70b-versatile for smarter reasoning, or keep 8b-instant for speed
        # model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1, 
        response_format={"type": "json_object"} 
    )

    # Note: Added [0] index to avoid the error in the logs
    return response.choices[0].message.content
