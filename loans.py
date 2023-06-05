
class Loans(object):
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def morph(self):
        return f"{self.__a},{self.__b},{self.__c},{self.__d},{self.__e},{self.__f}\n"

    def __str__(self):
        return f"""
The customer's ID is: {self.__a}
The customer's name is: {self.__b}
The book's name is: {self.__c}
The book's ID is: {self.__d}
The book was loaned in: {self.__e}
The book must be returned by: {self.__f}"""
