import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

# ----------------------------
# 1. Define Sample Data (NIFTY 50, mock scores & financials)
# ----------------------------
default_companies = [
    {
        "name": "Reliance Industries",
        "sector": "Oil & Gas",
        "environmental": {"carbonEmissions": 55, "renewableEnergy": 70, "wasteManagement": 70},
        "social": {"employeeSafety": 75, "diversity": 68, "communityImpact": 73},
        "governance": {"boardIndependence": 80, "executiveComp": 75, "transparency": 80}
    },
    {
        "name": "TCS",
        "sector": "IT Services",
        "environmental": {"carbonEmissions": 88, "renewableEnergy": 85, "wasteManagement": 82},
        "social": {"employeeSafety": 90, "diversity": 85, "communityImpact": 90},
        "governance": {"boardIndependence": 95, "executiveComp": 90, "transparency": 91}
    },
    {
        "name": "HDFC Bank",
        "sector": "Banking",
        "environmental": {"carbonEmissions": 80, "renewableEnergy": 75, "wasteManagement": 80},
        "social": {"employeeSafety": 85, "diversity": 78, "communityImpact": 83},
        "governance": {"boardIndependence": 92, "executiveComp": 88, "transparency": 90}
    },
    {
        "name": "Infosys",
        "sector": "IT Services",
        "environmental": {"carbonEmissions": 90, "renewableEnergy": 85, "wasteManagement": 86},
        "social": {"employeeSafety": 88, "diversity": 82, "communityImpact": 85},
        "governance": {"boardIndependence": 90, "executiveComp": 87, "transparency": 90}
    },
    {
        "name": "Hindustan Unilever",
        "sector": "FMCG",
        "environmental": {"carbonEmissions": 85, "renewableEnergy": 80, "wasteManagement": 81},
        "social": {"employeeSafety": 88, "diversity": 84, "communityImpact": 86},
        "governance": {"boardIndependence": 87, "executiveComp": 83, "transparency": 85}
    },
    {
        "name": "ITC",
        "sector": "FMCG",
        "environmental": {"carbonEmissions": 70, "renewableEnergy": 75, "wasteManagement": 75},
        "social": {"employeeSafety": 80, "diversity": 77, "communityImpact": 80},
        "governance": {"boardIndependence": 83, "executiveComp": 78, "transparency": 82}
    },
    {
        "name": "ICICI Bank",
        "sector": "Banking",
        "environmental": {"carbonEmissions": 78, "renewableEnergy": 74, "wasteManagement": 76},
        "social": {"employeeSafety": 83, "diversity": 76, "communityImpact": 81},
        "governance": {"boardIndependence": 89, "executiveComp": 85, "transparency": 87}
    },
    {
        "name": "Larsen & Toubro",
        "sector": "Infrastructure",
        "environmental": {"carbonEmissions": 65, "renewableEnergy": 70, "wasteManagement": 70},
        "social": {"employeeSafety": 78, "diversity": 70, "communityImpact": 74},
        "governance": {"boardIndependence": 85, "executiveComp": 80, "transparency": 84}
    },
]

sample_financials = {
    "Reliance Industries": {"P/E": 22.5, "ROE": 14.8, "Current Ratio": 1.4, "EPS": 55.7, "Dividend Yield": 0.5, "Debt-to-Equity": 0.6, "Gross Margin": 40, "Net Margin": 9, "ROI": 13, "Free Cash Flow": 4200},
    "TCS": {"P/E": 28.7, "ROE": 38.9, "Current Ratio": 2.1, "EPS": 113.2, "Dividend Yield": 1.4, "Debt-to-Equity": 0.2, "Gross Margin": 28, "Net Margin": 21, "ROI": 27, "Free Cash Flow": 9800},
    "HDFC Bank": {"P/E": 20.1, "ROE": 16.2, "Current Ratio": 1.7, "EPS": 75.2, "Dividend Yield": 0.9, "Debt-to-Equity": 0.9, "Gross Margin": 60, "Net Margin": 17, "ROI": 15, "Free Cash Flow": 3600},
}

financial_kpis_info = {
    "P/E": "Price/Earnings Ratio (10-25 typical)",
    "ROE": "Return on Equity (>15% is good)",
    "Current Ratio": "Current Assets / Liabilities (1.5-3 optimal)",
    "EPS": "Earnings per Share (higher = more profit)",
    "Dividend Yield": "Annual Dividend/Price (higher = income stock)",
    "Debt-to-Equity": "Total Liabilities/Equity (<1 is conservative)",
    "Gross Margin": "(Revenue - COGS)/Revenue (higher = efficient)",
    "Net Margin": "Net Income / Revenue",
    "ROI": "Return on Investment",
    "Free Cash Flow": "Cash left after capital expenditures"
}

