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

# 2
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

# 3
# import streamlit as st
# import requests

# # Set standard page config (removed the emoji icon)
# st.set_page_config(
#     page_title="Startup Intel AI",
#     layout="wide"
# )

# # ---------------- HEADER ----------------
# # Here is the magnificent line-art rocket SVG!
# magnificent_rocket = """
# <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" 
# stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#     <path d="M4 13a8 10 0 0 1 7 7a6 6 0 0 0 3 -5a9 9 0 0 0 6 -8a3 3 0 0 0 -3 -3a9 9 0 0 0 -8 6a6 6 0 0 0 -5 3"></path>
#     <path d="M7 14a6 6 0 0 0 -3 6a6 6 0 0 0 6 -3"></path>
#     <circle cx="15" cy="9" r="1.5"></circle>
# </svg>
# """

# st.markdown(
#     f"""
#     <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 5px;">
#         {magnificent_rocket}
#         <h1 style="margin: 0; padding: 0;">Startup Lead Intelligence</h1>
#     </div>
#     <p style="color: #64748b; font-size: 1.1em; margin-top: 0; margin-bottom: 30px;">
#         AI agent discovering startup hiring signals across the web
#     </p>
#     """,
#     unsafe_allow_html=True
# )

# # ---------------- SEARCH BOX ----------------
# query = st.text_input(
#     "Search Query",
#     label_visibility="collapsed",
#     placeholder="Search startup signals (example: Flutter developers remote)"
# )

# analyze = st.button("Analyze Leads", type="primary", use_container_width=True)
# st.markdown("<br>", unsafe_allow_html=True)

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

#                     # Native Streamlit metrics for a clean, bug-free layout
#                     col1, col2, col3, col4 = st.columns(4)

#                     with col1:
#                         st.metric(label="🏢 Startup", value=analysis.get("startup_name", "Unknown"))
#                     with col2:
#                         st.metric(label="💰 Funding", value=analysis.get("funding_stage", "N/A"))
#                     with col3:
#                         signal = "High" if analysis.get("hiring_signal") else "Low"
#                         st.metric(label="📡 Hiring Signal", value=signal)
#                     with col4:
#                         remote = "Yes" if analysis.get("remote_possible") else "No"
#                         st.metric(label="🌍 Remote", value=remote)

#                     st.divider()

#                     # AI reasoning section
#                     st.subheader("🤖 AI Reasoning")
#                     st.write(analysis.get("reasoning"))

#                     st.markdown("<br>", unsafe_allow_html=True)

#                     if analysis.get("source_url") and analysis["source_url"] != "Unknown":
#                         st.link_button("Open Source", analysis["source_url"])

#                     with st.expander("Retrieved Context"):
#                         for chunk in data["context_used"]:
#                             st.write(chunk)

#                 else:
#                     st.error(data.get("detail", "Unknown error"))

#             except Exception as e:
#                 st.error(f"Backend connection failed: {e}")

#     else:
#         st.warning("Please enter a search query before clicking analyze.")

# 4
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


# 5
import streamlit as st
import requests

# Set standard page config (removed the emoji icon)
st.set_page_config(
    page_title="Lead Intel AI",
      # layout="wide"
)

