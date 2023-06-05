
from books import Books
from customeres import Customers
from loans import Loans
import datetime


# Side functions

def inv(zz):
    if zz and zz.strip():
        x=2
    else:
        x=1
    for i in range(len(zz)):
        if zz[i]==',':
            x=1
    return x

def invn(zz):
    if zz.startswith("-") and zz[1:].isdigit():
        x=2
    else:
        if zz.isdigit():
            x=2
        else:
            x=1
    return x


def invage(zz):
    if zz.isdigit():
        if int(zz)>0:
            x=2
        else:
            x=1
    else:
        x=1
    return x


def readb():
    r=open('Books.txt','r')
    t=r.readlines()
    d=[]
    for i in range(len(t)):
        aspl=t[i].split(',')
        d.append(aspl)
        aspl=0
    r.close
    return d


def readl():
    r=open('Loans.txt','r')
    t=r.readlines()
    d=[]
    for i in range(len(t)):
        aspl=t[i].split(',')
        d.append(aspl)
        aspl=0
    r.close
    return d


def readc():
    r=open('Customers.txt','r')
    t=r.readlines()
    d=[]
    for i in range(len(t)):
        aspl=t[i].split(',')
        d.append(aspl)
        aspl=0
    r.close
    return d


def flist(b,c):
    l=[]
    for i in range(1,len(b)):
        if b[i][0]==c:
            l.append(i)
            l.append(b[i][1])
            l.append(1)
    if l==[]:
        l.append('error')
    return l


def blist(a,c):
    l=[]
    for i in range(1,len(a)):
        if a[i][0]==c:
            l.append(i)
            l.append(a[i][1])
            l.append(a[i][4])
    if l==[]:
        l.append('error')
    return l


def llist(li,c): 
    l=[]
    d=0
    for i in range(1,len(li)):
        if li[i][0]==c:
            d+=1
    l.append(d)
    return l


def bloan(l,c):
    d=[]
    for i in range(1,len(l)):
        if l[i][3]==c:
            d.append(i)
            d.append(1)
    if d==[]:
        d.append(0)
    return d


def sure():
    z=0
    while z==0:
        x=input("""
Note - you are about to delete data from the system
If you are sure, please type: 1
If not, please type: 2\n""")
        if x=='1' or x=='2':
            return x
        else:
            continue


def save(a,b,l):
    r=open('Books.txt','w')
    for i in range(len(a)):
        a[i]=','.join(a[i])
    r.writelines(a)
    for i in range(len(a)):
        a[i]=list(a[i].split(','))
    r.close
    r=open('Customers.txt','w')
    for i in range(len(b)):
        b[i]=','.join(b[i])
    r.writelines(b)
    for i in range(len(b)):
        b[i]=list(b[i].split(','))
    r.close
    r=open('Loans.txt','w')
    for i in range(len(l)):
        l[i]=','.join(l[i])
    r.writelines(l)
    for i in range(len(l)):
        l[i]=list(l[i].split(','))
    r.close


def chloan(g,a,d):
    if g==1:
        a[d][-1]='Loaned\n'
    elif g==2:
        a[d][-1]='Not Loaned\n'
    

def multidelb(a,li,c):
    l=[]
    d=0
    for i in range(1,len(li)):
        if li[i][0]==c:
            l.append(li[i][3])
    ttt=[]
    for j in range (len(l)):
        for i in range(1,len(a)):
            if a[i][0]==l[j]:
                ttt.append(i)
    for i in range(len(ttt)):
        a.pop(ttt[i]-d)
        d+=1


def multidelloan(li,c):
    l=[]
    d=0
    for i in range(1,len(li)):
        if li[i][0]==c:
            l.append(i)
    for i in range(len(l)):
        li.pop(l[i]-d)
        d+=1



# Main functions

