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


# import streamlit as st
# import requests

# # 1. Page Config with Dark Theme Vibes
# st.set_page_config(
#     page_title="Kloiai | Agentic Intelligence",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # 2. Premium CSS Injection
# st.markdown("""
#     <style>
#     /* Main Background and Text */
#     .stApp { background-color: #0E1117; color: #FFFFFF; }
    
#     /* Input Box Styling */
#     .stTextInput>div>div>input {
#         background-color: #1A1C23;
#         color: white;
#         border: 1px solid #30363D;
#         border-radius: 10px;
#     }
    
#     /* Card-like containers */
#     div[data-testid="stMetricValue"] { font-size: 24px; color: #00FFA3; }
#     .reportview-container .main .block-container { padding-top: 2rem; }
    
#     /* Custom Lead Card */
#     .lead-card {
#         background-color: #161B22;
#         padding: 20px;
#         border-radius: 15px;
#         border: 1px solid #30363D;
#         margin-bottom: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True) # FIXED THIS LINE

# # 3. Header Section
# st.title("⚡ Kloiai Agentic Intel")
# st.caption("Strategic Lead Generation via RAG & Real-Time Web Intelligence")
# st.divider()

# # 4. Search Bar with a clean layout
# col_a, col_b = st.columns([4, 1])
# with col_a:
#     query = st.text_input("", placeholder="Enter target (e.g. 'Fintech startups in New York hiring Flutter devs')...", label_visibility="collapsed")
# with col_b:
#     analyze_btn = st.button("Generate Intelligence", use_container_width=True)

# if analyze_btn:
#     if query:
#         with st.status("🔍 Agent initializing...", expanded=True) as status:
#             try:
#                 st.write("Checking local FAISS clusters...")
#                 st.write("Scanning Tavily Web Index...")
                
#                 response = requests.post(
#                     "https://agentic-lead-rag.onrender.com/analyze", 
#                     json={"text": query},
#                     timeout=60
#                 )
                
#                 if response.status_code == 200:
#                     status.update(label="✅ Intelligence Gathered", state="complete", expanded=False)
#                     data = response.json()
#                     analysis = data["analysis"]
                    
#                     # --- PREMIUM DASHBOARD UI ---
#                     st.subheader("🎯 Primary Target Found")
                    
#                     # Top Stats Row
#                     m1, m2, m3, m4 = st.columns(4)
#                     m1.metric("Organization", analysis.get("startup_name", "N/A"))
#                     m2.metric("Hiring Signal", "High ✅" if analysis.get("hiring_signal") else "Low ❌")
#                     m3.metric("Remote", "Global 🌐" if analysis.get("remote_possible") else "Local 📍")
#                     m4.metric("Stage", analysis.get("funding_stage", "Seed/Unknown"))

#                     # Intelligence Brief Box
#                     st.markdown("### 💡 Agent Reasoning")
#                     st.info(analysis.get("reasoning", "No specific reasoning provided."))

#                     # Action and Source
#                     c1, c2 = st.columns([1, 3])
#                     with c1:
#                         if analysis.get("source_url") and analysis["source_url"] != "Unknown":
#                             st.link_button("Open Source Signal", analysis["source_url"], use_container_width=True)
                    
#                     # Expandable Context
#                     with st.expander("🛠️ Raw Data & Context Chunks"):
#                         for i, chunk in enumerate(data["context_used"]):
#                             st.markdown(f"**Source {i+1}:** {chunk}")
                
#                 else:
#                     st.error(f"Backend Offline: {response.status_code}")
#             except Exception as e:
#                 st.error(f"Connection Error: {e}")
#     else:
#         st.warning("Please enter a target query.")

# # 5. Footer Sidebar (Optional branding)
# with st.sidebar:
#     st.title("Kloiai Pro")
#     st.write("V 0.1.0-Docker")
#     st.write("Powered by Groq Llama-3 & Tavily")


import streamlit as st
import requests

# Set standard page config
st.set_page_config(
    page_title="Startup Intel AI",
    layout="wide",
    page_icon="🚀"
)

