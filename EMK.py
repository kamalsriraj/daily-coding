Total_money = 0

print('Welcome to the game of "EVARU MEELO KOTEESWARULU"')
print("In this game i will ask some questions? \nif you answer them correctly you can win money as a reward")

Choice = (input("Are you ready: ")).lower()

if Choice == "yes":
    print("Ok, let's begin")
    player_name = input("Enter your name: ") 
elif Choice == "no":
    print("Iam wating here when ever you come")
    exit()
else:
    print("Invalid syntax, starting as Guest...")
    player_name = "Guest" 
print("  ")    

one = ["1.If you burn me I smell sweet but am not a paper and iam thin.Who am I?"]
print(*one)
options = ["A.Scented Candle", "B.Agarbatti", "C.Camphor", "D.Sandalwood log"]
print(options)
c = input("Enter the option:")
if c == "B":
    Total_money = Total_money + 500000
    print("Correct answer. you won 500,000")
else:
    Total_money = Total_money - 200000
    print("Wrong answer, your loss 200,000")
print("  ")

print("My second question")
two = ["2.I have keys but open no locks. I have space but no room. You can enter but you can't go outside.Who am I?"]
print(*two)
options = ["A.Piano", "B.Smart lock", "C.Keyboard", "D.Typewriter"]
print(options)
answer = (input("Enter the option:"))
if answer == "C":
    Total_money = Total_money + 800000
    print("Correct answer. You won 800,000")
else:
    Total_money = Total_money - 300000
    print("Wrong answer. You loss 300,000")
print(" ")

print("My third question")
third = ["The person who makes it has no need of it; the person who buys it does not use it. The person who uses it can neither see nor feel it. What is it?"]
print(*third)
options = ["A.Gift card", "B.Coffin", "C.Custom suit", "D.Wheelchair"]
print(options)
answer = (input("Enter the answer:"))
if answer == "B":
    Total_money = Total_money + 405000
    print("Correct answer. You won 405,000")
else:
    Total_money = Total_money - 500000
    print("Wrong answer. You loss 500,000")
print("  ")

print("My fouth question")
fourth = "I move without legs, I cry without eyes, and wherever I go, darkness follows me. What am I?"
print(fourth)
options = ["A.A shadow", "B.The wind", "C.Nighttime", "D.A raincloud"]
print(options)
answer = input("Enter the answer:")
if answer == "D":
    Total_money = Total_money + 300000
    print("Correct answer.You won 300,000")
else:
    Total_money = Total_money - 1050000
    print("Wrong answer.You loss 1,050,000")
print("  ")

print("LETS GO TO INTERMEDIATE LEVEL \nMy fourth question")
fifth = ["I have towns but no houses. I have forests but no trees. I have rivers but no water. What am I?"]
print(*fifth)
options = ["A.A painting", "B.A map", "C.A story book", "D.A halogram"]
print(options)
answer = (input("Enter the answer:"))
if answer == "B":
    Total_money = Total_money + 1000000
    print("Correct answer. You won 1,000,000")
else:
    Total_money = Total_money - 700000    
    print("Wrong answer. You loss 700,000")
print(" ")

print("My sixth question")
sixth = ["I weigh nothing, but you can see me. If you put me in a bucket, I will make the bucket lighter. What am I?"]
print(*sixth)
options = ["A.A hole", "B.Benethe of air", "C.A helium ballon", "D.A thought"] 
print(options)
answer = (input("Enter the answer:"))
if answer == "A":
    Total_money = Total_money + 2000000
    print("Correct answer. You won 2,000,000")
else:
    Total_money = Total_money - 1000000
    print("Wrong answer. You loss 1,000,000")

print("Do you want to go to last level.Because if you answer wrong you will loss all of your money,but if you win you get triple of your money")
Choice = input("Enter Yes or No:")
if Choice == "Yes" or Choice == "yes":
    print("Let's go then")
else:
    print(f"Ok {player_name}, you walk away! The total money you won is: {Total_money:,}")
    exit()
print("  ")

Last_question = ["A man is found dead in the middle of a vast, completely empty desert, face down in the sand.He is holding a single, broken matchstick in his hand, and there are no footprints, vehicle tracks, or signs of life anywhere around him.How did he die?"]
print(*Last_question)
print("A.He used the match to check a map, got lost, and ran out of water")
print("B.He fell from a malfunctioning hot air balloon after losing a high-stakes game of chance")
print("C He was buried by a sudden sandstorm that wiped away all surrounding tracks")
print("D.He dropped his match while trying to scare off a venomous desert predator")
answer = input("Enter the answer:")
if answer == "B":
    Total_money = Total_money * 3
    print(f"Correct answer! Congratulations {player_name}, you won Total money: {Total_money:,}")
else:
    print(f"Sorry {player_name}, you lost all the money. Better luck next time!")

print(" ")
print("Thank you for playing the game!")

