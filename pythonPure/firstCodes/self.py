class Employee:
    def employeeDetails(self):
        self.name = "Nishi"
        print("Name = ", self.name)
        self.age = 30
        print("Age = ", self.age)
    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ", self.name)
        print("Name: ", self.age)

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()