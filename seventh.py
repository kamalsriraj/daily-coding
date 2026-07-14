# i = (1,4,9,16,25,36,48,64,81,100)
# x = int(input("Enter any number: "))
# y = 0
# while y<len(i):
#     y += 1
#     if i[y] == x:
#         print("it is found at", y)
#         break


n = int(input("Enter any number"))
sum = 0
for i in range(n+1):
    sum = sum+i
    print(sum)

    