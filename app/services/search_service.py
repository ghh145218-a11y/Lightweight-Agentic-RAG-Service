import os
from tavily import TavilyClient

class SearchService:
    def __init__(self):
        # Fallback to None if the key is missing to avoid crash on init
        self.api_key = os.getenv("TAVILY_API_KEY")
        if self.api_key:
            self.client = TavilyClient(api_key=self.api_key)
        else:
            self.client = None

    def search_leads(self, query: str):
        if not self.client:
            print("Warning: Tavily Client not initialized. Skipping web search.")
            return []

        # Focus the search on high-signal platforms
        enhanced_query = f"{query} hiring startups reddit twitter linkedin 2026"
        
        try:
            # We use 'basic' for speed as you specified
            response = self.client.search(
                query=enhanced_query, 
                search_depth="basic",
                max_results=5
            )
            
            # Format the results into strings for our RAG context
            results = []
            for res in response.get('results', []):
                results.append(f"Source: {res['url']} | Content: {res['content']}")
            return results

        except Exception as e:
            # Log the error but don't crash the whole app
            print(f"Error during Tavily search: {e}")
            return []