
class Books(object):

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
The book's ID is: {self.__a}
The name of the book is: {self.__b}
The name of the author is: {self.__c}
The book was published in: {self.__d}
The type of loan is: {self.__e}
The status of the loan is: {self.__f}"""   
