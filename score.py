

def balance_score(balance):
    if balance >= 10000:
        return 3
    elif balance >= 5000 and balance <= 9999:        
        return 2
    elif balance >= 1000 and balance <= 4999:
        return 1
    else: 
        return 0
    
def load_list(path: str) -> set[str]:
    with open(path, "r",
encoding="utf-8") as f:
        return {line.strip().lower()
for line in f if line.strip()}

EU_HIGH_RISK = load_list("eu_high_risk_countries.txt")
FATF_BLACK = load_list("fatf_black_list.txt")
FATF_GREY = load_list("fatf_grey_list.txt")

def normalize_country(name:str) -> str:
    return name.strip().lower()

def country_risk_score(country: str) ->int:
    c = normalize_country(country)

    if c in EU_HIGH_RISK:
        return 3
    elif c in FATF_BLACK:
        return 3
    elif c in FATF_GREY:
        return 2
    else:
         return 0 

    
def transaction_type_score(transaction_type):
    if transaction_type == "crypto":
        return 3
    elif transaction_type == "cash":
        return 2
    elif transaction_type == "tranafer":
        return 1
    else:
        return 0
    
def risk_level(risk):
    if risk >= 7:
        return " High"
    elif risk >= 4:
        return "Medium"
    else:
        return "low"
    






