# Loan Status Prediction - Data Analytics Project

## 📊 Project Overview
This is a comprehensive data analytics and machine learning project for predicting loan approval status based on customer financial and demographic data.

**Dataset**: Banking Loan Data (Indonesian)
- **Records**: 50,000 customers
- **Features**: 20 columns
- **Target**: Loan Status (Approved=1, Rejected=0)

## 🎯 Project Objectives
1. Perform exploratory data analysis (EDA)
2. Clean and preprocess the data
3. Engineer meaningful features
4. Build and compare multiple ML models
5. Identify key factors influencing loan approval

## 📁 Project Structure
```
loan-prediction-project/
│
├── data.csv                          # Your dataset (place here)
├── loan_prediction_project.py        # Main analysis script
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
│
└── outputs/                          # Generated outputs
    ├── 01_target_distribution.png
    ├── 02_numerical_distributions.png
    ├── 03_categorical_distributions.png
    ├── 04_correlation_heatmap.png
    ├── 05_features_vs_target.png
    ├── 06_boxplots_by_target.png
    ├── 07_model_comparison.png
    ├── 08_confusion_matrices.png
    ├── 09_roc_curves.png
    ├── 10_feature_importance.png
    └── model_comparison.csv
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this project**

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Place your data file**
   - Extract `data.csv` from the archive
   - Place it in the same directory as `loan_prediction_project.py`

4. **Run the analysis**
   ```bash
   python loan_prediction_project.py
   ```

## 📊 Dataset Features

### Customer Demographics
- `id_pelanggan`: Customer ID
- `usia`: Age
- `status_pekerjaan`: Employment status

### Financial Information
- `pendapatan_tahunan`: Annual income
- `skor_kredit`: Credit score
- `aset_tabungan`: Savings assets
- `hutang_saat_ini`: Current debt
- `lama_bekerja_tahun`: Years of employment
- `lama_riwayat_kredit_tahun`: Years of credit history

### Credit History
- `gagal_bayar_tercatat`: Recorded defaults
- `tunggakan_2thn_terakhir`: Arrears in last 2 years
- `catatan_negatif`: Negative records

### Loan Details
- `tipe_produk`: Product type
- `tujuan_pinjaman`: Loan purpose
- `jumlah_pinjaman`: Loan amount
- `suku_bunga`: Interest rate

### Financial Ratios
- `rasio_hutang_terhadap_pendapatan`: Debt-to-income ratio
- `rasio_pinjaman_terhadap_pendapatan`: Loan-to-income ratio
- `rasio_pembayaran_terhadap_pendapatan`: Payment-to-income ratio

### Target Variable
- `status_pinjaman`: Loan status (0=Rejected, 1=Approved)

## 🔍 Analysis Pipeline

### 1. Data Loading & Exploration
- Load dataset
- Display basic statistics
- Check data types and missing values
- Analyze target variable distribution

### 2. Data Cleaning
- Handle missing values
- Remove duplicates
- Fix data type issues

### 3. Exploratory Data Analysis (EDA)
- Target variable distribution
- Numerical features distribution
- Categorical features analysis
- Correlation analysis
- Feature relationships with target

### 4. Feature Engineering
- Age groups
- Income categories
- Credit score groups
- Risk scores
- Composite features

### 5. Data Preprocessing
- Encode categorical variables
- Feature scaling
- Train-test split (80-20)

### 6. Model Training
Train and compare 7 different models:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

### 7. Model Evaluation
- Accuracy, Precision, Recall, F1-Score
- ROC-AUC curves
- Confusion matrices
- Feature importance analysis

## 📈 Expected Outputs

### Visualizations (10 PNG files)
1. **Target Distribution**: Loan approval rates
2. **Numerical Distributions**: All numerical features
3. **Categorical Distributions**: Employment, product type, loan purpose
4. **Correlation Heatmap**: Feature correlations
5. **Features vs Target**: Key features by loan status
6. **Box Plots**: Feature distributions by target
7. **Model Comparison**: Performance metrics
8. **Confusion Matrices**: All models
9. **ROC Curves**: Model comparison
10. **Feature Importance**: Top predictive features

### Data Files
- `model_comparison.csv`: Detailed metrics for all models

## 🎓 Key Insights

The analysis will help you understand:
- Which factors most influence loan approval
- Customer segments with higher approval rates
- Optimal credit score and income thresholds
- Risk factors for loan rejection
- Model performance comparison

## 🛠️ Customization

### Modify the script to:
1. **Change file path**: Update `filepath` variable in `main()` function
2. **Adjust train-test split**: Modify `test_size` in `train_test_split()`
3. **Add more models**: Extend the `models` dictionary
4. **Tune hyperparameters**: Use GridSearchCV for optimization
5. **Create new features**: Add to `engineer_features()` function

## 📊 Model Performance

Expected performance (approximate):
- **Accuracy**: 70-85%
- **ROC-AUC**: 0.75-0.90
- **Best Models**: Random Forest, XGBoost, Gradient Boosting

## 🔧 Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**
   ```bash
   pip install -r requirements.txt
   ```

2. **File not found**
   - Ensure `data.csv` is in the same directory
   - Update the `filepath` variable

3. **Memory issues**
   - Reduce dataset size for testing
   - Use sampling: `df.sample(n=10000)`

4. **Slow execution**
   - Reduce number of models
   - Decrease n_estimators for ensemble models

## 📝 Notes

- The script creates an `outputs/` directory automatically
- All visualizations are saved as high-resolution PNG files (150 DPI)
- Model training may take 5-15 minutes depending on your hardware
- The dataset is in Indonesian language

## 🤝 Contributing

Feel free to:
- Add new features
- Implement additional models
- Improve visualizations
- Optimize performance

## 📄 License

This project is for educational and analytical purposes.

## 👤 Author

Generated for: Anand kishor 
Date: 2026-06-23

## 🙏 Acknowledgments

- Dataset: Banking Loan Data
- Libraries: scikit-learn, pandas, matplotlib, seaborn, plotly, xgboost

---

**Happy Analyzing! 📊🚀**
