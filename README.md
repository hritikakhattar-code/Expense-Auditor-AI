# AI-Powered Expense Report Auditor

This project audits expense reports using rule-based logic and optional ML models to flag suspicious entries like over-budget claims, duplicate receipts, and out-of-policy expenses. It also uses **Hugging Face** for NLP-based description analysis.

## Features
- Upload CSV expense reports
- Rule-based anomaly detection
- NLP analysis for suspicious descriptions (e.g., alcohol, gift)
- Optional machine learning model
- Streamlit web interface
- Export flagged reports

## Run the App
```bash
pip install -r requirements.txt
streamlit run app/main.py
