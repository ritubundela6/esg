import streamlit as st  
import pandas as pd  
import numpy as np  
import io  
import matplotlib.pyplot as plt  
  
# --- Load Nifty Fifty data from CSV string ---  
  
# Assume the full "nift-50.csv" content is represented here as a string.  
# Replace this placeholder with the actual CSV text or path.  
nifty_csv = """  
Symbol,company,Sector,Industry,Description,esg_risk_score_2024,predicted_future_esg_score,esg_risk_exposure,esg_risk_management,esg_risk_level,Material ESG Issues 1,Material ESG Issues 2,Material ESG Issues 3,,Controversy Level,controversy_score  
ADANIENT,Adani Enterprises Ltd.,Energy,Metals & Mining,"...",32.9,33.23703095,Medium,Average,Medium,Business Ethics,Carbon,Human Capital,,High Controversy Level,4  
ADANIPORTS,Adani Ports and Special Economic Zone Ltd.,Industrials,Services,"...",12.6,14.823,Low,Strong,Low,Occupational Health & Safety,Land Use & Biodiversity,Community Relations,,High Controversy Level,4  
# Add the complete CSV content here...  
"""  
  
# Simulate loading the CSV data by reading a file or using a string  
try:  
    nifty_fifty_data = pd.read_csv("D:\\gt internship\\week 6\\nift 50.csv")  
except Exception as e:  
    st.error(f"Error loading Nifty Fifty CSV data: {e}")  
    nifty_fifty_data = pd.DataFrame()  
  
# Map esg_risk_level to corresponding colors for styling purposes  
risk_color_map = {'Low': 'lightgreen', 'Medium': 'khaki', 'High': 'salmon', 'Severe': 'red'}  

def color_risk_level(val):
    return f'background-color: {risk_color_map.get(val, "")}'

def prepare_summary_recommendations(df):
    # Prepare simple dummy recommendations based on scores and risk level
    recs = []
    for i, row in df.iterrows():
        esg_score = row.get('esg_risk_score_2024', np.nan)
        risk_level = row.get('esg_risk_level', '')

        if pd.isna(esg_score):
            continue
        if risk_level == 'Severe' or esg_score > 40:
            rec = f"{row['company']} needs significant ESG risk mitigation."
        elif risk_level == 'High' or esg_score > 30:
            rec = f"{row['company']} should improve ESG initiatives especially in {row.get('Material ESG Issues 1','')}."
        else:
            rec = f"{row['company']} maintains good ESG practices."
        recs.append(rec)
    return recs

def df_exists_and_not_empty(df):
    return df is not None and not df.empty

st.set_page_config(page_title="Season ESG Analysis", layout="wide")

st.title("🌿 Season ESG Analysis")

tabs = st.tabs(["Nifty Fifty ESG Overview", "Upload & Compare Company", "Custom Data ESG Analysis", "Indian Stock Exchange Trends"])

# Tab 1: Nifty Fifty ESG Overview
with tabs[0]:
    st.header("Nifty Fifty Companies ESG Analysis")

    if df_exists_and_not_empty(nifty_fifty_data):
        st.info("Use the search box below to filter companies.")

        # Search/filter box for companies
        search_term = st.text_input("Search Company by Name", "")

        filtered_df = nifty_fifty_data.copy()

        if search_term:
            filtered_df = filtered_df[filtered_df['company'].str.contains(search_term, case=False, na=False)]

        # Show dataframe with ESG risk coloring
        st.dataframe(filtered_df.style.applymap(color_risk_level, subset=['esg_risk_level']))

        # ESG risk score distribution histogram
        fig1 = px.histogram(filtered_df, x='esg_risk_score_2024', nbins=30, title="Distribution of ESG Risk Scores - Nifty Fifty")
        st.plotly_chart(fig1, use_container_width=True)

        # Sector wise average esg risk score bar chart
        sector_avg = filtered_df.groupby("Sector")['esg_risk_score_2024'].mean().reset_index()
        fig2 = px.bar(sector_avg, x='Sector', y='esg_risk_score_2024', title="Average ESG Risk Score by Sector")
        st.plotly_chart(fig2, use_container_width=True)

        # Recommendations summary
        st.markdown("### Recommendations Summary")
        recommendations = prepare_summary_recommendations(filtered_df)
        for rec in recommendations:
            st.write("- ", rec)

    else:
        st.warning("Nifty Fifty ESG data not loaded.")

