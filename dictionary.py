emp_details = (
    ("EmpID", input("Enter Employee ID: ")),
    ("EmpName", input("Enter Employee Name: ")),
    ("EmpAge", int(input("Enter Employee Age: "))),
    ("EmpCity", input("Enter Employee City: "))
)

dict1 = dict(emp_details)

print("\nDictionary is :", dict1)

print("\nEmployee Name is :", dict1["EmpName"])
print("\nEmployee City is :", dict1["EmpCity"])

print("\nAll Keys in Dictionary")
for x in dict1:
    print(x)

print("\nAll Values in Dictionary")
for x in dict1:
    print(dict1[x])

dict1["Phno"] = int(input("\nEnter Phone Number: "))
print("\nUpdated Dictionary is :", dict1)

dict1["EmpName"] = input("\nEnter New Employee Name: ")
print("\nUpdated Dictionary is :", dict1)

dict1.pop("EmpAge")
print("\nUpdated Dictionary is :", dict1)

print("Length of Dictionary is :", len(dict1))

dict2 = dict1.copy()
print("\nNew Dictionary is :", dict2)

dict1.clear()
print("\nUpdated Dictionary is :", dict1)
