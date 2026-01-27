import ZODB, ZODB.config
import persistent
import BTrees._OOBTree
import transaction
import z_obj


path='./config.xml'

db=ZODB.config.databaseFromURL(path)
connection=db.open()
root=connection.root()

root.customers=BTrees._OOBTree.BTree()
root.customers['Dave']=z_obj.Customer('Dave')
d=root.customers['Dave']
root.customers['Jone']=z_obj.Customer('Jone')
j=root.customers['Jone']

b1=d.addAcc(z_obj.SavingAccount(400, d))
b2=j.addAcc(z_obj.CurrentAccount(200, j))



b2.deposit(500)


b1.withdraw(200)

b2.transfer(150, b1)

for c in root.customers:
    obj=root.customers[c]
    obj.printStatus()
    print()
    i=0
    while obj.getAcc(i) !=None:
        obj.getAcc(i).printTransaction()
        print()
        i+=1


transaction.commit()
