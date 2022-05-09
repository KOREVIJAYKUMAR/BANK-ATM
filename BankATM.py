class atm ():

    def __init__ (self,number,pin):
        self.number=number
        self.pin=pin
        

    def displayInfo(self) :
        print('number:'+self.number)
        print('pin:'+self.pin)
       
object1=atm('123','1234') 

object2=atm('456','5678') 

print('slect any options below:')
print("""1.123
2.456
""")

n=input('enter your choice')

if (n=='1'):
    object1.displayInfo()
elif (n=='2'):
    object2.displayInfo()
else :
    print('enter correct option')