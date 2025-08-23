# Multiple_Disease_Predictor
The Multiple Disease Prediction System is a promising tool for enhancing healthcare accessibility and efficiency. By integrating advanced machine learning techniques with user-friendly interfaces, the system bridges the gap between technology and healthcare.

# 🧠 Disease Prediction Using Machine Learning  

This project is a **Machine Learning-based Disease Prediction System** that predicts the likelihood of different diseases (Kidney Disease, Liver Disease, and Parkinson’s Disease) using various ML models. It includes a **Streamlit web application** for user interaction and visualization.  

---

## 📌 Project Overview  

Healthcare prediction using ML is a growing field that helps in early detection of diseases. This project demonstrates how machine learning models can be applied to healthcare datasets to classify and predict disease outcomes.  

We worked on **three disease datasets**:  
1. **Kidney Disease** → Logistic Regression (Accuracy: **98.75%**)  
2. **Liver Disease** → XGBoost (Accuracy: **82.63%**)  
3. **Parkinson’s Disease** → Logistic Regression (Accuracy: **92.30%**)  

The Streamlit app provides a **user-friendly interface** to input patient details and get instant predictions.  

---

## ⚙️ Features  

- ✔️ Kidney Disease Prediction using **Logistic Regression**  
- ✔️ Liver Disease Prediction using **XGBoost Classifier**  
- ✔️ Parkinson’s Disease Prediction using **Logistic Regression**  
- ✔️ Preprocessing and feature scaling using **StandardScaler**  
- ✔️ Interactive **Streamlit Dashboard**  
- ✔️ Model accuracy displayed  

---

## 🗂️ Dataset Information  

### 1. Kidney Disease Dataset  
- Columns: `Age, Blood Pressure, Albumin, Sugar, Red Blood Cells, Packed Cell Volume, Serum Creatinine, Hemoglobin, etc.`  
- Target: **Presence of Kidney Disease**  

### 2. Liver Disease Dataset  
- Columns: `Age, Gender, Total Bilirubin, Direct Bilirubin, Alkaline Phosphotase, SGPT, SGOT, Albumin, A/G Ratio`  
- Target: **Liver Disease Outcome**  

### 3. Parkinson’s Disease Dataset  
- Columns: `MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz), Jitter(%) , Shimmer(dB), NHR, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE`  
- Target: **Parkinson’s Status**  

---

## 🏗️ Tech Stack  

- **Programming Language:** Python 🐍  
- **Frameworks:** Streamlit, Scikit-learn, XGBoost  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn  
- **Models Used:** Logistic Regression, XGBoost  

---

## 🚀 How to Run the Project  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/your-username/disease-prediction.git
cd disease-prediction```

🔹 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

🔹 3. Install Dependencies
pip install -r requirements.txt

🔹 4. Run the Streamlit App
streamlit run app.py

🔹 5. Open in Browser

The app will run at:
👉 http://localhost:8501/

📊 Model Performance
Disease	Algorithm	Accuracy
Kidney Disease	Logistic Regression	98.75%
Liver Disease	XGBoost	82.63%
Parkinson’s	Logistic Regression	92.30%
📸 Screenshots
🖥️ Streamlit App Interface

(Add your app screenshot here)

📂 Project Structure
📦 disease-prediction
 ┣ 📂 datasets
 ┃ ┣ kidney_disease.csv
 ┃ ┣ liver_disease.csv
 ┃ ┣ parkinsons.csv
 ┣ 📂 models
 ┃ ┣ kidney_model.pkl
 ┃ ┣ liver_model.pkl
 ┃ ┣ parkinsons_model.pkl
 ┣ app.py
 ┣ requirements.txt
 ┣ README.md

🧑‍💻 How It Works

Data Preprocessing

Handle missing values

Encode categorical variables

Apply StandardScaler

Model Training

Train Logistic Regression (Kidney, Parkinson)

Train XGBoost (Liver)

Evaluation

Split dataset (Train/Test)

Accuracy checked using classification metrics

Deployment

Build a Streamlit app for real-time predictions

✅ Usage

Select disease type from sidebar

Enter patient details in input form

Click Predict

Get instant result (Positive / Negative)

📌 Future Improvements

Add more diseases & datasets

Use deep learning models for better accuracy

Improve UI/UX of the Streamlit app

Deploy on cloud (Heroku/Streamlit Cloud)

🤝 Contributing

Contributions are welcome! Please fork the repo and create a pull request.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Mayank Meghwal
📧 Email: techie@techedu.com

🔗 GitHub: your-username


---

Do you also want me to **add badges** (like Python version, Streamlit, License, Accuracy) at the top
