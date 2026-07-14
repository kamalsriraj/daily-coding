print("Hello, Iam python")
print("I challenge you that what number you enters, i will give its table upto 20")
a=input("Shall we begin:yes or no=")
if(a=="no"):
    print("ok, you challenge me after")
    exit()
else:
    print("ok, let's go")
    num=int(input("Enter the number=")) 
for k in range(1,21):
    print(num*k)   


