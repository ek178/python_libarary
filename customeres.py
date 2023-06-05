
class Customers(object):
    def __init__(self,a,b,c,d):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
    
    def __str__(self):
        return f"""
The customer's ID is: {self.__a}
The customer's name is: {self.__b}
The customer's city is: {self.__c}
The customer's age is: {self.__d}"""
    
    def morph(self):
        return f"{self.__a},{self.__b},{self.__c},{self.__d}\n"