# --------- Utilities and Helper Functions ----------
def calculate_esg_score(c):
    env = c["environmental"]
    soc = c["social"]
    gov = c["governance"]
    env_score = round((env["carbonEmissions"] + env["renewableEnergy"] + env["wasteManagement"]) / 3)
    soc_score = round((soc["employeeSafety"] + soc["diversity"] + soc["communityImpact"]) / 3)
    gov_score = round((gov["boardIndependence"] + gov["executiveComp"] + gov["transparency"]) / 3)
    overall = round((env_score + soc_score + gov_score) / 3)
    return env_score, soc_score, gov_score, overall

def get_score_color(score):
    if score >= 80:
        return "🟢"
    elif score >= 60:
        return "🟡"
    return "🔴"

def get_score_badge(score):
    if score >= 80:
        return "✅"
    elif score >= 60:
        return "⚠️"
    return "❗️"

def get_improvement_areas(company):
    areas = []
    if company["environmental"]["score"] < 70:
        areas.append("Environmental practices need improvement")
    if company["social"]["score"] < 70:
        areas.append("Social responsibility initiatives required")
    if company["governance"]["score"] < 70:
        areas.append("Governance structure needs strengthening")
    if not areas:
        areas.append("Strong performance across all ESG categories")
    return areas

def get_sector_insights(companies):
    by_sector = {}
    for c in companies:
        by_sector.setdefault(c["sector"], []).append(c)
    sector_avg = {}
    for s, comps in by_sector.items():
        avg = round(sum(x["overallScore"] for x in comps) / len(comps))
        sector_avg[s] = avg
    return sector_avg

def get_sector_analysis(companies):
    sector_stats = {}
    for c in companies:
        sec = c['sector']
        if sec not in sector_stats:
            sector_stats[sec] = {"count": 0, "totalESG": 0, "totalEnv": 0, "totalSoc": 0, "totalGov": 0}
        sector_stats[sec]['count'] += 1
        sector_stats[sec]['totalESG'] += c['overallScore']
        sector_stats[sec]['totalEnv'] += c['environmental']['score']
        sector_stats[sec]['totalSoc'] += c['social']['score']
        sector_stats[sec]['totalGov'] += c['governance']['score']
    rows = []
    for sec, data in sector_stats.items():
        rows.append({
            "Sector": sec,
            "Companies": data["count"],
            "Avg ESG": round(data["totalESG"] / data["count"]),
            "Avg Env": round(data["totalEnv"] / data["count"]),
            "Avg Soc": round(data["totalSoc"] / data["count"]),
            "Avg Gov": round(data["totalGov"] / data["count"])
        })
    return pd.DataFrame(rows)

def get_investment_recommendation(company, financials=None):
    recs = []
    o = company['overallScore']
    if o >= 85:
        recs.append("Excellent ESG profile: Suitable for responsible investing.")
    elif o >= 75:
        recs.append("Good ESG profile: Consider for investment, validate financials.")
    elif o >= 65:
        recs.append("Moderate ESG profile: May need monitoring and further diligence.")
    else:
        recs.append("Low ESG profile: Higher sustainability risk, caution advised.")
    if financials:
        pe = financials.get("P/E")
        roe = financials.get("ROE")
        curr = financials.get("Current Ratio")
        if pe is not None:
            if pe < 10:
                recs.append("P/E ratio is low: Potentially undervalued.")
            elif pe > 30:
                recs.append("P/E ratio is high: May be overvalued.")
            else:
                recs.append("P/E ratio is in a healthy range.")
        if roe is not None:
            if roe > 15:
                recs.append("High ROE: Indicates efficient management.")
            else:
                recs.append("ROE could be improved for better efficiency.")
        if curr is not None:
            if curr < 1:
                recs.append("Liquidity risk: Current Ratio < 1. Caution required.")
            elif curr > 3:
                recs.append("Current Ratio is high: May suggest under-utilized assets.")
            else:
                recs.append("Healthy liquidity position indicated by Current Ratio.")
    return recs

