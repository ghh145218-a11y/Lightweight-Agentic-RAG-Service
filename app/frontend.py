# import streamlit as st
# import requests
# import json

# st.set_page_config(page_title="Startup Intel AI", page_icon="🚀")

# st.title("🚀 Startup Lead Intelligence")
# st.markdown("Analyze local signals and live web data (Reddit/X/LinkedIn) in real-time.")

# query = st.text_input("Enter a search (e.g., 'React developers in London'):", placeholder="Flutter jobs remote...")

# if st.button("Analyze Leads"):
#     if query:
#         with st.spinner("Agent is searching local FAISS and Live Web..."):
#             try:
#                 # This talks to your FastAPI Docker container
#                 response = requests.post("https://agentic-lead-rag.onrender.com/analyze", 
#                     json={"text": query}
#                 )
#                 data = response.json()
                
#                 if response.status_code == 200:
#                     analysis = data["analysis"]
                    
#                     # Dashboard Layout
#                     col1, col2 = st.columns(2)
#                     with col1:
#                         st.metric("Startup", analysis.get("startup_name", "Unknown"))
#                         st.write(f"**Funding:** {analysis.get('funding_stage', 'N/A')}")
                    
#                     with col2:
#                         signal = "✅ High" if analysis.get("hiring_signal") else "❌ Low"
#                         st.write(f"**Hiring Signal:** {signal}")
#                         st.write(f"**Remote:** {'🌐 Yes' if analysis.get('remote_possible') else '📍 No'}")

#                     st.info(f"**Reasoning:** {analysis.get('reasoning')}")
                    
#                     if analysis.get("source_url") and analysis["source_url"] != "Unknown":
#                         st.link_button("Go to Source", analysis["source_url"])
                    
#                     with st.expander("See Raw Context Used"):
#                         for chunk in data["context_used"]:
#                             st.write(f"- {chunk}")
#                 else:
#                     st.error(f"Error: {data.get('detail', 'Unknown error')}")
#             except Exception as e:
#                 st.error(f"Could not connect to Backend: {e}")
#     else:
#         st.warning("Please enter a query first.")


import streamlit as st
import requests

# 1. Page Config with Dark Theme Vibes
st.set_page_config(
    page_title="Kloiai | Agentic Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium CSS Injection
st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Input Box Styling */
    .stTextInput>div>div>input {
        background-color: #1A1C23;
        color: white;
        border: 1px solid #30363D;
        border-radius: 10px;
    }
    
    /* Card-like containers */
    div[data-testid="stMetricValue"] { font-size: 24px; color: #00FFA3; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    
    /* Custom Lead Card */
    .lead-card {
        background-color: #161B22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True) # FIXED THIS LINE

# 3. Header Section
st.title("⚡ Kloiai Agentic Intel")
st.caption("Strategic Lead Generation via RAG & Real-Time Web Intelligence")
st.divider()

# 4. Search Bar with a clean layout
col_a, col_b = st.columns([4, 1])
with col_a:
    query = st.text_input("", placeholder="Enter target (e.g. 'Fintech startups in New York hiring Flutter devs')...", label_visibility="collapsed")
with col_b:
    analyze_btn = st.button("Generate Intelligence", use_container_width=True)

if analyze_btn:
    if query:
        with st.status("🔍 Agent initializing...", expanded=True) as status:
            try:
                st.write("Checking local FAISS clusters...")
                st.write("Scanning Tavily Web Index...")
                
                response = requests.post(
                    "https://agentic-lead-rag.onrender.com/analyze", 
                    json={"text": query},
                    timeout=60
                )
                
                if response.status_code == 200:
                    status.update(label="✅ Intelligence Gathered", state="complete", expanded=False)
                    data = response.json()
                    analysis = data["analysis"]
                    
                    # --- PREMIUM DASHBOARD UI ---
                    st.subheader("🎯 Primary Target Found")
                    
                    # Top Stats Row
                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("Organization", analysis.get("startup_name", "N/A"))
                    m2.metric("Hiring Signal", "High ✅" if analysis.get("hiring_signal") else "Low ❌")
                    m3.metric("Remote", "Global 🌐" if analysis.get("remote_possible") else "Local 📍")
                    m4.metric("Stage", analysis.get("funding_stage", "Seed/Unknown"))

                    # Intelligence Brief Box
                    st.markdown("### 💡 Agent Reasoning")
                    st.info(analysis.get("reasoning", "No specific reasoning provided."))

                    # Action and Source
                    c1, c2 = st.columns([1, 3])
                    with c1:
                        if analysis.get("source_url") and analysis["source_url"] != "Unknown":
                            st.link_button("Open Source Signal", analysis["source_url"], use_container_width=True)
                    
                    # Expandable Context
                    with st.expander("🛠️ Raw Data & Context Chunks"):
                        for i, chunk in enumerate(data["context_used"]):
                            st.markdown(f"**Source {i+1}:** {chunk}")
                
                else:
                    st.error(f"Backend Offline: {response.status_code}")
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter a target query.")

# 5. Footer Sidebar (Optional branding)
with st.sidebar:
    st.title("Kloiai Pro")
    st.write("V 0.1.0-Docker")
    st.write("Powered by Groq Llama-3 & Tavily")