# Tab 2: Upload & Compare Own Company ESG
with tabs[1]:
    st.header("Upload Your Company ESG Data and Compare")

    uploaded_file = st.file_uploader("Upload your company ESG CSV with columns: company, esg_risk_score_2024, Environment, Social, Governance", type=["csv"])

    if uploaded_file:
        try:
            user_df = pd.read_csv(uploaded_file)
            st.success(f"Data for company: {user_df['company'].iloc[0]} loaded.")
            st.dataframe(user_df.style.highlight_max(axis=1))

            # Validate expected columns
            expected_cols = {"company", "esg_risk_score_2024"}
            if not expected_cols.issubset(set(user_df.columns.str.lower())):
                st.error(f"CSV must contain at least the columns: {expected_cols}")
            else:
                user_company = user_df.iloc[0]

                # Calculate Nifty Fifty averages
                nifty_avg_score = nifty_fifty_data['esg_risk_score_2024'].mean()
                nifty_avg_sector = None

                # Attempt to find sector for user company if provided
                user_sector = user_company.get('Sector') if 'Sector' in user_company else None
                if user_sector and user_sector in nifty_fifty_data['Sector'].values:
                    sector_data = nifty_fifty_data[nifty_fifty_data['Sector'] == user_sector]
                    nifty_avg_sector = sector_data['esg_risk_score_2024'].mean()

                st.markdown("### Comparison of ESG Risk Score")
                st.write(f"Your company ESG Risk Score: {user_company['esg_risk_score_2024']:.2f}")
                st.write(f"Nifty Fifty Average ESG Risk Score: {nifty_avg_score:.2f}")

                if nifty_avg_sector:
                    st.write(f"Average ESG Risk Score for Sector '{user_sector}': {nifty_avg_sector:.2f}")

                # Plot comparison
                comp_df = pd.DataFrame({
                    "Comparison": ["Your Company", "Nifty Fifty Average"],
                    "ESG Risk Score": [user_company['esg_risk_score_2024'], nifty_avg_score]
                })
                fig_compare = px.bar(comp_df, x='Comparison', y='ESG Risk Score', color='Comparison',
                                     title=f"ESG Risk Score Comparison for {user_company['company']}")
                st.plotly_chart(fig_compare, use_container_width=True)

                # Recommendations based on relative position
                diff = user_company['esg_risk_score_2024'] - nifty_avg_score

                if diff > 5:
                    st.warning("Your company's ESG risk score is higher than average, indicating higher risks. Consider improving sustainability and governance.")
                elif diff < -5:
                    st.success("Your company scores better than the Nifty Fifty average in ESG risk. Maintain your good practices!")
                else:
                    st.info("Your company's ESG risk score is close to the Nifty Fifty average.")

                # Download summary report
                def generate_report():
                    summary = {
                        "Company": user_company['company'],
                        "Company ESG Risk Score": user_company['esg_risk_score_2024'],
                        "Nifty Fifty Avg ESG Risk Score": nifty_avg_score,
                        "Sector": user_sector if user_sector else "Unknown",
                        "Sector Avg ESG Risk Score": nifty_avg_sector if nifty_avg_sector else "N/A",
                        "Recommendation": ""
                    }
                    if diff > 5:
                        summary["Recommendation"] = "Improve ESG risk management."
                    elif diff < -5:
                        summary["Recommendation"] = "Maintain strong ESG practices."
                    else:
                        summary["Recommendation"] = "Continue current ESG efforts."

                    return pd.DataFrame([summary])

                if st.button("Download Summary Report as CSV"):
                    report_df = generate_report()
                    csv_data = report_df.to_csv(index=False).encode('utf-8')
                    st.download_button(label="Download CSV", data=csv_data, file_name="esg_comparison_report.csv", mime="text/csv")

        except Exception as e:
            st.error(f"Error processing your uploaded file: {e}")

    else:
        st.info("Upload your company ESG CSV to begin comparison.")

