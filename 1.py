'''
def mul_by(n):
    def inner(x):
        return x*n
    return inner
times_2=mul_by(2)
times_3=mul_by(3)
print(times_2(5))
print(times_3(10))
'''
'''
def great(text):
    def inner(name):
        return f"{text},{name}"
    return inner
hi=great("hello")
print(hi("vijay"))
   '''
   
x=100
y=10
def display():
    x=22
    print("x=",x)
    print("locally",x+y)
display()
print("x=", x)
y=10
y=25
print("least of y:",y)
print("globally",x+y)        


    