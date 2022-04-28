class BankEMP:
 
    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age
 
    def __repr__(self):
        return self.name + self.dept + str(self.age)
 
if __name__ == '__main__':
 
    emps = [
        BankEMP('Elijah', 'IT', 20),
        BankEMP('Nik', 'Banking', 21),
        BankEMP('Lucien', 'Finance', 19)
    ]
    # sort list by `name` in the natural order
    emps.sort(key=lambda x: x.name)
    print(emps)
 
    # sort list by `name` in reverse order
    emps.sort(key=lambda x: x.name, reverse=True)
    print(emps)