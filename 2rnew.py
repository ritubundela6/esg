import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# ----------------------------
# 1. Define Sample Data (NIFTY 50, mock scores)
# ----------------------------

nifty50_data = [
    {
        "id": "nifty_1",
        "name": "Reliance Industries",
        "sector": "Oil & Gas",
        "environmental": {"score": 72, "carbonEmissions": 65, "renewableEnergy": 78, "wasteManagement": 73},
        "social": {"score": 78, "employeeSafety": 82, "diversity": 71, "communityImpact": 81},
        "governance": {"score": 85, "boardIndependence": 88, "executiveComp": 80, "transparency": 87},
        "overallScore": 78,
        "isNifty50": True
    },
    # ... (all the other entries for nifty_2 to nifty_10 exactly as in your original code)
    # [Include all entries from your original nifty50_data]
]

# ----------------------------
# 2. App Utilities: Helper Functions
# ----------------------------

def calculate_esg_score(company):
    env = company['environmental']
    soc = company['social']
    gov = company['governance']
    env_score = round((env['carbonEmissions'] + env['renewableEnergy'] + env['wasteManagement'])/3)
    soc_score = round((soc['employeeSafety'] + soc['diversity'] + soc['communityImpact'])/3)
    gov_score = round((gov['boardIndependence'] + gov['executiveComp'] + gov['transparency'])/3)
    overall = round((env_score + soc_score + gov_score)/3)
    return {'environmental': env_score, 'social': soc_score, 'governance': gov_score, 'overall': overall}

def get_improvement_areas(company):
    areas = []
    if company['environmental']['score'] < 70:
        areas.append("Environmental practices need improvement")
    if company['social']['score'] < 70:
        areas.append("Social responsibility initiatives required")
    if company['governance']['score'] < 70:
        areas.append("Governance structure needs strengthening")
    if not areas:
        areas.append("Strong performance across all ESG categories")
    return areas

def get_sector_analysis(companies):
    sector_stats = {}
    for c in companies:
        sec = c['sector']
        if sec not in sector_stats:
            sector_stats[sec] = {
                "count": 0,
                "totalESG": 0,
                "totalEnv": 0,
                "totalSoc": 0,
                "totalGov": 0
            }
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
            "Avg ESG": round(data["totalESG"]/data["count"]),
            "Avg Env": round(data["totalEnv"]/data["count"]),
            "Avg Soc": round(data["totalSoc"]/data["count"]),
            "Avg Gov": round(data["totalGov"]/data["count"])
        })
    return pd.DataFrame(rows)

def get_score_color(score):
    if score >= 80:
        return "✅"
    if score >= 60:
        return "⚠️"
    return "❌"

# ----------------------------
# 3. Streamlit App Starts Here
# ----------------------------

st.set_page_config(page_title="NIFTY50 ESG Dashboard", layout="wide")
st.title("ESG Analysis & Comparison Tool")

if 'companies' not in st.session_state:
    st.session_state.companies = nifty50_data.copy()

tabs = st.tabs(["NIFTY50 Companies", "Custom Comparison", "Sector Analytics", "Data & Trend Analysis"])

# ---------------------------------------------------------------
# Tab 1: View Nifty 50 Companies, ESG Scores, View Details
# ---------------------------------------------------------------
with tabs[0]:
    st.header("NIFTY 50 Companies - ESG Overview")

    df = pd.DataFrame([
        {
            "Company": c["name"],
            "Sector": c["sector"],
            "Env": c["environmental"]["score"],
            "Soc": c["social"]["score"],
            "Gov": c["governance"]["score"],
            "Overall ESG": c["overallScore"]
        }
        for c in st.session_state.companies if c["isNifty50"]
    ])
    st.dataframe(df.sort_values("Overall ESG", ascending=False).reset_index(drop=True), use_container_width=True)

    st.subheader("View ESG Details")
    selected = st.selectbox(
        "Select a company",
        [c["name"] for c in st.session_state.companies if c["isNifty50"]],
        key="view_select"
    )
    company = next(c for c in st.session_state.companies if c["name"] == selected)
    st.markdown(f"""
    **{company['name']}**  
    Sector: {company['sector']}
    - Environmental: {company['environmental']['score']} ({get_score_color(company['environmental']['score'])})
    - Social: {company['social']['score']} ({get_score_color(company['social']['score'])})
    - Governance: {company['governance']['score']} ({get_score_color(company['governance']['score'])})
    - **Overall ESG**: {company['overallScore']} ({get_score_color(company['overallScore'])})
    """)
    st.info('\n'.join(get_improvement_areas(company)))

