class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depozit qilindi. Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balans yetarli emas")
        else:
            self.balance -= amount
            print(f"Pul yechildi. Yangi balans: {self.balance}")

    def check_balance(self):
        print(f"Akaunt balansi: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, balance=0):
        self.accounts[account_number] = BankAccount(account_number, account_name, balance)
        print("Akaunt yaratildi")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        for account in self.accounts.values():
            print(f"Akaunt raqami: {account.account_number}, Akaunt nomi: {account.account_name}, Balans: {account.balance}")

def main():
    bank = Bank()
    while True:
        print("1. Akaunt yaratish")
        print("2. Akauntga depozit qilish")
        print("3. Akauntdan pul yechish")
        print("4. Akaunt balansini tekshirish")
        print("5. Barcha akauntrlar haqida ma'lumot")
        print("6. Dasturni to'xtatish")
        choice = input("Tanlang: ")
        if choice == "1":
            account_number = input("Akaunt raqami: ")
            account_name = input("Akaunt nomi: ")
            balance = float(input("Boshlang'ich balans: "))
            bank.create_account(account_number, account_name, balance)
        elif choice == "2":
            account_number = input("Akaunt raqami: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Depozit miqdori: "))
                account.deposit(amount)
            else:
                print("Akaunt topilmadi")
        elif choice == "3":
            account_number = input("Akaunt raqami: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Yechiladigan miqdor: "))
                account.withdraw(amount)
            else:
                print("Akaunt topilmadi")
        elif choice == "4":
            account_number = input("Akaunt raqami: ")
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Akaunt topilmadi")
        elif choice == "5":
            bank.list_accounts()
        elif choice == "6":
            break
        else:
            print("Noto'g'ri tanlov")

if __name__ == "__main__":
    main()