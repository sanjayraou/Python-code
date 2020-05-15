def pcm():
    p=float(input("Enter your physics marks: "))
    c=float(input("Enter your Chemistry marks: "))
    m=float(input("Enter your Maths marks: "))
    pcm=p+c+m
    return pcm


def eba():
    e=float(input("Enter your Economics marks: "))
    b=float(input("Enter your Business studies marks: "))
    a=float(input("Enter your Accountancy marks: "))
    eba=e+b+a
    return eba

def percent():
    tot=globals()['sum']
    percent=tot/4
    print("The percentage is {} %".format(percent))

def grade():
    tot=globals()['sum']
    per=tot/4
    if per>=85:
        print("Distinction")
    if per>=60 and per<85:
        print("First class")
    if per>=35 and per<60:
        print("Second class")
    if per<35:
        print("FAIl")

print("Enter your stream")
print("1.science 2. Commerce")
ch=int(input())
if ch==1:
    print("Enter your comination")
    print("1.PCMB\n 2.PCMC\n 3.PCMS\n 4.PCME\n")
    ch1=int(input())
    if ch1==1:
        b=float(input("Enter your biology marks: "))
        pcm=pcm()
        sum=b+pcm
        print("Total marks is",sum)
        percent()
        grade()
    if ch1==2:
        cs=float(input("Enter your Computer science marks: "))
        pcm=pcm()
        sum=cs+pcm
        print('Total marks is',sum)
        percent()
        grade()

    if ch1==3:
        stat=float(input("Enter your Statistics marks: "))
        pcm=pcm()
        sum=pcm+stat
        print("Total marks is",sum)
        percent()
        grade()
    if ch1==4:
        el=float(input("Enter your electronics marks: "))
        pcm=pcm()
        sum=pcm+el
        print("Total marks is",sum)
        percent()
        grade()

if ch==2:
    print("Enter your stream")
    print('1.BEBA 2.SEBA 3.CEBA')
    ch2=int(input())
    if ch2==1:
        ba=float(input("enter your Basic maths marks:"))
        eba=eba()
        sum=eba+ba
        print("The total marks is: ",sum)
        percent()
        grade()
    if ch2==2:
        sta=float(input("Enter your Statistics marks: "))
        eba=eba()
        sum=eba+sta
        print("The total marks is",sum)
        percent()
        grade()
    if ch2==3:
        comp=float(input("Enter your computer science marks: "))
        eba=eba()
        sum=eba+comp
        print("The total marks is",sum)
        percent()
        grade()



print("NOTE: This is excluding the language marks")
