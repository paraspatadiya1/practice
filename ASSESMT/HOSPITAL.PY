# MediTrack - Simple Hospital System (Beginner Version)
# All code in ONE file :)

patients = []
doctors = []
appointments = []
records = []

# Add doctor
def add_doctor():
    name = input("Enter doctor name: ")
    spec = input("Enter specialization: ")
    doc = {"name": name, "spec": spec}
    doctors.append(doc)
    print("Doctor added!\n")

# Add patient
def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    pat = {"name": name, "age": age}
    patients.append(pat)
    print("Patient added!\n")

# Book appointment
def book_appointment():
    if len(patients) == 0 or len(doctors) == 0:
        print("Please add doctors and patients first!\n")
        return
    pname = input("Enter patient name: ")
    dname = input("Enter doctor name: ")
    date = input("Enter date (dd-mm-yyyy): ")
    app = {"patient": pname, "doctor": dname, "date": date, "status": "Pending"}
    appointments.append(app)
    print("Appointment booked!\n")

# Show appointments
def show_appointments():
    if len(appointments) == 0:
        print("No appointments yet.\n")
        return
    print("\nAll Appointments:")
    for a in appointments:
        print(f"{a['patient']} -> {a['doctor']} on {a['date']} ({a['status']})")
    print()

# Upload medical record
def upload_record():
    pname = input("Enter patient name: ")
    notes = input("Enter diagnosis/prescription notes: ")
    rec = {"patient": pname, "notes": notes}
    records.append(rec)
    print("Record uploaded!\n")

# Show patient history
def patient_history():
    pname = input("Enter patient name: ")
    print(f"\nHistory for {pname}:")
    for r in records:
        if r["patient"] == pname:
            print("Notes:", r["notes"])
    for a in appointments:
        if a["patient"] == pname:
            print("Appointment with", a["doctor"], "on", a["date"])
    print()

# ----------------- Main Menu -----------------
while True:
    print("=== MediTrack Menu ===")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Book Appointment")
    print("4. Show Appointments")
    print("5. Upload Medical Record")
    print("6. Patient History")
    print("7. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_doctor()
    elif ch == "2":
        add_patient()
    elif ch == "3":
        book_appointment()
    elif ch == "4":
        show_appointments()
    elif ch == "5":
        upload_record()
    elif ch == "6":
        patient_history()
    elif ch == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
