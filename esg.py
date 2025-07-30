import streamlit as st
import pandas as pd
import numpy as np

# ----- CONFIGURATION -----
st.set_page_config(
    page_title="Season ESG Analysis",
    page_icon="🌱",  # Use your professional logo here if available
    layout="wide",
)

# ----- HEADER & BRANDING -----
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("https://your-logo-url.com/logo.png", width=70)  # Replace with your logo
with col2:
    st.markdown(
        '<h1 style="color:#254441;font-family:sans-serif;">Season ESG Analysis</h1>',
        unsafe_allow_html=True
    )
    st.caption(
        "Comprehensive and professional ESG insights for Indian companies and the Nifty 50 benchmark."
    )
st.markdown("---")

# ----- HELPER FUNCTIONS -----
def color_score(val):
    # Apply color coding: <25 Red, 25-50 Orange/Yellow, 50-75 GreenYellow, >75 Green.
    if val >= 75:
        color = "#51bd6b"  # Green
    elif val >= 50:
        color = "#b5e07a"  # Light green/yellow
    elif val >= 25:
        color = "#fdc13c"  # Orange/yellow
    else:
        color = "#e2574c"  # Red
    return f"background-color: {color}"

def esg_recommendation(score):
    if score >= 75:
        return "Excellent ESG practices. Keep up with disclosures and innovation."
    elif score >= 50:
        return "Good performance. Scope to lead with targeted improvements."
    elif score >= 25:
        return "Below average. Focus on risk mitigation and better reporting."
    else:
        return "High ESG risk. Prioritize improvements in all ESG domains."

def sector_recommendation(sector_score):
    if sector_score > 70:
        return "Sector is an ESG leader, well-aligned with regulatory and investor expectations."
    elif sector_score > 50:
        return "Sector making good progress, but must innovate on governance and environment."
    elif sector_score > 30:
        return "Sector lags on ESG, urgent improvements in transparency and social practices needed."
    else:
        return "Sector at high ESG risk; regulatory scrutiny and divestment risk high."

# ----- FAKE DATA FOR DEMO (Replace with real data or API in production!) -----
# Sample Nifty 50 ESG Data: In production, fetch current data (see [2] for source)
nifty_companies = [
    "Reliance Industries", "HDFC Bank", "Bharti Airtel", "TCS", "ICICI Bank", "SBI", "Infosys", "Hindustan Unilever",
    "LIC", "Bajaj Finance", "Sun Pharma", "HCL Tech", "Mahindra & Mahindra", "Maruti Suzuki", "UltraTech Cement",
    "Axis Bank", "NTPC", "Bajaj Finserv", "ONGC", "Adani Ports"
]
np.random.seed(42)
nifty_esg_scores = np.random.randint(20, 95, size=20)
nifty_sectors = [
    "Oil & Gas", "Banking", "Telecom", "IT", "Banking", "Banking", "IT", "FMCG", "Insurance", "Finance", "Healthcare",
    "IT", "Automobile", "Automobile", "Construction", "Banking", "Power", "Finance", "Oil & Gas", "Infrastructure"
]
nifty_data = pd.DataFrame({
    "Company": nifty_companies,
    "Sector": nifty_sectors,
    "ESG Score": nifty_esg_scores,
    "Recommendation": [esg_recommendation(s) for s in nifty_esg_scores]
})

# ---- TAB 1: Nifty 50 Analysis ----
tab1, tab2, tab3, tab4 = st.tabs([
    "🏢 Nifty 50 Analysis",
    "📊 Company Comparison",
    "📈 General Analysis",
    "📱 Market Trends"
])

with tab1:
    st.header("Nifty 50: ESG Performance (Top 20 Companies)")
    st.markdown(
        "Comprehensive ESG rankings of major Indian companies based on the latest available data."
    )
    st.dataframe(
        nifty_data.style.applymap(color_score, subset=['ESG Score'])
    )
    top_performers = nifty_data[nifty_data["ESG Score"] > 70]
    st.markdown(f"""
        <b>Top Performers</b>: {', '.join(top_performers['Company'].tolist())}<br>
        <b>Median ESG Score</b>: {nifty_data['ESG Score'].median()}<br>
        <b>Areas for Improvement</b>: {', '.join(nifty_data[nifty_data['ESG Score'] < 40]['Company'].tolist())}
    """, unsafe_allow_html=True)

