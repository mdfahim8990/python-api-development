class family:
 
    def getFamily(self):
        return f"Hello {self.name} you are{self.age}  years old. and you are a {self.designation} in the family"

print(family().getFamily("Fahim",25,"Son"))    