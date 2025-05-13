import pandas as pd

# Load the Excel file
file_path = "HSN_SAC.xlsx"  # Update this if your filename is different
df = pd.read_excel(file_path)

# Normalize column names: remove spaces, make uppercase
df.columns = df.columns.str.strip().str.replace(" ", "").str.upper()

# Check if 'HSNCODE' column exists
if 'HSNCODE' not in df.columns:
    print("Error: 'HSNCODE' column not found in the Excel file after normalization.")
    print("Available columns:", df.columns.tolist())
    exit()

# Convert HSN codes to string (preserve leading zeros)
df["HSNCODE"] = df["HSNCODE"].astype(str)

# Create a set of valid HSN codes for fast lookup
valid_hsn_codes = set(df["HSNCODE"])

# Get user input
user_input = input("Enter one or more HSN codes separated by commas: ")

# Process input
input_codes = [code.strip() for code in user_input.split(",")]

# Validate each input code
for code in input_codes:
    if not code.isdigit():
        print(f"[Invalid Format] '{code}' is not numeric.")
    elif code not in valid_hsn_codes:
        print(f"[Not Found] '{code}' is not a valid HSN code.")
    else:
        description = df.loc[df["HSNCODE"] == code, "DESCRIPTION"].values[0]
        print(f"[Valid] {code}: {description}")
