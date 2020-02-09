# Below code demonstrates multiple inheritance and also Global and Local variables

company = 'CTS'  # Global Variable
city = 'Hyd'


class A:
    def __init__(self):
        self.name = 'Sharath'
        self.study = 'Python'

    def printName(self):
        print("Name from Class A: ", self.name)
        print("Study from Class A: ", self.study)
        print("Company from Class A: ", company)
        print("City from Class A: ", city)


class B:
    def __init__(self):
        self.name = 'Gaurav'
        self.study = 'Java'
        global company  # Always use global keyword to use the global variable
        company = 'TR'

    def printName(self):
        print("Name from Class B: ", self.name)
        print("Study from Class B: ", self.study)
        print("Company from Class B: ", company)
        print("City from Class B: ", city)


class C(A, B):
    def __init__(self):
        super().__init__()

    def printName(self):
        newcity = 'Pune'
        # Values will come from A: In case of multiple inheritance, values will be used from Left class towards Right
        print("Name from Class C: ", self.name)
        print("Study from Class C: ", self.study)
        print("Company from Class C: ", company)
        print("City from Class C: ", newcity)


a = A()
a.printName()

b = B()
b.printName()

c = C()
c.printName()