def addb(a):
    newb=0
    while newb==0:
        while newb==0:
            dfg=input("""
Please enter the book's ID (if there is ',' in the ID please use '.'
Or type escape to return to the menu: """)
            ccc=dfg.lower()
            s=blist(a,dfg)
            if ccc=='escape':
                print("Returning to the menu\n")
                return a
            elif s[-1]!='error':
                print("""\nThis Book ID is allready in the system
Please enter a new ID or type escape\n""")
                continue
            else:
                x=inv(dfg)
                if x==1:
                    print("\nInvalid, please enter the necessary information\n")
                    continue
                else:
                    break
        while newb==0:
            qwe=input("\nPlease enter the book's name (if there is ',' in the name please use '.'): ")
            x=inv(qwe)
            if x==1:
                print("\nInvalid, please enter the necessary information\n")
                continue
            else:
                break
        while newb==0:
            ert=input("\nPlease enter the author's name (if there is ',' in the name please use '.'): ")
            x=inv(ert)
            if x==1:
                print("\nInvalid, please enter the necessary information\n")
                continue
            else:
                break
        while newb==0:
            qaz=input("\nPlease enter the book's publication year (Type only full numbers): ")
            x=invn(qaz)
            if x==1:
                print("\nInvalid, please enter the necessary information\n")
                continue
            else:
                break
        while newb==0:
            nbv=input("\nPlease enter the loan's type: ")
            if nbv!='1' and nbv!='2' and nbv!='3':
                print("\nError, must be 1/2/3")
                continue
            else:
                break
        ty=Books(dfg,qwe,ert,qaz,nbv,'Not Loaned')
        print("\nThis is the information you have entered:")
        print(ty)
        ne=input("""\nIf the information is correct please type 1
If not, type any other key to return to the start: """)
        if ne=='1':
            break
        else:
            print("\nPlease enter the correct information or type escape\n")
            continue
    ty=Books(dfg,qwe,ert,qaz,nbv,'Not Loaned')
    ty=Books.morph(ty)
    ty=list(ty.split(','))
    a.append(ty)
    print("\nThe book was added to the system, returning to the menu\n")
    return a


def delb(a,l):
    cid=[a,l]
    while cid!=0:
        dfg=input("""
Please enter the book's ID (if there is ',' in the ID please use '.')
Or type escape to return to the menu: """)
        ccc=dfg.lower()
        s=blist(a,dfg)
        if ccc=='escape':
            print("Returning to the menu\n")
            return cid
        elif s[-1]=='error':
            print("""
This ID is not in the system
Please enter a new ID or type escape\n""")
            continue
        else:
            asd=bloan(l,dfg)
            if asd[-1]>0:
                t=input("""
Please note - the book is currently been loaned
To resume please type: 1
To return to the start of the function please type: 2\n""")
                if t=='1':
                    mnb=sure()
                    if mnb!='1':
                        continue
                    else:
                        l.pop(int(asd[0]))
                        break
                else:
                    continue
            else:
                mnb=sure()
                if mnb!='1':
                    continue
                else:
                    break
    a.pop(int(s[0]))
    print("\nThe book has been deleted from the system, returning to the menu\n")
    return cid


def addc(b):
    newc=1
    while newc!=0:
        while newc!=0:
            dfg=input("""
Please enter the customer's ID (if there is ',' in the ID please use '.')
Or type escape to return to the menu: """)
            ccc=dfg.lower()
            if ccc=='escape':
                print("Returning to the menu\n")
                return b
            elif ccc!='escape':
                x=inv(ccc)
                if x==1:
                    print("\nInvalid, please enter the necessary information\n")
                    continue
                else:
                    s=flist(b,dfg)
                    if s[-1]==1:
                        print("""\nThis ID is allready in the system, please enter a new ID\n""")
                        continue
                    else:
                        break
        while newc!=0:
            qwe=input("\nPlease enter the customer's name (if there is ',' in the name please use '.'): ")
            x=inv(qwe)
            if x==1:
                print("\nInvalid, please enter the necessary information\n")
                continue
            else:
                break
        while newc!=0:
            ert=input("\nPlease enter the customer's city (if there is ',' in the name please use '.'): ")
            x=inv(ert)
            if x==1:
                print("\nInvalid, please enter the necessary information\n")
                continue
            else:
                break
        while newc!=0:
            qaz=input("\nPlease enter the customer's age (full numbers only): ")
            x=invage(qaz)
            if x==1:
                print("\nInvalid, please enter the necessary information\n")
                continue
            else:
                break
        ty=Customers(dfg,qwe,ert,qaz)
        print("\nThis is the information you have entered:")
        print(ty)
        ne=input("""\nIf the information is correct please type 1
If not, type any other key to return to the start: """)
        if ne=='1':
            break
        else:
            print("\nPlease enter the correct information or type escape\n")
            continue
    ty=Customers(dfg,qwe,ert,qaz)
    ty=Customers.morph(ty)
    ty=list(ty.split(','))
    b.append(ty)
    print("\nThe customer was added to the system, returning to the menu\n")
    return b


