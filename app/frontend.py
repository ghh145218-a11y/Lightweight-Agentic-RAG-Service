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

st.set_page_config(
    page_title="Startup Intel AI",
    page_icon="🚀",
    layout="wide"
)

# --------- Custom CSS ----------
st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
    color:white;
}

.title{
    font-size:42px;
    font-weight:700;
}

.subtitle{
    color:#94a3b8;
    margin-bottom:25px;
}

.card{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    box-shadow:0 8px 25px rgba(0,0,0,0.4);
}

.metric{
    font-size:22px;
    font-weight:600;
}

.reason{
    background:#111827;
    padding:20px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# --------- Header ----------
st.markdown('<div class="title">🚀 Startup Lead Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Agent analyzing startup hiring signals across the web</div>', unsafe_allow_html=True)

# --------- Input ----------
query = st.text_input(
    "",
    placeholder="Search startup signals (ex: Flutter dev jobs remote...)"
)

# --------- Button ----------
if st.button("Analyze Leads"):

    if query:

        with st.spinner("🧠 AI Agent scanning signals across web + vector database..."):

            try:

                response = requests.post(
                    "https://agentic-lead-rag.onrender.com/analyze",
                    json={"text": query}
                )

                data = response.json()

                if response.status_code == 200:

                    analysis = data["analysis"]

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.markdown(
                            f"""
                            <div class="card">
                            <div class="metric">Startup</div>
                            {analysis.get("startup_name","Unknown")}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col2:

                        funding = analysis.get("funding_stage","N/A")

                        st.markdown(
                            f"""
                            <div class="card">
                            <div class="metric">Funding Stage</div>
                            {funding}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col3:

                        hiring = "High Signal ✅" if analysis.get("hiring_signal") else "Low Signal ❌"

                        st.markdown(
                            f"""
                            <div class="card">
                            <div class="metric">Hiring Signal</div>
                            {hiring}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown("<br>", unsafe_allow_html=True)

                    # Reasoning block
                    st.markdown(
                        f"""
                        <div class="reason">
                        <b>AI Reasoning</b><br><br>
                        {analysis.get("reasoning")}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if analysis.get("source_url") and analysis["source_url"] != "Unknown":
                        st.link_button("🔎 View Source", analysis["source_url"])

                    with st.expander("🔍 See Retrieved Context"):
                        for chunk in data["context_used"]:
                            st.write(chunk)

                else:
                    st.error(data.get("detail","Unknown error"))

            except Exception as e:
                st.error(f"Backend connection failed: {e}")

    else:
        st.warning("Please enter a search query.")
