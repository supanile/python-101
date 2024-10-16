''' ตัวอย่างที่ 1 โปรแกรมตัดเกรด '''
# รับคะแนนจากผู้ใช้
score = int(input("Enter the student's score: "))

# ตรวจสอบคะแนนและตัดเกรด
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'

# แสดงผลลัพธ์
print(f"The grade for the score {score} is: {grade}")

''' ตัวอย่างที่ 2 โปรแกรมตัดเกรดหลายคน '''
# กำหนดจำนวนของนักเรียน
num_students = int(input("Enter the number of students: "))

# วนลูปรับคะแนนและตัดเกรดสำหรับนักเรียนแต่ละคน
for i in range(num_students):
    score = int(input(f"Enter the score for student {i + 1}: "))

    # ตรวจสอบคะแนนและตัดเกรด
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # แสดงผลลัพธ์
    print(f"Student {i + 1}: Score = {score}, Grade = {grade}")