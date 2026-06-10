# MINI PROJECT 1: Student Data Manager (Half Day)
# Build a Student Record System using OOP
# Features: Add, Update, Delete, Search Records

class StudentManager:
    def __init__(self):
        self.rolls = []
        self.names = []
        self.grades = []

    def add(self):
        roll = input("Enter Roll Number: ")
        if roll in self.rolls:
            print("Roll number already exists!")
            return
        
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        
        self.rolls.append(roll)
        self.names.append(name)
        self.grades.append(grade)
        print("Student added!")

    def update(self):
        roll = input("Enter Roll Number to update: ")
        if roll in self.rolls:
            index = self.rolls.index(roll)
            self.names[index] = input("Enter New Name: ")
            self.grades[index] = input("Enter New Grade: ")
            print("Student updated!")
        else:
            print("Not found!")

    def delete(self):
        roll = input("Enter Roll Number to delete: ")
        if roll in self.rolls:
            index = self.rolls.index(roll)
            self.rolls.pop(index)
            self.names.pop(index)
            self.grades.pop(index)
            print("Student deleted!")
        else:
            print("Not found!")

    def search(self):
        roll = input("Enter Roll Number to search: ")
        if roll in self.rolls:
            index = self.rolls.index(roll)
            print(f"Name: {self.names[index]} | Grade: {self.grades[index]}")
        else:
            print("Not found!")

manager = StudentManager()

while True:
    print("\n1. Add  2. Update  3. Delete  4. Search  5. Exit")
    choice = input("Choose (1-5): ")
    
    if choice == "1": manager.add()
    elif choice == "2": manager.update()
    elif choice == "3": manager.delete()
    elif choice == "4": manager.search()
    elif choice == "5": break
    else: print("Invalid choice!")