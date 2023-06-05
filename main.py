
## Note, the customer's/book's ID is set to be a string to allow the user freedom to choose any
# ID system in their library (letters,numbers,empty spaces,etc.),
# Also, the customer's/book's ID MUST be precise (A is not the same as a).

## Note, the program allows for multiple copies of the same book - HOWEVER:
# Like in the case of people with the same name each ID is unique to its own copy,
# this allows the library to know exactly where each copy is.

## Note, At each main function menu the users can choose to save their changes - And even if they
# Choose not to save their progress the program will save their changes automatically after typing
# Finish (before the program ends).

## Note, while entering input the users can NOT use ',' (because it distorts the text files ),
# Insted the users are instructed to use '.'


import func

if __name__=='__main__':
    try:
        a=func.readb()
        b=func.readc()
        l=func.readl()
        print("\nWelcome to the library")
        while a!=1:
            t=input("""
Please enter the function you would like to do:
To add a book/customer please type: add
To remove a book/customer please type: remove
To loan/return a book please type: loan
To find a book/customer please type: find
To display books/customers/loans/late loans please type: display
To end the program please type: finish\n""")
            t=t.lower()
            if t=="finish":
                func.save(a,b,l)
                break
            elif t=="add":
                while a!=1:
                    t=input("""
To add a book please type: 1
To add a customer please type: 2
To return to the main menu please type: escape
To save the changes you made type: save\n""")
                    t=t.lower()
                    if t=='1':
                        a=func.addb(a)
                        continue
                    elif t=='2':
                        b=func.addc(b)
                        continue
                    elif t=='escape':
                        break
                    elif t=='save':
                        func.save(a,b,l)
                        print("\nYour changes had been saved\n")
                        continue
                    else:
                        print("\nInvalid, please type: 1/2/escape/save\n")
                        continue
            elif t=="remove":
                while a!=1:
                    t=input("""
To remove a book please type: 1
To remove a customer please type: 2
To return to the main menu please type: escape
To save the changes you made type: save\n""")
                    t=t.lower()
                    if t=='1':
                        p=func.delb(a,l)
                        continue
                    elif t=='2':
                        p=func.delc(a,b,l)
                        continue
                    elif t=='escape':
                        break
                    elif t=='save':
                        func.save(a,b,l)
                        print("\nYour changes had been saved\n")
                        continue
                    else:
                        print("\nInvalid, please type: 1/2/escape/save\n")
                        continue
            elif t=="loan":
                while a!=1:
                    t=input("""
To loan a book please type: 1
To return a book please type: 2
To return to the main menu please type: escape
To save the changes you made type: save\n""")
                    t=t.lower()
                    if t=='1':
                        p=func.loan(a,b,l)
                        continue
                    elif t=='2':
                        m=func.rloan(a,l)
                        continue
                    elif t=='escape':
                        break
                    elif t=='save':
                        func.save(a,b,l)
                        print("\nYour changes had been saved\n")
                        continue
                    else:
                        print("\nInvalid, please type: 1/2/escape/save\n")
                        continue
            elif t=="find":
                while a!=1:
                    t=input("""
To find a book please type: 1
To find a customer please type: 2
To return to the main menu please type: escape\n""")
                    t=t.lower()
                    if t=='1':
                        f=func.fbook(a)
                        continue
                    elif t=='2':
                        f=func.fcus(b)
                        continue
                    elif t=='escape':
                        break
                    else:
                        print("\nInvalid, please type: 1/2/escape\n")
                        continue
            elif t=="display":
                while a!=1:
                    t=input("""
To display all the books in the library please type: 1
To display all the customers in the library please type: 2
To display all the loans in the library please type: 3
To display the late loans in the library please type: 4
To return to the main menu please type: escape\n""")
                    t=t.lower()
                    if t=='1':
                        f=func.dbook(a)
                        continue
                    elif t=='2':
                        f=func.dcus(b)
                        continue
                    elif t=='3':
                        f=func.dloan(l)
                        continue
                    elif t=='4':
                        f=func.dlate(l)
                        continue
                    elif t=='escape':
                        break
                    else:
                        print("\nInvalid, please type: 1/2/3/4/escape\n")
                        continue
            else:
                continue
    
    except Exception as e:
        print(f"An error occured: {e}")
        
    finally:
        print("\nGoodbye, and have a nice day")