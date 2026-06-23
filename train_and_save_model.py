import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import os
import warnings

warnings.filterwarnings('ignore')

def main():
    print("Loading data...")
    # Adjust path if script is run from project root
    df = pd.read_csv("data.csv")
    
    # 1. Cleaning
    print("Cleaning data...")
    if df["usia"].isnull().sum() > 0:
        df["usia"].fillna(df["usia"].median(), inplace=True)
    if df["status_pekerjaan"].isnull().sum() > 0:
        df["status_pekerjaan"].fillna(df["status_pekerjaan"].mode()[0], inplace=True)
        
    # 2. Feature Engineering
    print("Engineering features...")
    df_fe = df.copy()
    
    # Age groups but we don't necessarily encode it for the final model since we use the numeric values directly 
    # Wait, in the notebook, these were created but not included in `feature_cols`! 
    # Let me check the original feature_cols from the notebook:
    feature_cols = [
        "usia",
        "lama_bekerja_tahun",
        "pendapatan_tahunan",
        "skor_kredit",
        "lama_riwayat_kredit_tahun",
        "aset_tabungan",
        "hutang_saat_ini",
        "gagal_bayar_tercatat",
        "tunggakan_2thn_terakhir",
        "catatan_negatif",
        "jumlah_pinjaman",
        "suku_bunga",
        "rasio_hutang_terhadap_pendapatan",
        "rasio_pinjaman_terhadap_pendapatan",
        "rasio_pembayaran_terhadap_pendapatan",
        "status_pekerjaan_encoded",
        "tipe_produk_encoded",
        "tujuan_pinjaman_encoded",
    ]
    
    # 3. Encoding
    print("Encoding categorical variables...")
    encoders = {}
    categorical_cols = ["status_pekerjaan", "tipe_produk", "tujuan_pinjaman"]
    for col in categorical_cols:
        le = LabelEncoder()
        df_fe[f"{col}_encoded"] = le.fit_transform(df_fe[col])
        encoders[col] = le
        
    X = df_fe[feature_cols]
    y = df_fe["status_pinjaman"]

    # 4. Splitting & Scaling
    print("Splitting and scaling data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 5. Model Training (XGBoost)
    print("Training XGBoost model...")
    model = xgb.XGBClassifier(
        random_state=42,
        n_estimators=100,
        eval_metric="logloss",
        use_label_encoder=False,
    )
    model.fit(X_train_scaled, y_train)
    
    # Quick evaluation
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model test accuracy: {acc:.4f}")
    
    # 6. Saving Artifacts
    print("Saving model and preprocessors to artifacts/ directory...")
    os.makedirs("artifacts", exist_ok=True)
    
    joblib.dump(model, "artifacts/xgboost_model.joblib")
    joblib.dump(scaler, "artifacts/scaler.joblib")
    joblib.dump(encoders, "artifacts/encoders.joblib")
    
    # Also save the feature columns list so we know the exact order for the Streamlit app
    joblib.dump(feature_cols, "artifacts/feature_cols.joblib")
    
    print("Done! Artifacts saved successfully.")

if __name__ == "__main__":
    main()
