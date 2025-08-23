import joblib
import streamlit as st
import numpy as np

# ----------------- Load Models & Scalers -----------------
kidney_model = joblib.load("Models/Kidney_model.pkl")
kidney_scaler = joblib.load("Models/Kidney_scaler.pkl")

liver_model = joblib.load("Models/liver_model.pkl")
liver_scaler = joblib.load("Models/Liver_scaler.pkl")

parkinson_model = joblib.load("Models/Parkinson_model.pkl")
parkinson_scaler = joblib.load("Models/Parkinson_scaler.pkl")

# ----------------- App UI -----------------
st.set_page_config(page_title="Disease Prediction", layout="wide")

st.title("🩺 Multiple Disease Prediction System")
st.write("Easily predict **Kidney Disease**, **Liver Disease**, or **Parkinson’s Disease** in one app!")

# Sidebar for selection
disease_choice = st.sidebar.radio(
    "🔍 Select Disease to Predict",
    ("Kidney Disease", "Liver Disease", "Parkinson’s Disease")
)

# ----------------- Kidney Section -----------------
if disease_choice == "Kidney Disease":
    st.header("🧪 Kidney Disease Prediction")

    with st.expander("ℹ️ About this test"):
        st.write("Enter the patient's clinical details below to predict the likelihood of **Kidney Disease**.")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=45)
        bp = st.number_input("Blood Pressure", min_value=0, value=80)
        sg = st.number_input("Specific Gravity", format="%.2f", value=1.02)
        al = st.number_input("Albumin", value=1)
        su = st.number_input("Sugar", value=0)
        rbc = st.number_input("Red Blood Cells", value=5)
        pc = st.number_input("Pus Cell", value=5)

    with col2:
        pcc = st.number_input("Pus Cell Clumps", value=0)
        ba = st.number_input("Bacteria", value=0)
        bgr = st.number_input("Blood Glucose Random", value=120)
        bu = st.number_input("Blood Urea", value=40)
        sc = st.number_input("Serum Creatinine", value=1)
        sod = st.number_input("Sodium", value=140)
        pot = st.number_input("Potassium", value=4)

    with col3:
        hemo = st.number_input("Hemoglobin", value=13)
        pcv = st.number_input("Packed Cell Volume", value=40)
        wc = st.number_input("White Blood Cell Count", value=8000)
        rc = st.number_input("Red Blood Cell Count", value=5)
        htn = st.selectbox("Hypertension", ("yes", "no"), index=1)
        dm = st.selectbox("Diabetes Mellitus", ("yes", "no"), index=1)
        cad = st.selectbox("Coronary Artery Disease", ("yes", "no"), index=1)
        appet = st.selectbox("Appetite", ("good", "poor"), index=0)
        pe = st.selectbox("Pedal Edema", ("yes", "no"), index=1)
        ane = st.selectbox("Anemia", ("yes", "no"), index=1)

    if st.button("🔮 Predict Kidney Disease"):
        features = np.array([[ 
            age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc,
            sod, pot, hemo, pcv, wc, rc,
            1 if htn=="yes" else 0,
            1 if dm=="yes" else 0,
            1 if cad=="yes" else 0,
            1 if appet=="good" else 0,
            1 if pe=="yes" else 0,
            1 if ane=="yes" else 0
        ]])

        features_scaled = kidney_scaler.transform(features)
        prediction = kidney_model.predict(features_scaled)

        if prediction[0] == 1:
            st.error("⚠️ Kidney Disease Detected!")
        else:
            st.success("✅ No Kidney Disease Detected.")

