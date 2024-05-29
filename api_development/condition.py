a = 30.000000000001
b = 30.000000000002

result = a == b

if result:
    print("Equal")
else:
    print("Not Equal")

if a == b:
    print("A is Equal B")
elif a > b :
    print("A is greater than B")
elif a < b :
    print('A is less than B')