def process_init_company_list(company_dicts):
    processed = []
    for i, c in enumerate(company_dicts):
        env_score, soc_score, gov_score, overall = calculate_esg_score(c)
        processed.append({
            "id": i + 1,
            "name": c["name"],
            "sector": c["sector"],
            "environmental": {**c["environmental"], "score": env_score},
            "social": {**c["social"], "score": soc_score},
            "governance": {**c["governance"], "score": gov_score},
            "overallScore": overall,
            "isNifty50": True
        })
    return processed

# ----------------------------
# Streamlit App
# ----------------------------
st.set_page_config(page_title="NIFTY50 ESG + Financial Dashboard", layout="wide")
st.title("ESG & Financial Analytics Dashboard for Investment Decisions")

if 'companies' not in st.session_state:
    st.session_state.companies = process_init_company_list(default_companies)

tabs = st.tabs([
    "NIFTY50 Companies",
    "Custom Comparison",
    "Sector Analytics",
    "Data & Trend Analysis"
])

# Tab 1: NIFTY50 Companies ESG & Financial Overview
with tabs[0]:
    st.header("NIFTY 50 Companies - ESG & Financial Overview")
    df = pd.DataFrame([{
        "Company": c["name"],
        "Sector": c["sector"],
        "Env": c["environmental"]["score"],
        "Soc": c["social"]["score"],
        "Gov": c["governance"]["score"],
        "Overall ESG": c["overallScore"]
    } for c in st.session_state.companies if c["isNifty50"]])
    st.dataframe(df.sort_values("Overall ESG", ascending=False).reset_index(drop=True), use_container_width=True)
    st.subheader("View ESG & Financial Details")
    selected = st.selectbox(
        "Select a company",
        [c["name"] for c in st.session_state.companies if c["isNifty50"]],
        key="view_select"
    )
    company = next(c for c in st.session_state.companies if c["name"] == selected)
    st.markdown(f"""
**{company['name']}**

Sector: {company['sector']}
- Environmental: {company['environmental']['score']} {get_score_badge(company['environmental']['score'])}
- Social: {company['social']['score']} {get_score_badge(company['social']['score'])}
- Governance: {company['governance']['score']} {get_score_badge(company['governance']['score'])}
- **Overall ESG**: {company['overallScore']} {get_score_badge(company['overallScore'])}
""")
    for a in get_improvement_areas(company):
        st.info(a)
    st.markdown("### Financial KPIs")
    fin = sample_financials.get(company["name"], None)
    if fin:
        for k, v in financial_kpis_info.items():
            st.write(f"**{k}:** {fin.get(k, 'N/A')} — {v}")
    else:
        st.warning("Financial data not available for this company.")
    st.markdown("### Investment Recommendations")
    st.info('\n'.join(get_investment_recommendation(company, fin)))

# Tab 2: Custom Company Comparison
with tabs[1]:
    st.header("Custom Company Comparison")
    st.markdown("**Add your own company and compare with NIFTY 50 leaders**")
    with st.form("add_company_form", clear_on_submit=True):
        name = st.text_input("Company Name")
        sector = st.text_input("Sector (e.g., Technology, Banking, FMCG)")
        st.markdown("#### Environmental Factors (0-100)")
        ce = st.slider("Carbon Emissions", 0, 100, 50)
        re = st.slider("Renewable Energy", 0, 100, 50)
        wm = st.slider("Waste Management", 0, 100, 50)
        st.markdown("#### Social Factors (0-100)")
        es = st.slider("Employee Safety", 0, 100, 50)
        dv = st.slider("Diversity & Inclusion", 0, 100, 50)
        ci = st.slider("Community Impact", 0, 100, 50)
        st.markdown("#### Governance Factors (0-100)")
        bi = st.slider("Board Independence", 0, 100, 50)
        ec = st.slider("Executive Compensation", 0, 100, 50)
        tr = st.slider("Transparency", 0, 100, 50)
        submit = st.form_submit_button("Add Company")
        if submit and name and sector:
            d = {
                "name": name,
                "sector": sector,
                "environmental": {"carbonEmissions": ce, "renewableEnergy": re, "wasteManagement": wm},
                "social": {"employeeSafety": es, "diversity": dv, "communityImpact": ci},
                "governance": {"boardIndependence": bi, "executiveComp": ec, "transparency": tr}
            }
            env_score, soc_score, gov_score, overall = calculate_esg_score(d)
            d["environmental"]["score"] = env_score
            d["social"]["score"] = soc_score
            d["governance"]["score"] = gov_score
            d["overallScore"] = overall
            d["isNifty50"] = False
            d["id"] = max([c["id"] for c in st.session_state.companies])+1 if st.session_state.companies else 1
            st.session_state.companies.append(d)
            st.success("Company added successfully!")
    custom_companies = [c for c in st.session_state.companies if not c['isNifty50']]
    if not custom_companies:
        st.warning("No custom companies added yet.")
    else:
        df_cust = pd.DataFrame([{ "Company": c["name"], "Sector": c["sector"], "Env": c["environmental"]["score"],
                                "Soc": c["social"]["score"], "Gov": c["governance"]["score"], "Overall ESG": c["overallScore"] }
                                for c in custom_companies])
        st.dataframe(df_cust, use_container_width=True)
        compare_names = st.multiselect(
            "Choose companies to compare",
            [c["name"] for c in custom_companies + [c for c in st.session_state.companies if c['isNifty50']]],
            default=[custom_companies[0]["name"]] if custom_companies else []
        )
        data = [c for c in st.session_state.companies if c["name"] in compare_names]
        if data:
            df_cmp = pd.DataFrame([
                {"Company": c["name"], "Sector": c["sector"], "Env": c["environmental"]["score"],
                 "Soc": c["social"]["score"], "Gov": c["governance"]["score"], "Overall ESG": c["overallScore"] }
                for c in data
            ])
            st.dataframe(df_cmp.sort_values("Overall ESG", ascending=False), use_container_width=True)
            st.bar_chart(df_cmp.set_index("Company")[["Env", "Soc", "Gov", "Overall ESG"]])

