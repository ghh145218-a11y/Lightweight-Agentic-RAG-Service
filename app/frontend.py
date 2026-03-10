import streamlit as st
import requests
import json

st.set_page_config(page_title="Startup Intel AI", page_icon="🚀")

st.title("🚀 Startup Lead Intelligence")
st.markdown("Analyze local signals and live web data (Reddit/X/LinkedIn) in real-time.")

query = st.text_input("Enter a search (e.g., 'React developers in London'):", placeholder="Flutter jobs remote...")

if st.button("Analyze Leads"):
    if query:
        with st.spinner("Agent is searching local FAISS and Live Web..."):
            try:
                # This talks to your FastAPI Docker container
                response = requests.post("https://agentic-lead-rag.onrender.com/analyze", 
                    json={"text": query}
                )
                data = response.json()
                
                if response.status_code == 200:
                    analysis = data["analysis"]
                    
                    # Dashboard Layout
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Startup", analysis.get("startup_name", "Unknown"))
                        st.write(f"**Funding:** {analysis.get('funding_stage', 'N/A')}")
                    
                    with col2:
                        signal = "✅ High" if analysis.get("hiring_signal") else "❌ Low"
                        st.write(f"**Hiring Signal:** {signal}")
                        st.write(f"**Remote:** {'🌐 Yes' if analysis.get('remote_possible') else '📍 No'}")

                    st.info(f"**Reasoning:** {analysis.get('reasoning')}")
                    
                    if analysis.get("source_url") and analysis["source_url"] != "Unknown":
                        st.link_button("Go to Source", analysis["source_url"])
                    
                    with st.expander("See Raw Context Used"):
                        for chunk in data["context_used"]:
                            st.write(f"- {chunk}")
                else:
                    st.error(f"Error: {data.get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Could not connect to Backend: {e}")
    else:
        st.warning("Please enter a query first.")
