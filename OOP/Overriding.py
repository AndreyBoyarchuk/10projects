class Employee:
    def setNumberOfWorkingHours(self):
        self.numberofworkingHours = 40

    def displayNumberofworkingHours(self):
        print(self.numberofworkingHours)
class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberofworkingHours = 50

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()



employee=Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end ='')
employee.displayNumberofworkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end ='')
trainee.displayNumberofworkingHours()

trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset: ", end ='')
trainee.displayNumberofworkingHours()