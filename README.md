# AML Risk Scoring Tool (Python)

A simple Anti-Money Laundering (AML) risk scoring tool built in Python.  
The tool evaluates transaction risk based on balance, country risk, and transaction type.

This project is created as a learning and portfolio project.

---

## Features

- Calculates risk score based on account balance
- Evaluates country risk using:
  - EU High-Risk Countries list
  - FATF Black List
  - FATF Grey List
- Evaluates transaction type risk (cash / transfer / crypto)
- Generates a total risk score
- Classifies risk level (Low / Medium / High)

---

## Project Structure

- main.py  
- score.py  
- eu_high_risk_countries.txt  
- fatf_black_list.txt  
- fatf_grey_list.txt  
- README.md  


## Risk Scoring Logic

This tool calculates the overall AML risk score based on three main factors:

### 1. Account Balance
- Balance ≥ 10,000 → Score: 3
- Balance 5,000 – 9,999 → Score: 2
- Balance 1,000 – 4,999 → Score: 1
- Balance < 1,000 → Score: 0

### 2. Country Risk
- EU High-Risk List → Score: 3
- FATF Black List → Score: 3
- FATF Grey List → Score: 2
- Other countries → Score: 0

### 3. Transaction Type Risk
- Crypto transactions → Score: 3
- Cash transactions → Score: 2
- Bank transfer → Score: 1


## How to Run

1. Clone the repository:
git clone https://github.com/SniFeris/AML-Risk-Scoring-Tool-Python-.git

2. Open project folder:
cd AML-Risk-Scoring-Tool-Python-

3. Run the program:
python main.py

## Example run

![Example run](screenshot/example_run.png)