# ---------------------------------------------------------------
# Tab 2: Add & Compare Custom Companies
# ---------------------------------------------------------------
with tabs[1]:
    st.header("Custom Company Comparison")
    st.markdown("**Add your own company and compare with NIFTY 50 leaders**")
    with st.form(key="add_company"):
        name = st.text_input("Company Name")
        sector = st.text_input("Sector")
        st.markdown("### Environmental")
        ce = st.slider("Carbon Emissions", 0, 100, 50)
        re = st.slider("Renewable Energy", 0, 100, 50)
        wm = st.slider("Waste Management", 0, 100, 50)
        st.markdown("### Social")
        es = st.slider("Employee Safety", 0, 100, 50)
        dv = st.slider("Diversity", 0, 100, 50)
        ci = st.slider("Community Impact", 0, 100, 50)
        st.markdown("### Governance")
        bi = st.slider("Board Independence", 0, 100, 50)
        ec = st.slider("Executive Compensation", 0, 100, 50)
        tr = st.slider("Transparency", 0, 100, 50)
        submitted = st.form_submit_button("Add Company")
        if submitted and name and sector:
            d = {
                "name": name, "sector": sector,
                "environmental": {"carbonEmissions": ce, "renewableEnergy": re, "wasteManagement": wm, "score": 0},
                "social": {"employeeSafety": es, "diversity": dv, "communityImpact": ci, "score": 0},
                "governance": {"boardIndependence": bi, "executiveComp": ec, "transparency": tr, "score": 0}
            }
            scores = calculate_esg_score(d)
            d["environmental"]["score"] = scores['environmental']
            d["social"]["score"] = scores['social']
            d["governance"]["score"] = scores['governance']
            d["overallScore"] = scores['overall']
            d["isNifty50"] = False
            d["id"] = "custom_" + str(len(st.session_state.companies)+1)
            st.session_state.companies.append(d)
            st.success("Added company: " + name)
    custom_companies = [c for c in st.session_state.companies if not c['isNifty50']]
    if not custom_companies:
        st.warning("No custom companies added yet.")
    else:
        df_cust = pd.DataFrame([
            {
                "Company": c["name"],
                "Sector": c["sector"],
                "Env": c["environmental"]["score"],
                "Soc": c["social"]["score"],
                "Gov": c["governance"]["score"],
                "Overall ESG": c["overallScore"],
            }
            for c in custom_companies
        ])
        st.dataframe(df_cust, use_container_width=True)
        if len(custom_companies):
            st.subheader("Compare with NIFTY50")
            compare_names = st.multiselect(
                "Choose companies to compare",
                [c["name"] for c in custom_companies + [c for c in st.session_state.companies if c['isNifty50']]],
                default=[custom_companies[0]["name"]]
            )
            data = [c for c in st.session_state.companies if c["name"] in compare_names]
            if data:
                df_cmp = pd.DataFrame([
                    {
                        "Company": c["name"],
                        "Sector": c["sector"],
                        "Env": c["environmental"]["score"],
                        "Soc": c["social"]["score"],
                        "Gov": c["governance"]["score"],
                        "Overall ESG": c["overallScore"]
                    }
                    for c in data
                ])
                st.dataframe(df_cmp.sort_values("Overall ESG", ascending=False), use_container_width=True)
                st.bar_chart(df_cmp.set_index("Company")[["Env", "Soc", "Gov", "Overall ESG"]])

# ---------------------------------------------------------------
# Tab 3: Sector-level Analytics (Averages by Sector)
# ---------------------------------------------------------------
with tabs[2]:
    st.header("Sector-wise ESG Averages (NIFTY50)")
    df_sector = get_sector_analysis(
        [c for c in st.session_state.companies if c["isNifty50"]]
    )
    st.dataframe(df_sector.set_index("Sector"), use_container_width=True)
    st.bar_chart(df_sector.set_index("Sector")[["Avg ESG", "Avg Env", "Avg Soc", "Avg Gov"]])

# ---------------------------------------------------------------
# Tab 4: Data & Trend Analysis (File Upload and Visualization)
# ---------------------------------------------------------------
with tabs[3]:
    st.header("Data & Trend Analysis")
    st.title("📊 Data Uploader & Trend Analysis")

    # Step 1: Let the user upload a CSV or Excel file
    uploaded_file = st.file_uploader("Upload your data file (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Step 2: Read the data with pandas
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.subheader("Preview of Uploaded Data")
        st.write(df.head())

        # Step 3: Let user select columns for analysis
        st.subheader("Select columns for Trend Analysis")
        all_columns = df.columns.tolist()
        x_col = st.selectbox("Select X-axis column (usually date/time or index)", all_columns)
        y_col = st.selectbox("Select Y-axis column (numeric)", all_columns)

        # Step 4: Display a line chart for a quick trend view
        st.subheader(f"Trend Line: {y_col} over {x_col}")
        fig, ax = plt.subplots()
        ax.plot(df[x_col], df[y_col], marker='o')
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} Trend over {x_col}")
        st.pyplot(fig)

        # (Optional) Step 5: Show basic statistics
        st.subheader("Basic Statistics")
        st.write(df[y_col].describe())
