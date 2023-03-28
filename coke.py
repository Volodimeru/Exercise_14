def main():
    amount_due = 50
    print(f"Amount Due: {amount_due}")
    while True:
        coin = int(input("Insert Coin: "))
        if coin in [5,10,25]:
            amount_due=amount_due-coin

            if amount_due <= 0:
                print("change owed:", -amount_due)
                break
            print(f"Amount Due: {amount_due}")
main()