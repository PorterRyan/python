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
    output = output + '\n' + "{0:<12} ${1:<10.2f} ${2:<10.2f}".format(input_cat, input_month, yearly)
    print()

print()
print("Monthly Budget")
print("=================================")
print("Item         Month       Year")
print("=================================")
print(output)