# app.py

import streamlit as st
import pandas as pd

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
    {
        "id": "nifty_2",
        "name": "TCS",
        "sector": "Information Technology",
        "environmental": {"score": 88, "carbonEmissions": 85, "renewableEnergy": 92, "wasteManagement": 87},
        "social": {"score": 91, "employeeSafety": 89, "diversity": 94, "communityImpact": 90},
        "governance": {"score": 93, "boardIndependence": 95, "executiveComp": 89, "transparency": 95},
        "overallScore": 91,
        "isNifty50": True
    },
    {
        "id": "nifty_3",
        "name": "HDFC Bank",
        "sector": "Banking",
        "environmental": {"score": 76, "carbonEmissions": 78, "renewableEnergy": 72, "wasteManagement": 78},
        "social": {"score": 84, "employeeSafety": 86, "diversity": 79, "communityImpact": 87},
        "governance": {"score": 89, "boardIndependence": 92, "executiveComp": 85, "transparency": 90},
        "overallScore": 83,
        "isNifty50": True
    },
    {
        "id": "nifty_4",
        "name": "Infosys",
        "sector": "Information Technology",
        "environmental": {"score": 86, "carbonEmissions": 83, "renewableEnergy": 90, "wasteManagement": 85},
        "social": {"score": 89, "employeeSafety": 87, "diversity": 92, "communityImpact": 88},
        "governance": {"score": 91, "boardIndependence": 93, "executiveComp": 87, "transparency": 93},
        "overallScore": 89,
        "isNifty50": True
    },
    {
        "id": "nifty_5",
        "name": "ICICI Bank",
        "sector": "Banking",
        "environmental": {"score": 74, "carbonEmissions": 76, "renewableEnergy": 70, "wasteManagement": 76},
        "social": {"score": 82, "employeeSafety": 84, "diversity": 77, "communityImpact": 85},
        "governance": {"score": 87, "boardIndependence": 90, "executiveComp": 83, "transparency": 88},
        "overallScore": 81,
        "isNifty50": True
    },
    {
        "id": "nifty_6",
        "name": "Hindustan Unilever",
        "sector": "FMCG",
        "environmental": {"score": 91, "carbonEmissions": 89, "renewableEnergy": 94, "wasteManagement": 90},
        "social": {"score": 88, "employeeSafety": 85, "diversity": 90, "communityImpact": 89},
        "governance": {"score": 86, "boardIndependence": 88, "executiveComp": 83, "transparency": 87},
        "overallScore": 88,
        "isNifty50": True
    },
    {
        "id": "nifty_7",
        "name": "ITC",
        "sector": "FMCG",
        "environmental": {"score": 79, "carbonEmissions": 75, "renewableEnergy": 82, "wasteManagement": 80},
        "social": {"score": 85, "employeeSafety": 87, "diversity": 81, "communityImpact": 87},
        "governance": {"score": 83, "boardIndependence": 85, "executiveComp": 80, "transparency": 84},
        "overallScore": 82,
        "isNifty50": True
    },
    {
        "id": "nifty_8",
        "name": "Bajaj Finance",
        "sector": "Financial Services",
        "environmental": {"score": 71, "carbonEmissions": 73, "renewableEnergy": 67, "wasteManagement": 73},
        "social": {"score": 79, "employeeSafety": 81, "diversity": 75, "communityImpact": 81},
        "governance": {"score": 84, "boardIndependence": 87, "executiveComp": 80, "transparency": 85},
        "overallScore": 78,
        "isNifty50": True
    },
    {
        "id": "nifty_9",
        "name": "Larsen & Toubro",
        "sector": "Engineering",
        "environmental": {"score": 73, "carbonEmissions": 70, "renewableEnergy": 75, "wasteManagement": 74},
        "social": {"score": 81, "employeeSafety": 85, "diversity": 76, "communityImpact": 82},
        "governance": {"score": 86, "boardIndependence": 88, "executiveComp": 83, "transparency": 87},
        "overallScore": 80,
        "isNifty50": True
    },
    {
        "id": "nifty_10",
        "name": "Asian Paints",
        "sector": "Paints",
        "environmental": {"score": 84, "carbonEmissions": 81, "renewableEnergy": 87, "wasteManagement": 84},
        "social": {"score": 80, "employeeSafety": 82, "diversity": 76, "communityImpact": 82},
        "governance": {"score": 82, "boardIndependence": 84, "executiveComp": 79, "transparency": 83},
        "overallScore": 82,
        "isNifty50": True
    }
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
    # Group by sector and compute averages
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
st.title("NIFTY 50 ESG Analysis & Comparison Tool")