# Tab 3: Sector Analytics
with tabs[2]:
    st.header("Sector-wise ESG Averages (NIFTY50)")
    df_sector = get_sector_analysis([c for c in st.session_state.companies if c["isNifty50"]])
    st.dataframe(df_sector.set_index("Sector"), use_container_width=True)
    st.bar_chart(df_sector.set_index("Sector")[["Avg ESG", "Avg Env", "Avg Soc", "Avg Gov"]])
    st.subheader("Nifty 50: Average ESG Scores (Current Year)")
    df_all = pd.DataFrame([{
        "Environmental": c["environmental"]["score"],
        "Social": c["social"]["score"],
        "Governance": c["governance"]["score"]
    } for c in st.session_state.companies if c["isNifty50"]])
    avg_scores = df_all.mean()
    st.bar_chart(avg_scores)
    df_esg = pd.DataFrame([
        {"Company": c["name"], "Sector": c["sector"], "Overall ESG": c["overallScore"]}
        for c in st.session_state.companies if c["isNifty50"]])
    chart = alt.Chart(df_esg).mark_circle(size=80).encode(
        x='Sector',
        y='Overall ESG',
        color='Sector',
        tooltip=['Company', 'Overall ESG']
    ).properties(width=700, height=400)
    st.altair_chart(chart, use_container_width=True)

# Tab 4: Data & Trend Analysis
with tabs[3]:
    st.header("Data & Trend Analysis")
    st.title("📊 Data Uploader & Trend Analysis")
    uploaded_file = st.file_uploader("Upload your data file (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df_upload = pd.read_csv(uploaded_file)
        else:
            df_upload = pd.read_excel(uploaded_file)
        st.subheader("Preview of Uploaded Data")
        st.write(df_upload.head())
        st.subheader("Select columns for Trend Analysis")
        all_columns = df_upload.columns.tolist()
        x_col = st.selectbox("Select X-axis column (usually date/time or index)", all_columns)
        y_col = st.selectbox("Select Y-axis column (numeric)", all_columns)
        st.subheader(f"Trend Line: {y_col} over {x_col}")
        x_data = df_upload[x_col]
        y_data = df_upload[y_col]
        if np.issubdtype(x_data.dtype, np.datetime64):
            x_numeric = x_data.map(lambda x: x.toordinal())
        else:
            x_numeric = x_data
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, marker='o', label="Actual Data")
        if len(y_data) > 1:
            z = np.polyfit(x_numeric, y_data, 1)
            p = np.poly1d(z)
            ax.plot(x_data, p(x_numeric), "r--", label="Trend Line")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} Trend over {x_col}")
        ax.legend()
        st.pyplot(fig)
        st.write(df_upload[y_col].describe())
        st.markdown("##### Automated Recommendation")
        mean_val = df_upload[y_col].mean()
        if mean_val > df_upload[y_col].iloc[0]:
            rec = f"Uptrend detected in {y_col}; consider further analysis for growth opportunities."
        else:
            rec = f"No clear uptrend in {y_col}; proceed cautiously or seek alternative investments."
        st.info(rec)

   