# Tab 3: Custom Data ESG & Financial Analysis
with tabs[2]:
    st.header("Upload Custom ESG / Financial Data for Analysis")

    custom_file = st.file_uploader("Upload any CSV with ESG or financial data for analysis", type=["csv"])

    if custom_file:
        try:
            custom_df = pd.read_csv(custom_file)
            st.success("File uploaded successfully.")
            st.dataframe(custom_df.head(10))

            esg_cols = [c for c in custom_df.columns if 'esg' in c.lower() or c.lower() in ['environment', 'social', 'governance']]
            fin_cols = [c for c in custom_df.columns if any(keyword in c.lower() for keyword in ['revenue', 'profit', 'income', 'expense', 'transaction', 'cost'])]

            if esg_cols:
                st.markdown("### ESG Metrics Summary")
                st.dataframe(custom_df[esg_cols].describe())

                # Plot averages
                avg_esg = custom_df[esg_cols].mean()
                fig_esg_avg = px.bar(avg_esg, title="Average ESG Scores")
                st.plotly_chart(fig_esg_avg, use_container_width=True)
            else:
                st.warning("No ESG related columns detected.")

            if fin_cols:
                st.markdown("### Financial Metrics Summary")
                st.dataframe(custom_df[fin_cols].describe())

                # Boxplots for financials
                fig_fin_box = px.box(custom_df[fin_cols], title="Financial Metrics Distribution")
                st.plotly_chart(fig_fin_box, use_container_width=True)
            else:
                st.warning("No financial related columns detected.")

            # Correlation heatmap if enough numeric columns
            numeric_cols = custom_df.select_dtypes(include=np.number).columns.tolist()
            if len(numeric_cols) >= 3:
                corr = custom_df[numeric_cols].corr()
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
                st.pyplot(fig)

            # Recommendations based on average ESG
            if esg_cols:
                for col in esg_cols:
                    avg_score = custom_df[col].mean()
                    if avg_score < 50:
                        st.warning(f"Average {col} score ({avg_score:.1f}) is low; consider improvements.")
                    elif avg_score > 80:
                        st.success(f"Average {col} score ({avg_score:.1f}) is strong; maintain practices.")
                    else:
                        st.info(f"Average {col} score ({avg_score:.1f}) is moderate.")

            # Download analysis summary
            def create_custom_summary():
                summary_dict = {}
                if esg_cols:
                    for col in esg_cols:
                        summary_dict[f"Avg {col}"] = custom_df[col].mean()
                if fin_cols:
                    for col in fin_cols:
                        summary_dict[f"Avg {col}"] = custom_df[col].mean()
                return pd.DataFrame([summary_dict])

            if st.button("Download Analysis Summary CSV"):
                summary_df = create_custom_summary()
                csv_out = summary_df.to_csv(index=False).encode('utf-8')
                st.download_button("Download CSV", csv_out, "custom_data_summary.csv", "text/csv")

        except Exception as e:
            st.error(f"Error processing file: {e}")

    else:
        st.info("Upload CSV file containing ESG or financial data for detailed analysis.")

# Tab 4: Indian Stock Exchange Performance & ESG Trends
with tabs[3]:
    st.header("Indian Stock Exchange Sector Performance")

    if df_exists_and_not_empty(nifty_fifty_data):
        sector_esg_avg = nifty_fifty_data.groupby('Sector').agg({
            'esg_risk_score_2024': 'mean',
            'predicted_future_esg_score': 'mean',
            'controversy_score': 'mean'
        }).reset_index()

        st.dataframe(sector_esg_avg)

        fig = px.bar(sector_esg_avg, x='Sector', y=['esg_risk_score_2024', 'predicted_future_esg_score'],
                     title='Sector-wise Current and Predicted ESG Risk Scores', barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### Insights & Recommendations:
        - Sectors with higher ESG risk scores may require focused improvement strategies.
        - Monitor predicted ESG risk scores for future trends.
        - High controversy score sectors should implement transparency and governance reforms.
        """)

    else:
        st.warning("Nifty Fifty ESG data not loaded.")

# Footer
st.markdown("---")
st.markdown("© 2025 Season ESG Analysis | Professional ESG Strategy & Financial Insights")
