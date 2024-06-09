class family:
 
    def getFamily(self):
        return f"Hello {self.name} you are {self.age} years old. and you are a {self.designation}"


obj1 = family()
print(obj1.getFamily("Monjurur", 25, "Software Engineer"))