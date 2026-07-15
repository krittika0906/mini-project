from student import Student


def show_menu():
	print("==============================")
	print(" Student Management System")
	print("==============================")
	print("1. Add Student")
	print("2. View Students")
	print("3. Search Student")
	print("4. Update Marks")
	print("5. Delete Student")
	print("6. Show Topper")
	print("7. Exit")


def add_student():
	roll = input("Enter Roll Number: ")
	name = input("Enter Name: ")
	marks = input("Enter Marks: ")
	
	Student.add_student(roll, name, marks)
	print("Student added")


def view_students():
	students = Student.view_all()
	if len(students) == 0:
		print("No students found.")
	else:
		for student in students:
			student.display()


def search_student():
	roll = input("Enter Roll Number to search: ")
	student = Student.find_by_roll(roll)
	
	if student:
		student.display()
	else:
		print("Student Not Found")


def update_marks():
	roll = input("Enter Roll Number to update: ")
	new_marks = input("Enter new marks: ")
	
	Student.update_marks(roll, new_marks)
	print("Marks updated!")


def delete_student():
	roll = input("Enter Roll Number to delete: ")
	Student.delete(roll)
	print("Student deleted!")


def show_topper():
	topper = Student.get_topper()
	if topper:
		print("Topper:")
		topper.display()
	else:
		print("No students found.")


def main():
	while True:
		show_menu()
		choice = input("Enter your choice: ")
		
		if choice == "1":
			add_student()
		elif choice == "2":
			view_students()
		elif choice == "3":
			search_student()
		elif choice == "4":
			update_marks()
		elif choice == "5":
			delete_student()
		elif choice == "6":
			show_topper()
		elif choice == "7":
			print("Exiting...")
			break
		else:
			print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
	main()