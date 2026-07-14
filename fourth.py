# # # LISTS
# Movies=["Rakka", "Varanasi", "Dragon", "Kalki", "The Paradise", "Toxic"]
# print(Movies)
# print(Movies[0])
# print(Movies[1])
# print(Movies[2])
# print(len(Movies))
# print(Movies[:-4])
# print(Movies[0:len(Movies)])
# print(Movies[0:len(Movies)-4])
# if("Rakka"):
#     print("Coming soon")
# print(Movies[1:6:2])
# Nothing=[i*i for i in range(21) if i%2==0]
# print(Nothing)

# # LISTS METHODS
# n=[2,7,478,37,5,4,335,9,4,4,8,7]
# print(n)
# n.append(88)
# print(n)
# print(n.count(4))
# n.sort(reverse=True)
# print(n)
# n.reverse()
# print(n)
# n.insert(3,99)
# print(n)
# m=[1,2,3,4]
# n.extend(m)
# print(n)
# k=n+m
# print(k) 
# print(type(n))
# print(m.index(3))

# # TUPLE
# tup=("Kamal", "sri", "raj", 1,2,2,2,45,6,7,74)
# print(type(tup))
# tup2=tup[0:4]
# print(tup2)
# print(tup[0])
# print(tup.count(2))

# TUPLE INTO LISTS AND AGAIN INTO TUPLE
subjects=("Telugu", "Hindi", "English", "Maths", "Science", "Social", "Sanskrit")
l=list(subjects)
l.append("GK")
l.pop(4)
subjects=tuple(l)
print(l)

# ADDITION OF TWO TUPLES
a=(2,3,4,5,9,2,2,2)
b=(77,88,5843,22)
print(a+b)
print(a.count(2))

print(a.index(2,4,6))