# ---- TAB 2: Company Comparison ----
with tab2:
    st.header("Company vs. Nifty 50 ESG Benchmark")
    st.write("Upload your company's ESG data for a personalized benchmark comparison against Nifty 50 companies.")
    uploaded_file = st.file_uploader("Upload CSV (columns: Company, ESG Score, Sector)", type=["csv"])
    if uploaded_file:
        user_data = pd.read_csv(uploaded_file)
        merged = user_data.merge(nifty_data[["Company", "ESG Score", "Sector"]], on="Sector", suffixes=("_User", "_Nifty"))
        st.write("**Comparison Table**:")
        st.dataframe(
            merged[
                ["Company_User", "ESG Score_User", "Company_Nifty", "ESG Score_Nifty"]
            ].rename(columns={
                "Company_User": "Your Company", "ESG Score_User": "Your ESG Score",
                "Company_Nifty": "Nifty Peer", "ESG Score_Nifty": "Nifty ESG Score"
            }).style.applymap(color_score, subset=["Your ESG Score", "Nifty ESG Score"])
        )
        personalized = [esg_recommendation(sc) for sc in user_data["ESG Score"]]
        st.markdown(
            f"<b>Personalized Recommendations</b>:<br>{'<br>'.join(personalized)}",
            unsafe_allow_html=True
        )

# ---- TAB 3: General Analysis ----
with tab3:
    st.header("General ESG Portfolio Analysis")
    st.write(
        "Upload any CSV (Company, ESG Score, Sector) for detailed, multi-company ESG evaluation and professional recommendations."
    )
    data_file = st.file_uploader("Upload your ESG data (CSV)", type=["csv"], key="general_upload")
    if data_file:
        custom_df = pd.read_csv(data_file)
        st.dataframe(
            custom_df.style.applymap(color_score, subset=["ESG Score"])
        )
        summary = custom_df["ESG Score"].describe()
        st.write("**Summary Stats**:")
        st.write(summary)
        recommendations = [esg_recommendation(x) for x in custom_df["ESG Score"]]
        st.write("**Key Recommendations**:")
        st.write("\n".join(recommendations))

# ---- TAB 4: Market Trends ----
with tab4:
    st.header("Indian ESG Market Trends by Sector")
    # Simulate sector-wise ESG trends for demo
    sector_names = ["Banking", "IT", "Oil & Gas", "Automobile", "Finance", "Healthcare", "FMCG", "Infrastructure", "Power"]
    sector_scores = [60, 75, 40, 58, 62, 66, 72, 45, 54]
    sector_trend = pd.DataFrame({"Sector": sector_names, "Average ESG Score": sector_scores})
    st.bar_chart(sector_trend.set_index("Sector"))
    st.markdown("<b>Current Sector Highlights:</b>", unsafe_allow_html=True)
    for i, row in sector_trend.iterrows():
        st.write(
            f"- {row['Sector']}: Score {row['Average ESG Score']} – {sector_recommendation(row['Average ESG Score'])}"
        )
    st.markdown("""
    #### Regulatory Insights
    - SEBI's new BRSR Core framework increases ESG disclosure requirements for top 250 companies and value-chain partners.
    - Green credit and climate risk reporting are areas to watch in 2025.
    ---
    #### Investment Recommendations
    - **Focus on sectors with scores >65** for sustainable outperformance.
    - **Monitor lagging sectors** for turnaround signals—but adjust portfolios for regulatory and reputational risk[9][13].
    """, unsafe_allow_html=True)

# ----- FOOTER -----
st.markdown("---")
st.caption("Season ESG Analysis • Professional ESG insights. Contact: info@seasoneg.com")

