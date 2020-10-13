#! C:\Users\Ryan\AppData\Local\Programs\Python\Python38 python3
# personal_budget_inputs.py

print("Monthly Budget Program")
print()
print("Enter a category name of \"stop\" to submit")
print()
# Input loop
input_cat = ''
output = ''
while input_cat != 'stop' or 'STOP':
    input_cat = input("Enter a category name: ")
    if input_cat == 'stop':
        break
    input_month = float(input("Enter a monthly amount: "))
    yearly = input_month * 12
    output = output + '\n' + f"{input_cat:<12} ${input_month:<10.2f} ${yearly:<10.2f}"
    print()

print()
print("Monthly Budget")
print("=================================")
print("Item         Month       Year")
print("=================================")
print(output)