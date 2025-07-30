import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with st.container():
    st.header("Data & Trend Analysis")
    st.title("📊 Data Uploader & Trend Analysis")

    uploaded_file = st.file_uploader("Upload your data file (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        # Automatically detect file type
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

        # Prepare data
        x_data = df_upload[x_col]
        y_data = df_upload[y_col]

        # Convert datetime for regression if needed
        if np.issubdtype(x_data.dtype, np.datetime64):
            x_numeric = x_data.apply(lambda x: x.toordinal())
        else:
            x_numeric = pd.to_numeric(x_data, errors='coerce')

        fig, ax = plt.subplots()

        # Plot actual data
        ax.plot(x_data, y_data, marker='o', label="Actual Data")

        # Plot linear fit (trend line)
        if y_data.notna().sum() > 1 and x_numeric.notna().sum() > 1:
            z = np.polyfit(x_numeric.dropna(), y_data[x_numeric.notna()], 1)
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
