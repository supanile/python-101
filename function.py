''' Function '''
'''
Function คือกลุ่มของคำสั่งที่ถูกจัดเก็บไว้ด้วยกันภายใต้ชื่อหนึ่งชื่อ เพื่อให้สามารถเรียกใช้งานได้หลายครั้งโดยไม่ต้องเขียนคำสั่งซ้ำไปซ้ำมา function ช่วยทำให้โปรแกรมเป็นระเบียบและอ่านเข้าใจได้ง่ายขึ้น อีกทั้งยังช่วยลดความซ้ำซ้อนของ code อีกด้วย
การสร้างfunction ใน Python ใช้คำสำคัญ (keyword) def ตามด้วยชื่อของfunction และวงเล็บ (). ข้างในวงเล็บสามารถใส่พารามิเตอร์ (parameter) ซึ่งเป็นตัวแปรที่ส่งค่าไปยังfunction เมื่อfunction ถูกเรียกใช้งาน คำสั่งที่อยู่ในfunction จะถูกดำเนินการ
'''
def function_name(parameters):
    # คำสั่งที่ต้องการให้ function ทำ
    return value  # ค่าที่ function จะส่งคืน (ถ้ามี)
'''
- Parameter คือค่าหรือข้อมูลที่คุณสามารถส่งเข้าไปในfunction เมื่อคุณเรียกใช้งานfunction นั้น พารามิเตอร์จะถูกประกาศในวงเล็บ () หลังชื่อfunction เมื่อคุณกำหนดfunction พารามิเตอร์เหล่านี้เป็นตัวแปรที่function สามารถใช้เพื่อดำเนินการต่าง ๆ ได้
- Return value (ค่าที่คืนกลับมา) คือค่าที่function ส่งกลับไปยังที่เรียกใช้function เมื่อfunction ทำงานเสร็จแล้ว การคืนค่าทำได้โดยใช้คำสั่ง return ภายในfunction function สามารถคืนค่ากลับมาได้เพียงค่าเดียว แต่ค่านั้นอาจเป็นโครงสร้างข้อมูลเช่น ลิสต์ (list), ทูเพิล (tuple), หรือดิกชันนารี (dictionary) ที่ประกอบด้วยหลายค่า
ตัวอย่าง
''' 

''' ตัวอย่างการใช้ function ใน Python '''
''' 
ตัวอย่างที่ 1: function ที่ไม่รับ parameter และไม่คืนค่า
function ที่ไม่รับ parameter และไม่คืนค่า คือfunction ที่ไม่ต้องการข้อมูลจากภายนอกเพื่อทำงาน และจะไม่มีการส่งค่ากลับไปหลังจากที่function ทำงานเสร็จ function ประเภทนี้มักใช้เพื่อดำเนินการเฉพาะบางอย่าง เช่น การแสดงข้อความบนหน้าจอ โดยไม่ต้องคำนวณหรือประมวลผลข้อมูลเพิ่มเติม 
'''
def greet():
    print("Hello, welcome to Python programming!")
    
# เรียกใช้function  greet
greet()
''' function greet() ไม่มี parameter (ไม่มีข้อมูลที่ต้องส่งไปให้function ) และไม่คืนค่า (ไม่มี return statement)

เมื่อเรียกใช้ greet(), function จะพิมพ์ข้อความ "Hello, welcome to Python programming!" บนหน้าจอ '''

''' 
ตัวอย่างที่ 2: function ที่รับ parameter และคืนค่า
function ที่รับ parameter และคืนค่า คือ function ที่ต้องการข้อมูลจากภายนอกเพื่อใช้ในการประมวลผล และจะส่งค่ากลับไปเมื่อfunction ทำงานเสร็จ function ประเภทนี้มักใช้เมื่อคุณต้องการส่งข้อมูลเข้าสู่function เพื่อให้function ดำเนินการบางอย่างกับข้อมูลนั้น และผลลัพธ์จากการประมวลผลนั้นจะถูกส่งกลับออกมาเพื่อใช้งานต่อไป
'''
def add_numbers(a, b):
    result = a + b
    return result

# เรียกใช้function  add_numbers พร้อมส่งค่าพารามิเตอร์
sum_result = add_numbers(5, 7)
print(f"The sum is: {sum_result}")
# ตัวอย่างนี้ function add\_numbers(a, b) รับพารามิเตอร์สองตัว ( a และ b) แล้วนำมาบวกกัน จากนั้นส่งผลลัพธ์กลับด้วย return. ผลลัพธ์จะถูกเก็บในตัวแปร sum\_result และพิมพ์ออกมา

''' ลองกับตัวอย่าง ตัดเกรด '''
def calculate_grade(score):
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
    
    return grade

# function หลักเพื่อเรียกใช้และแสดงผล
def main():
    # รับคะแนนจากผู้ใช้
    score = int(input("Enter the student's score: "))
    
    # เรียกใช้function  calculate_grade() เพื่อคำนวณเกรด
    grade = calculate_grade(score)
    
    # แสดงผลลัพธ์
    print(f"The grade for the score {score} is: {grade}")

# เรียกใช้function  main() เพื่อเริ่มโปรแกรม
main()

'''
function calculate_grade(score):
function นี้รับพารามิเตอร์ score ซึ่งเป็นคะแนนของนักเรียนที่ต้องการตัดเกรด
ใช้โครงสร้างควบคุมแบบเงื่อนไข ( if, elif, else) เพื่อตรวจสอบค่าของ score และกำหนดเกรด ( grade) ตามเงื่อนไขที่กำหนดไว้
สุดท้ายfunction จะส่งค่าเกรด ( grade) กลับไปให้ที่เรียกใช้function ด้วยคำสั่ง return
function main():
function นี้ทำหน้าที่เป็นfunction หลักในการรับข้อมูลจากผู้ใช้, เรียกใช้function calculate_grade() เพื่อคำนวณเกรด และแสดงผลลัพธ์
เริ่มด้วยการรับคะแนนจากผู้ใช้ด้วย input(), จากนั้นส่งคะแนนนั้นไปยังfunction calculate_grade() เพื่อคำนวณเกรด
เมื่อได้ค่าเกรดที่คืนกลับมาแล้ว จะแสดงผลลัพธ์เป็นข้อความที่บอกคะแนนและเกรด
เรียกใช้ function main():
code ส่วนสุดท้ายเรียกใช้function main() เพื่อเริ่มการทำงานของโปรแกรมทั้งหมด
'''