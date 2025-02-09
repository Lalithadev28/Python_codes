class Staff:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def netSalary(self):
        hra = 0.5 * self.salary
        cca = 0.25 * self.salary
        total_salary = self.salary + hra + cca
        return hra, cca, total_salary

    def displayInfo(self):
        allowances = self.netSalary()
        hra = allowances[0]
        cca = allowances[1]
        total_salary = allowances[2]
        print(f"Name          : {self.name}")
        print(f"Role          : {self.role}")
        print(f"Salary        : {self.salary}")
        print(f"HRA           : {hra}")
        print(f"CCA           : {cca}")
        print(f"TotalSalary   : {total_salary}")

staff1 = Staff("Lalitha", "Python Developer", 50000)
staff1.displayInfo()