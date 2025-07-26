import streamlit as st
import pandas as pd

st.set_page_config(page_title="ESG Score Calculator", layout="wide")

if "companies" not in st.session_state:
    st.session_state.companies = []

def calculate_esg_score(company):
    env = company["environmental"]
    soc = company["social"]
    gov = company["governance"]

    env_score = round((env["carbonEmissions"] + env["renewableEnergy"] + env["wasteManagement"]) / 3)
    soc_score = round((soc["employeeSafety"] + soc["diversity"] + soc["communityImpact"]) / 3)
    gov_score = round((gov["boardIndependence"] + gov["executiveComp"] + gov["transparency"]) / 3)
    overall = round((env_score + soc_score + gov_score) / 3)

    return env_score, soc_score, gov_score, overall

def get_improvement_areas(company):
    areas = []
    if company["environmental_score"] < 70:
        areas.append("Environmental practices need improvement")
    if company["social_score"] < 70:
        areas.append("Social responsibility initiatives required")
    if company["governance_score"] < 70:
        areas.append("Governance structure needs strengthening")
    return areas

st.title("ESG Score Calculator")
st.markdown("Evaluate companies based on Environmental, Social, and Governance factors for better financial decisions.")

with st.expander("➕ Add New Company"):
    with st.form("add_company"):
        name = st.text_input("Company Name")
        sector = st.text_input("Sector (e.g., Technology, Healthcare)")
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
            company = {
                "name": name,
                "sector": sector,
                "environmental": {
                    "carbonEmissions": c_emissions,
                    "renewableEnergy": r_energy,
                    "wasteManagement": w_management
                },
                "social": {
                    "employeeSafety": emp_safety,
                    "diversity": diversity,
                    "communityImpact": c_impact
                },
                "governance": {
                    "boardIndependence": b_indep,
                    "executiveComp": exec_comp,
                    "transparency": transparency
                }
            }
            env_score, soc_score, gov_score, overall = calculate_esg_score(company)
            company.update({
                "environmental_score": env_score,
                "social_score": soc_score,
                "governance_score": gov_score,
                "overall_score": overall
            })
            st.session_state.companies.append(company)
            st.success("Company added!")

if len(st.session_state.companies) == 0:
    st.info('No companies added yet.')
else:
    st.header("Company Comparison Table")
    df = pd.DataFrame([
        {
            "Company": c["name"],
            "Sector": c["sector"],
            "Environmental": c["environmental_score"],
            "Social": c["social_score"],
            "Governance": c["governance_score"],
            "Overall ESG": c["overall_score"]
        }
        for c in st.session_state.companies
    ])
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.header("Detailed Company Analysis")
    selected = st.selectbox("Select a company to view details", [c["name"] for c in st.session_state.companies])
    comp = next(c for c in st.session_state.companies if c["name"] == selected)
    st.subheader(f"{comp['name']} ({comp['sector']})")
    st.metric("Overall ESG Score", comp["overall_score"])
    st.progress(comp["overall_score"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Environmental", comp["environmental_score"])
    col2.metric("Social", comp["social_score"])
    col3.metric("Governance", comp["governance_score"])

    st.markdown("#### Areas for Improvement")
    areas = get_improvement_areas(comp)
    if areas:
        for area in areas:
            st.warning(area)
    else:
        st.success("Strong performance across all ESG categories!")

