def  getInfo(name: str, age: int, designation: str) -> str:
    return f"Hello {name} you are {age} years old. and you are a {designation}"

print(getInfo("Monjurur", 25, "Software Engineer"))


def getSum(a: int, b: int) -> int:
    return f"Add = {a + b}"

print(getSum(10, 20))

def getSub(a: int, b: int) -> int:
    return f"sub = {a - b}"     

print(getSub(20, 10))

def getFamily(family: list) -> list:
    return family

print(getFamily(['Fahim','Tamim','Abbu','ammu','bhai','vai','bon','vagni']))
list = ['Fahim','Tamim','Abbu','ammu','bhai','vai','bon','vagni']
for l in list:
    print(l)    