# ----------------- Liver Section -----------------
elif disease_choice == "Liver Disease":
    st.header("🧪 Liver Disease Prediction")

    with st.expander("ℹ️ About this test"):
        st.write("Provide the following liver function test values to predict **Liver Disease**.")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=45)
        gender = st.selectbox("Gender", ("Male", "Female"), index=0)
        total_bilirubin = st.number_input("Total Bilirubin", format="%.2f", value=1.2)
        direct_bilirubin = st.number_input("Direct Bilirubin", format="%.2f", value=0.5)
        alkaline_phosphotase = st.number_input("Alkaline Phosphotase", value=210)

    with col2:
        alamine_aminotransferase = st.number_input("Alamine Aminotransferase", value=35)
        aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", value=40)
        total_proteins = st.number_input("Total Proteins", format="%.2f", value=6.8)
        albumin = st.number_input("Albumin", format="%.2f", value=3.9)
        ag_ratio = st.number_input("Albumin and Globulin Ratio", format="%.2f", value=1.0)

    if st.button("🔮 Predict Liver Disease"):
        features = np.array([[ 
            age, 1 if gender=="Male" else 0, total_bilirubin, direct_bilirubin,
            alkaline_phosphotase, alamine_aminotransferase, aspartate_aminotransferase,
            total_proteins, albumin, ag_ratio
        ]])

        features_scaled = liver_scaler.transform(features)
        prediction = liver_model.predict(features_scaled)

        if prediction[0] == 1:
            st.error("⚠️ Liver Disease Detected!")
        else:
            st.success("✅ No Liver Disease Detected.")

# ----------------- Parkinson Section -----------------
elif disease_choice == "Parkinson’s Disease":
    st.header("🧪 Parkinson’s Disease Prediction")

    with st.expander("ℹ️ About this test"):
        st.write("Provide the following vocal features to check for **Parkinson’s Disease**.")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", format="%.2f", value=119.992)
        fhi = st.number_input("MDVP:Fhi(Hz)", format="%.2f", value=157.302)
        flo = st.number_input("MDVP:Flo(Hz)", format="%.2f", value=74.997)
        jitter_percent = st.number_input("MDVP:Jitter(%)", format="%.5f", value=0.00784)
        jitter_abs = st.number_input("MDVP:Jitter(Abs)", format="%.5f", value=0.00007)
        rap = st.number_input("MDVP:RAP", format="%.5f", value=0.00370)
        ppq = st.number_input("MDVP:PPQ", format="%.5f", value=0.00344)

    with col2:
        ddp = st.number_input("Jitter:DDP", format="%.5f", value=0.01109)
        shimmer = st.number_input("MDVP:Shimmer", format="%.5f", value=0.04374)
        shimmer_db = st.number_input("MDVP:Shimmer(dB)", format="%.5f", value=0.426)
        apq3 = st.number_input("Shimmer:APQ3", format="%.5f", value=0.02182)
        apq5 = st.number_input("Shimmer:APQ5", format="%.5f", value=0.03130)
        apq = st.number_input("MDVP:APQ", format="%.5f", value=0.02971)
        dda = st.number_input("Shimmer:DDA", format="%.5f", value=0.06545)

    with col3:
        nhr = st.number_input("NHR", format="%.5f", value=0.02211)
        hnr = st.number_input("HNR", format="%.2f", value=21.033)
        rpde = st.number_input("RPDE", format="%.5f", value=0.414783)
        dfa = st.number_input("DFA", format="%.5f", value=0.815285)
        spread1 = st.number_input("spread1", format="%.5f", value=-4.813031)
        spread2 = st.number_input("spread2", format="%.5f", value=0.266482)
        d2 = st.number_input("D2", format="%.5f", value=2.301442)
        ppe = st.number_input("PPE", format="%.5f", value=0.284654)

    if st.button("🔮 Predict Parkinson’s Disease"):
        features = np.array([[ 
            fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
            shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
            rpde, dfa, spread1, spread2, d2, ppe
        ]])

        features_scaled = parkinson_scaler.transform(features)
        prediction = parkinson_model.predict(features_scaled)

        if prediction[0] == 1:
            st.error("⚠️ Parkinson’s Disease Detected!")
        else:
            st.success("✅ No Parkinson’s Disease Detected.")
