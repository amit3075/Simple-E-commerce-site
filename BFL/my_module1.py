"""print("import my_module...")
test = "Test string"
def find_index(to_search,target):
    #find the index of value in sequence 
    for i,value in enumerate((to_search)):
        if value == target:
            return i
    return -1
import pratites

print("second Module's Name :{}".format(__name__))
print('hello world')
#class variable
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    
emp_1 = Employee('Amit','panthi',5000)
empl_2 = Employee('abc','cde',8000)

print(emp_1)
print(empl_2)
print(emp_1.email)
print(empl_2.email)
print(Employee.fullname(empl_2))
emp_1.fullname()
print(Employee.fullname(emp_1))
emp_1.first = 'Amit'
emp_1.last = 'Panthi'
emp_1.email ='Buddhafoolland@company.com'
emp_1.pay = 5000

empl_2.first = 'bupin'
empl_2.last ='khathauda'
empl_2.email ='Test@try.com'
empl_2.pay =1000

print(emp_1.email)
print(empl_2.email)
#instance of class

class Employee:
    num_of_emps =0
    raise_amount =1.06

    def __init__(self,first,last,pay):
        self.first =first
        self.last =last
        self.pay =pay
        self.email = first +'.' + last + '@company.com'

        Employee.num_of_emps +=1
    
    def fullname(self):
        return ('{}{}'.format(self.first,self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay*self.raise_amount)

print(Employee.num_of_emps)
emp_1 = Employee('Amit', 'Panthi',4000000)
emp_2 = Employee('Omit', 'Panthi',600000)
emp_3 = Employee('OOmit', 'Panthi',4000000)
emp_4 = Employee('mit', 'Panthi',600000)
#print(Employee.__dict__)
#emp_1.raise_amount = 1.05
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(Employee.num_of_emps)
class Employee:
     num_of_emps = 0
     raise_amt =1.04

     def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
     def fullname(self):
        return '{}{}'.format(self.first,self.last)
    
     def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt )


emp_1 =Employee('Amit','Panthi',90000000)

print(Employee.raise_amt)
print(emp_1.fullname())

print("import my_module...")
test = "Test string"
def find_index(to_search,target):
    #find the index of value in sequence 
    for i,value in enumerate((to_search)):
        if value == target:
            return i
    return -1
class InputNumber:
    def __init__(self):
        pass
    def getInput(self,Number):
        a = int(input("enter the Number"))
InputNumbers =InputNumber()
InputNumbers.getInput(InputNumber)
def getInputs():
    b =int(input("enter password"))
    return b
getInputs()"""
def echo(text:str,repetitions:int = 3)->str:
    echoed_text = " "
    for i in range(repetitions,0,-1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}"
if __name__ == "__main__":
    text = input("yell something at a mountain:")
    print(echo(text))

    