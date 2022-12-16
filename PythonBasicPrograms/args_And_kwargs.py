def function_name_print(a, b ,c, d):
    print(a, b ,c ,d)

# function_name_print("Adarsh", "Shabri", "Gopal", "Gnanesh")

# there is convention to be followed : normal, *args, kwargs
def funargs(normal, *args, **kwargs):
    print(type(args))
    print(normal)

    for items in args:
        print(items)
    print("\nLoves To:")
    for key,value in kwargs.items():
        print(f"{key} likes to {value}")

har = ["Adarsh", "Shabri", "Gopal", "Gnanesh", "Manoj Gouda"]
normal = "Vajpayee"
kw = {"Adarsh":"Explore New Things", "shabri":"do Civil Engineering.","Gopal": "Code Because he is Talented.", "Gnanesh":"Cook"}
funargs(normal,*har,**kw)
