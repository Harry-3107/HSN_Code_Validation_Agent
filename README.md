# HSN Code Validation Agent

The HSN Code Validation Agent is a smart Python-based tool built to validate Harmonized System Nomenclature (HSN) codes using a master Excel dataset. Designed for compliance and trade categorization tasks, this agent ensures quick and accurate HSN validation, including format checks, lookup, and descriptive feedback.<br>

## 📌Use Case:<br>
- Customs, invoicing, product classification, or regulatory systems needing verified HSN codes. <br>
<br>

## 📌Project Highlight:<br>
- Validates format and existence of HSN codes

- Accepts single or multiple codes as input

- Fast lookup using a preloaded dataset

- Returns descriptive details for valid codes

- Flags invalid or incorrectly formatted entries
<br>

## 📌Built With:<br>

- Python 3.6+
  
- pandas for Excel data handling
  
- openpyxl for .xlsx file support
<br>
 
## 📌Run Instructions:<br>

### 1. Clone the Repository:<br>

  git clone https://github.com/Harry-3107/HSN_Validation_Agent.git <br>

  cd HSN_Validation_Agent <br>

### 2. Install Dependencies:<br>

- Run this manually in your terminal<br>

    pip install pandas openpyxl<br>

### 3. Ensure Dataset File:<br>

- Place the HSN_SAC.xlsx file in the same directory as HSNCode.py.<br>

### 4. Run the Agent:<br>

  python HSNCode.py<br>

### 5. Provide HSN Input:<br>

- When prompted, enter one or more HSN codes separated by commas:<br>

  ![image](https://github.com/user-attachments/assets/eeefe204-6db2-4a93-836e-bfb7919d497d)

  
- Sample Output:<br>

 ![image](https://github.com/user-attachments/assets/5e5cdc90-8a4e-4a73-8b00-df057d051333)


