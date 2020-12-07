# This is not the way to do it
class Employee:
    name = "Ben"
    designation = "Sales Excecutive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print( "Target has been achieved" )
        else:
            print( "Target has not achieved" )


employeeOne = Employee()
print(employeeOne.name)
emp
