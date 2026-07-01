import pandas as pd

# Load sample dataset
df = pd.read_excel("sample_card_transdata.xlsx")

# Test 1: Check for missing values
assert df.isnull().sum().sum() == 0, "Dataset contains missing values."

# Test 2: Check for duplicate rows
assert df.duplicated().sum() == 0, "Dataset contains duplicate rows."

# Test 3: Check target column exists
assert "fraud" in df.columns, "Target column 'fraud' is missing."

print("All automated validation tests passed successfully.")
