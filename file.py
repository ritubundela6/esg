import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.graph_objs as go

# ----------------------------
# Data & Constants
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

# Sample financial KPI data (mock values for top companies)
sample_financials = {
    "Reliance Industries": {"P/E": 22.5, "ROE": 14.8, "Current Ratio": 1.4, "EPS": 55.7, "Dividend Yield": 0.5, "Debt-to-Equity": 0.6, "Gross Margin": 40, "Net Margin": 9, "ROI": 13, "Free Cash Flow": 4200, "Market Cap": 180_000},
    "TCS": {"P/E": 28.7, "ROE": 38.9, "Current Ratio": 2.1, "EPS": 113.2, "Dividend Yield": 1.4, "Debt-to-Equity": 0.2, "Gross Margin": 28, "Net Margin": 21, "ROI": 27, "Free Cash Flow": 9800, "Market Cap": 150_000},
    "HDFC Bank": {"P/E": 20.1, "ROE": 16.2, "Current Ratio": 1.7, "EPS": 75.2, "Dividend Yield": 0.9, "Debt-to-Equity": 0.9, "Gross Margin": 60, "Net Margin": 17, "ROI": 15, "Free Cash Flow": 3600, "Market Cap": 90_000},
    "Infosys": {"P/E": 25.0, "ROE": 22.0, "Current Ratio": 2.2, "EPS": 50.4, "Dividend Yield": 1.1, "Debt-to-Equity": 0.1, "Gross Margin": 33, "Net Margin": 19, "ROI": 20, "Free Cash Flow": 5000, "Market Cap": 75_000}, 
    "Hindustan Unilever": {"P/E": 30.2, "ROE": 28.5, "Current Ratio": 1.3, "EPS": 45.1, "Dividend Yield": 1.0, "Debt-to-Equity": 0.5, "Gross Margin": 65, "Net Margin": 10, "ROI": 18, "Free Cash Flow": 4100, "Market Cap": 70_000},
}

financial_kpis_info = {
    "P/E": "Price/Earnings Ratio (10-25 typical)",
    "ROE": "Return on Equity (>15% is good)",
    "Current Ratio": "Current Assets / Liabilities (1.5-3 optimal)",
    "EPS": "Earnings per Share (higher = more profit)",
    "Dividend Yield": "Annual Dividend / Price (higher = income stock)",
    "Debt-to-Equity": "Total Liabilities / Equity (<1 is conservative)",
    "Gross Margin": "(Revenue - COGS) / Revenue (higher = efficient)",
    "Net Margin": "Net Income / Revenue (higher = profitable)",
    "ROI": "Return on Investment",
    "Free Cash Flow": "Cash left after capital expenditures",
    "Market Cap": "Company total market capitalization (in crores)"
}

# ----------------------------
# Helpers - ESG Score Calculation and Styles
# ----------------------------

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
        debt_eq = financials.get("Debt-to-Equity")
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
        if debt_eq is not None:
            if debt_eq > 1:
                recs.append("High debt-to-equity: Financial risk may be elevated.")
            else:
                recs.append("Conservative debt-to-equity: Balance sheet looks stable.")
    return recs

# ----------------------------
# Initialize Session State
# ----------------------------

st.set_page_config(page_title="NIFTY50 ESG + Financial Dashboard", layout="wide")
st.title("ESG & Financial Analytics Dashboard for Investment Decisions")

if 'companies' not in st.session_state:
    st.session_state.companies = process_init_company_list(default_companies)

# ----------------------------
# Utility for Peer Benchmarking
# ----------------------------
def peer_benchmark(company_name, companies, kpi="overallScore"):
    company = next((c for c in companies if c["name"] == company_name), None)
    if not company:
        return None
    sector = company["sector"]
    sector_companies = [c for c in companies if c["sector"] == sector]
    if not sector_companies:
        return None
    values = [c[kpi] for c in sector_companies]
    median_val = np.median(values)
    rank = sum(1 for v in values if v > company[kpi]) + 1
    percentile = int((1 - (rank-1)/len(values)) * 100)
    return {"median": median_val, "percentile": percentile, "sector": sector}

# ----------------------------
# Tabs
# ----------------------------

tabs = st.tabs([
    "1. NIFTY50 Companies",
    "2. Custom Comparison",
    "3. Sector Analytics",
    "4. Data & Trend Analysis"
])

