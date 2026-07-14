# IF ELSE, STATEMENTS
# Cost of flowers
# Rose=15(1)
# Lily=30(1)
# Total=45
# Budget=int(input("Enter the Budget= "))
# if (Budget-Total>80):
#     print("Ira,give them the rose and lily")
#     print("Thank you")
# elif (Budget>50):
#     print("You budget is enough to buy the flowers")
# else:
#     print("Sorry,you don't have enough Budget to buy flowers")

# FOR LOOP
Name="Kamal sri raj"
for i in Name:
    print(i, end=",")

# FOR LOOP WITH IF, ELSE STATEMENT
Fruits=["Apple", "Mango", "Orange"]
for fruit in Fruits:
    print(fruit)
    if fruit=="Apple":
        print("It is red in colour")
    elif fruit=="Mango":
        print("It is yellow in colour")
    else:
        print("Is is orange in colour")   

# TO FIND RANGE USING FOR LOOP
for x in range(11):
    print(5*x)        

# WHILE LOOP
i=1
while(i<11):
    print(i)
    i=i+1

# BREAK AND CONTINUE IN FOR AND WHILE LOOP
for x in range(11):
    if(x==5):
        continue
    print(x)

x=0
while(x<11):
    x=x+1
    if(x==9):
        break
    print(x)    
    