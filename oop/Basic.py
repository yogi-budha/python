#  creating the atm banking system

class Atm:
    def __init__(self):
        self.pin = "";
        self.balance = 0;
        self.menu()
    
    def menu(self):
        inputval = input("""
        1.Create the Pin
        2.Change the Pin
        3.See the balance
        4.WithDraw the balance 
        5.Anything else Exit
            """
        )

        if inputval == "1":
            self.create_pin()
        elif inputval == "2":
            # Change the pin
            self.change_pin()
       
        elif inputval == "3":
            # Check the balance
            self.check_balance()
        elif inputval == "4":
            # withDraw the balance
            self.withDraw_balance()
        else:
            exit()
        
    
    def create_pin(self):
        pinval = input("enter the pin: ")
        self.pin = pinval

        balance = input("enter you balance: ")
        self.balance = balance
        self.menu()

    def change_pin(self):
        pinval = input("enter you old pin: ")
        if(pinval == self.pin):
            #create the new pin
            newPin = input("enter the new Pin")
            self.pin = newPin
        else:
            print("your pin is incorrect : try again!!")
        self.menu()

    def check_balance(self):
        pinval = input("enter the pin :")
        if(pinval == self.pin):
            print("you current balance is :" , self.balance)
        else:
            print("you pin is incorrect")
        self.menu()
    
    def withDraw_balance(self):
        pinval = input("enter the pin: ")
        if pinval == self.pin:
           drawAmount =  int(input("enter the amount you want to draw: "))
           if drawAmount <= self.balance:
            self.balance = self.balance - drawAmount
            print("you withdraw the  balance successfully , the balance is :", self.balance)
           else:
                print("garab xas ta")

        else:
            print("your pin is incorrect ")

        self.menu()

             
 

user1 = Atm()