# ----------------------------
# Tab 1: NIFTY50 Companies ESG & Financial Overview
# ----------------------------
with tabs[0]:
    st.header("NIFTY 50 Companies - ESG & Financial Overview")
    companies = [c for c in st.session_state.companies if c['isNifty50']]
    df = pd.DataFrame([{
        "Company": c["name"],
        "Sector": c["sector"],
        "Env": c["environmental"]["score"],
        "Soc": c["social"]["score"],
        "Gov": c["governance"]["score"],
        "Overall ESG": c["overallScore"]
    } for c in companies])

    st.dataframe(df.sort_values("Overall ESG", ascending=False).reset_index(drop=True), use_container_width=True)

    st.subheader("View ESG & Financial Details")
    selected = st.selectbox(
        "Select a company",
        [c["name"] for c in companies],
        key="view_select"
    )

    company = next(c for c in companies if c["name"] == selected)
    
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

    # Peer benchmarking summary
    bench = peer_benchmark(company['name'], companies)
    if bench:
        st.markdown("### Peer Benchmarking Summary")
        st.write(f"Sector: **{bench['sector']}**")
        st.write(f"Median Overall ESG Score in sector: **{bench['median']}**")
        st.write(f"Company percentile rank in sector: **{bench['percentile']}%**")

# ----------------------------
# Tab 2: Custom Company Comparison
# ----------------------------
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
        if submit:
            if name and sector:
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
                st.success(f"Company '{name}' added successfully!")
            else:
                st.error("Please provide both company Name and Sector.")

    custom_companies = [c for c in st.session_state.companies if not c['isNifty50']]

    if not custom_companies:
        st.warning("No custom companies added yet.")
    else:
        df_cust = pd.DataFrame([{ "Company": c["name"], "Sector": c["sector"], "Env": c["environmental"]["score"],
                                "Soc": c["social"]["score"], "Gov": c["governance"]["score"], "Overall ESG": c["overallScore"] }
                                for c in custom_companies])
        st.dataframe(df_cust, use_container_width=True)

        # Multi-select to compare companies (custom + nifty)
        compare_options = [c["name"] for c in custom_companies] + [c["name"] for c in st.session_state.companies if c["isNifty50"]]
        compare_names = st.multiselect(
            "Choose companies to compare",
            compare_options,
            default=[custom_companies[0]["name"]] if custom_companies else []
        )

        data = [c for c in st.session_state.companies if c["name"] in compare_names]

        if data:
            df_cmp = pd.DataFrame([
                {"Company": c["name"], "Sector": c["sector"], "Env": c["environmental"]["score"],
                 "Soc": c["social"]["score"], "Gov": c["governance"]["score"], "Overall ESG": c["overallScore"] }
                for c in data
            ])
            st.subheader("ESG Score Comparison")
            st.dataframe(df_cmp.sort_values("Overall ESG", ascending=False), use_container_width=True)
            st.bar_chart(df_cmp.set_index("Company")[["Env", "Soc", "Gov", "Overall ESG"]])

            # Show key financial KPIs for compared companies
            compare_financials = []
            for c in data:
                fin = sample_financials.get(c["name"], {})
                row = {"Company": c["name"]}
                # Select KPIs for better visibility
                for k in ["P/E", "ROE", "Current Ratio", "Dividend Yield", "Debt-to-Equity", "Market Cap"]:
                    row[k] = fin.get(k, None)
                compare_financials.append(row)
            df_kpi = pd.DataFrame(compare_financials).set_index("Company")
            
            st.subheader("Financial KPIs Comparison")
            st.dataframe(df_kpi)

            chosen_kpi = st.selectbox("Select Financial KPI to compare", df_kpi.columns.tolist())
            if chosen_kpi:
                st.bar_chart(df_kpi[chosen_kpi])

            # Radar Chart for ESG and Financial KPIs
            st.subheader("Radar Chart: ESG and Financial Overview")
            
            categories = ['Env', 'Soc', 'Gov', 'Overall ESG']
            financial_categories = ['P/E', 'ROE', 'Dividend Yield', 'Debt-to-Equity', 'Market Cap']

            radar_categories = categories + financial_categories

            def radar_chart(companies):
                fig = go.Figure()
                for comp in companies:
                    name = comp['name']
                    env = comp['environmental']['score']
                    soc = comp['social']['score']
                    gov = comp['governance']['score']
                    overall = comp['overallScore']
                    fin = sample_financials.get(name, {})
                    # Normalize financials for radar (simple normalization/scaling)
                    def norm(x, low, high):
                        if x is None:
                            return 0
                        return max(0, min(1, (x-low)/(high-low)))
                    pe = norm(fin.get("P/E"), 5, 40)
                    roe = norm(fin.get("ROE"), 0, 40)
                    dy = norm(fin.get("Dividend Yield"), 0, 5)
                    de = 1 - norm(fin.get("Debt-to-Equity"), 0, 3)  # reversed (lower better)
                    mc = norm(fin.get("Market Cap"), 0, 200_000)
                    values = [env/100, soc/100, gov/100, overall/100, pe, roe, dy, de, mc]

                    fig.add_trace(go.Scatterpolar(
                        r=values,
                        theta=radar_categories,
                        fill='toself',
                        name=name
                    ))
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 1]
                        )),
                    showlegend=True,
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)

            radar_chart(data)

            # Recommendations for selected companies
            st.subheader("Investment Recommendations")
            for c in data:
                fin = sample_financials.get(c["name"], None)
                recs = get_investment_recommendation(c, fin)
                st.markdown(f"**{c['name']}**:")
                for r in recs:
                    st.write(f"- {r}")

