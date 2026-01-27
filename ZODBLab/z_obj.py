import ZODB, ZODB.config
import persistent.list


import persistent

class Customer(persistent.Persistent):
    def __init__(self, name=""):
        self.name=name
        self.accounts=persistent.list.PersistentList()
    
    def __str__(self):
        return "Customer name : "+self.name
    
    def setName(self, n):
        self.name=n

    def addAcc(self, a):
        self.accounts.append(a)
        return a
    

    def getAcc(self, n):
        if n>=0 and n<len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(f"Customer name : {self.name}")
        for a in self.accounts:
            print('\t', end="")
            a.printStatus()
    
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0, owner=None):
        self.balance=balance
        self.owner=owner
        self.transactions=persistent.list.PersistentList()
    

    
    @abstractmethod
    def __str__(self):
        raise NotImplementedError('not defined for base class')
    
   
    def accountDetails(self):
        print(f'Owner : {self.owner.name}')
        print(f'Blance : {self.balance}')
        print(f'Did {len(self.transactions)} transactions')
        

    def deposit(self, b):
        if b>0:
            t=Transaction(f'Deposit', b,self.balance, self.balance+b )
            self.transactions.append(t)
            self.balance+=b
            print(t)
        return b
        
    def getBalance(self):
        return self.balance
    
    @abstractmethod
    def  printStatus(self):
        pass

    def printTransaction(self):
        for t in self.transactions:
            print(t)
            print()
    
    def transfer(self, b, acc):
        if b <= self.balance and b>0:
            t=Transaction(f'Transfer to {acc.owner.name}', b,self.balance, self.balance-b )
            p=Transaction(f'Transfer from {self.owner.name}', b,acc.balance, acc.balance+b )
            self.balance-=b
            acc.balance+=b
            self.transactions.append(t)
            acc.transactions.append(p)
            print(t)
           
            

    def transferIn(self, b, acc):
        if b <= self.balance and b>0:
            self.balance+=b
            acc.balance-=b
        

    def withdraw(self, b):
        if b>=0 and self.balance-b >=0:
            t=Transaction(f'Withdraw', b,self.balance, self.balance-b )
            self.transactions.append(t)
            self.balance-=b
            print(t)


class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None):
        Account.__init__(self, balance,owner)  
        self.interest=1.00
    
    def accountDetails(self):
        print('Account Type : Saving Account')
        Account.accountDetails(self)

    def printStatus(self):
        print(f'Saving Account of Customer : {self.owner.name} : Balance : {self.balance} Interest : {self.interest} ')
    
    
class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance=0.0, owner=None):
        Account.__init__(self, balance,owner)  
        self.limit=-5000.00
    
    def accountDetails(self):
        print('Account Type : Current Account')
        Account.accountDetails(self)

    def printStatus(self):
        print(f'Current Account of Customer : {self.owner.name} : Balance : {self.balance} Limit : {self.limit} ')
    
from datetime import datetime
class Transaction (persistent.Persistent):
    def __init__(self,label, amount, ob, nb):
        self.label=label
        self.amount=amount
        self.oldbalance=ob
        self.newbalance=nb
        self.timestamp=str(datetime.now())

    def __str__(self):
        return f'{self.label}\nAmount : {self.amount}\nOld balance : {self.oldbalance}\nNew balance : {self.newbalance}\nTime Stamp : {self.timestamp}'