if 'companies' not in st.session_state:
    st.session_state.companies = nifty50_data.copy()

# -- Tabs for navigation like React's useState(activeTab)
tabs = st.tabs(["NIFTY50 Companies", "Custom Comparison", "Sector Analytics"])

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
    **{company['name']}**  \n
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
                "name": name,
                "sector": sector,
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

    # Custom companies table
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
            } for c in custom_companies
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
                    } for c in data
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

import numpy as np

# --- Insert inside the app below st.title() or in the NIFTY50 Companies tab ---

st.subheader("Nifty 50: Average ESG Scores (Current Year)")
df_all = pd.DataFrame([
    {
        "Environmental": c["environmental"]["score"],
        "Social": c["social"]["score"],
        "Governance": c["governance"]["score"]
    }
    for c in st.session_state.companies if c["isNifty50"]
])
avg_scores = df_all.mean()
st.bar_chart(avg_scores)

import altair as alt

df_esg = pd.DataFrame([
    {"Company": c["name"],
     "Sector": c["sector"],
     "Overall ESG": c["overallScore"]}
    for c in st.session_state.companies if c["isNifty50"]
])
chart = alt.Chart(df_esg).mark_circle(size=80).encode(
    x='Sector',
    y='Overall ESG',
    color='Sector',
    tooltip=['Company', 'Overall ESG']
).properties(width=700,height=400)
st.altair_chart(chart, use_container_width=True)

df_long = pd.melt(df_all, var_name='Factor', value_name='Score')
chart2 = alt.Chart(df_long).mark_boxplot().encode(
    x='Factor',
    y='Score',
    color='Factor'
).properties(width=600)
st.altair_chart(chart2, use_container_width=True)

df_top10 = pd.DataFrame([
    {"Company": c["name"],
     "ESG Score": c["overallScore"]}
    for c in st.session_state.companies if c["isNifty50"]
]).sort_values("ESG Score", ascending=False).head(10)
st.subheader("Top 10 Nifty 50 Companies: ESG Score")
st.bar_chart(df_top10.set_index("Company"))

df_stack = pd.DataFrame([
    {
        "Company": c["name"],
        "Environmental": c["environmental"]["score"],
        "Social": c["social"]["score"],
        "Governance": c["governance"]["score"]
    }
    for c in st.session_state.companies if c["isNifty50"]
]).head(10)  # Top 10 for clarity
df_stack = df_stack.set_index("Company")
st.subheader("ESG Component Distribution (Top 10 Companies)")
st.bar_chart(df_stack)

import pandas as pd
import streamlit as st
import altair as alt

# Load your full ESG dataset (update 'your_esg_file.csv' or DataFrame name as needed)
# df = pd.read_csv('your_esg_file.csv')
# For this example, use an in-memory DataFrame:


# -- Multi-company ESG trend line chart
st.subheader("ESG Score Trend Lines (All Listed Companies, 2019–2023)")

chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Year:O', title='Year'),
    y=alt.Y('ESG Score:Q', title='ESG Score', scale=alt.Scale(domain=[df['ESG Score'].min() - 5, df['ESG Score'].max() + 5])),
    color=alt.Color('Company:N', legend=alt.Legend(title="Company")),
    tooltip=['Company', 'Year', 'ESG Score']
).properties(width=800, height=450)

st.altair_chart(chart, use_container_width=True)

# (Optional) Add overall index average as a thicker black trend line
avg_df = df.groupby('Year', as_index=False)['ESG Score'].mean()
avg_chart = alt.Chart(avg_df).mark_line(color='black', strokeDash=[5,5], size=3).encode(
    x='Year:O',
    y='ESG Score:Q',
    tooltip=['Year', 'ESG Score']
)
st.altair_chart(chart + avg_chart, use_container_width=True)

years = [2019, 2020, 2021, 2022, 2023]
historical_avg_esg = [72, 74, 76, 78, 81]  # Example; update with real data if available
df_trend = pd.DataFrame({'Year': years, 'Average ESG Score': historical_avg_esg})

st.subheader("Nifty 50: ESG Score Trend (Last 5 Years)")
st.line_chart(df_trend.set_index('Year'))


# ---------------------------------------------------------------
# Tab 3: Sector-level Analytics (Averages by Sector)
# ---------------------------------------------------------------
with tabs[3]:
    st.header("Data & Trend Analysis")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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


st.caption("© NIFTY 50 ESG Dashboard, Streamlit version.")    
