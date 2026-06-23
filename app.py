import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Fintech Analytics | Loan Approval Dashboard",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a professional look
st.markdown("""
<style>
    /* Main Layout */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* KPI Cards */
    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
        border-left: 5px solid #1E3A8A;
        margin-bottom: 1rem;
    }
    
    .kpi-title {
        color: #64748b;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }
    
    .kpi-value {
        color: #0f172a;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    /* Status Cards */
    .status-approved {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.3);
    }
    
    .status-rejected {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3);
    }
    
    /* Submit Button styling */
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        border: none;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        color: white;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.4);
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #1e293b;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load("artifacts/xgboost_model.joblib")
        scaler = joblib.load("artifacts/scaler.joblib")
        encoders = joblib.load("artifacts/encoders.joblib")
        feature_cols = joblib.load("artifacts/feature_cols.joblib")
        return model, scaler, encoders, feature_cols
    except Exception as e:
        return None, None, None, None

def create_gauge_chart(probability):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = probability * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Approval Confidence Probability", 'font': {'size': 18, 'color': '#64748b'}},
        number = {'suffix': "%", 'font': {'size': 40, 'color': '#0f172a'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#1E3A8A"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e2e8f0",
            'steps': [
                {'range': [0, 40], 'color': '#fee2e2'},
                {'range': [40, 70], 'color': '#fef3c7'},
                {'range': [70, 100], 'color': '#d1fae5'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def main():
    model, scaler, encoders, feature_cols = load_artifacts()

    # Sidebar for inputs
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135679.png", width=60)
        st.title("Client Profile Input")
        st.markdown("Enter applicant details to generate the risk profile.")
        
        with st.form("input_form"):
            st.subheader("Demographics")
            usia = st.slider("Age (Usia)", 18, 100, 35)
            
            st.subheader("Financials")
            pendapatan_tahunan = st.number_input("Annual Income ($)", value=65000, step=1000)
            aset_tabungan = st.number_input("Savings Assets ($)", value=20000, step=1000)
            hutang_saat_ini = st.number_input("Current Debt ($)", value=15000, step=1000)
            
            st.subheader("Loan Specifics")
            jumlah_pinjaman = st.number_input("Requested Loan Amount ($)", value=25000, step=1000)
            suku_bunga = st.slider("Interest Rate (%)", 1.0, 30.0, 8.5, 0.1)
            tujuan_pinjaman = st.selectbox("Loan Purpose", ["Home Improvement", "Debt Consolidation", "Business", "Education", "Other"])
            tipe_produk = st.selectbox("Product Type", ["Personal Loan", "Auto Loan", "Mortgage", "Business Loan", "Credit Card"])
            
            st.subheader("Credit & Employment")
            skor_kredit = st.slider("Credit Score", 300, 850, 710)
            status_pekerjaan = st.selectbox("Employment Status", ["Employed", "Self-Employed", "Unemployed", "Student", "Retired"])
            lama_bekerja_tahun = st.number_input("Years Employed", value=6.0, step=0.5)
            lama_riwayat_kredit_tahun = st.number_input("Credit Hist Length (yrs)", value=8.0, step=0.5)
            
            st.subheader("Risk Indicators")
            col1, col2, col3 = st.columns(3)
            with col1:
                gagal_bayar_tercatat = st.number_input("Defaults", value=0, min_value=0)
            with col2:
                tunggakan_2thn_terakhir = st.number_input("Arrears (2y)", value=0, min_value=0)
            with col3:
                catatan_negatif = st.number_input("Neg Records", value=0, min_value=0)

            submitted = st.form_submit_button("Run Analytics Engine 🚀")

    # Main Dashboard Area
    st.title("Risk Assessment Dashboard")
    st.markdown("##### Real-time automated underwriting and predictive analytics module")
    st.markdown("---")
    
    if not submitted:
        # Default empty state
        st.info("👈 Please input the client profile in the sidebar and run the analytics engine to generate the dashboard.")
        
        # Skeleton KPIs just to show layout
        col1, col2, col3, col4 = st.columns(4)
        kpis = [("Monthly Income", "$ -"), ("Credit Score", "-"), ("DTI Ratio", "- %"), ("Requested Loan", "$ -")]
        for col, (title, val) in zip([col1, col2, col3, col4], kpis):
            with col:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">{title}</div>
                    <div class="kpi-value">{val}</div>
                </div>
                """, unsafe_allow_html=True)
                
    else:
        if model is None:
            st.error("Model artifacts not found! Ensure artifacts/ directory exists with joblib files.")
            return
            
        # Process and Predict
        income_safe = max(pendapatan_tahunan, 1)
        dti_ratio = hutang_saat_ini / income_safe
        lti_ratio = jumlah_pinjaman / income_safe
        
        monthly_interest = (suku_bunga / 100) / 12
        if monthly_interest > 0:
            monthly_payment = jumlah_pinjaman * (monthly_interest * (1 + monthly_interest)**60) / ((1 + monthly_interest)**60 - 1)
        else:
            monthly_payment = jumlah_pinjaman / 60
        annual_payment = monthly_payment * 12
        pti_ratio = annual_payment / income_safe

        input_data = {
            "usia": usia,
            "lama_bekerja_tahun": lama_bekerja_tahun,
            "pendapatan_tahunan": pendapatan_tahunan,
            "skor_kredit": skor_kredit,
            "lama_riwayat_kredit_tahun": lama_riwayat_kredit_tahun,
            "aset_tabungan": aset_tabungan,
            "hutang_saat_ini": hutang_saat_ini,
            "gagal_bayar_tercatat": gagal_bayar_tercatat,
            "tunggakan_2thn_terakhir": tunggakan_2thn_terakhir,
            "catatan_negatif": catatan_negatif,
            "jumlah_pinjaman": jumlah_pinjaman,
            "suku_bunga": suku_bunga,
            "rasio_hutang_terhadap_pendapatan": dti_ratio,
            "rasio_pinjaman_terhadap_pendapatan": lti_ratio,
            "rasio_pembayaran_terhadap_pendapatan": pti_ratio,
            "status_pekerjaan": status_pekerjaan,
            "tipe_produk": tipe_produk,
            "tujuan_pinjaman": tujuan_pinjaman
        }
        
        df_input = pd.DataFrame([input_data])
        
        for cat in ["status_pekerjaan", "tipe_produk", "tujuan_pinjaman"]:
            try:
                df_input[f"{cat}_encoded"] = encoders[cat].transform([input_data[cat]])[0]
            except:
                df_input[f"{cat}_encoded"] = 0
                
        X_input = df_input[feature_cols]
        X_scaled = scaler.transform(X_input)
        
        prediction = model.predict(X_scaled)[0]
        probability = model.predict_proba(X_scaled)[0][1]
        
        # 1. Top KPI Row
        col1, col2, col3, col4 = st.columns(4)
        
        kpis = [
            ("Monthly Income", f"${pendapatan_tahunan/12:,.0f}"),
            ("Credit Score", f"{skor_kredit}"),
            ("DTI Ratio", f"{dti_ratio*100:.1f}%"),
            ("Requested Amount", f"${jumlah_pinjaman:,.0f}")
        ]
        
        for col, (title, val) in zip([col1, col2, col3, col4], kpis):
            with col:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">{title}</div>
                    <div class="kpi-value">{val}</div>
                </div>
                """, unsafe_allow_html=True)
                
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 2. Main Content Row
        left_col, right_col = st.columns([1.2, 1])
        
        with left_col:
            st.markdown("### Underwriting Verdict")
            if prediction == 1:
                st.markdown(f"""
                <div class="status-approved">
                    <h1 style='color: white; margin: 0; font-size: 2.5rem;'>APPROVED</h1>
                    <p style='margin-top: 10px; font-size: 1.2rem; opacity: 0.9;'>Client meets all financial criteria for this product.</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### Recommendations")
                st.success("✅ **Favorable DTI:** The client's Debt-to-Income ratio is well within limits.")
                if skor_kredit > 700:
                    st.success("✅ **Excellent Credit:** Premium tier interest rates apply.")
                if aset_tabungan > hutang_saat_ini:
                    st.success("✅ **Strong Liquidity:** Assets exceed current liabilities.")
                    
            else:
                st.markdown(f"""
                <div class="status-rejected">
                    <h1 style='color: white; margin: 0; font-size: 2.5rem;'>REJECTED</h1>
                    <p style='margin-top: 10px; font-size: 1.2rem; opacity: 0.9;'>Profile exceeds acceptable risk thresholds.</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### Primary Risk Factors")
                if dti_ratio > 0.4:
                    st.error("⚠️ **High Debt-to-Income:** DTI ratio exceeds maximum allowable threshold (40%).")
                if skor_kredit < 600:
                    st.error("⚠️ **Poor Credit History:** Credit score falls below minimum portfolio standards.")
                if gagal_bayar_tercatat > 0 or catatan_negatif > 0:
                    st.error("⚠️ **Negative Records:** Past defaults or negative records found on file.")
                if lti_ratio > 0.5:
                    st.warning("⚠️ **High Requested Volume:** Loan volume requested is large relative to base income.")

        with right_col:
            st.plotly_chart(create_gauge_chart(probability), use_container_width=True)
            
            # Simple bar chart comparing assets to debt
            fig2 = px.bar(
                x=["Liquid Assets", "Current Debt", "Requested"], 
                y=[aset_tabungan, hutang_saat_ini, jumlah_pinjaman],
                color=["Assets", "Liabilities", "Liabilities"],
                color_discrete_map={"Assets": "#10b981", "Liabilities": "#ef4444"},
                title="Financial Snapshot"
            )
            fig2.update_layout(height=280, showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig2, use_container_width=True)

if __name__ == "__main__":
    main()
