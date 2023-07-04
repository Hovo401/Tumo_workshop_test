

# ----------- 1 -----------
# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} - even number.")
#     else:
#         print(f"{number} - odd number.")

# num = int(input("Enter the number: "))

# check_even_odd(num)

# =========================


# ----------- 2 -----------
# def sum (n):
#     out = 0
#     for i in range(1, n+1):
#         out += i
#     return out

# n = int(input("Enter the N: "))

# result = sum(n)
# print(f"result: {result}")

# =========================

# ----------- 3 -----------
# def Fibonacci (n):
#     if (n <= 0 ):
#         return 'Invalid'
    
#     sequence = [0, 1]

#     while sequence[-1] < n:
#         next_number = sequence[-1] + sequence[-2]
#         if next_number >= n:
#             break
#         sequence.append(next_number)

#     return sequence


# n = int(input("Enter the N: "))

# result = Fibonacci(n)
# print(f"result: {result}")

# =========================

# ----------- 4 -----------

# def find_max_element(lst):
#     max_element = lst[0]  

#     for element in lst:
#         if element > max_element:
#             max_element = element

#     return max_element


# input_list = input("Enter a list separated by a space: ").split(" ")
# input_list = [int(num) for num in input_list]

# max_element = find_max_element(input_list)

# print("Largest element in the list:", max_element)

# =========================


# ----------- 5 -----------

class BankAccount:
    def __init__(self, account_password = '0000', balance=0.0):
        self.account_password = account_password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The amount {amount} was successfully deposited into the account. New balance: {self.balance}")

    def withdraw(self, amount, password):
        if (amount > self.balance or self.account_password != password):
            print("Error.")
        else:
            self.balance -= amount
            print(f"The amount {amount} was successfully deducted from the account. New balance: {self.balance}")

    def get_balance(self):
        return self.balance




account = BankAccount('1010', 1000.0)

print("Current balance:", account.get_balance())

account.deposit(500.0)

account.withdraw(200.0,'1010')

print("Current balance:", account.get_balance())


# =========================
