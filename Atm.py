class Atm:
    def __init__(self,noofcard,password):
        self.noofcard = noofcard
        self.password= password


    def check_your_balance(self):
        print("Your balance is 50000")

    def withdraw_money(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    number_on_card = input("input your card number - ")
    password_of_card  = input("enter your password number - ")

    new_user =  Atm(number_on_card ,password_of_card)

    print("Choose your activity ")
    print("1.Balance_Enquriy   2.withdraw_money")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_your_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdraw_money(amount)
    else:
        print("enter a valid number")

main()