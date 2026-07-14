info = {
    "name" : {"kamal" : 95, "ravi" : 96, "harsha" : 97},
    "city"  : {"hyd": "kamal", "mum" : "ravi", "del" : "harsha"},
}

student_name = input("Enter the student name: ")
if student_name in info["name"]:
    n = int(input("Enter the marks: "))
    if n >= info["name"][student_name]:
        print("Nice marks")
    else:
        print("Work hard")