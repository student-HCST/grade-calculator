def grade_calculator():
    print("===== Student Grade Calculator =====")

    subjects = int(input("Enter number of subjects: "))

    total_marks = 0
    total_max_marks = 0

    for i in range(subjects):
        print(f"\nSubject {i + 1}")
        name = input("Enter subject name: ")
        marks = float(input(f"Enter marks obtained in {name}: "))
        max_marks = float(input(f"Enter maximum marks in {name}: "))

        if marks < 0 or marks > max_marks:
            print("Invalid marks. Please try again.")
            return

        total_marks += marks
        total_max_marks += max_marks

    percentage = (total_marks / total_max_marks) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    status = "PASS" if percentage >= 40 else "FAIL"

    print("\n===== Result =====")
    print(f"Total Marks: {total_marks:.2f} / {total_max_marks:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Status: {status}")


grade_calculator()
