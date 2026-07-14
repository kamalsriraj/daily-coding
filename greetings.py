from datetime import datetime

# Fetch the current date and time
a = datetime.now()

print("Full Date & Time:", a)

if(a.hour>=5 and a.hour<=12):
    print("Good morning \"sir\"")
    print("Have a nice day")
elif(a.hour>12 and a.hour<=19):
    print("Good afternoon \"sir\"")
else:
    print("Good night \"sir\"")
    print("Sweet Dreams")


import random
Companies=["Tata", "Infosys", "Google", "Amazon"]
print(random.sample(Companies,2))