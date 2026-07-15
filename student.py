class Student:
    
    students = []  

    def __init__(self, roll_no: int, name: str, marks: float):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def grade(self) -> str:
        m = self.marks
        if m >= 90:
            return "A+"
        if m >= 80:
            return "A"
        if m >= 70:
            return "B"
        if m >= 60:
            return "C"
        if m >= 40:
            return "D"
        return "Fail"

    def display(self) -> None:
        print("-" * 32)
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Grade   : {self.grade()}")
        print("-" * 32)

    @classmethod
    def add_student(cls, roll_no: int, name: str, marks: float):
        if cls.find_by_roll(roll_no) is not None:
            return False, "Roll Number must be unique."
        if not (0 <= marks <= 100):
            return False, "Marks should be between 0 and 100."
        s = Student(roll_no, name, marks)
        cls.students.append(s)
        return True, "Student added successfully."

    @classmethod
    def view_all(cls):
        return cls.students

    @classmethod
    def find_by_roll(cls, roll_no: int):
        for s in cls.students:
            if s.roll_no == roll_no:
                return s
        return None

    @classmethod
    def update_marks(cls, roll_no: int, marks: float):
        s = cls.find_by_roll(roll_no)
        if s is None:
            return False, "Student Not Found"
        if not (0 <= marks <= 100):
            return False, "Marks should be between 0 and 100."
        s.marks = marks
        return True, "Marks Updated Successfully"

    @classmethod
    def delete(cls, roll_no: int):
        s = cls.find_by_roll(roll_no)
        if s is None:
            return False, "Student Not Found"
        cls.students.remove(s)
        return True, "Student Deleted Successfully"

    @classmethod
    def get_topper(cls):
        if not cls.students:
            return None
        return max(cls.students, key=lambda s: s.marks)

    @staticmethod
    def parse_int(value: str, default=None):
        try:
            return int(value)
        except Exception:
            return default