# ----------------------------
# Tab 3: Sector Analytics
# ----------------------------
with tabs[2]:
    st.header("Sector-wise ESG & Financial Analytics (NIFTY50)")
    nifty_companies = [c for c in st.session_state.companies if c["isNifty50"]]
    df_sector = get_sector_analysis(nifty_companies)
    st.dataframe(df_sector.set_index("Sector"), use_container_width=True)
    st.bar_chart(df_sector.set_index("Sector")[["Avg ESG", "Avg Env", "Avg Soc", "Avg Gov"]])

    # Sector KPI cards (avg P/E & ROE & others)
    st.subheader("Sector Financial Metrics")
    sectors = df_sector["Sector"].tolist()
    for sector in sectors:
        comps = [c for c in nifty_companies if c["sector"] == sector]
        pes = [sample_financials.get(c["name"], {}).get("P/E") for c in comps if sample_financials.get(c["name"], {}).get("P/E") is not None]
        roes = [sample_financials.get(c["name"], {}).get("ROE") for c in comps if sample_financials.get(c["name"], {}).get("ROE") is not None]
        debt_eqs = [sample_financials.get(c["name"], {}).get("Debt-to-Equity") for c in comps if sample_financials.get(c["name"], {}).get("Debt-to-Equity") is not None]
        avg_pe = round(np.mean(pes), 2) if pes else None
        avg_roe = round(np.mean(roes), 2) if roes else None
        avg_de = round(np.mean(debt_eqs), 2) if debt_eqs else None
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(f"{sector} Avg P/E", avg_pe if avg_pe is not None else "N/A")
        with col2:
            st.metric(f"{sector} Avg ROE", avg_roe if avg_roe is not None else "N/A")
        with col3:
            st.metric(f"{sector} Avg Debt-to-Equity", avg_de if avg_de is not None else "N/A")
        with col4:
            st.metric(f"{sector} Company Count", len(comps))

    # Correlation matrix of ESG and key Financial KPIs
    st.subheader("Correlation: ESG Scores vs Financial KPIs")
    corr_data = []
    for c in nifty_companies:
        fin = sample_financials.get(c["name"], {})
        corr_data.append({
            "Env": c["environmental"]["score"],
            "Soc": c["social"]["score"],
            "Gov": c["governance"]["score"],
            "Overall": c["overallScore"],
            "P/E": fin.get("P/E"),
            "ROE": fin.get("ROE"),
            "Current Ratio": fin.get("Current Ratio"),
            "Dividend Yield": fin.get("Dividend Yield"),
            "Debt-to-Equity": fin.get("Debt-to-Equity"),
            "Market Cap": fin.get("Market Cap")
        })
    corr_df = pd.DataFrame(corr_data).dropna()
    if corr_df.shape[0] > 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.info("Not enough complete data to show correlation matrix.")

    # Dynamic narrative / summary
    st.subheader("Sector Summary Narrative")
    best_sector = df_sector.loc[df_sector["Avg ESG"].idxmax()]
    worst_sector = df_sector.loc[df_sector["Avg ESG"].idxmin()]
    st.markdown(f"""
- The sector with the **highest average ESG score** is **{best_sector['Sector']}** ({best_sector['Avg ESG']})
- The sector with the **lowest average ESG score** is **{worst_sector['Sector']}** ({worst_sector['Avg ESG']})
- Recommend focusing on sectors with avg ESG ≥ 75 for sustainable investments.
- Financial KPI averages assist in validating sector financial health.
    """)

