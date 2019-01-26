from abc import ABCMeta, abstractmethod
#'{:>{}}'.format('text',5)

class menu(metaclass=ABCMeta):
    @abstractmethod
    def print(self)->None:
        pass
    def __str__(self):
        return (type(self).__name__)
    def show(self,deep=0)->None:
        print(' '*deep*2,str(self))
        #print('{:>{}}'.format(str(self),deep*3))

class category(menu):
    def __init__(self,name):
        self.obj=[]
        self.name=str(name)

    def __str__(self):
        return self.name
    
    def print(self)->None:
        print('\n'+self.name+':')
        for o in self.obj:
            o.print()
        print('\n')
        
    def show(self, deep=0):
        print(' '*deep*2,self.name+':')
        #print('{:>{}}:'.format(self.name,deep*3)+'deep:'+str(deep))
        for o in self.obj:
            o.show(deep+1)
    
    def add(self, obj:menu)->None:
        for o in self.obj:
            if o==obj:
                print("Already in")
                return
        self.obj.append(obj)

    def remove(self, obj:menu)->None:
        for o in self.obj:
            if o==obj:
                self.obj.remove(o)
                return
        print("No such obj")


class pizza(menu):
    def print(self)->None:
        print('pizza')
        
class pasta(menu):
    def print(self)->None:
        print('pasta')

class sushi(menu):
    def print(self)->None:
        print('sushi')

class rolls(menu):
    def print(self)->None:
        print('rolls')

class cocacola(menu):
    def print(self)->None:
        print('coca-cola')

class fanta(menu):
    def print(self)->None:
        print('fanta')

class martini(menu):
    def print(self)->None:
        print('martini')

class gin(menu):
    def print(self)->None:
        print('gin')

class coffee(menu):
    def print(self)->None:
        print('coffee')

class tea(menu):
    def print(self)->None:
        print('tea')
            
MENU=category("Menu")
italian_menu=category("Italian food")
italian_menu.add(pizza())
italian_menu.add(pasta())
asian_menu=category("Asian food")
asian_menu.add(sushi())
asian_menu.add(rolls())
drinks=category("Drinks")
hot_drinks=category("Hot drinks")
hot_drinks.add(coffee())
hot_drinks.add(tea())
alcohol_drinks=category("Alcohol drinks")
alcohol_drinks.add(martini())
alcohol_drinks.add(gin())
nonalcohol_drinks=category("Non alcohol drinks")
nonalcohol_drinks.add(hot_drinks)
nonalcohol_drinks.add(cocacola())
nonalcohol_drinks.add(fanta())
drinks.add(nonalcohol_drinks)
drinks.add(alcohol_drinks)
MENU.add(italian_menu)
MENU.add(asian_menu)
MENU.add(drinks)
#MENU.print()
MENU.remove(drinks)
#MENU.print()
MENU.add(drinks)
MENU.show()




       
