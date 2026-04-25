Project: Tax and Total Calculator
# Goal: Practice function parameters, type conversion, and rounding

def total_with_tax(price, tax_percent):
    price = input("Enter the price: ")
    price = float(price)
    total = price + (price * tax_percent / 100)
    total = round(total, 2)
    return total
result = total_with_tax(0, 7)
print(result)
