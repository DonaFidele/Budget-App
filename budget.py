#coding:utf-8

class Category:

    def __init__(self,name):
        self.ledger=[]
        self.name=name
        self.retrait=0
        self.depot=0

    def __repr__(self):
        char=''
        char+=self.name.center(30,'*')
        char+='\n'

        for i in self.ledger:
            if len(i["description"])>23:
                a=i["description"][:23]
                b=str("{:.2f}".format(i["amount"]))
                char+=a
                char+=' '*(30-len(a+b))
                char+=b
            else:
                a=i["description"]
                b=str("{:.2f}".format(i["amount"]))
                char+=a
                char+=' '*(30-len(a+b))
                char+=b
            char+='\n'   
        char+=f'Total: {self.get_balance()}' 
        return char

    def deposit(self,amount,description=None):
        self.depot+=amount
        if description==None:
            self.ledger.append({"amount":amount,"description":""})
        else:
            self.ledger.append({"amount":amount,"description":description})
        #print(self.ledger)

    def withdraw(self,amount,description=None):    
        self.retrait+=amount
        funds=sum([amounts["amount"] for amounts in self.ledger])

        if amount <= funds:            
            if description==None:  
                self.ledger.append({"amount":-amount,"description":""})
            else:

                self.ledger.append({"amount":-amount,"description":description})
            return True
        return False

    def get_balance(self):
        return sum([amounts["amount"] for amounts in self.ledger])

    def transfer(self,amount,budgetCategory):
        if self.get_balance()>amount:
          self.withdraw(amount,description=f"Transfer to {budgetCategory.name}")
          budgetCategory.deposit(amount,description=f"Transfer from {self.name}")
          return True
        return False
        
    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        return True
        

def create_spend_chart(liste):
    pourcentageC=0;pourcentageE=0
    for categorie in liste:
        
        if categorie.name=="Food":
            pourcentageF=categorie.ledger[0]["amount"]-categorie.get_balance()
        if categorie.name=="Clothing":
            pourcentageC=categorie.ledger[0]["amount"]-categorie.get_balance()
        if categorie.name=="Auto":
            pourcentageE=categorie.ledger[0]["amount"]-categorie.get_balance()

    
    representation="""
Percentage spent by category
100| J  L  w           
 90| K  m  x          
 80| M  N  _           
 70| D  O  z           
 60| V  +  W         
 50| f  q  X          
 40| G  R  Y          
 30| H  S  Z         
 20| I  T  Q    
 10| j  U  E   
  0| k  v  B   
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g"""

    food='JKMDVfGHIjk';df={'J':100,'K':90,'M':80,'D':70,'V':60,'f':50,'G':40,'H':30,'I':20,'j':10,'k':0}
    clothing='LmNO+qRSTUv';dc={'L':100,'m':90,'N':80,'O':70,'+':60,'q':50,'R':40,'S':30,'T':20,'U':10,'v':0}
    auto='wx_zWXYZQEB';da={'w':100,'x':90,'_':80,'z':70,'W':60,'X':50,'Y':40,'Z':30,'Q':20,'E':10,'B':0}
    for i in food:
        if df[i]<=pourcentageF:
            representation=representation.replace(i,'o')
        else:
            representation=representation.replace(i,' ')
    for i in clothing:
        if dc[i] <= pourcentageC:
            representation=representation.replace(i,'o')
        else:
            representation=representation.replace(i,' ')
    for i in auto:
        if da[i]<=pourcentageE:
            representation=representation.replace(i,'o')
        else:
            representation=representation.replace(i,' ')

    return representation.strip()