def delc(a,b,l):
    cid=[a,b,l]
    while cid!=0:
        dfg=input("""
Please enter the customer's ID (if there is ',' in the ID please use '.')
Or type escape to return to the menu: """)
        ccc=dfg.lower()
        if ccc=='escape':
            print("Returning to the menu\n")
            return cid
        s=flist(b,dfg)
        if s[-1]!=1:
            print("""\nThis ID is not in the system
please enter a new ID or type escape\n""")
            continue
        else:
            asd=llist(l,dfg)
            if asd[-1]>0:
                while cid!=0:
                    t=input(f"""
Please note - the customer has {asd[-1]} book/s he had yet to return
To resume please type: 1 (will delete his loans and books from the system)
To return to the start of the function please type: 2 (will not delete data from the system)\n""")
                    if t=='1':
                        mnb=sure()
                        if mnb!='1':
                            continue
                        else:
                            multidelb(a,l,dfg)
                            multidelloan(l,dfg)
                            b.pop(int(s[0]))
                            print("\nThe customer has been deleted from the system, returning to the menu\n")
                            return cid
                    elif t=='2':
                        break
                    else:
                        continue
                if t=='2':
                    continue
            else:
                mnb=sure()
                if mnb!='1':
                    continue
                else:
                    break
    b.pop(int(s[0]))
    print("\nThe customer has been deleted from the system, returning to the menu\n")
    return cid


def loan(a,b,l):
    loan=[a,b,l]
    while loan!=0:
        while loan!=0:
            dfg=input("""
Please enter the customer's ID (if there is ',' in the ID please use '.')
Or type escape to return to the menu: """)
            ccc=dfg.lower()
            if ccc=='escape':
                print("Returning to the menu\n")
                return loan
            si=flist(b,dfg)
            if si[-1]!=1:
                print("""
This ID is not in the system
Please enter a new ID\n""")
                continue
            else:
                break
        while loan!=0:
            zzz=input("""
Please enter the book's ID (if there is ',' in the ID please use '.')
Or type escape to return to the menu: """)
            ccc=zzz.lower()
            s=blist(a,zzz)
            if ccc=='escape':
                print("Returning to the menu\n")
                return loan
            elif s[-1]=='error':
                print("""
This Book ID is not in the system
Please enter a new ID or type escape\n""")
                continue
            else:
                bnm=1
                for i in range(1,len(l)):
                    if l[i][3]==zzz:
                        print("\nThe book has allready been loaned")
                        bnm=0
                if bnm==0:
                    continue
                else:
                    qwe=s[1]
                    break
        nnn=si[1]
        ert=datetime.datetime.today()
        plm=ert.strftime(("%d-%m-%Y"))
        pdt=int(s[2])
        if pdt==1:
            ado=10
        elif pdt==2:
            ado=5
        elif pdt==3:
            ado=2
        ggg=ert+datetime.timedelta(ado)
        qaz=ggg.strftime(("%d-%m-%Y"))
        ty=Loans(dfg,nnn,qwe,zzz,plm,qaz)
        print("\nThis is the information you have entered:")
        print(ty)
        ne=input("""\nIf the information is correct please type 1
If not, type any other key to return to the start: """)
        if ne=='1':
            break
        else:
            print("\nPlease enter the correct information or type escape\n")
            continue
    ty=Loans(dfg,nnn,qwe,zzz,plm,qaz)
    ty=Loans.morph(ty)
    ty=list(ty.split(','))
    l.append(ty)
    chloan(1,a,s[0])
    print("\nThe book was loaned, returning to the menu\n")
    return loan


