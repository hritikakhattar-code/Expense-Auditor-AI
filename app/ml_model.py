import pickle
import pandas as pd

def load_model(path='models/expense_model.pkl'):
    try:
        with open(path, 'rb') as f:
            return pickle.load(f)
    except:
        return None

def predict_expense_risk(model, df):
    if model is None:
        return ["Not Available"] * len(df)
    
    X = df[['Amount']]  # You can expand this with other features
    return model.predict(X)
