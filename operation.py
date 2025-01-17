''' Operation '''
''' 
ใน Python การดำเนินการ (operation) มีหลายประเภท ซึ่งรวมถึง Arithmetic (เลขคณิต), Logical (ตรรกะ), และ Comparison (การเปรียบเทียบ) การดำเนินการเหล่านี้ใช้เพื่อคำนวณหรือประมวลผลข้อมูลในโปรแกรม มาดูกันทีละประเภทกัน 
'''

''' 1. Arithmetic Operations (การดำเนินการทางเลขคณิต) '''
''' การดำเนินการทางเลขคณิตใช้ในการคำนวณทางคณิตศาสตร์ เช่น การบวก ลบ คูณ หาร การหาค่าที่เหลือ หรือการยกกำลัง '''
x = 10
y = 3

print(x + y)   # ผลลัพธ์คือ 13
print(x - y)   # ผลลัพธ์คือ 7
print(x * y)   # ผลลัพธ์คือ 30
print(x / y)   # ผลลัพธ์คือ 3.3333...
print(x % y)   # ผลลัพธ์คือ 1
print(x ** y)  # ผลลัพธ์คือ 1000
print(x // y)  # ผลลัพธ์คือ 3

''' รวมถึง Operator สามารถใช้งานกับตัวแปรประเภท String ได้ (String Operator) โดยสามารถใช้กับการบวก (+) และการคูณ (*) ได้ '''
# การบวก string
str1 = "Hello"
str2 = "World"
result_str_add = str1 + " " + str2  # ผลลัพธ์คือ "Hello World"

# การคูณ string (การทำซ้ำ)
result_str_mul = str1 * 3  # ผลลัพธ์คือ "HelloHelloHello"

''' รวมถึง ใน Python เราสามารถใช้ Arithmetic Operators กับ List ได้ แต่จะมีข้อจำกัดบางประการ เนื่องจาก List ไม่ได้รองรับการใช้ Arithmetic Operators ทุกตัว เช่น การบวก และการคูณ แต่ไม่สามารถใช้การลบ หรือการหารกับ List ได้โดยตรง '''
# ตัวอย่างการบวก List
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result_add = list1 + list2  # ผลลัพธ์คือ [1, 2, 3, 4, 5, 6]

# ตัวอย่างการคูณ List
list1 = [1, 2, 3]

result_mul = list1 * 3  # ผลลัพธ์คือ [1, 2, 3, 1, 2, 3, 1, 2, 3]

''' 2. Logical Operations (การดำเนินการทางตรรกะ) '''
''' การดำเนินการทางตรรกะใช้ในการเปรียบเทียบค่าหรือเงื่อนไข และคืนค่าผลลัพธ์เป็น True หรือ False '''
a = True
b = False

print(a and b)  # ผลลัพธ์คือ False
print(a or b)   # ผลลัพธ์คือ True
print(not a)    # ผลลัพธ์คือ False

''' 3. Comparison Operations (การดำเนินการเปรียบเทียบ)
 '''
''' การดำเนินการเปรียบเทียบใช้ในการเปรียบเทียบค่าระหว่างตัวแปรสองตัว และคืนค่าผลลัพธ์เป็น True หรือ False '''
x = 10
y = 5

print(x == y)   # ผลลัพธ์คือ False
print(x != y)   # ผลลัพธ์คือ True
print(x > y)    # ผลลัพธ์คือ True
print(x < y)    # ผลลัพธ์คือ False
print(x >= y)   # ผลลัพธ์คือ True
print(x <= y)   # ผลลัพธ์คือ False