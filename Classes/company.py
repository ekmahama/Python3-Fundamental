from employee import Employee

class Company:
    def __init__(self, name):
        self.name = name
        self.employee = []
    def AddEmployy(self, newEmployee):
        self.employee.append(newEmployee)

    def GetEmployee(self):
        for emp in self.employee:
            print(emp.fname)

if __name__=="__main__":
    microsoft = Company("Microsoft")
    eddie = Employee("Mahama", "Kofi",50000)
    lark  = Employee("Tetteh","Mavis", 52000)
    microsoft.AddEmployy(eddie)
    microsoft.AddEmployy(lark)
    print(microsoft.GetEmployee())

