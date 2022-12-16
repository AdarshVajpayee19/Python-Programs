import time

initial1 = time.time()
print("*************WHILE LOOP*************")
k = 0
while(k<45):
    print("This is Adarsh Vajpayee")
    time.sleep(2)
    k = k + 1
print(f"While Loop ran in{time.time()-initial1}","seconds")

initial2 = time.time()
print("*************FOR LOOP*************")
for i in range(45):
    print("Hi i am Adarsh V")
print(f"For loop ran in {time.time()-initial2}","seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
