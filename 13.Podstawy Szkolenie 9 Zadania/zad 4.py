# Stwórz Pythonową klasę BankAccount, która reprezentować będzie konto bankowe zawierające takie informacje jak:
# numer_konta, nazwa właściciela konta, stan konta.
# 1. Stwórz konstruktor odpowiednio uzupełniający pola.
# 2. Napisz metodę deposit(), która przyjmować będzie kwotę, jaką chcesz wpłacić na konto.
# Dodaj założenie, że za każde wpłacone 100 zł, pobierana będzie prowizja równa 2 zł.
# 3. Stwórz metodę withdraw(), która przyjmować będzie jako parametr kwotę, którą chcesz wypłacić z konta.
# Program ma wyświetlać odpowiedni komunikat,
# gdy niemożliwe jest wypłacanie wskazanej ilości pieniędzy
# (przykładowo z powodu braku wystarczającej ilości środków na koncie).
# 4. Napisz metodę change_ownership(),
# która przyjmować będzie imię nowego właściciela konta i będzie aplikowała tę zmianę w obiekcie klasy.
# 5. Stwórz metodę display(), która będzie wyświetlać wszystkie informacje o koncie.


class BankAccount:
    def __init__(self, account_number, owner, account_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        self.account_balance -= round(amount/100) * 2

    def withdraw(self, amount):
        if amount > self.account_balance:
            print(f"niemozliwe do realizacji , saldo wynosi {self.account_balance} , a chcesz wyplacic amount")

    def change_ownership(self, new_owner):
        self.owner = new_owner

    def display(self):
        print(f"account_number to {self.account_number} , "
              f"owner to {self.owner} ,"
              f"account_balance to {self.account_balance} ")


BankAccount1 = BankAccount("001", "Pan A", 200)
BankAccount1.display()
BankAccount1.deposit(900)
BankAccount1.withdraw(50)
BankAccount1.change_ownership("Pan B")
BankAccount1.display()