def rloan(a,l):
    while a!=0:
        dfg=input("""
Please enter the book's ID (if there is ',' in the ID please use '.')
Or type escape to return to the menu: """)
        ccc=dfg.lower()
        s=bloan(l,dfg)
        if ccc=='escape':
            print("Returning to the menu\n")
            return l
        elif s[-1]==0:
            print("""
This ID is not in the system
Please enter a new ID or type escape\n""")
            continue
        else:
            mnb=sure()
            if mnb!='1':
                continue
            else:
                l.pop(int(s[0]))
                s=blist(a,dfg)
                chloan(2,a,s[0])
                print("\nThe book was returned, returning to the menu\n")
                return l


def fcus(b):
    qaz=0
    while qaz==0:
        n=input("""
Please enter the customer's name or 
Type escape to return to the menu
If the customer's name is escape, please type escape1: """)
        n=n.lower()
        if n=='escape':
                print("\nReturning to the menu\n")
                return
        else:
            for i in range(1,len(b)):
                if b[i][1].lower()==n:
                    qaz+=1
            if qaz<1:
                print("""
This customer's name is not in the system
Please enter a new name\n""")
                continue
            print(f"\n{b[0][0] : <10}  {b[0][1] : ^30}  {b[0][2] : ^30}  {b[0][3]:>10}")
            for i in range(1,len(b)):
                if b[i][1].lower()==n:
                    print(f"{b[i][0]:<10}  {b[i][1]:^30}  {b[i][2]:^30}  {b[i][3]:>10}")
            print("Returning to the menu\n")


def fbook(a):
    qaz=0
    while qaz==0:
        n=input("""
Please enter the book's name or 
Type escape to return to the menu 
If the book's name is escape, please type escape1: """)
        n=n.lower()
        if n=='escape':
                print("\nReturning to the menu\n")
                return
        else:
            for i in range(1,len(a)):
                if a[i][1].lower()==n:
                    qaz+=1
            if qaz<1:
                print("""
This book's name is not in the system
Please enter a new name\n""")
                continue
            print(f"\n{a[0][0] : <10}  {a[0][1] : ^30}  {a[0][2] : ^30}  {a[0][3] : ^30}  {a[0][4] : ^30}  {a[0][5]:>10}")
            for i in range(1,len(a)):
                if a[i][1].lower()==n:
                    print(f"{a[i][0]:<10}  {a[i][1]:^30}  {a[i][2]:^30}  {a[i][3] : ^30}  {a[i][4] : ^30}  {a[i][5]:>10}")
            print("Returning to the menu\n")


def dloan(li):
    print("\nThe loans in the library:\n")
    for i in range(len(li)):
        print(f"\n{li[i][0] : <10}{li[i][1] : ^25}{li[i][2] : ^25}{li[i][3] : ^25}{li[i][4] : ^25}{li[i][5]:>5}")
    print("\nReturning to the menu\n")


def dbook(a):
    print("\nThe books in the library:\n")
    for i in range(len(a)):
        print(f"\n{a[i][0] : <10}{a[i][1] : ^30}{a[i][2] : ^30}{a[i][3] : ^30}{a[i][4] : ^30}{a[i][5]:>10}")
    print("\nReturning to the menu\n")


def dcus(b):
    print("\nThe customers of the library:\n")
    for i in range(len(b)):
        print(f"{b[i][0]:<10}  {b[i][1]:^30}  {b[i][2]:^30}  {b[i][3]:>10}")
    print("\nReturning to the menu\n")


def dlate(li):
    l=[]
    print("\nThe late loans in the library:\n")
    for i in range (1,len(li)):
        e=li[i][5].strip('\n')
        d=datetime.datetime.today()
        e=datetime.datetime.strptime(e,"%d-%m-%Y")
        e=e+datetime.timedelta(1)
        if d>e:
            l.append([i])
    if l==[]:
        print("There are no late loans currently\n")
        return
    print(f"\n{li[0][0] : <10}{li[0][1] : ^30}{li[0][2] : ^30}{li[0][3] : ^20}{li[0][4] : ^30}{li[0][5]:>10}")
    for i in range (1,len(li)):
        e=li[i][5].strip('\n')
        d=datetime.datetime.today()
        e=datetime.datetime.strptime(e,"%d-%m-%Y")
        if d>e:
            print(f"\n{li[i][0] : <10} {li[i][1] : ^30} {li[i][2] : ^30}{li[i][3] : ^20}{li[i][4] : ^30}{li[i][5]:>10}")
    print("\nReturning to the menu\n")



