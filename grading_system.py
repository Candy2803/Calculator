students = {}
def student():
    for i in range(3):
        print(f"\nEnter Details for Student {i+1}")
        id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        math = input("Enter Math Grade: ")
        math = int(math)
        english = input("Enter English Grade: ")
        english = int(english)
        chemistry = input("Enter Chemistry Grade: ")
        chemistry = int(chemistry)
        biology = input("Enter Biology Grade: ")
        biology = int(biology)
        physics = input("Enter Physics Grade: ")
        physics = int(physics)
        
        average = (math + english + chemistry + biology + physics) / 5
        
        if average >= 70:
            grade = 'A'
        elif average >= 60:
            grade = 'B'
        elif average >= 50:
            grade = 'C'
        elif average >= 40:
            grade = 'D'
        else:
            grade = 'E'
            
        students[id] = {
        'Name': name,
        'Math': math,
        'English': english,
        'Chemistry': chemistry,
        'Biology': biology,
        'Physics': physics,
        'Average': round(average, 2),
        'Grade': grade
    }

    print("\nAll students' data:")
    for student, details in students.items():
        print(f"\nStudent: {student}")
        for subject, score in details.items():
            print(f"{subject}: {score}")
        
student()