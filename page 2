import streamlit as st
import pandas as pd

st.set_page_config(page_title="ESG Score Calculator", layout="wide")

# ---- Default Companies (NIFTY 50 sample) ----
default_companies = [
    {
        "name": "Reliance Industries",
        "sector": "Oil & Gas",
        "environmental": {"carbonEmissions": 55, "renewableEnergy": 70, "wasteManagement": 70},
        "social": {"employeeSafety": 75, "diversity": 68, "communityImpact": 73},
        "governance": {"boardIndependence": 80, "executiveComp": 75, "transparency": 80}
    },
    {
        "name": "Tata Consultancy Services",
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

def calculate_esg_score(c):
    # Compute category scores and overall
    env = c["environmental"]
    soc = c["social"]
    gov = c["governance"]
    env_score = round((env["carbonEmissions"] + env["renewableEnergy"] + env["wasteManagement"]) / 3)
    soc_score = round((soc["employeeSafety"] + soc["diversity"] + soc["communityImpact"]) / 3)
    gov_score = round((gov["boardIndependence"] + gov["executiveComp"] + gov["transparency"]) / 3)
    overall = round((env_score + soc_score + gov_score) / 3)
    return env_score, soc_score, gov_score, overall

def process_init_company_list(company_dicts):
    # add scores per company
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
        })
    return processed

if "companies" not in st.session_state:
    st.session_state.companies = process_init_company_list(default_companies)

# --- Functions for UI rendering ---
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
    return areas

def get_sector_insights(companies):
    sector_avg = {}
    by_sector = {}
    for c in companies:
        by_sector.setdefault(c["sector"], []).append(c)
    for s, comps in by_sector.items():
        avg = round(sum(x["overallScore"] for x in comps) / len(comps))
        sector_avg[s] = avg
    return sector_avg

# --- UI ---
st.title("ESG Score Calculator")
st.markdown("Evaluate **NIFTY 50** companies based on Environmental, Social, and Governance factors for smarter investment!")

companies = st.session_state.companies
sectors = sorted(set(c["sector"] for c in companies))

# ---- Quick Stats ----
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Excellent ESG", sum(c["overallScore"] >= 80 for c in companies))
with col2:
    st.metric("Good ESG", sum(60 <= c["overallScore"] < 80 for c in companies))
with col3:
    st.metric("Needs Improvement", sum(c["overallScore"] < 60 for c in companies))
with col4:
    st.metric("Average Score", round(sum(c["overallScore"] for c in companies) / len(companies)))

st.markdown("---")

# ---- Sector Filter and Sort ----
with st.sidebar:
    st.header("Filters & Controls")
    filter_sector = st.selectbox("Sector", ["All Sectors"] + sectors, index=0)
    sort_options = {
        "Overall ESG Score (desc)": "overallScore",
        "Environmental Score (desc)": "environmental.score",
        "Social Score (desc)": "social.score",
        "Governance Score (desc)": "governance.score",
        "Company Name (A-Z)": "name",
        "Sector (A-Z)": "sector"
    }
    sort_by = st.selectbox("Sort by", list(sort_options.keys()))
    st.markdown("---")
    add_new = st.button("➕ Add Company")

# -- Filtering and Sorting --
def get_for_sort(company, key):
    if key in ["overallScore", "name", "sector"]:
        val = company[key]
    elif key == "environmental.score":
        val = company["environmental"]["score"]
    elif key == "social.score":
        val = company["social"]["score"]
    elif key == "governance.score":
        val = company["governance"]["score"]
    else:
        val = company["overallScore"]
    return val

filtered = companies if filter_sector == "All Sectors" else [c for c in companies if c["sector"] == filter_sector]
sort_key = sort_options[sort_by]
reverse = not (sort_key in ["name", "sector"])
filtered = sorted(filtered, key=lambda c: get_for_sort(c, sort_key), reverse=reverse)

# ---- Main Table ----
st.subheader("NIFTY 50 ESG Comparison")
df_records = []
for c in filtered:
    df_records.append({
        "Company": f"{c['name']}",
        "Sector": c["sector"],
        "Env": f"{get_score_color(c['environmental']['score'])} {c['environmental']['score']}",
        "Soc": f"{get_score_color(c['social']['score'])} {c['social']['score']}",
        "Gov": f"{get_score_color(c['governance']['score'])} {c['governance']['score']}",
        "Overall ESG": f"{get_score_color(c['overallScore'])} {c['overallScore']}"
    })