# ---------------- HEADER ----------------
# We use stroke="currentColor" so the rocket adapts to Light/Dark mode automatically
st.markdown(
    """
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 5px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" 
        stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M13.5 10.5 21 3M16 16l-3.5-3.5M10 14 3.5 20.5a2.12 2.12 0 0 0 3 3L13 17l5-5-5-5-5 5Z"/>
            <path d="M3.5 20.5 3 21"/>
        </svg>
        <h1 style="margin: 0; padding: 0;">Startup Lead Intelligence</h1>
    </div>
    <p style="color: #64748b; font-size: 1.1em; margin-top: 0; margin-bottom: 30px;">
        AI agent discovering startup hiring signals across the web
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- SEARCH BOX ----------------
query = st.text_input(
    "Search Query", # Label is hidden visually by Streamlit but good for accessibility
    label_visibility="collapsed",
    placeholder="Search startup signals (example: Flutter developers remote)"
)

# Using type="primary" gives it the standard Streamlit accent color
analyze = st.button("Analyze Leads", type="primary", use_container_width=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------- ANALYSIS ----------------
if analyze:
    if query:
        with st.spinner("AI agent scanning vector DB + live web signals..."):
            try:
                response = requests.post(
                    "https://agentic-lead-rag.onrender.com/analyze",
                    json={"text": query}
                )
                data = response.json()

                if response.status_code == 200:
                    analysis = data["analysis"]

                    # USING NATIVE STREAMLIT METRICS (No more raw HTML bugs)
                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.metric(label="🏢 Startup", value=analysis.get("startup_name", "Unknown"))
                    with col2:
                        st.metric(label="💰 Funding", value=analysis.get("funding_stage", "N/A"))
                    with col3:
                        signal = "High" if analysis.get("hiring_signal") else "Low"
                        st.metric(label="📡 Hiring Signal", value=signal)
                    with col4:
                        remote = "Yes" if analysis.get("remote_possible") else "No"
                        st.metric(label="🌍 Remote", value=remote)

                    st.divider()

                    # AI reasoning section
                    st.subheader("🤖 AI Reasoning")
                    st.write(analysis.get("reasoning"))

                    st.markdown("<br>", unsafe_allow_html=True)

                    if analysis.get("source_url") and analysis["source_url"] != "Unknown":
                        st.link_button("Open Source", analysis["source_url"])

                    with st.expander("Retrieved Context"):
                        for chunk in data["context_used"]:
                            st.write(chunk)

                else:
                    st.error(data.get("detail", "Unknown error"))

            except Exception as e:
                st.error(f"Backend connection failed: {e}")

    else:
        st.warning("Please enter a search query before clicking analyze.")


# import streamlit as st
# import requests

# st.set_page_config(
#     page_title="Startup Intel AI",
#     layout="wide"
# )

# # ---------------- ICONS (SVG) ----------------

# rocket_icon = """
# <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="none"
# stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
# <path d="M4.5 16.5c-1.5 3-1.5 6 0 9l6-1.5 3 3-1.5 6c3 1.5 6 1.5 9 0l-1.5-6 3-3 6 1.5c1.5-3 1.5-6 0-9l-6 1.5-3-3 1.5-6c-3-1.5-6-1.5-9 0l1.5 6-3 3-6-1.5z"/>
# </svg>
# """

# startup_icon = """
# <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none"
# stroke="white" stroke-width="2">
# <rect x="3" y="3" width="18" height="18" rx="2"/>
# <path d="M9 21V9h6v12"/>
# </svg>
# """

# fund_icon = """
# <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none"
# stroke="white" stroke-width="2">
# <circle cx="12" cy="12" r="10"/>
# <path d="M12 6v12M8 10h8"/>
# </svg>
# """

# signal_icon = """
# <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none"
# stroke="white" stroke-width="2">
# <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
# </svg>
# """

# remote_icon = """
# <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="none"
# stroke="white" stroke-width="2">
# <circle cx="12" cy="12" r="10"/>
# <path d="M2 12h20"/>
# </svg>
# """

# # ---------------- CSS STYLE ----------------

# st.markdown("""
# <style>

# .stApp{
# background: linear-gradient(135deg,#0f172a,#020617);
# color:white;
# }

# .title-row{
# display:flex;
# align-items:center;
# gap:15px;
# margin-bottom:10px;
# }

# .main-title{
# font-size:40px;
# font-weight:800;
# }

# .subtitle{
# color:#94a3b8;
# margin-bottom:35px;
# }

# .search-box{
# background:#0f172a;
# padding:30px;
# border-radius:18px;
# box-shadow:0px 10px 35px rgba(0,0,0,0.6);
# margin-bottom:40px;
# }

# .card{
# background:#0f172a;
# padding:25px;
# border-radius:16px;
# box-shadow:0 8px 30px rgba(0,0,0,0.6);
# text-align:center;
# }

# .metric-title{
# color:#94a3b8;
# font-size:14px;
# margin-top:8px;
# }

# .metric-value{
# font-size:22px;
# font-weight:700;
# margin-top:5px;
# }

# .reason{
# background:#020617;
# padding:25px;
# border-radius:14px;
# border:1px solid #1e293b;
# }

# .stButton>button{
# width:100%;
# background:linear-gradient(90deg,#6366f1,#8b5cf6);
# color:white;
# border-radius:12px;
# font-weight:600;
# padding:12px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- HEADER ----------------

# st.markdown(
# f"""
# <div class="title-row">
# {rocket_icon}
# <div class="main-title">Startup Lead Intelligence</div>
# </div>
# <div class="subtitle">
# AI agent discovering startup hiring signals across the web
# </div>
# """,
# unsafe_allow_html=True
# )

# # ---------------- SEARCH BOX ----------------

# st.markdown('<div class="search-box">', unsafe_allow_html=True)

# query = st.text_input(
# "",
# placeholder="Search startup signals (example: Flutter developers remote)"
# )

# analyze = st.button("Analyze Leads")

# st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- ANALYSIS ----------------

# if analyze:

#     if query:

#         with st.spinner("AI agent scanning vector DB + live web signals..."):

#             try:

#                 response = requests.post(
#                     "https://agentic-lead-rag.onrender.com/analyze",
#                     json={"text": query}
#                 )

#                 data = response.json()

#                 if response.status_code == 200:

#                     analysis = data["analysis"]

#                     col1,col2,col3,col4 = st.columns(4)

#                     with col1:
#                         st.markdown(f"""
#                         <div class="card">
#                         {startup_icon}
#                         <div class="metric-title">Startup</div>
#                         <div class="metric-value">{analysis.get("startup_name","Unknown")}</div>
#                         </div>
#                         """, unsafe_allow_html=True)

#                     with col2:
#                         st.markdown(f"""
#                         <div class="card">
#                         {fund_icon}
#                         <div class="metric-title">Funding</div>
#                         <div class="metric-value">{analysis.get("funding_stage","N/A")}</div>
#                         </div>
#                         """, unsafe_allow_html=True)

#                     with col3:

#                         signal = "High" if analysis.get("hiring_signal") else "Low"

#                         st.markdown(f"""
#                         <div class="card">
#                         {signal_icon}
#                         <div class="metric-title">Hiring Signal</div>
#                         <div class="metric-value">{signal}</div>
#                         </div>
#                         """, unsafe_allow_html=True)

#                     with col4:

#                         remote = "Yes" if analysis.get("remote_possible") else "No"

#                         st.markdown(f"""
#                         <div class="card">
#                         {remote_icon}
#                         <div class="metric-title">Remote</div>
#                         <div class="metric-value">{remote}</div>
#                         </div>
#                         """, unsafe_allow_html=True)

#                     st.markdown("<br>", unsafe_allow_html=True)

#                     # AI reasoning
#                     st.markdown(
#                     f"""
#                     <div class="reason">
#                     <h4>AI Reasoning</h4>
#                     {analysis.get("reasoning")}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                     )

#                     st.markdown("<br>", unsafe_allow_html=True)

#                     if analysis.get("source_url") and analysis["source_url"] != "Unknown":
#                         st.link_button("Open Source", analysis["source_url"])

#                     with st.expander("Retrieved Context"):
#                         for chunk in data["context_used"]:
#                             st.write(chunk)

#                 else:
#                     st.error(data.get("detail","Unknown error"))

#             except Exception as e:
#                 st.error(f"Backend connection failed: {e}")

#     else:
#         st.warning("Please enter a search query.")


import streamlit as st
import requests

st.set_page_config(page_title="Startup Intel AI", page_icon="🚀")

# ----------- Rocket Icon (SVG like Streamlit deploy UI) -----------

rocket_icon = """
<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="none"
stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M4.5 16.5c-1.5 3-1.5 6 0 9l6-1.5 3 3-1.5 6c3 1.5 6 1.5 9 0l-1.5-6 3-3 6 1.5c1.5-3 1.5-6 0-9l-6 1.5-3-3 1.5-6c-3-1.5-6-1.5-9 0l1.5 6-3 3-6-1.5z"/>
</svg>
"""

# ----------- Header with Rocket -----------

st.markdown(
f"""
<div style="display:flex;align-items:center;gap:10px;">
{rocket_icon}
<h2 style="margin:0;">Startup Lead Intelligence</h2>
</div>
""",
unsafe_allow_html=True
)

st.caption("AI agent discovering startup hiring signals across the web")

st.write("")

# ----------- Search Input -----------

query = st.text_input(
    "Search leads",
    placeholder="Example: Flutter developer remote"
)

# ----------- Analyze Button -----------

if st.button("Analyze Leads"):

    if query:

        with st.spinner("AI agent scanning vector database and live web..."):

            try:

                response = requests.post(
                    "https://agentic-lead-rag.onrender.com/analyze",
                    json={"text": query}
                )

                data = response.json()

                if response.status_code == 200:

                    analysis = data["analysis"]

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.metric(
                            label="Startup",
                            value=analysis.get("startup_name", "Unknown")
                        )

                    with col2:
                        st.metric(
                            label="Funding",
                            value=analysis.get("funding_stage", "N/A")
                        )

                    with col3:

                        signal = "High" if analysis.get("hiring_signal") else "Low"

                        st.metric(
                            label="Hiring Signal",
                            value=signal
                        )

                    with col4:

                        remote = "Yes" if analysis.get("remote_possible") else "No"

                        st.metric(
                            label="Remote",
                            value=remote
                        )

                    st.write("")

                    st.info(
                        f"**AI Reasoning:** {analysis.get('reasoning')}"
                    )

                    if analysis.get("source_url") and analysis["source_url"] != "Unknown":
                        st.link_button("Open Source", analysis["source_url"])

                    with st.expander("Retrieved Context"):
                        for chunk in data["context_used"]:
                            st.write(chunk)

                else:
                    st.error(data.get("detail", "Unknown error"))

            except Exception as e:
                st.error(f"Backend connection failed: {e}")

    else:
        st.warning("Please enter a query.")
