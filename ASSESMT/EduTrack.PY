# EduTrack - Simple Attendance System
# Made by Beginner Developer :)

attendance = []   # list to store attendance records

# Function to mark attendance
def mark_attendance():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    date = input("Enter date (dd-mm-yyyy): ")
    status = input("Present/Absent (P/A): ")

    record = {
        "name": name,
        "roll": roll,
        "course": course,
        "date": date,
        "status": status.upper()
    }
    attendance.append(record)
    print("Attendance marked!\n")

# Function to show attendance of one student
def student_report():
    roll = input("Enter roll number: ")
    total = 0
    present = 0
    absent = 0
    for rec in attendance:
        if rec["roll"] == roll:
            total += 1
            if rec["status"] == "P":
                present += 1
            else:
                absent += 1
    if total == 0:
        print("No record found.\n")
    else:
        percent = (present / total) * 100
        print(f"\nReport for Roll No: {roll}")
        print("Total Days:", total)
        print("Present:", present)
        print("Absent:", absent)
        print("Attendance %:", percent)
        if percent < 75:
            print("⚠ Defaulter (Below 75%)\n")
        else:
            print("Good Attendance!\n")

# Function to show report of full class
def class_report():
    if len(attendance) == 0:
        print("No records yet.\n")
        return
    students = {}
    for rec in attendance:
        roll = rec["roll"]
        if roll not in students:
            students[roll] = {"present": 0, "total": 0}
        students[roll]["total"] += 1
        if rec["status"] == "P":
            students[roll]["present"] += 1

    print("\nClass Report")
    print("Roll\tPresent\tTotal\t% Attendance\tStatus")
    for roll, data in students.items():
        percent = (data["present"] / data["total"]) * 100
        status = "Defaulter" if percent < 75 else "OK"
        print(f"{roll}\t{data['present']}\t{data['total']}\t{percent:.2f}%\t{status}")
    print()

# Main program
while True:
    print("==== EduTrack Menu ====")
    print("1. Mark Attendance")
    print("2. Student Report")
    print("3. Class Report")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        student_report()
    elif choice == "3":
        class_report()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
