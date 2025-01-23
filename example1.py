# Example 1 หน้า 39
# ร้านไอศกรีมในท้องถิ่นจะติดตามปริมาณไอศกรีมที่พวกเขาขายเทียบกับอุณหภูมิในวันนั้น นี่คือตัวเลขของพวกเขาในช่วง 12 วันที่ผ่านมา

import numpy as np
import matplotlib.pyplot as plt

# ข้อมูล Temperature และ Ice Cream Sales
temperatures = np.array([14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2])
sales = np.array([215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408])

# หาค่าเฉลี่ยของ Temperature (x) และ Ice Cream Sales (y)
x_mean = np.mean(temperatures)
y_mean = np.mean(sales)

# คำนวณค่าสัมประสิทธิ์สหสัมพันธ์ (Correlation Coefficient, r)
r = np.corrcoef(temperatures, sales)[0, 1]

# พล็อตกราฟ
plt.figure(figsize=(10, 6))
plt.scatter(temperatures, sales, color='blue', label='Data Points') # จุดข้อมูล

# เพิ่มเส้นแนวโน้ม (Trendline)
coefficients = np.polyfit(temperatures, sales, 1) # หาค่าสมการเส้นตรง
trendline = np.poly1d(coefficients)
plt.plot(temperatures, trendline(temperatures), color='red', label='Trendline')

# ตกแต่งกราฟ
plt.title('Ice Cream Sales vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales ($)')
plt.legend()
plt.grid()
plt.show()

# แสดงผลค่าเฉลี่ยและค่า r
print(f"ค่าเฉลี่ยของ Temperature (x̄): {x_mean:.2f} °C")
print(f"ค่าเฉลี่ยของ Ice Cream Sales (ȳ): {y_mean:.2f} $")
print(f"ค่าสัมประสิทธิ์สหสัมพันธ์ (r): {r:.5f}")
# อธิบายความสัมพันธ์
if r > 0:
    print("ความสัมพันธ์เชิงบวก: เมื่ออุณหภูมิเพิ่มขึ้น ปริมาณการขายไอศกรีมมีแนวโน้มเพิ่มขึ้น")
elif r < 0:
    print("ความสัมพันธ์เชิงลบ: เมื่ออุณหภูมิเพิ่มขึ้น ปริมาณการขายไอศกรีมมีแนวโน้มลดลง")
else:
    print("ไม่พบความสัมพันธ์เชิงเส้นที่มีนัยสำคัญระหว่างอุณหภูมิและปริมาณการขายไอศกรีม")

# คำอธิบายโค้ด
# 1. นำเข้าห้องสมุด
#    - `numpy` ใช้สำหรับการคำนวณทางคณิตศาสตร์ เช่น ค่าเฉลี่ย และค่าสหสัมพันธ์
#    - `matplotlib.pyplot` ใช้สำหรับการพล็อตกราฟ
# 2. ข้อมูล
#    - สร้างอาร์เรย์สำหรับเก็บค่าของอุณหภูมิ (`temperatures`) และยอดขายไอศกรีม (`sales`)
# 3. คำนวณค่าเฉลี่ย
#    - ใช้ `np.mean` เพื่อหาค่าเฉลี่ยของแต่ละชุดข้อมูล
# 4. คำนวณค่าสหสัมพันธ์ r
#    - ใช้ `np.corrcoef` เพื่อคำนวณสัมประสิทธิ์สหสัมพันธ์
# 5. พล็อตกราฟ:
#    - สร้างกราฟกระจาย (Scatter Plot) เพื่อแสดงความสัมพันธ์ระหว่างอุณหภูมิและยอดขาย
#    - เพิ่มเส้นแนวโน้ม (Trendline) ด้วยสมการเชิงเส้น
# 6. ผลลัพธ์
#    - พิมพ์ค่าเฉลี่ยของทั้งสองตัวแปรและค่าสัมประสิทธิ์สหสัมพันธ์
