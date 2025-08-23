# 🧠 Multiple Disease Predictor using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Accuracy](https://img.shields.io/badge/Max_Accuracy-98.75%25-brightgreen?style=for-the-badge)](./#%EF%B8%8F-model-performance)

A Machine Learning-based system to predict the likelihood of multiple diseases (Kidney, Liver, and Parkinson's) through a user-friendly web interface built with Streamlit.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#️-features)
- [Model Performance](#%EF%B8%8F-model-performance)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [How It Works](#-how-it-works)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📜 Project Overview

The Multiple Disease Prediction System is a promising tool for enhancing healthcare accessibility and efficiency. By integrating advanced machine learning techniques with user-friendly interfaces, the system bridges the gap between technology and healthcare, enabling early detection of diseases.

This project demonstrates how machine learning models can be applied to healthcare datasets to classify and predict three different diseases:
1.  **Kidney Disease**
2.  **Liver Disease**
3.  **Parkinson’s Disease**

The primary goal is to provide a simple yet effective tool for preliminary health assessment.

---

## ⚙️ Features

-   ✔️ **Multi-Disease Prediction**: Classifies three major diseases from user input.
-   ✔️ **High-Accuracy Models**:
    -   Kidney Disease Prediction using **Logistic Regression**.
    -   Liver Disease Prediction using **XGBoost Classifier**.
    -   Parkinson’s Disease Prediction using **Logistic Regression**.
-   ✔️ **Data Preprocessing**: Includes robust preprocessing with **StandardScaler** for feature scaling.
-   ✔️ **Interactive Dashboard**: A clean and intuitive user interface built with **Streamlit**.
-   ✔️ **Instant Results**: Provides real-time predictions based on the input data.

---

## 📊 Model Performance

The models were trained and evaluated on their respective datasets, achieving the following accuracies:

| Disease             | Algorithm             | Test Accuracy |
| ------------------- | --------------------- | ------------- |
| **Kidney Disease** | `Logistic Regression` | **98.75%** |
| **Liver Disease** | `XGBoost Classifier`  | **82.63%** |
| **Parkinson’s Disease** | `Logistic Regression` | **92.30%** |

---

## 🛠️ Tech Stack

-   **Programming Language:** `Python`
-   **Web Framework:** `Streamlit`
-   **Machine Learning:** `Scikit-learn`, `XGBoost`
-   **Data Manipulation:** `Pandas`, `NumPy`
-   **Data Visualization:** `Matplotlib`, `Seaborn`

---

## 🗂️ Project Structure

The repository is organized as follows:
📦 multiple-disease-predictor/
 ┣ 📂 datasets/
 ┃ ┣ 📜 kidney_disease.csv
 ┃ ┣ 📜 liver_disease.csv
 ┃ ┗ 📜 parkinsons.csv
 ┣ 📂 models/
 ┃ ┣ 📜 kidney_model.pkl
 ┃ ┣ 📜 liver_model.pkl
 ┃ ┗ 📜 parkinsons_model.pkl
 ┣ 📜 .gitignore
 ┣ 📜 app.py
 ┣ 📜 model.ipynb
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

-   Python 3.8 or higher
-   `pip` package manager

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/multiple-disease-predictor.git](https://github.com/your-username/multiple-disease-predictor.git)
    cd multiple-disease-predictor
    ```
    2.  **Create and Activate a Virtual Environment** (Recommended)
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit App**
    ```bash
    streamlit run app.py
    ```

5.  **Access the Application**
    Open your web browser and navigate to:
    👉 **http://localhost:8501**

---

## 🧑‍💻 How It Works

The prediction pipeline involves the following steps:

1.  **Data Preprocessing**:
    -   Missing values are handled appropriately for each dataset.
    -   Categorical features are encoded into numerical formats.
    -   Features are scaled using `StandardScaler` to normalize the data.

2.  **Model Training**:
    -   The dataset is split into training and testing sets.
    -   `Logistic Regression` is trained for Kidney and Parkinson's disease.
    -   `XGBoost Classifier` is trained for Liver disease.
    -   The trained models are saved as `.pkl` files.

3.  **Deployment**:
    -   The Streamlit application loads the pre-trained models.
    -   It provides a user-friendly form to input patient data.
    -   The input data is preprocessed in the same way as the training data.
    -   The model predicts the outcome, which is displayed to the user as "Positive" or "Negative".

---

## 📌 Future Improvements

-   **Add More Diseases**: Integrate more datasets and models to expand the prediction capabilities.
-   **Enhance Model Accuracy**: Experiment with deep learning models like ANNs or LSTMs for potentially better performance.
-   **Improve UI/UX**: Enhance the Streamlit app with better visualizations, explanations of features, and a more polished design.
-   **Cloud Deployment**: Deploy the application on a cloud platform like Heroku, AWS, or Streamlit Cloud for public access.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvement, please fork the repository and create a pull request. You can also open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📜 License

This project is distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

**Mayank Meghwal**

-   **Email:** `mayankmeg207@gmail.com`
-   **GitHub:** [your-username](https://github.com/itz-Mayank) ```