# ----------------------------
# Tab 4: Data & Trend Analysis
# ----------------------------
with tabs[3]:
    st.header("Data Upload & Trend Analysis for ESG Consultant")

    uploaded_file = st.file_uploader("Upload data file (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df_upload = pd.read_csv(uploaded_file)
            else:
                df_upload = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Failed to load file: {e}")
            df_upload = None

        if df_upload is not None:
            st.subheader("Preview of Uploaded Data")
            st.write(df_upload.head())

            numeric_cols = df_upload.select_dtypes(include=np.number).columns.tolist()
            non_numeric_cols = df_upload.select_dtypes(exclude=np.number).columns.tolist()

            # Allow user to select x and y for trendplot
            x_col = st.selectbox("Select X-axis column (usually date/time or index)", df_upload.columns)
            y_col = st.selectbox("Select Y-axis numeric column for trend", numeric_cols)

            if x_col and y_col:
                st.subheader(f"Trend Line: {y_col} over {x_col}")

                x_data = df_upload[x_col]
                y_data = df_upload[y_col]

                # Convert x_data to numeric if possible for fitting line
                try:
                    x_numeric = pd.to_datetime(x_data)
                    x_numeric_vals = x_numeric.map(pd.Timestamp.toordinal)
                except:
                    try:
                        x_numeric_vals = pd.to_numeric(x_data)
                    except:
                        x_numeric_vals = range(len(x_data))

                fig, ax = plt.subplots()
                ax.plot(x_data, y_data, marker="o", label="Actual Data")
                if len(y_data) > 1:
                    z = np.polyfit(x_numeric_vals, y_data, 1)
                    p = np.poly1d(z)
                    ax.plot(x_data, p(x_numeric_vals), "r--", label="Trend Line")
                    slope = z[0]
                else:
                    slope = 0
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"{y_col} Trend over {x_col}")
                ax.legend()
                st.pyplot(fig)

                st.write(df_upload[y_col].describe())

                st.markdown("##### Automated Recommendations")
                if slope > 0:
                    st.info(f"Uptrend detected in **{y_col}** (slope={slope:.3f}); consider growth opportunities.")
                elif slope < 0:
                    st.warning(f"Downtrend detected in **{y_col}** (slope={slope:.3f}); assess risks.")
                else:
                    st.info(f"No significant trend detected in **{y_col}**.")

                # Additional rolling stats
                window = st.slider("Select rolling window for moving average and volatility", 2, 20, 5)

                roll_mean = df_upload[y_col].rolling(window=window).mean()
                roll_std = df_upload[y_col].rolling(window=window).std()

                st.line_chart(roll_mean.rename(f"{y_col} Rolling Mean ({window})"))
                st.line_chart(roll_std.rename(f"{y_col} Rolling Volatility ({window})"))

                # Financial related columns (market cap, volume)
                fin_cols = [c for c in numeric_cols if c.lower() in ['market cap', 'market_cap', 'volume']]
                if fin_cols:
                    st.subheader("Financial Time Series Trends")
                    for col in fin_cols:
                        st.markdown(f"**Trend for {col}**")
                        st.line_chart(df_upload.set_index(x_col)[col])

            # Optional: Allow user to download a filtered dataset
            st.markdown("---")
            if st.button("Download current data as CSV"):
                csv = df_upload.to_csv(index=False).encode('utf-8')
                st.download_button(label="Download CSV", data=csv, file_name="data_download.csv", mime='text/csv')

    else:
        st.info("Upload a CSV or Excel file to analyze trends and KPIs.")

# ----------------------------
# END OF APP
# ----------------------------


