# 🚀 QUICK START GUIDE

## For Complete Beginners

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. During installation, CHECK "Add Python to PATH"
3. Verify installation: Open Command Prompt/Terminal and type:
   ```
   python --version
   ```

### Step 2: Set Up Your Project
1. Create a new folder called `loan-prediction-project`
2. Extract all files from the downloaded zip into this folder
3. Your folder should contain:
   - data.csv
   - loan_prediction_project.py
   - requirements.txt
   - README.md
   - loan_prediction_analysis.ipynb
   - QUICK_START.md (this file)

### Step 3: Install Required Libraries
1. Open Command Prompt/Terminal
2. Navigate to your project folder:
   ```
   cd path/to/loan-prediction-project
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   This will install:
   - pandas (data manipulation)
   - numpy (numerical computing)
   - matplotlib (plotting)
   - seaborn (statistical visualization)
   - plotly (interactive plots)
   - scikit-learn (machine learning)
   - xgboost (advanced ML)
   - scipy (scientific computing)

### Step 4: Run the Analysis

#### Option A: Using Python Script (Recommended for VS Code)
1. Open VS Code
2. Open the project folder: File → Open Folder
3. Open `loan_prediction_project.py`
4. Run the script:
   - Press F5, OR
   - Right-click → Run Python File in Terminal, OR
   - Click the ▶️ button in top-right corner

#### Option B: Using Jupyter Notebook
1. Install Jupyter:
   ```
   pip install jupyter
   ```
2. Start Jupyter:
   ```
   jupyter notebook
   ```
3. Open `loan_prediction_analysis.ipynb`
4. Run cells one by one (Shift + Enter)

### Step 5: View Results
After running, check the `outputs/` folder for:
- 10 visualization PNG files
- model_comparison.csv

---

## Troubleshooting

### "python is not recognized"
- Reinstall Python and check "Add to PATH"
- Or use full path: `C:\Python3X\python.exe`

### "No module named 'pandas'"
- Run: `pip install -r requirements.txt`

### "Permission denied"
- Run Command Prompt as Administrator
- Or use: `pip install --user -r requirements.txt`

### Script runs but no output
- Check if `outputs/` folder was created
- Look for error messages in terminal

### Out of memory error
- Reduce dataset size in code:
  ```python
  df = df.sample(n=10000)  # Use only 10,000 rows
  ```

---

## VS Code Setup (Recommended)

### Install VS Code
1. Download from https://code.visualstudio.com/
2. Install Python extension:
   - Open VS Code
   - Click Extensions (Ctrl+Shift+X)
   - Search "Python"
   - Install the Microsoft Python extension

### Run Your First Analysis
1. Open project folder in VS Code
2. Open `loan_prediction_project.py`
3. Select Python interpreter (bottom-left)
4. Press F5 to run
5. View output in Terminal panel

---

## Understanding the Output

### Visualizations Created:

1. **01_target_distribution.png**
   - Shows how many loans were approved vs rejected
   - Helps understand class balance

2. **02_numerical_distributions.png**
   - Distribution of all numerical features
   - Identifies skewness and outliers

3. **03_categorical_distributions.png**
   - Employment status, product type, loan purpose
   - Shows category frequencies

4. **04_correlation_heatmap.png**
   - Relationships between features
   - Red = positive correlation, Blue = negative

5. **05_features_vs_target.png**
   - How key features differ by loan status
   - Identifies discriminative features

6. **06_boxplots_by_target.png**
   - Feature distributions by approval status
   - Shows median, quartiles, outliers

7. **07_model_comparison.png**
   - Performance metrics for all models
   - Helps select best model

8. **08_confusion_matrices.png**
   - True vs predicted classifications
   - Shows where models make mistakes

9. **09_roc_curves.png**
   - Trade-off between true/false positives
   - Higher curve = better model

10. **10_feature_importance.png**
    - Which features matter most
    - Guides business decisions

### Model Metrics Explained:

- **Accuracy**: Overall correctness (70-85% is good)
- **Precision**: Of predicted approvals, how many were correct
- **Recall**: Of actual approvals, how many were caught
- **F1-Score**: Balance between precision and recall
- **ROC-AUC**: Overall model quality (0.75-0.90 is good)

---

## Customization Tips

### Change Dataset
```python
# In loan_prediction_project.py, line ~450
filepath = 'your_data.csv'  # Change this
```

### Reduce Runtime
```python
# Use fewer models
models = {
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=50),
    'XGBoost': xgb.XGBClassifier(random_state=42, n_estimators=50)
}
```

### Adjust Train-Test Split
```python
# Line ~350
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42  # 30% for testing
)
```

### Add New Features
```python
# In engineer_features() function
df_fe['new_feature'] = df_fe['column1'] / df_fe['column2']
```

---

## Next Steps

1. ✅ Run the basic analysis
2. 📊 Study the visualizations
3. 🔍 Analyze feature importance
4. 🎯 Tune the best model
5. 📈 Try different features
6. 🚀 Deploy for predictions

---

## Getting Help

- **Python Errors**: Google the error message
- **Library Issues**: Check library documentation
- **VS Code**: https://code.visualstudio.com/docs/python/python-tutorial
- **Pandas**: https://pandas.pydata.org/docs/
- **Scikit-learn**: https://scikit-learn.org/stable/

---

## Sample Commands Cheat Sheet

```bash
# Navigate to project
cd loan-prediction-project

# Install packages
pip install -r requirements.txt

# Run Python script
python loan_prediction_project.py

# Start Jupyter
jupyter notebook

# Check Python version
python --version

# List installed packages
pip list

# Update a package
pip install --upgrade pandas
```

---

**Happy Analyzing! 🎉**

If you encounter any issues, check the error message carefully and search for solutions online. Most errors are due to missing packages or incorrect file paths.
