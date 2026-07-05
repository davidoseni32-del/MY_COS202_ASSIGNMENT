# ==========================================
# COS202 Personal Pocket CGPA Calculator (PPC)
# Author: David Oseni
# ==========================================

print("=" * 45)
print("   PERSONAL POCKET CGPA CALCULATOR (PPC)")
print("=" * 45)

courses = int(input("Enter number of courses: "))

total_quality_points = 0
total_units = 0

for i in range(1, courses + 1):
    print(f"\nCourse {i}")

    unit = int(input("Course Unit: "))
    score = float(input("Score: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    quality = point * unit

    total_quality_points += quality
    total_units += unit

    print("Grade:", grade)
    print("Grade Point:", point)

cgpa = total_quality_points / total_units

print("\n" + "=" * 40)
print("TOTAL COURSE UNITS:", total_units)
print("TOTAL QUALITY POINTS:", total_quality_points)
print("CGPA =", round(cgpa, 2))
print("=" * 40)

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
else:
    print("Class of Degree: Pass")
