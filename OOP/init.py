class Employee:

    def __init__(self,name):
        self.name = name

    def employeeDetails(self):
        print(self.name )


employee = Employee("Mark")

employee.employeeDetails()
