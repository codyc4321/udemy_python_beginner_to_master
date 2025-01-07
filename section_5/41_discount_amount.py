
def discount_amount():
    amount = int(input("Enter the amount: "))
    if amount <= 1000:
        discount = 0.10
    elif amount <= 5000:
        discount = 0.20
    elif amount <= 10000:
        discount = 0.30
    else:
        discount = 0.50
    multiplier = 1 - discount
    new_amount = amount * multiplier
    print(f"The amount due is {new_amount}")


if __name__ == "__main__":
    discount_amount()