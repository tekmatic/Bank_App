import json

class Customer:
    def open_account(self):
        customers = {}
        fullname = input("Enter full name: ").lower()
        initial_balance = float(input("Enter initial amount: "))
        pin = int(input("Enter a 4 digit PIN: "))
        customers = {"name":fullname, "balance":initial_balance, "PIN":pin}
        print()
        print("COngratulations! Your account has been created.")

        with open('customers.json', 'w') as f:
            json.dump(customers, f, indent=4)


class Get_Customer:
    def read_json(self, filename = 'customers.json'):
        with open(filename) as json_file:
            user_list = json.load(json_file)
            user = user_list['name']
            balance = user_list['balance']
            print("Customer name is: {0} | balance is: ${1}".format((user), (balance)))

def exit():
    print("Thank you for your business.  See you soon.")

c = Customer()
g = Get_Customer()

choice = input("""
1: Open an account
2: Get Account Balance
3: Deposit to Account
4: Withdraw from Account
5: Exit

Please enter your selection: """)

if choice == "1":
    c.open_account()
elif choice == "2":
    g.read_json()
else:
    exit()