class Student:
  
  def __init__(self, name, IDnumber):
    self.name = name
    self.id = IDnumber
    
    
  def setAge(self, age):
    self.age = age
  
  def setMarks(self, marks):
    self.marks = marks
  
  
  def display(self):
    print("Name:", self.name , "Age:", self.age , "Marks:", self.marks , "IDnumber:", self.id)

emp1 = Student("Vish", "ID123")
emp1.setAge(18) #here we are using set age function to set age- different method from line above
emp1.setMarks(69)
emp1.display()