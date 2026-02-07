from score import (
    balance_score,
    country_risk_score,    
    transaction_type_score,
    risk_level
)


balance = int(input("Enter your balance: "))
country = input("Enter country: ")
transaction_type = input("Enter transaction type cash/transaction/crypto: ")

b = balance_score(balance)
c = country_risk_score(country)
t = transaction_type_score(transaction_type)

total = b + c + t


print("Balance score is: " , b)
print("Country risk score is:" , c)
print("Transaction type score is: " , t)
print("Total score is: " , total)
print("Risk level is: " , risk_level(total))


