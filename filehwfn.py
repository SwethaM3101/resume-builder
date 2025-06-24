def write():
    a=input("enter your create file name:")
    b=input("enter your content:")
    c=open(a,"w")
    c.write(b)
    c.close()
    b=open(a,"r")
    print(f"//{a}//file content:",b.read())
    print("---------")
    return a
    
        
def read():
    try:
        a=input("enter your read file name:")
        c=open(a,"r")
        print(c.read())
        print("-----")
    except FileNotFoundError:
        print("file not found error:....please enter correct file name")
        read()

def append():
    a=input("enter your add context file name:")
    b=input("enter your  add content:")
    c=open(a,"a")
    c.write(b)
    c.close()
    b=open(a,"r")
    print(f"//{a}//file content:",b.read())
    print("-----")
    return a



def append1():
    n=input("add your content:")
    c=open(m,"a")
    c.write(n)
    c.close()
    o=open(m,"r")
    print(f"//{m}//file content:",o.read())
    o.close()
    print("-----")
    

    
    



while True:
    print("------------------")
    print("/n file read write add mini project:")
    print("1.create new file and write")
    print("2.file read")
    print("3.created file content add")
    print("4.exit")

    s=int(input("enter your above choice:"))

    if s==1:
        m=write()
        while True:
            e=input("add content this file yes or no:")
            if e=="yes":
                append1()
            
            else:
                break

    elif s==2:
        read()

    elif s==3:
        m=append()
        while True:
            e=input("add content this file yes or no:")
            if e=="yes":
                append1()
            
            else:
                break
    elif s==4:
        print("exiting bye....see you later")
        break

    else:
        print("-----")
        print("please enter correct choice number")



























































                      
































































































































































































