# ---------------- HEADER ----------------
# Here is the magnificent line-art rocket SVG! viewBox="0 0 24 24"
rocket_icon = """
<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" width="44" height="44" style="display: block;">
    <g stroke-linecap="round" stroke-linejoin="round">
        <path d="M461.81,53.81a4.4,4.4,0,0,0-3.3-3.39c-54.38-13.3-180,34.09-248.13,102.17a294.9,294.9,0,0,0-33.09,39.08c-21-1.9-42-.3-59.88,7.5-50.49,22.2-65.18,80.18-69.28,105.07a9,9,0,0,0,9.8,10.4l81.07-8.9a180.29,180.29,0,0,0,1.1,18.3,18.15,18.15,0,0,0,5.3,11.09l31.39,31.39a18.15,18.15,0,0,0,11.1,5.3,179.91,179.91,0,0,0,18.19,1.1l-8.89,81a9,9,0,0,0,10.39,9.79c24.9-4,83-18.69,105.07-69.17,7.8-17.9,9.4-38.79,7.6-59.69a293.91,293.91,0,0,0,39.19-33.09C427.82,233.76,474.91,110.9,461.81,53.81ZM298.66,213.67a42.7,42.7,0,1,1,60.38,0A42.65,42.65,0,0,1,298.66,213.67Z" fill="none" stroke="currentColor" stroke-width="32"></path>
        <path d="M109.64,352a45.06,45.06,0,0,0-26.35,12.84C65.67,382.52,64,448,64,448s65.52-1.67,83.15-19.31A44.73,44.73,0,0,0,160,402.32" fill="none" stroke="currentColor" stroke-width="32"></path>
    </g>
</svg>
"""
# """
# <svg fill="currentColor" viewBox="-1.92 -1.92 27.84 27.84" xmlns="http://www.w3.org/2000/svg" 
# stroke="currentColor" stroke-width="0.5" height="55" width="25">
#     <path fill-rule="evenodd" d="M20.322.75a10.75 10.75 0 00-7.373 2.926l-1.304 1.23A23.743 23.743 0 0010.103 6.5H5.066a1.75 1.75 0 00-1.5.85l-2.71 4.514a.75.75 0 00.49 1.12l4.571.963c.039.049.082.096.129.14L8.04 15.96l1.872 1.994c.044.047.091.09.14.129l.963 4.572a.75.75 0 001.12.488l4.514-2.709a1.75 1.75 0 00.85-1.5v-5.038a23.741 23.741 0 001.596-1.542l1.228-1.304a10.75 10.75 0 002.925-7.374V2.499A1.75 1.75 0 0021.498.75h-1.177zM16 15.112c-.333.248-.672.487-1.018.718l-3.393 2.262.678 3.223 3.612-2.167a.25.25 0 00.121-.214v-3.822zm-10.092-2.7L8.17 9.017c.23-.346.47-.685.717-1.017H5.066a.25.25 0 00-.214.121l-2.167 3.612 3.223.679zm8.07-7.644a9.25 9.25 0 016.344-2.518h1.177a.25.25 0 01.25.25v1.176a9.25 9.25 0 01-2.517 6.346l-1.228 1.303a22.248 22.248 0 01-3.854 3.257l-3.288 2.192-1.743-1.858a.764.764 0 00-.034-.034l-1.859-1.744 2.193-3.29a22.248 22.248 0 013.255-3.851l1.304-1.23zM17.5 8a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zm-11 13c.9-.9.9-2.6 0-3.5-.9-.9-2.6-.9-3.5 0-1.209 1.209-1.445 3.901-1.49 4.743a.232.232 0 00.247.247c.842-.045 3.534-.281 4.743-1.49z"></path>
# </svg>
# """

# import streamlit as st
# import requests

# st.set_page_config(page_title="Startup Intel AI", page_icon="")

# # ----------- Rocket Icon (SVG like Streamlit deploy UI) -----------

# rocket_icon = """
# <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="none"
# stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
# <path d="M4.5 16.5c-1.5 3-1.5 6 0 9l6-1.5 3 3-1.5 6c3 1.5 6 1.5 9 0l-1.5-6 3-3 6 1.5c1.5-3 1.5-6 0-9l-6 1.5-3-3 1.5-6c-3-1.5-6-1.5-9 0l1.5 6-3 3-6-1.5z"/>
# </svg>
# """

# ----------- Header with Rocket -----------

# st.markdown(
# f"""
# <div style="display:flex;align-items:center;gap:10px;">
# {rocket_icon}
# <h2 style="margin:0;">Startup Lead Intelligence</h2>
# </div>
# """,
# unsafe_allow_html=True
# )

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
