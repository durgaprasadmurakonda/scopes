#creates 3 functions and create every function scoped variables in them and create 3 global 
#variables and try to access global variables in every function and try to access 
#every function variables in functions and try to access function variables outside 
#of the function

dp = 10
m =  9
s = 4

def abc():
    p = 5
    print (p)
    print (dp)
    def xyz():
        c = 8
        print(m)
        print (c)
        print(p)
       
        def mno ():
          g = 4
          print(g)
          print(p)
          print(c)
          print(s)
          
          mno()
    
    xyz()

abc()

print (dp+s)
print(s+m)













