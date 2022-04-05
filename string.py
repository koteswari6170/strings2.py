# p="pythON proGRAMMing"
# print(p.swapcase()) #PYTHon PROgrammING
# a=4 ; b=66
# print(a) #4
# del a,b
# print(a,b) #Nameerror=name 'a' is not defined
# print("Buy this for Rs.{d} or for Rs.{b}".format(d=11,b=5)) #Buy this for Rs.11 or for Rs.5
'''expantabs  ,by default=8'''
# a='k\tv\tB'
# print(a.expandtabs(0)) #kvB 
# print(a.expandtabs(1)) #k v B
# print(a.expandtabs(2)) #k  v  B
# print(a.expandtabs(3)) #k   v   B
# print(a.expandtabs(4)) #k    v    B
# print(a.expandtabs(5)) #k     v     B
# print(a.expandtabs(6)) #k      v      B
# print(a.expandtabs(7)) #k       v       B
# print(a.expandtabs(8)) #k        v        B
# print(a.expandtabs())  #k        v        B
# print(a.expandtabs(-1)) #kvB
'''join'''
# a="welcome","to","Andra"
# n="java"
# print('-'.join(a)) #welocme-to-Andra
# print('*'.join(a)) #welcome*to*Andra
# print('*'.join(n)) #j*a*v*a
# print("-".join("Hello")) #H-e-l-l-o
"maketrans and translate"
# r="helly hello"
# a=r.maketrans("l","r") 
# print(a,type(a)) #dict
# print(r.translate(a)) #herry herro
# s="kaveri tutukuri"
# a=s.maketrans("uk","oo")
# print(a,type(a)) #dict
# print(s.translate(a)) #oaveri totooori
# b="chinnaa"
# v=b.maketrans("aa","uu")
# print(b.translate(v)) #chinnuu
# r={}
# print(r,type(r))  #dict
# a={1:'hello',2:'python'} 
# print(a[1])   #hello
# print(a[2])   #python
'''splitlines'''
# a="hello\nCore Python\nProgramming"
# print(a) #hello newline Core Python newline Programming
# g=a.splitlines()
# print(g,type(g)) #['hello', 'Core Python', 'Programming'] list
# print(g[0]) #hello
# print(g[1]) #Core Python
# print(g[2]) #Programming
# print(g[4]) #Indexerror: list index out of range
# h="HelloWelcome to python programming"
# w=h.split()
# print(w)# ['HelloWelcome', 'to', 'python', 'programming'] list
# print(w[0][::-1]) #emocleWolleH
# print("Guntur City".split()) #['Guntur', 'City]
# y="HaiWhat is your Name?"
# print(y.split()) #['HaiWhat', 'is', 'your', 'Name?']
# print(y.split(" "))#['HaiWhat', 'is', 'your', 'Name?']
# print(y.split("")) #Valueerror: empty separator
# m=4.2,6
# print(type(m)) #tuple
# p=[int(x) for x in input().split()]
# print(sum(p)) #7,8 =15
# print("The sum is"+' '+str(sum(p))) #The sum is 15
# print("The sum is",sum(p))#The sum is 15
# c="Hello Welcome to Josh Innovations"
# print(c.split()) #['Hello', 'Welcome', 'to', 'Josh', 'Innovations']
# n="Hello:Welcome:Hyderabad"
# print(n.split(":"))#['Hello', 'Welcome', 'to', 'Hyderabad']
# m="python&c&java&c++"
# print(m.split("&"))#['python', 'c', 'java', 'c++']

# v=r"hello\nollywod"
# print(v,type(v)) #hello\nollywood str
# k="Hello!\nWelcome to \nGuntur"
# print(k.splitlines())#['Hello!', 'Welcome to ', 'Guntur']
# print(k.split())#['Hello!', 'Welcome', 'to', 'Guntur']
# d="Hello!\nWelcome to \nGuntur"
# print(d.splitlines(True))#['Hello!\n', 'Welcome to \n', 'Guntur']
# f="hello"
# print(f.zfill(6)) #0hello
# print(f.zfill(7)) #00hello
'''partition'''
# i="Hey! How are you Doing?"
# print(i.partition("are")) #('Hey How ', 'are', ' you Doing?)
# t= "Hey! How are you Doing?"
# r=t.partition("you") 
# print(r)#('Hey! How are ', 'you', ' doing')
# print(r[2])#Doing?
# m="We are Learning Python Programing , Python is Basic need \
    # for ML DS AI DL BigData...etc"
# print(m.partition("python"))
# print(m.rpartition("python"))

# x="Python"
# print(x.ljust(8),"programming Basics") #Python  programming Basics
# y="python"
# print(y.rjust(8),"python programming") #  python python programming
# s="programm"
# print(s.rjust(10,'R')) #RRprogramm
# v="programm"
# print(v.ljust(10,'V')) #programmVV
# b="Python, C, Java"
# l=b.rsplit(",", 0)
# v=b.rsplit(", ", 1)
# n=b.split(", ", 1)
# print(l)#['Python, C, Java']
# print(v)#['Python,  C', 'Java']
# print(n)#['Python', 'C, Java']
