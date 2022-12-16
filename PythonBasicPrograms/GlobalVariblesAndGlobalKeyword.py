i = 210 # Global Variable

def function1(n):
    # i = 3 # local Variable
    m = 10
    global i  #  it allows to  change the value of global Variable.without writing this line it show error in the below u can try out.
    i = i + 45
    print(i, m)
    print(n, " Started learning Python",i)

# function1("Hi Everyone, I am Adarsh Vajpayee")
# print(m) error

x = 89
def adarsh():
    x = 25
    def gnanesh():
        global x # It will search for global variable outside the function name adarsh().
        x = 88 # It makes Variable x Outside adarsh().
    print("Before Calling gnanesh()", x)
    gnanesh()
    print("After Calling gnanesh()", x)

adarsh()
print(x)