st.dataframe(pd.DataFrame(df_records), use_container_width=True, hide_index=True)

# ---- Company Detail and Sector Analysis ----
cols = st.columns([2, 1])
with cols[0]:
    if len(filtered) > 0:
        company_names = [c["name"] for c in filtered]
        selected_name = st.selectbox("View details of...", company_names, key="selected_company")
        selectedCompany = next(c for c in filtered if c["name"] == selected_name)
    else:
        selectedCompany = None

with cols[1]:
    st.markdown("#### Sector ESG Performance")
    for sector, avg in get_sector_insights(companies).items():
        color = "🟢" if avg >= 80 else "🟡" if avg >= 60 else "🔴"
        st.write(f"{sector}: {color} {avg}")

if selectedCompany:
    st.markdown(f"## {selectedCompany['name']} ({selectedCompany['sector']})")

    c, s, g, o = selectedCompany["environmental"]["score"], selectedCompany["social"]["score"], selectedCompany["governance"]["score"], selectedCompany["overallScore"]
    st.markdown(
        f'''**Overall ESG Score:** <span style="font-size:1.5em">{get_score_color(o)} {o}/100</span>''',
        unsafe_allow_html=True
    )
    st.progress(o, text="Overall ESG Score")
    st.write("**Environmental:**", get_score_color(c), c)
    st.write(f"→ Carbon: {selectedCompany['environmental']['carbonEmissions']} | Renewable: {selectedCompany['environmental']['renewableEnergy']} | Waste: {selectedCompany['environmental']['wasteManagement']}")
    st.write("**Social:**", get_score_color(s), s)
    st.write(f"→ Safety: {selectedCompany['social']['employeeSafety']} | Diversity: {selectedCompany['social']['diversity']} | Community: {selectedCompany['social']['communityImpact']}")
    st.write("**Governance:**", get_score_color(g), g)
    st.write(f"→ Board: {selectedCompany['governance']['boardIndependence']} | Exec Pay: {selectedCompany['governance']['executiveComp']} | Transparency: {selectedCompany['governance']['transparency']}")

    st.markdown("**Areas for Improvement:**")
    areas = get_improvement_areas(selectedCompany)
    if not areas:
        st.success("Strong performance across all ESG categories.")
    else:
        for a in areas:
            st.warning(a)

# ---- Add Company Modal ----
if add_new:
    with st.form("add_company_form", clear_on_submit=True):
        st.markdown("### Add New Company")
        name = st.text_input("Company Name")
        sector = st.text_input("Sector (e.g., Technology, Banking, FMCG)")
        st.markdown("#### Environmental Factors (0-100)")
        c_emissions = st.number_input("Carbon Emissions", 0, 100, 0)
        r_energy = st.number_input("Renewable Energy", 0, 100, 0)
        w_management = st.number_input("Waste Management", 0, 100, 0)
        st.markdown("#### Social Factors (0-100)")
        emp_safety = st.number_input("Employee Safety", 0, 100, 0)
        diversity = st.number_input("Diversity & Inclusion", 0, 100, 0)
        c_impact = st.number_input("Community Impact", 0, 100, 0)
        st.markdown("#### Governance Factors (0-100)")
        b_indep = st.number_input("Board Independence", 0, 100, 0)
        exec_comp = st.number_input("Executive Compensation", 0, 100, 0)
        transparency = st.number_input("Transparency", 0, 100, 0)
        submit = st.form_submit_button("Add Company")

        if submit and name and sector:
            new_company = {
                "name": name,
                "sector": sector,
                "environmental": {"carbonEmissions": c_emissions, "renewableEnergy": r_energy, "wasteManagement": w_management},
                "social": {"employeeSafety": emp_safety, "diversity": diversity, "communityImpact": c_impact},
                "governance": {"boardIndependence": b_indep, "executiveComp": exec_comp, "transparency": transparency}
            }
            env_score, soc_score, gov_score, overall = calculate_esg_score(new_company)
            new = {
                "id": max([c["id"] for c in companies])+1 if companies else 1,
                "name": name,
                "sector": sector,
                "environmental": {**new_company["environmental"], "score": env_score},
                "social": {**new_company["social"], "score": soc_score},
                "governance": {**new_company["governance"], "score": gov_score},
                "overallScore": overall,
            }
            st.session_state.companies.append(new)
            st.success("Company added successfully!")

