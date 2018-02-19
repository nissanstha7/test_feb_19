class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def mail_generator(self):
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@gmail.com"

    def display(self):
        print("{}\n{}\n{}\n{}\n".format(self.first_name, self.last_name, self.salary, self.email))

employee_1 = Employee("Nissan", "Shrestha", "1000000000")
employee_1.mail_generator()
employee_1.display()
