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

# Replace this sample with your true dataset
data = [
  Symbol,company,Sector,Industry,Description,esg_risk_score_2024,predicted_future_esg_score,esg_risk_exposure,esg_risk_management,esg_risk_level,Material ESG Issues 1,Material ESG Issues 2,Material ESG Issues 3,,Controversy Level,controversy_score
ADANIENT,Adani Enterprises Ltd.,Energy,Metals & Mining,"Adani Enterprises Limited, together with its subsidiaries, operates as a conglomerate company in India and internationally. It operates through Integrated Resources Management, Mining Services, Commercial Mining, New Energy Ecosystem, Airport, Road, and Others segments. The company offers transport and logistics services; and manufactures cement, hydrogen and its derivatives, polysilicon, ingots, wafers, solar cells with modules, wind turbines, generators, electrolysers, and fuel cells, as well as ammonia and urea. It offers integrated coal management services; imports apples, pears, kiwis, oranges, grapes, and other fruits; markets fruits under the FARM-PIK brand; generates solar and wind energy; and manufactures solar panels. The company is also involved in the mining of iron ore, copper, and aluminum properties; and minerals, such as limestone, chromite, diamond, bauxite, and graphite, as well as mining and trading of coal. In addition, it offers edible oils, rice, pulses, besan, and wheat flour, as well as specialty fats, and oleo chemicals under the Fortune, King's, Bullet, Raag, Avsar, Pilaf, Jubilee, Fryola, Alpha, and Aadhar brands; and manufactures polyvinyl chloride, caustic soda, tar, hydrated lime, etc. Further, the company manufactures fighter aircraft, unmanned aerial systems, helicopters, submarines, air defense guns, and missiles and small arms; develops avionics and systems, opto-electronics, aero structures and components, aerospace composites, and radar and electronic warfare systems, as well as constructs national highways, motorways, tunnels, metro-rail, railways, etc. Additionally, it engages in the sewage and wastewater treatment, recycle, and reuse business; and operates, manage, and develops airports; and develops and operates data centers. The company was founded in 1988 and is headquartered in Ahmedabad, India. Adani Enterprises Limited operates as a subsidiary of S.B. Adani Family Trust.",32.9,33.23703095,Medium,Average,Medium,Business Ethics,Carbon,Human Capital,,High Controversy Level,4
ADANIPORTS,Adani Ports and Special Economic Zone Ltd.,Industrials,Services,"Adani Ports and Special Economic Zone Limited, together with its subsidiaries, operates and maintains port infrastructure facilities in India. The company operates ports and terminals, including bulk and break bulk, container, liquid, LPG, LNG, and crude cargos. It also engages in the ports related infrastructure development activities; and development of infrastructure at contiguous Special Economic Zone at Mundra. In addition, it offers logistic services, which includes logistic parks, container rail and bulk cargo logistic solutions, and warehousing, as well as auto, road, and agriculture logistic services. Further, the company operates a fleet of dredging and reclamation service equipment comprising cutter suction, trailing suction hopper, grab, inland cutter suction, water injection, and specialized dredgers, as well as split hopper and jack up barges, and floating cranes. Additionally, it offers non-scheduled passenger airline; hospital and related services; and marine services, such as pilotage, laying, and maintenance of buoys. The company also engages in development, construction, operation, and maintenance of railway corridors; and land development activities. The company was incorporated in 1998 and is headquartered in Ahmedabad, India.",12.6,14.823,Low,Strong,Low,Occupational Health & Safety,Land Use & Biodiversity,Community Relations,,High Controversy Level,4
APOLLOHOSP,Apollo Hospitals Enterprise Ltd.,Healthcare,Healthcare,"Apollo Hospitals Enterprise Limited, together with its subsidiaries, provides healthcare services in India and internationally. It operates through Healthcare Services, Retail Health & Diagnostics, Digital Health & Pharmacy Distribution, and Others segments. The company's healthcare facilities comprise primary, secondary, and tertiary care facilities. It offers services in cardiac sciences, orthopedics, oncology, neurosciences, emergency, robotic surgery, and transplants; and cardiology, neurology, gastroenterology, dermatology, ophthalmology, pediatric, endocrinology, gynecology, urology, nephrology, pulmonology, rheumatology, neurosurgery, radiology, plastic-surgery, neonatology, vascular-surgery, psychiatry, dentistry, ear, nose, and throat care services. The company also provides other services, such as project consultancy, health insurance, medical colleges, medvarsity for e-learning, and research services. In addition, it operates pharmacies, primary care clinics, birthing centers, specialized birthing centers, dialysis centers, cradle and fertility centers, diabetes management centers, single specialty clinics, primary health centers and diagnostic chains, dental clinics, and daycare and home healthcare centers. Further, the company engages in the business of bio-banking of tissues. The company serves through national retail healthcare centers and genomics institutes, as well as Apollo 24/7, a digital health platform; and www.apollopharmacy.in, an online pharmacy. Apollo Hospitals Enterprise Limited was incorporated in 1979 and is based in Chennai, India.",25,25.231625,Medium,Strong,Medium,Human Capital,Product Governance,Business Ethics,,Moderate Controversy Level,2
ASIANPAINT,Asian Paints Ltd.,Basic Materials,Consumer Durables,"Asian Paints Limited, together with its subsidiaries, engages in the manufacturing, selling, and distribution of paints, coatings, and products related to home decoration and bath fittings in Asia, the Middle East, Africa, and the South Pacific region. The company offers wall coverings; textures painting aids; waterproofing products; wall stickers; mechanized tools; adhesives; modular kitchens and wardrobes; bath fittings and sanitaryware; decorative lighting products; fabrics, furniture, furnishings, and rugs; and unplasticized polyvinyl chloride windows and door systems, as well as personalized interior design, safe painting, and color consulting services. It also provides interior and exterior wall finishes, wood finishes, enamels, tools, undercoats, thinners, and varnishers. The company offers its products under the Asian Paints, SCIB Paints, Apco Coatings, Asian Paints Berger, Taubman, Asian Paints Causeway, and Kadisco Asian Paints brand names through a network of dealers and retail stores, as well as operates asianpaints.com, an online shop. Asian Paints Limited was founded in 1942 and is headquartered in Mumbai, India.",25.4,26.52641667,Medium,Strong,Medium,Occupational Health & Safety,Environmental & Social Impact of Products & Services,"Emissions, Effluents & Waste",,Low Controversy Level,1
AXISBANK,Axis Bank Ltd.,Financial Services,Financial Services,"Axis Bank Limited provides various financial products and services. It operates through four segments: Treasury, Retail Banking, Corporate/Wholesale Banking, and Other Banking Business. The Treasury segment is involved in investments in sovereign and corporate debt, and equity and mutual funds, as well as in trading operations, derivative trading, and foreign exchange operations. The Retail Banking segment engages in the provision of lending services to individuals/small businesses, liability products, card services, internet banking, mobile banking, ATM services, depository, financial advisory services, NRI services, and digital banking services. The Corporate/Wholesale Banking segment offers corporate advisory, placements and syndication, project appraisals, trade finance products, letter of credits, bank guarantees, commercial cards, and cash management services. The Other Banking Business segment is involved in para banking activities. It also offers life and non-life insurance products; and government small saving schemes and pension schemes. The company operates multiple branches; ATMs; and recyclers in India. It also has international offices with branches in Singapore and Dubai, and representative offices in Dhaka, Dubai, Abu Dhabi, and Sharjah. The company was formerly known as UTI Bank Limited and changed its name to Axis Bank Limited in July 2007. The company was incorporated in 1993 and is based in Mumbai, India.",24.2,28.3514119,Medium,Strong,Medium,Data Privacy & Cybersecurity,Business Ethics,Product Governance,,Significant Controversy Level,3
BAJAJ-AUTO,Bajaj Auto Ltd.,Consumer Cyclical,Automobile and Auto Components,"Bajaj Auto Limited develops, manufactures, and distributes automobiles in India. It operates through Automotive, Investments, and Others segments. The company offers motorcycles, commercial vehicles, electric two-wheelers, and three-wheeler, as well as related parts. It also exports its products. The company was founded in 1945 and is based in Pune, India.",17,17.4,Low,Average,Low,Carbon,"Emissions, Effluents & Waste",Occupational Health & Safety,,Low Controversy Level,1
BAJFINANCE,Bajaj Finance Ltd.,Financial Services,Financial Services,"Bajaj Finance Limited operates as a deposit-taking non-banking financial company in India. The company offers consumer finance, which includes durable, lifestyle, digital product, EMI card, two and three wheeler, personal loan, loan against fixed deposit, extended warranty, home and gold loans, retail EMI, retailer finance, e-commerce, and co-branded credit card and wallets. It also provides SME finance; and loan against property and shares, lease rental discounting, business and professional loans, working capital loans, and developer and used car finance. In addition, the company offer commercial lending, such as short-term and flexible loan solutions; vendor financing including large value lease rental discounting, loans against securities, financial institution lending, light engineering and corporate finance, and warehouse financing; investment services in fixed deposit and mutual funds; and partnership and services comprising insurance services. Bajaj Finance Limited was formerly known as Bajaj Auto Finance Limited. The company was incorporated in 1987 and is based in Pune, India. Bajaj Finance Limited is a subsidiary of Bajaj Finserv Ltd.",18.5,19.274,Medium,Strong,Low,Data Privacy & Cybersecurity,Product Governance,Business Ethics,,Low Controversy Level,1
BAJAJFINSV,Bajaj Finserv Ltd.,Financial Services,Financial Services,"Bajaj Finserv Ltd., through its subsidiaries, provides financial services in India. The company operates through Life Insurance, General Insurance, Windpower, Retail Financing, and Investments and Others segments. It offers personal, business, home, commercial, and gold loans; two and three wheeler loans; mortgages; education loans; unsecured and secured loans to small and medium-sized enterprises, micro, small and medium enterprises, and professionals; loans against properties; financing for products, such as consumer durable, digital, lifecare, furniture, etc.; and lease rental discounting products. The company also provides investment products, including fixed deposits, demat accounts, systematic deposit plans, and mutual funds; savings products; life, health, motor, car, two-wheeler, marine, home, crop, and pocket insurance products; wealth management and retirement planning services; healthcare needs for the family; and wallets and credit cards. In addition, it offers pocket subscription plans; bill and recharge services; and trading account, margin trading, and HNI and retail broking services. Further, the company owns and operates 138 windmills with total installed capacity of 65.2 megawatts. Bajaj Finserv Ltd. was incorporated in 2007 and is based in Pune, India.",26.5,25.95716667,Medium,Average,Medium,Product Governance,ESG Integration,Data Privacy & Cybersecurity,,Low Controversy Level,1
BPCL,Bharat Petroleum Corporation Ltd.,Energy,Oil Gas & Consumable Fuels,"Bharat Petroleum Corporation Limited refines crude oil and markets petroleum products in India. It operates through two segments: Downstream Petroleum, and Exploration and Production of Hydrocarbons. The company operates fuel stations that sell petrol, diesel, automotive liquefied petroleum gas (LPG), and compressed natural gas. It also provides Bharatgas fuels; MAK lubricants, such as automotive engine oils, gear oils, greases, and specialties, as well as industrial lubricants; and aviation fuel services to airlines. In addition, the company offers industrial fuels products, such as white oil, black oil, bitumen, sulphur, petcoke, propylene, petchem, and solvents products; and bunkering facilities. Further, it imports and exports petroleum products, as well as engages in the natural gas business. Its marketing infrastructure includes a network of installations, depots, retail outlets, aviation fuelling stations, and LPG distributors. The company was formerly known as Bharat Refineries Limited and changed its name to Bharat Petroleum Corporation Limited in August 1977. Bharat Petroleum Corporation Limited was incorporated in 1952 and is based in Mumbai, India.",37.8,34.99188095,High,Average,High,Carbon,"Emissions, Effluents & Waste",Occupational Health & Safety,,Moderate Controversy Level,2
BHARTIARTL,Bharti Airtel Ltd.,Communication Services,Telecommunication,"Bharti Airtel Limited operates as a telecommunications company in Asia and Africa. It operates through Mobile Services India, Mobile Services Africa, Mobile Services South Asia, Airtel Business, Tower Infrastructure Services, Homes Services, Digital TV Services, and Others segments. The company engages in provision of voice and data telecom services through wireless technology including 2G/3G/4G/5G services; and operates as a single point of contact for telecommunication across data and voice, network integration, and managed services. It also provides services related to setting up, operation, and maintenance of wireless communication towers; and voice and data communications services through fixed-line network and broadband technology for homes, as well as offers digital broadcasting services under the DTH platform. In addition, the company offers post-paid, prepaid, roaming, internet, and various value-added services, as well as Mobile TV, video calls, live-streaming videos, gaming and buffer-less HD and 4K video streaming, other services; and network integration, data centers, managed services, enterprise mobility applications and digital media services. The company was formerly known as Bharti Tele-Ventures Limited and changed its name to Bharti Airtel Limited in April 2006. Bharti Airtel Limited was incorporated in 1995 and is headquartered in New Delhi, India.",19.5,19.599,Medium,Strong,Low,Business Ethics,Data Privacy & Cybersecurity,Human Capital,,Significant Controversy Level,3
BRITANNIA,Britannia Industries Ltd.,Consumer Defensive,Fast Moving Consumer Goods,"Britannia Industries Limited manufactures and sells various food products in India. It offers bakery products, such as biscuits, breads, cakes, and rusks; dairy products, including milk-based beverages, cheese, dahi, and dairy whiteners; and cream wafers, center filled croissants, and salted snacks. The company offers its biscuits under the Good Day, Crackers, NutriChoice, Marie Gold, Tiger, Milk Bikis, Jim Jam + Treat, Bourbon, Little Hearts, Pure Magic, Nice Time, 50-50, Biscafe, and Chocolush brand names; and cakes under the Gobbles, Tiffin Fun, Nut & Raisin, Muffills, Layerz, Rollyo, and Fudgeit brand names, as well as rusks under the Toastea brand and center filled croissants under the Treat brand. It exports its products to approximately 70 countries worldwide. Britannia Industries Limited was founded in 1892 and is based in Bengaluru, India.",26,26.04994524,Medium,Strong,Medium,Carbon,Environmental & Social Impact of Products & Services,Product Governance,,Low Controversy Level,1
CIPLA,Cipla Ltd.,Healthcare,Healthcare,"Cipla Limited, together with its subsidiaries, manufactures, develops, and sells pharmaceutical products in India, the United States, South Africa, and internationally. The company operates through Pharmaceuticals and New ventures segments. It also offers active pharmaceutical ingredients; and formulations in various therapeutic areas, such as MI, angina, heart failure, hypertension, arrhythmia, lipid abnormalities and diabetes, obesity, HIV, respiratory, urology, oncology, cardio-metabolism, child health, infectious diseases and critical care, hepatitis, women's health, ophthalmology, and neuro psychiatry. In addition, the company provides respiratory products, including inhalers and nasal sprays, as well as other respiratory products consists of injectables and biosimilars. Further, it offers Easylax and Easylax L, a liquid paraffin for constipation. Cipla Limited was incorporated in 1935 and is based in Mumbai, India.",28.4,29.63553651,Medium,Average,Medium,Product Governance,Business Ethics,Access to Basic Services,,Moderate Controversy Level,2
COALINDIA,Coal India Ltd.,Energy,Oil Gas & Consumable Fuels,"Coal India Limited, together with its subsidiaries, produces and market coal and coal products in India. The company offers coking coal for use in steel making and metallurgical industries, and for hard coke manufacturing; and semi coking coal that is used as blend-able coal in steel making, merchant coke manufacturing, and other metallurgical industries. It provides non-coking coal that is used as thermal grade coal for power generation, as well as for cement, fertilizer, glass, ceramic, paper, chemical, and brick manufacturing, and other heating purposes. In addition, it offers beneficiated and washed non-coking coal for use in power generation; beneficiated non-coking coal for use in cement, sponge iron, and other industrial plants; and middling products for power generation and by domestic fuel plants, brick manufacturing units, cement plants, industrial plants, etc. Further, the company provides rejects that are used for fluidized bed combustion boilers for power generation, road repairs, briquette making, land filling, etc. Coal India Limited was incorporated in 1973 and is headquartered in Kolkata, India.",45.5,38.44051429,High,Average,Severe,Carbon,Community Relations,Occupational Health & Safety,,Moderate Controversy Level,2
DIVISLAB,Divi's Laboratories Ltd.,Healthcare,Healthcare,"Divi's Laboratories Limited engages in the manufacture and sale of generic active pharmaceutical ingredients (APIs) and intermediates, and nutraceutical ingredients in India, North America, Asia, Europe, and internationally. It also undertakes custom synthesis contract manufacturing services of APIs and intermediates; and supplies a range of carotenoids, such as beta carotene, astaxanthin, lycopene, and canthaxanthin, as well as other finished forms, including lutein, and vitamins to food, dietary supplement, and feed manufacturers industries. It also exports its products. The company was formerly known as Divi's Research Center and changed its name to Divi's Laboratories Limited in 1994. The company was incorporated in 1990 and is headquartered in Hyderabad, India.",32.8,32.26554167,Medium,Average,High,Product Governance,Access to Basic Services,Business Ethics,,Low Controversy Level,1
DRREDDY,Dr. Reddy's Laboratories Ltd.,Healthcare,Healthcare,"Dr. Reddy's Laboratories Limited, together with its subsidiaries, operates as an integrated pharmaceutical company worldwide. It operates through Global Generics, Pharmaceutical Services and Active Ingredients (PSAI), and Others segments. The company's Global Generics segment manufactures and markets prescription and over-the-counter finished pharmaceutical products that are marketed under a brand name or as a generic finished dosages with therapeutic equivalence to branded formulations. This segment also engages in the biologics business. The PSAI segment manufactures and markets active pharmaceutical ingredients and intermediates, which are principal ingredients for finished pharmaceutical products. This segment also provides contract research services; and manufactures and sells active pharmaceutical ingredients and steroids in accordance with the specific customer requirements. The Others segment engages in developing therapies in the fields of oncology and inflammation; research and development of differentiated formulations; and provides digital healthcare and information technology enabled business support services. The therapeutic categories primarily include gastro-intestinal, cardiovascular, anti-diabetic, dermatology, oncology, respiratory, stomatology, urology, and nephrology. Dr. Reddy's Laboratories Limited was incorporated in 1984 and is headquartered in Hyderabad, India.",26.6,28.58275317,Medium,Average,Medium,Product Governance,Business Ethics,Access to Basic Services,,Significant Controversy Level,3
EICHERMOT,Eicher Motors Ltd.,Consumer Cyclical,Automobile and Auto Components,"Eicher Motors Limited, an automobile company, engages in the manufacture and sale of motorcycles and commercial vehicles in India and internationally. It owns the Royal Enfield motorcycle brand that offers Classic 350, Bullet 350, Meteor 350, Hunter 350, Himalayan, Scram 411, Interceptor 650, Continental GT 650, Super Meteor 650, and Thunderbird models. The company also designs, develops, manufactures, assembles, and sells two-wheelers, as well as sells related parts and accessories and apparel. It offers through its joint venture, Volvo Eicher Commercial Vehicles Limited, manufactures and sells light and medium duty trucks, heavy duty trucks, and buses under the Eicher and Volvo brands, as well as provides medium-duty base engines, engineering components, and aggregates. The company was founded in 1901 and is headquartered in Gurugram, India.",13.3,14.90266667,Low,Average,Low,Carbon,Product Governance,Business Ethics,,Moderate Controversy Level,2
GRASIM,Grasim Industries Ltd.,Basic Materials,Construction Materials,"Grasim Industries Limited operates in fibre, yarn, pulp, chemicals, textile, fertilizers, and insulators businesses in India and internationally. The company operates through Viscose, Chemicals, Cement, Financial Services, and Others segments. It provides viscose staple fiber, a man-made biodegradable fiber for use in apparels, home textiles, dress materials, knit wear products, and non-woven applications; wood pulp products; viscose filament yarn, a natural fibre for manufacturing fabrics such as georgettes, crepes, chiffons, and others; and textile products, such as linen and wool. The company offers various chemical products, including chlor-alkali and epoxy resin products. In addition, it provides electrical insulators for transmission lines and substations, as well as equipment and railways. Further, the company offers grey cement; white cement; ready mix concrete; and cement-based putty. Additionally, it provides various financial services comprising non-bank financial, life insurance, asset management, housing finance, equity broking, wealth management, general insurance advisory, and health insurance services. The company involved in solar power designing, engineering procurement, and commissioning business. Grasim Industries Limited was incorporated in 1947 and is based in Mumbai, India.",43.1,36.47793095,Medium,Strong,Severe,Carbon,Environmental & Social Impact of Products & Services,Business Ethics,,Moderate Controversy Level,2
HCLTECH,HCL Technologies Ltd.,Technology,Information Technology,"HCL Technologies Limited offers software development, business process outsourcing, and infrastructure management services worldwide. The company operates through IT and Business Services; Engineering and R&D Services; and HCL Software segments. It offers digital business services, which includes digital consulting, data and AI, application development, maintenance, and modernization, software as a service, automation and integration, and enterprise application; and digital foundation services including digital foundation consulting and workplace, hybrid cloud, cybersecurity, network, intelligent operator, and unified services management services. The company also provides digital process operations, such as lending solution, supply chain management, finance and accounting, digital and content, and cognitive automation; and engineering and R&D services, which includes digital engineering, manufacturing operation, product engineering, and industry verticals. In addition, it offers CloudSMART, an adaptive portfolio of solutions enabling continuous modernization; IoT WoRKS, which offers digital transformation services; Career Shaper, earning and assessment platform for driving talent transformation; and HCLTech X, a cloud based digital platform that integrates content, commerce, and engagement tools. The company also provides engineering services and solutions for software, embedded, mechanical; modernized software products; and artificial intelligence solutions. The company serves aerospace and defense, energy and utilities, manufacturing, public sector, telecom, media and entertainment, captive business services, technology, mining and natural resources, retail, consumer goods, life sciences and healthcare, oil and gas, banking, insurance, capital markets, fintech, and financial crime compliance and risk, as well as travel, transport, logistics, and hospitality industries. HCL Technologies Limited was founded in 1976 and is headquartered in Noida, India.",12.9,13.56383333,Low,Strong,Low,Human Capital,Data Privacy & Cybersecurity,Business Ethics,,Moderate Controversy Level,2
HDFCBANK,HDFC Bank Ltd.,Financial Services,Financial Services,"HDFC Bank Limited provides banking and financial services to individuals and businesses in India, Bahrain, Hong Kong, and Dubai. The company operates in three segments: Wholesale Banking, Retail Banking, and Treasury Services. It accepts savings, salary, current, rural, public provident fund, pension, and demat accounts; fixed and recurring deposits; and safe deposit lockers, as well as offshore accounts and deposits, and overdrafts against fixed deposits. The company also provides personal, home, car, two-wheeler, business, doctor, educational, gold, consumer, and rural loans; loans against properties, securities, fixed deposits, rental receivables, and assets; loans for professionals; government sponsored programs; and loans on credit card, as well as working capital and commercial/construction equipment finance, healthcare/medical equipment and commercial vehicle finance, dealer finance, and term loans. In addition, it offers credit, debit, prepaid, and forex cards; payment and collection, export, import, remittance, bank guarantee, letter of credit, trade, hedging, and merchant and cash management services; insurance and investment products. Further, the company provides short term finance, bill discounting, structured finance, export credit, loan repayment, and documents collection services; online and wholesale, mobile, and phone banking services; unified payment interface, immediate payment, national electronic funds transfer, and real time gross settlement services; and channel financing, vendor financing, reimbursement account, money market, derivatives, employee trusts, cash surplus corporates, tax payment, and bankers to rights/public issue services, as well as financial solutions for supply chain partners and agricultural customers. It operates branches and automated teller machines in various cities/towns. The company was incorporated in 1994 and is headquartered in Mumbai, India.",30.6,30.979125,Medium,Average,High,Data Privacy & Cybersecurity,Product Governance,Business Ethics,,Moderate Controversy Level,2
HDFCLIFE,HDFC Life Insurance Company Ltd.,Financial Services,Financial Services,"HDFC Life Insurance Company Limited provides individual and group insurance solutions in India. It offers insurance and investment products, such as protection, pension, savings, investment, annuity, and health, as well as term, retirement, children, and unit linked insurance plans. The company was formerly known as HDFC Standard Life Insurance Company Limited changed its name to HDFC Life Insurance Company Limited in January 2019. HDFC Life Insurance Company Limited was incorporated in 2000 and is headquartered in Mumbai, India. HDFC Life Insurance Company Limited operates as a subsidiary of HDFC Bank Limited.",20.8,26.21291667,Medium,Strong,Medium,Product Governance,Data Privacy & Cybersecurity,Business Ethics,,Low Controversy Level,1
HEROMOTOCO,Hero MotoCorp Ltd.,Consumer Cyclical,Automobile and Auto Components,"Hero MotoCorp Limited manufactures and sells motorized two wheelers, spare parts, and related services in India, Asia, Central and Latin America, and Africa and Middle East. It offers motorcycles and scooters. The company provides engines, as well as related parts and accessories. The company was formerly known as Hero Honda Motors Ltd. and changed its name to Hero MotoCorp Limited in July 2011. Hero MotoCorp Limited was incorporated in 1984 and is based in New Delhi, India.",12.2,13.621,Low,Strong,Low,Product Governance,Business Ethics,Carbon,,Moderate Controversy Level,2
HINDALCO,Hindalco Industries Ltd.,Basic Materials,Metals & Mining,"Hindalco Industries Limited, together with its subsidiaries, produces and sells aluminum and copper products in India and internationally. It operates through Novelis, Aluminium Upstream, Aluminium Downstream, and Copper segments. The company offers alumina; primary aluminum in the form of ingots, billets, and wire rods; aluminum flat rolled products (FRP); aluminum extrusions; and aluminum foil and packaging solutions for use in the automotive and transport, building and construction, aerospace and defense, electrical and electronics, pharmaceuticals and packaging, consumer durables and kitchenware, and white goods industries, as well as industrial applications. It also provides coarse alumina hydrate for use in alum, poly aluminum chloride, zeolites, aluminum fluoride, sodium aluminate, glass, catalysts, and aluminum hydroxide gel; and fine alumina hydrates, as well as flame retardants and smoke suppressants in cables, rubbers, plastics, etc.; and calcined alumina for use in ceramics, refractories, and polishing. In addition, the company offers copper products, including copper cathodes and continuous cast copper rods that are used in the agrochemical, automotive and transport, consumer durable, electrical equipment, railway, wire and cable, and EV and renewables industries. Further, it operates an all-weather jetty in the Gulf of Khambhat on the west coast of India; produces di-ammonium phosphate and nitrogen phosphorus potassium complexes; and offers phosphoric acid, phosphogypsum, sulfuric acid, copper slag, and aluminum fluoride, as well as sells gold, silver, and other materials. The company offers its aluminum extrusion products under the Hindalco extrusions, Maxloader, Eternia, and Totalis brands; aluminum FRP under the Everlast brand; aluminum foils under the Freshwrapp and Superwrap brands; and copper products under the Birla Balwan brand. Hindalco Industries Limited was incorporated in 1958 and is based in Mumbai, India.",31.6,31.2641,High,Strong,High,Carbon,"Emissions, Effluents & Waste",Community Relations,,Significant Controversy Level,3
HINDUNILVR,Hindustan Unilever Ltd.,Consumer Defensive,Fast Moving Consumer Goods,"Hindustan Unilever Limited, a fast-moving consumer good company, manufactures and sells food, home care, personal care, and refreshment products in India and internationally. The company operates through Home Care, Beauty & Personal Care, Foods & Refreshment, and Others segments. The Home Care segment engages in detergent bars and powders, detergent liquids, scourers, water business, purifiers business, etc. The Beauty & Personal Care segment provides oral, skin, and hair care products; and soaps, deodorants, talcum powder, color cosmetics, salon services, etc. The Foods & Refreshment segment provides culinary products, including tomato-based products, fruit-based products, soups, etc.; and tea, coffee, nutrition drinks, ice-cream, and frozen desserts. The Others segment engages in activities, such as export, consignment, etc. The company is also involved in the job work, real estate, and discharge trust businesses. The company was founded in 1888 and is headquartered in Mumbai, India.",23.4,25.56881984,Medium,Strong,Medium,Resource Use,Environmental & Social Impact of Products & Services,Business Ethics,,Moderate Controversy Level,2
ICICIBANK,ICICI Bank Ltd.,Financial Services,Financial Services,"ICICI Bank Limited provides various banking products and services in India and internationally. It operates through Retail Banking, Wholesale Banking, Treasury, Other Banking, Life Insurance, and Others segments. The company offers savings, salary, pension, current, and other accounts; and time, fixed, recurring, and security deposits services. It also provides home, car, two-wheeler, personal, gold, and commercial business loans, as well as loans against securities and other loans; business loans, including working capital finance, term loans, collateral free loans, loans without financials, finance for importers and exporters, and overdraft facilities, as well as loans for new entities and card swipes; and credit, debit, prepaid, travel, forex, and corporate cards. In addition, the company offers pockets wallet; fixed income products; investment products, such as mutual funds, gold monetization schemes, initial public offerings, and other online investment services; and agri and rural business, farmer finance, tractor loans, and micro banking services, as well as other services to agri corporates. Further, it provides portfolio management, trade, foreign exchange, locker, private and NRI banking, and cash management services; family wealth and demat accounts; commercial and investment banking, capital market, custodial, and institutional banking services; health, personal accident, fire, and motor insurance, as well as distributes general and life insurance products; and Internet, mobile, and phone banking services. Additionally, the company offers securities investment, broking, trading, and underwriting services; and merchant banking, trusteeship, housing finance, pension fund management, asset management, investment advisory, points of presence, and private equity/venture capital fund management services. ICICI Bank Limited was founded in 1955 and is headquartered in Mumbai, India.",24,25.89101984,Medium,Strong,Medium,Business Ethics,Data Privacy & Cybersecurity,Product Governance,,Significant Controversy Level,3
ITC,ITC Ltd.,Consumer Defensive,Fast Moving Consumer Goods,"ITC Limited engages in the fast-moving consumer goods, hotels, paperboards and paper and packaging, agri, and information technology businesses in India and internationally. It primarily offers cigarettes and cigars; staples, spices, biscuits, confectionery and gums, snacks, noodles and pasta, beverages, dairy, ready to eat meals, chocolate, coffee, and frozen foods; personal care products; notebooks, pens and pencils, geometry boxes, erasers, sharpeners, rulers, wax and plastic crayons, sketch pens, and oil pastels; safety matches; and incense sticks under various brands. The company also operates approximately 120 hotels under the ITC Hotel, Mementos, Welcomhotel, Storii, Fortune, and WelcomHeritage brands; and Kaya Kalp spas. In addition, it offers virgin, recycled, barrier, biodegradable barrier, solid, and graphic boards, as well as specialty papers; and packaging products, such as carton board, flexible, tobacco, and green packaging products; and exports feed ingredients, food grains, marine products, processed fruits, coffee products, leaf tobacco products, and spices. Further, the company offers information technology services for the banking, financial services, consumer goods, manufacturing, travel, hospitality, and healthcare industries. Additionally, it provides property infrastructure and estate maintenance; engineering, procurement, and construction management services; project management consultancy services; business consulting, real estate development, and agro-forestry and other related services; manages and operates golf courses; fabricates and assembles machinery for tube filling; cartooning and wrapping services; conveyor solutions; and produces and commercializes seed potato technology products. ITC Limited was incorporated in 1910 and is headquartered in Kolkata, India.",28,29.47321151,Medium,Average,Medium,Product Governance,Environmental & Social Impact of Products & Services,Business Ethics,,Moderate Controversy Level,2
INDUSINDBK,IndusInd Bank Ltd.,Financial Services,Financial Services,"IndusInd Bank Limited provides various banking products and services to individuals, NRIs, business owners, corporates, and government and financial institutions. It operates through four segments: Treasury, Corporate/Wholesale Banking, Retail Banking, and Other Banking Operations. The company offers current, savings, defense, and corporate salary; and fixed and FCNR, sweep in/out deposits, senior citizen schemes, young saver deposits, and recurring and RFC deposits, as well as Rupee multiplier products. It also provides home, personal, car, two wheeler, gold, agricultural, and medical equipment loans, as well as loans against property and securities; micro-finance loans; MSME loans; business loans; loans to merchants and retailers; personal and professional loans; and loan on credit cards. In addition, the company offers transaction banking services, including letters of credit/guarantees, structured trade and export finance, and import finance solutions, as well as cash management and remittance services; investment products, such as demat account, mutual fund, gold bond, national pension system, and equity trading; project finance, supply chain financing; investment advisory, strategic M&A, and other advisory services; and health, general, life, and card protection insurance. Further, it provides debit, credit, forex, and commercial cards; individual outward remittances, foreign currency bank notes and demand drafts, and travelers cheques; financial inclusion products; trade and foreign exchange accounts; real estate developer financing and bullion services; correspondent banking services; and forex and derivative desk, information and advisory, and remittances through forex channel services. IndusInd Bank Limited was incorporated in 1994 and is based in Mumbai, India. IndusInd Bank Limited was incorporated in 1994 and is based in Mumbai, India.",30.1,31.04503333,Medium,Average,High,Data Privacy & Cybersecurity,Business Ethics,Product Governance,,Moderate Controversy Level,2
INFY,Infosys Ltd.,Technology,Information Technology,"Infosys Limited, together with its subsidiaries, provides consulting, technology, outsourcing, and next-generation digital services in North America, Europe, India, and internationally. It provides digital marketing and digital workplace, digital commerce, digital experience and interactions, metaverse, data analytics and AI, applied AI, generative AI, sustainability, blockchain, engineering, Internet of Things, enterprise agile DevOps, application modernization, cloud, digital process automation, digital supply chain, Microsoft business application and cloud business, service experience transformation, energy transition, cyber security, and quality engineering solutions; Oracle, SAP, and Saleforce solutions; API economy and microservices; and Topaz, an AI-first set of services, solutions, and platforms using generative AI technologies. The company's products and platforms include Finacle, a core banking solution; Edge suite of products; Panaya platform, Infosys Equinox, Infosys Helix, Infosys Applied AI, Infosys Cortex, and Stater digital platforms; and Infosys McCamish, an insurance platform. It serves aerospace and defense, agriculture, automotive, chemical manufacturing, communication, consumer packaged goods, education, engineering procurement and construction, healthcare, high technology, industrial manufacturing, information services and publishing, insurance, life science, logistics and distribution, media, entertainment, mining, oil and gas, private equity, professional, public, retail, travel, hospitality, utilities, and waste management industries. The company was formerly known as Infosys Technologies Limited and changed its name to Infosys Limited in June 2011. Infosys Limited was incorporated in 1981 and is headquartered in Bengaluru, India.",13.1,13.498,Low,Strong,Low,Data Privacy & Cybersecurity,Business Ethics,Human Capital,,Moderate Controversy Level,2
JSWSTEEL,JSW Steel Ltd.,Basic Materials,Metals & Mining,"JSW Steel Limited engages in the manufacture and sale of iron and steel products in India and internationally. It provides hot rolled and cold-rolled coils, galvanized, galvalume, electrical, and color coated steel products, as well as tin plate; and TMT bars, wire rods, and alloy steel products. The company is also involved in trades in steel and allied products, iron ore, steel, cement, paint, and other products; logistic infrastructure, real estate, mining, and coal loading; manufactures forged steel ball, slabs and hot rolled coils, plates, pipes, and double jointing; production of gaseous and liquid form of oxygen, nitrogen, argon, and other products recoverable from separation of air; and operates coke oven and pellet plant, and steel plant. Its products are used in automotive, general engineering, machinery, and projects and construction applications. The company was formerly known as Jindal Vijayanagar Steel Limited and changed its name to JSW Steel Limited in June 2005. JSW Steel Limited was founded in 1982 and is based in Mumbai, India.",36.7,33.00233333,High,Strong,High,Carbon,Community Relations,Occupational Health & Safety,,Significant Controversy Level,3
KOTAKBANK,Kotak Mahindra Bank Ltd.,Financial Services,Financial Services,"Kotak Mahindra Bank Limited provides a range of banking and financial services to corporate and individual customers in India. It operates through Treasury, BMU and Corporate Centre; Retail Banking; Corporate / Wholesale Banking; Vehicle Financing; Other Lending Activities; Broking; Advisory and Transactional Services; Asset Management; and Insurance segments. The company offers savings, current, and salary accounts; fixed, recurring, tax saving fixed, senior citizen and fixed deposit products; home, personal, business, payday, gold, education, Commercial Vehicle, car, and crop loans as well as loan against securities and properties; land-based project, construction equipment / infrastructure, farm equipment, healthcare, trade and supply chain, and working capital finance solutions; and credit and debit cards. It also provides Investment products; life, term, health, car, and two wheeler insurance; payment services; trade services; business management and marketing, enterprise resource planning, supply chain and logistics, human resource, business travel, workspace management, taxation and legal, and healthcare/medical equipment services; cash management services, such as digital payments, physical collections, digital collections, prepaid cards, and payment gateways; private banking services; net banking; and NRI services. Kotak Mahindra Bank Limited was incorporated in 1985 and is based in Mumbai, India.",19.1,18.539,Medium,Strong,Low,Data Privacy & Cybersecurity,Business Ethics,Product Governance,,Moderate Controversy Level,2
LTIM,LTIMindtree Ltd.,Technology,Information Technology,"LTIMindtree Limited, a technology consulting and digital solutions company, provides information technology services and solutions in India, North America, Europe, and internationally. The company operates through Banking, Financial Services & Insurance; Hi-Tech, Media & Entertainment; Manufacturing & Resources; Retail, CPG & Travel, Transport & Hospitality; and Health & Public Services. It offers cloud and infrastructure services, consulting, cyber security, data and insights, digital engineering, disruptive SaaS, enterprise application, platform operation, RPA, and testing services. The company serves various industries, such as banking and financial services, energy, utilities, healthcare, Hi-tech, insurance, life sciences, manufacturing, retail and consumer packaged goods, travel, transport, and hospitality, as well as communications, media, and entertainment industries. LTIMindtree Limited has a strategic collaboration agreement with Amazon Web Services, Inc.; a strategic partnership with eClinicalHealth Limited to enhance digital innovation in clinical trials management process for patient centric drug development, as well as with Aforza to deliver digital transformation in CRM and TPM across the consumer products industry; and a strategic collaboration with CAST AI to help businesses optimize their cloud investments. The company was formerly known as Larsen & Toubro Infotech Limited and changed its name to LTIMindtree Limited in November 2022. The company was incorporated in 1996 and is based in Mumbai, India. LTIMindtree Limited operates as a subsidiary of Larsen & Toubro Limited.",21.5,27.26077222,Medium,Average,Medium,Human Capital,Data Privacy & Cybersecurity,Business Ethics,,Moderate Controversy Level,2
LT,Larsen & Toubro Ltd.,Industrials,Construction,"Larsen & Toubro Limited engages in engineering, construction, and manufacturing operations worldwide. The Infrastructure segment engineers and constructs building and factories, transportation infrastructure, heavy civil infrastructure, power transmission and distribution, water and effluent treatment, and minerals, and metals. The Hydrocarbon segment provides front-end design, modular fabrication, procurement, project management, construction, installation, and commissioning for the oil and gas industry. The Power segment offers coal-based and gas-based thermal power plants, including power generation equipment with associated systems and balance-of-plant packages. The Heavy Engineering segment manufactures and supplies custom designed, engineered critical equipment and systems to the fertilizer, refinery, petrochemical, chemical, oil and gas, and thermal and nuclear power industries. The Defence Engineering segment designs, develops, produces, and supports equipment, systems, and platforms for the defense and aerospace sectors. This segment also designs, constructs, and repairs/refits defense vessels. The Others segment engages in the realty, smart world, and communication businesses, including military communications; marketing and servicing of construction and mining machinery and parts; and manufacturing and sale of rubber processing machinery. This segment also operates digital platforms, such as SuFin for B2B e-commerce; and EduTech offers engineering and technology related content. Larsen & Toubro Limited was founded in 1938 and is headquartered in Mumbai, India.",34.1,30.02483333,High,Strong,High,Bribery & Corruption,Human Capital,Carbon,,Moderate Controversy Level,2
M&M,Mahindra & Mahindra Ltd.,Consumer Cyclical,Automobile and Auto Components,"Mahindra & Mahindra Limited provides mobility products and farm solutions in India and internationally. The company operates through Automotive, Farm Equipment, Financial Services, Real Estate, Hospitality, and Others segments. It offers passenger and commercial vehicles, trucks, buses, vans, cars, utility vehicles, and electric vehicles; watercrafts; motorcycles, scooters, and mopeds; manufactures, assembles, and maintains various kinds of aircrafts and aircraft components, and aerostructures; offers construction equipment, such as backhoe loaders under the Mahindra EarthMaster brand; and road construction equipment comprising motor graders under the Mahindra RoadMaster brand. It is also involved in the provision of farm equipment, including tractors; and manufacture and distribute the SMART Seeder Mini-MAX in collaboration with Clean Seed Capital Group Ltd., as well as engages in renewable energy business. Further, the company offers financial services comprising retail and other loans, SME finance, housing finance, mutual funds, and life and non-life insurance broking services, as well as vehicle and equipment financing; provides logistics services; power backup solutions, such as diesel and gas generators; and technology services, including business process services, integrated engineering services, infrastructure and cloud services, application development and maintenance services. Additionally, it engages in the sale of timeshare and vacation ownership through its resorts; develops and sells residential properties, and engages in the development, management, and operation of commercial complexes; and processing and trading of steel for automotive, non-automotive, and power industries, as well as offers agriculture products comprising seeds, crop care products, micro-irrigation products, and pumps; and exports grapes. The company was incorporated in 1945 and is based in Mumbai, India.",27.8,30.1063869,Medium,Strong,Medium,Product Governance,Carbon,Human Capital,,Moderate Controversy Level,2
MARUTI,Maruti Suzuki India Ltd.,Consumer Cyclical,Automobile and Auto Components,"Maruti Suzuki India Limited manufactures, purchases, and sells motor vehicles, components, and spare parts primarily in India. The company offers passenger vehicles, utility vehicles, and multi-purpose vehicles. It is also involved in the facilitation of pre-owned car sales, fleet management, and car financing activities. In addition, the company offers driving school, accessories, insurance, and financing products and services. It also exports its products to Chile, Ivory Coast, Saudi Arabia, Ethiopia, South Africa, and internationally. The company was formerly known as Maruti Udyog Limited and changed its name to Maruti Suzuki India Limited in September 2007. The company was incorporated in 1981 and is headquartered in New Delhi, India. Maruti Suzuki India Limited is a subsidiary of Suzuki Motor Corporation.",25.8,26.06583333,Medium,Average,Medium,Product Governance,Carbon,Human Capital,,Moderate Controversy Level,2
NTPC,NTPC Ltd.,Utilities,Power,"NTPC Limited generates and sells bulk power to state power utilities in India. It operates through two segments: Generation of Energy and Others. The company generates power from coal, gas, liquid fuel, hydro, solar, nuclear, wind, thermal, and renewable energy sources. It offers consultancy, project management, and supervision services. In addition, the company is involved in the energy trading, oil and gas exploration, and coal mining activities. Further, the company sells electricity to private DISCOMs operating in various states. NTPC Limited was incorporated in 1975 and is headquartered in New Delhi, India.",39.4,36.45783333,High,Strong,High,Carbon,Occupational Health & Safety,Product Governance,,High Controversy Level,4
NESTLEIND,Nestle India Ltd.,Consumer Defensive,Fast Moving Consumer Goods,"Nestlé India Limited manufactures and sells food products in India and internationally. It provides milk products and nutrition, including dairy whitener, condensed and UHT milk, yoghurt, maternal and infant formula, baby food, and health care nutrition products; prepared dishes and cooking aids, such as noodles, sauces, seasonings, pasta, cereals, and pet foods; powdered and liquid beverages comprising instant coffee and tea, as well as ready to drink beverages; and confectionery products consisting of bar countlines, tablets, and sugar confectionery products. The company was incorporated in 1959 and is headquartered in Gurugram, India.",28.3,27.64517222,Medium,Strong,Medium,Product Governance,Environmental & Social Impact of Products & Services,Resource Use,,Moderate Controversy Level,2
ONGC,Oil & Natural Gas Corporation Ltd.,Energy,Oil Gas & Consumable Fuels,"Oil and Natural Gas Corporation Limited explores for, develops, and produces crude oil and natural gas in India and internationally. It operates through two segments, Exploration and Production, and Refining & Marketing. The company also engages in the refining and marketing of petroleum products; transportation of oil and natural gas; and production of liquefied petroleum gas, naphtha, ethane/propane, butane, kerosene oil, low sulphur heavy stock, aviation turbine fuel, mineral turpentine oil, carbon credits, and diesel. In addition, it generates wind power through a total installed capacity of 153 MW; and solar power through a total installed capacity of 36.52 MW, as well as generates geothermal power. The company was incorporated in 1993 and is based in New Delhi, India.",52.2,46.78,High,Average,Severe,Community Relations,"Emissions, Effluents & Waste",Carbon,,Severe Controversy Level,5
POWERGRID,Power Grid Corporation of India Ltd.,Utilities,Power,"Power Grid Corporation of India Limited, an electric power transmission utility, engages in the transmission of power in India. It operates in three segments: Transmission Services, Telecom Services, and Consultancy Services. As of July 31, 2023, the company owned and operated 1,76,109 circuit kms of transmission lines, as well as 275 substations with transformation capacity of 5,12,001 mega volt ampere. It provides consultancy services, including power system planning and techno-economic feasibility studies; environmental and social impact assessment; design and engineering; procurement assistance; project management and construction supervision; asset management; and other services, such as owners' and lenders' engineer service; grid code and tariff mechanisms preparation; legal and technical advisory; and market analysis advisory services, as well as renewable energy certificate mechanism implementation. The company offers its consultancy services. In addition, it provides overhead optic fiber network services using optical ground wire on power transmission lines under the POWERTEL brand name; and operates EV charging stations. The company was formerly known as National Power Transmission Corporation Limited and changed its name to Power Grid Corporation of India Limited in October 1992. Power Grid Corporation of India Limited was incorporated in 1989 and is based in Gurugram, India.",22.1,26.01066667,Medium,Average,Medium,Community Relations,Business Ethics,Occupational Health & Safety,,Low Controversy Level,1
RELIANCE,Reliance Industries Ltd.,Energy,Oil Gas & Consumable Fuels,"Reliance Industries Limited engages in hydrocarbon exploration and production, oil and chemicals, textile, retail, digital, material and composites, renewables, and financial services businesses worldwide. The company produces and markets petroleum products, such as liquefied petroleum gas, propylene, naphtha, gasoline, jet/aviation turbine fuel, kerosene oil, diesel, Sulphur, and petroleum coke. It also provides petrochemicals, including high-density and low-density polyethylene (PE), linear low density PE, polyester fibers and yarns, polypropylene, polyvinyl chloride, purified terephthalic acid, ethylene glycols and oxide, paraxylene, ortho xylene, benzene, linear alkyl benzene and paraffin, poly butadiene rubber, styrene butadiene rubber, butyl rubber, and polyethylene terephthalate. In addition, the company manufactures and markets yarns, fabrics, apparel, and auto furnishings; explores, develops, and produces crude oil and natural gas; and operates various stores comprising neighborhood, supermarket, hypermarket, wholesale cash and carry, specialty, online stores, as well as stores that offer apparel, beauty and cosmetics, accessories, footwear, consumer electronics, connectivity products, and others. Further, the company provides range of digital services under the Jio brand name; and non-banking financial and insurance broking services. Additionally, it operates news and entertainment platforms, and Network18 and television channels; publishes magazines; and offers highway hospitality and fleet management services. Reliance Industries Limited was incorporated in 1973 and is based in Mumbai, India.",41,35.15170556,High,Average,Severe,Carbon,Occupational Health & Safety,Occupational Health & Safety,,Moderate Controversy Level,2
SBILIFE,SBI Life Insurance Company Ltd.,Financial Services,Financial Services,"SBI Life Insurance Company Limited operates as a private life insurance company in India. The company's life insurance business comprises of individual life and group business, including participating, non-participating, pension, group gratuity, group leave encashment, group superannuation, group immediate annuity, unit-linked and variable insurance products, health, and micro insurance. It provides accident and disability benefit, level term, and critical illness insurance products. The company offers its products through a multi-channel distribution network comprising individual agents, brokers, corporate agents, banca partners, as well as certified insurance facilitators. It operates various partner branches. The company was incorporated in 2000 and is based in Mumbai, India. SBI Life Insurance Company Limited operates as a subsidiary of State Bank of India.",24.8,24.885,Medium,Average,Medium,Product Governance,Data Privacy & Cybersecurity,Business Ethics,,Low Controversy Level,1
SHRIRAMFIN,Shriram Finance Ltd.,Financial Services,Financial Services,"Shriram Finance Limited, a non-banking financial company, primarily provides commercial vehicle financing services in India. The company offers commercial vehicle loans for commercial goods vehicles, passenger vehicles, tractors and farm equipment, and construction equipment; and multi-utility vehicle, three-wheeler, two-wheeler, gold, and personal loans. It also provides business loans; and working capital loans, including tyre, tax, fuel, and toll finance, as well as vehicle insurance and repair/top-up loans; and fixed and recurring deposits. In addition, the company offers challan discounting services. It serves first time buyers, small road transport operators, and individuals; and micro, small, and medium enterprises (MSMEs) customers consisting of self-employed professionals, wholesale and retail dealers, merchants, builders, small and medium scale manufacturing concerns, and service providers. The company was formerly known as Shriram Transport Finance Company Limited and changed its name to Shriram Finance Limited in November 2022. Shriram Finance Limited was incorporated in 1979 and is based in Mumbai, India.",20.1,26.07583333,Medium,Average,Medium,Product Governance,Data Privacy & Cybersecurity,Business Ethics,,Moderate Controversy Level,2
SBIN,State Bank of India,Financial Services,Financial Services,"State Bank of India provides banking products and services to individuals, commercial enterprises, corporates, public bodies, and institutional customers in India and internationally. The company operates through Treasury, Corporate/Wholesale Banking, Retail Banking, Insurance Business, and Other Banking Business segments. It offers personal banking products and services, including current accounts, savings accounts, salary accounts, fixed and recurring deposits, and flexi and annual deposits; home, personal, auto, education, and gold loans, as well as loans against property and securities; overdrafts; mutual funds, insurance, equity trading, portfolio investment schemes, remittance services; and mobile, internet, and digital banking services. The company also provides corporate banking products and services comprising corporate accounts, working capital and project finance, deferred payment guarantees, corporate term loans, structured finance, dealer and channel financing, equipment leasing, loan syndication, construction equipment loans, financing Indian firms' overseas subsidiaries or JVs, cash management, and asset-backed loans, as well as trade and service products. In addition, it offers NRI services, including accounts and deposits, remittances, investments, and loans; agricultural banking and micro-credit to agriculturists and farmers; supply chain finance, and deposits and transaction banking services for SME customers; and international banking services. Further, the company provides treasury, broking, bill payment, and MICR services; and merchant banking, advisory, securities broking, business & management consultancy, trustee business, factoring, payment, asset management, investment management, credit cards, and custody and fund accounting services. It also offers support and business correspondent services. The company was founded in 1806 and is headquartered in Mumbai, India.",27,26.1763,Medium,Average,Medium,Data Privacy & Cybersecurity,Product Governance,Business Ethics,,Moderate Controversy Level,2
SUNPHARMA,Sun Pharmaceutical Industries Ltd.,Healthcare,Healthcare,"Sun Pharmaceutical Industries Limited, a generic pharmaceutical company, develops, manufactures, and markets branded and generic formulations and active pharmaceutical ingredients (APIs) in India and internationally. The company offers formulations in various therapeutic areas, including central nervous system, dermatology, cardiology, oncology, neuropsychiatry, gastroenterology, anti-infectives, diabetology, pain/analgesics, vitamins/minerals/nutrients, respiratory, gynaecology, urology, ophthalmology, orthopaedic, nephrology, dental, and other areas. It provides APIs for anti-cancers, peptides, steroids, hormones, and immunosuppressant drugs. In addition, the company offers generic medications, such as tablets, capsules, injectables, inhalers, ointments, creams, and liquids; speciality medications, and anti retro viral medications, as well as over-the-counter products. The company was founded in 1983 and is based in Mumbai, India.",31.6,30.28466667,Medium,Average,High,Product Governance,Business Ethics,Access to Basic Services,,Significant Controversy Level,3
TCS,Tata Consultancy Services Ltd.,Technology,Information Technology,"Tata Consultancy Services Limited provides information technology (IT) and IT enabled services in the Americas, Europe, India, and internationally. It operates through Banking, Financial Services and Insurance; Manufacturing; Consumer Business; Communication, Media and Technology; Life Sciences and Healthcare; and Others segments. The company provides TCS ADD, a suite of technology platforms for clinical research and drug development; TCS BaNCS, a financial services platform; TCS BFSI Platforms, a cloud-native, as-a-service that helps financial institutions and insurance firms; TCS CHROMA, a cloud-based workforce management solution; customer intelligence and insight solutions; TCS ERP on Cloud, a hosted ERP applications and services platform; TCS HOBS, a cloud-native catalog-centric platform for personalization of products and processes; and ignio, an autonomous enterprise software. It also offers TCS Intelligent Urban Exchange for smart cities and enterprises solution; TCS OmniStore, a retail commerce platform; TCS Optumera, a retail-connected strategic intelligence platform; TCS TAP, a procurement offering; TCS MasterCraft, a platform of intelligent automation products; Quartz- the Smart Ledgers, a blockchain solution; Jile, an enterprise agile planning and delivery tool; TCS iON, an IT-as-a-Service model that provides business solutions; and TCS TwinX, an enterprise digital twin platform. In addition, the company offers cloud, cognitive business, consulting, cybersecurity, data and analytics, enterprise solutions, Internet of Things and digital engineering, TCS interactive, and sustainability services. It serves banking; capital markets; consumer goods and distribution; communications, media, and information services; education; energy, resources, and utilities; healthcare; high technology; insurance; life sciences; manufacturing; public services; retail; and travel and logistics industries. The company was founded in 1968 and is based in Mumbai, India. Tata Consultancy Services Limited is a subsidiary of Tata Sons Private Limited.",11.4,12.607,Low,Strong,Low,Human Capital,Data Privacy & Cybersecurity,Business Ethics,,Low Controversy Level,1
TATACONSUM,Tata Consumer Products Ltd.,Consumer Defensive,Fast Moving Consumer Goods,"Tata Consumer Products Limited, together with its subsidiaries, produces, distributes, and trades in food products in India, the United States, the United Kingdom, and internationally. It operates through Branded Business and Non Branded Business segments. The company provides tea, coffee products, salt, mineral water, food ingredients, sweeteners, ready to cook and ready to eat options, breakfast cereals, snacks, mini meals, pulses, spices, sauces, chutney, pasta masala, ginger garlic paste, and dry fruits. It also offers health supplements; plant-based meat variants, including nuggets, burger patty, awadhi seekh kebab, and spicy fingers; honey and preserves; Chinese food products; glucose-based ready-to-serve drink; juices; and instant beverages. The company offers its products primarily under the Tata Tea, Tetley, 1868 by Tata Tea, Organic India, Tata Coffee Grand, Tata Coffee Gold, Tata Coffee Quick Filter, Sonnets by Tata Coffee, Tata Salt, Tata Sampann, Smith & Jones, Tata Sampann Yumside, Tata Soulfull, Himalayan honey and preserves, Ching's Secret, Tata Simply Better, Tata GoFit, Himalayan water, Tata Copper+, Tata Gluco+, Tata Fruski, Good Earth, Teapigs, Eight O'Clock, Tata Raasa, Joyfull Millets, Ching's Secret, Vitax, Laager, and Tea4Kidz brands. Tata Consumer Products Limited was formerly known as Tata Global Beverages Limited and changed its name to Tata Consumer Products Limited in February 2020. The company was incorporated in 1962 and is headquartered in Mumbai, India.",26.5,27.05097579,Medium,Strong,Medium,Product Governance,Human Capital,Resource Use,,Significant Controversy Level,3
TATAMOTORS,Tata Motors Ltd.,Consumer Cyclical,Automobile and Auto Components,"Tata Motors Limited designs, develops, manufactures, and sells various automotive vehicles. The company offers passenger cars; sports utility vehicles; intermediate and light commercial vehicles; small, medium, and heavy commercial vehicles; defense vehicles; pickups, wingers, buses, vans, and trucks; and electric vehicles, as well as related spare parts and accessories. It also manufactures engines for industrial applications, and aggregates comprising axles and transmissions for commercial vehicles; and factory automation equipment, as well as provides information technology and vehicle financing services. The company offers its products under the Tata, Daewoo, Harrier, Safari, Fiat, Nexon, Altroz, Punch, Tiago, Tigor, Jaguar, and Land Rover brands. It operates in India, China, the United States, the United Kingdom, rest of Europe, and internationally. It offers its products to fleet owners, transporters, government agencies, defense, public transport utilities, small and medium enterprises (SMEs), agriculture and rural segment, mining and construction industry, etc. The company was incorporated in 1945 and is headquartered in Mumbai, India.",27.5,29.74712024,Medium,Strong,Medium,Product Governance,Carbon,Human Capital,,Moderate Controversy Level,2
TATASTEEL,Tata Steel Ltd.,Basic Materials,Metals & Mining,"Tata Steel Limited manufactures and distributes steel products in India and internationally. It operates in Tata Steel India, Tata Steel Long Products, Other Indian Operations, Tata Steel Europe, Other Trade Related Operations, South-East Asian operations, and Rest of the World segments. The company offers hot-rolled (HR) and cold-rolled (CR) coated steel coils and sheets, precision tubes, tire bead wires, spring wires, and bearings, as well as auto ancillaries for the automotive market; and galvanized iron wires, agriculture and garden tools, and conveyance tubes, as well as fencing, farming, and irrigation equipment for the agriculture market. In addition, the company provides rebars, steel doors and windows, roofing sheets, plumbing pipes, tubes, prefabricated houses, water kiosks, modular toilets, office cabins, rooftop houses, EV charging stations, rebars and corrosion-resistance steels, cut and bend bars, PC strands, and ground granulated blast furnace slags for individual house builders, corporate and government bodies, infrastructure companies, and housing and commercial customers in the construction market. Further, it offers CR, coated, HR, tube, wire rod, ferro chrome and manganese, boiler tube, pipes, ferroshot, blast furnace slag, coal tar, and metallic coated coil and sheet products for use in panels and appliances, fabrication and capital goods, furniture, Liquid Petroleum Gas cylinders, as well as the process industries, such as cement, power, and steel in the industrial and general engineering markets. The company was incorporated in 1907 and is based in Mumbai, India.",30.7,27.06296667,High,Strong,High,Occupational Health & Safety,Community Relations,"Emissions, Effluents & Waste",,Significant Controversy Level,3
TECHM,Tech Mahindra Ltd.,Technology,Information Technology,"Tech Mahindra Limited provides information technology (IT) services and solutions in the Americas, Europe, India, and internationally. The company operates through IT Business and Business Processing Outsourcing (BPO) segments. It offers infrastructure and cloud services, including cloud, FLEX Digital workplace, enterprise network, data center, and enterprise security services; network services; integrated engineering solutions; SAP; and data analytics solutions, as well as customer experience and sustainability as a service. The company also provides experience design, testing, performance engineering, oracle, artificial intelligence, digital supply chain, business process, business excellence, telecom product engineering, cyber security, and intelligent automation services and solutions. The company serves communication; banking, financial, and insurance services; energy and utilities; media and entertainment; health life sciences; hi-tech; professional services; manufacturing; retail and consumer goods; travel, transportation, hospitality, and logistics; oil and gas; and public and government sectors. The company was incorporated in 1986 and is based in Pune, India.",11.6,12.825,Low,Strong,Low,Data Privacy & Cybersecurity,Human Capital,Business Ethics,,Low Controversy Level,1
TITAN,Titan Company Ltd.,Consumer Cyclical,Consumer Durables,"Titan Company Limited, together with its subsidiaries, manufactures and sells watches, jewelry, eyewear, and other accessories and products in India and internationally. It operates through four segments: Watches and Wearables, Jewellery, Eyecare, and Others. The company offers watches and accessories under the Titan, Titan Clock, Helios, Titan Edge, Titan Raga, Nebula, Octane, Fastrack, Zoop, Sonata, Favre-Leuba, SF, Xylys, and World of Titan, as well as Helios brand. It provides jewelry products under the Mia, CaratLane, Tanishq, and Zoya brands. In addition, the company offers optical products under the Titan EyePlus brand, as well as Fastrack and Titan Glares brands. Further, it provides a range of fragrance products under the SKINN brand; and saree, blouse, petticoat, fall and finishing products under the Taneira brand, as well as engages in component manufacturing, and automation solution, aerospace, and defense industries. It offers its products through retail stores and dealers, as well as online. The company was formerly known as Titan Industries Limited and changed its name to Titan Company Limited in August 2013. Titan Company Limited was incorporated in 1984 and is based in Bengaluru, India.",16,17.00341667,Low,Average,Low,Data Privacy & Cybersecurity,Human Rights,Human Capital,,Moderate Controversy Level,2
ULTRACEMCO,UltraTech Cement Ltd.,Basic Materials,Construction Materials,"UltraTech Cement Limited, together with its subsidiaries, manufactures and sells cement and cement related products in India. It offers ordinary Portland cement, Portland blast furnace slag cement, Portland Pozzolana cement, ready mix concrete, white cement, and white cement-based products; and ready-mix concrete. The company provides Tile Adhesive polymer under TILEFIXO, FLEX, HIFLEX; Seal & Dry water proofing products for kitchen balconies, chajjas, slope roofs, bathrooms, canal linings, swimming pools, and water tanks; Power Grout, an industrial grout for machine foundation, precast elements, and safety vaults; Readi Plast and Super Stucco, a plastering agent for internal and external walls; as well as liquid system for mortar and concrete modifier, repair mortars and concrete under the name of Basekrete and Microkrete. In addition, the company offers bed jointing material for AAC block, Fly Ash Bricks, and concrete blocks, and light weight block for masonry construction, and flooring screeds. Further, the company offers construction products for home builders; and value-added services that include technical advice during concreting, vaastu consultancy, various training programs, and other related services. The company exports its products to the United Arab Emirates, Bahrain, and Sri Lanka. UltraTech Cement Limited was incorporated in 2000 and is based in Mumbai, India. The company operates as a subsidiary of Grasim Industries Limited.",32.9,30.15695833,Medium,Average,High,Carbon,Business Ethics,Resource Use,,Moderate Controversy Level,2
WIPRO,Wipro Ltd.,Technology,Information Technology,"Wipro Limited operates as an information technology (IT), consulting, and business process services company worldwide. It operates through IT Services and IT Products segments. The IT Services segment offers IT and IT-enabled services, including digital strategy advisory, customer-centric design, technology and IT consulting, custom application design, development, re-engineering and maintenance, systems integration, package implementation, cloud and infrastructure, business process, cloud, mobility and analytics, research and development, and hardware and software design services to enterprises. It serves customers in various industry sectors, such as communications, retail connectivity and services, consumer goods, healthcare, technology products and platforms, banking and financial services, energy, manufacturing and resources, capital markets and insurance, and hi-tech. The IT Products segment provides a range of third-party IT products comprising enterprise platforms, networking solutions, software and data storage products, contact center infrastructure, enterprise security, IT optimization technologies, video solutions, and end-user computing solutions. It serves enterprises in various industries primarily in the Indian market, which comprise the government, defense, IT and IT-enabled services, telecommunications, manufacturing, utilities, education, and financial services sectors. The company was incorporated in 1945 and is based in Bengaluru, India.",13.2,16.92086667,Medium,Strong,Low,Human Capital,Data Privacy & Cybersecurity,Business Ethics,,Moderate Controversy Level,2

]
df = pd.DataFrame(data)

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


# Simulate historical ESG scores for demo purposes
#years = [2019, 2020, 2021, 2022, 2023]
#historical_avg_esg = [72, 74, 76, 78, 81]  # Example; update with real data if available
#df_trend = pd.DataFrame({'Year': years, 'Average ESG Score': historical_avg_esg})

#st.subheader("Nifty 50: ESG Score Trend (Last 5 Years)")
#st.line_chart(df_trend.set_index('Year'))

st.caption("© NIFTY 50 ESG Dashboard, Streamlit version.")    
