def printthakur(str):
    return f"Ye string Adarsh Ko de de {str}"

def wrongadd(num1,num2):
    return num1+num2+5

# If we import this file to avoid re writing the above code. it will lead to execution of this whole file + the file which
# import this file. so to avoid this we use if_name_==_main_

print("And the file name is : ",__name__)

if __name__ == '__main__':
    print(printthakur("Thakur."))
    add = wrongadd(4 ,6)
    print(add)

# The use of if __name__ == '__main__': is that whatever code written in main will get executed only when we run this file.
