class ATM:
    def __init__(self, user_pin, initial_balance=0):
        self.user_pin = user_pin
        self.balance = initial_balance
        self.authenticated = False

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")
            if pin == self.user_pin:
                self.authenticated = True
                print("Authentication successful!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")
        print("Too many incorrect attempts. Exiting.")
        return False

    def show_menu(self):
        while True:
            print("===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Deposit amount must be positive.\n")
            else:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be positive.\n")
            elif amount > self.balance:
                print("Insufficient balance.\n")
            else:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

# -------------------- Main Execution --------------------
if __name__ == "__main__":
    # Create an ATM object with a sample PIN and optional starting balance
    atm = ATM(user_pin="1234", initial_balance=500.00)

    if atm.authenticate():
        atm.show_menu()
