# Example 2 หน้า 42
# บริษัทรถยนต์ต้องการตรวจสอบว่ามีความสัมพันธ์ระหว่างปีที่ใช้กับราคาขายหรือไม่

import numpy as np
import matplotlib.pyplot as plt

# ข้อมูลที่ให้มา
x = np.array([4, 10, 2, 1, 3, 5])  # Year Used
y = np.array([895000, 125000, 1395000, 1795000, 1245000, 695000])  # Selling Price

# คำนวณค่าเฉลี่ยของ x และ y
mean_x = np.mean(x)  # ค่าเฉลี่ยของ Year Used
mean_y = np.mean(y)  # ค่าเฉลี่ยของ Selling Price

# คำนวณค่าสัมประสิทธิ์สหสัมพันธ์ r
covariance = np.cov(x, y, ddof=0)[0, 1]  # ความแปรปรวนร่วมระหว่าง x และ y
std_x = np.std(x, ddof=0)  # ส่วนเบี่ยงเบนมาตรฐานของ x
std_y = np.std(y, ddof=0)  # ส่วนเบี่ยงเบนมาตรฐานของ y
r = covariance / (std_x * std_y)  # ค่าสัมประสิทธิ์สหสัมพันธ์

# สร้างกราฟ scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')  # จุดข้อมูล

# สร้างเส้นแนวโน้ม (Trend Line)
m, b = np.polyfit(x, y, 1)  # คำนวณสมการเส้นตรง y = mx + b
plt.plot(x, m*x + b, color='red', label=f'Trend Line (y = {m:.2f}x + {b:.2f})')

# ตกแต่งกราฟ
plt.title('Relationship between Year Used and Selling Price', fontsize=14)
plt.xlabel('Year Used', fontsize=12)
plt.ylabel('Selling Price', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# แสดงผลลัพธ์
print(f"ค่าเฉลี่ยของ x (Year Used): {mean_x:.2f}")
print(f"ค่าเฉลี่ยของ y (Selling Price): {mean_y:,.2f}")
print(f"ค่าสัมประสิทธิ์สหสัมพันธ์ (r): {r:.5f}")
# อธิบายความสัมพันธ์
if r > 0:
    print("ความสัมพันธ์เชิงบวก: ยิ่งจำนวนปีการใช้งานเพิ่มขึ้น ราคาขายมีแนวโน้มเพิ่มขึ้น")
elif r < 0:
    print("ความสัมพันธ์เชิงลบ: ยิ่งจำนวนปีการใช้งานเพิ่มขึ้น ราคาขายมีแนวโน้มลดลง")
else:
    print("ไม่มีความสัมพันธ์ระหว่างจำนวนปีการใช้งานและราคาขาย")


# อธิบายโค้ด
# 1. การนำเข้าไลบรารี
#    - `numpy` ใช้สำหรับการคำนวณทางคณิตศาสตร์ เช่น ค่าเฉลี่ย และค่าสัมประสิทธิ์สหสัมพันธ์
#    - `matplotlib.pyplot` ใช้สำหรับการวาดกราฟ

# 2. ข้อมูลที่ใช้
#    - ตัวแปร `x` เก็บจำนวนปีที่ใช้งาน (ตัวแปรอิสระ)
#    - ตัวแปร `y` เก็บราคาขาย (ตัวแปรตาม)

# 3. คำนวณค่าเฉลี่ย
#    - `np.mean()` ใช้หาค่าเฉลี่ยของ `x` และ `y`

# 4. คำนวณค่าสัมประสิทธิ์สหสัมพันธ์ r
#    - ตัวเศษ: คำนวณความสัมพันธ์ร่วมกันระหว่างความแตกต่างของค่า x และ y จากค่าเฉลี่ย
#    - ตัวส่วน: คำนวณค่าความแปรปรวนของ x และ y
#    - r: หารตัวเศษด้วยตัวส่วน

# 5. การ plot กราฟ
#    - `plt.scatter(x, y, ...)` ใช้สร้างกราฟ scatter เพื่อแสดงจุดข้อมูล
#    - `np.polyfit(x, y, 1)` ใช้หาค่าสมการเส้นตรง y = mx + b
#    - `plt.plot(...)` ใช้เพิ่มเส้นแนวโน้ม (trendline)

# 6. ผลลัพธ์ที่ได้
#    - ค่า r จะบอกถึงความสัมพันธ์ 
#      - r > 0 : ความสัมพันธ์เชิงบวก
#      - r < 0 : ความสัมพันธ์เชิงลบ
#      - r = 0 : ไม่มีความสัมพันธ์
#    กราฟจะแสดงความสัมพันธ์ระหว่างตัวแปร x และ y และเส้นแนวโน้มช่วยบ่งบอกทิศทางของความสัมพันธ์