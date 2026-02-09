class Bank:
    # Constructure
    def __init__(self,name,password,balance):
        self.name=name
        self.__password=password
        self.__balance=balance
    # Deposit
    def deposit(self,name,password,amount):
        if  name!=self.name or password!=self.__password:
            return "Authentication failed"
        if amount <=0:
            return "Invalid Amount"
        
        self.__balance+=amount
        print(f"Deposit successful {amount}")
        return f"{name} Balance={self.__balance}"
            
    # Withdraw
    def withdraw(self,name,password,amount):
        if  name!=self.name or password!=self.__password:
            return "Authentication failed"
        if amount <=0:
            return "Invalid Amount"
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance-=amount
        print(f"Withdraw successful {amount}")
        return f"{name} Balance={self.__balance}"
    # Tranfer
    def transfer(self,name,password,amount,to_user):
        if  name!=self.name or password!=self.__password:
            return "Authentication failed"
        if amount <=0:
            return "Invalid Amount"
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance-=amount
        to_user.__balance+=amount
        print(f"Transfer successful To {to_user.name} {amount}")
        return f"{name} Balance={self.__balance}"
        
    # Payment
    def payment(self,name,password,amount,service):
        if  name!=self.name or password!=self.__password:
            return "Authentication failed"
        if amount <=0:
            return "Invalid Amount"
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance-=amount
        print(f"Payment successful {service} Service {amount}")
        return f"{name} Balance={self.__balance}"
    def mybalance(self,name):
        return f"{name} Balance={self.__balance}"
    # Destructure
    def __del__(self):
        return "Exiting from the bank!!!!"
user=Bank("Soknath","123",10000)
user1=Bank("kari","321",5000)
print(user.mybalance("Soknath"))
print(user.deposit("Soknath","123",5000))
print(user.withdraw("Soknath","123",2000))
print(user.transfer("Soknath","123",3000,user1))
print(user1.mybalance("kari"))
print(user.payment("Soknath","123",5000,"Internet"))
print(user.deposit("III","111",3000))

        
        