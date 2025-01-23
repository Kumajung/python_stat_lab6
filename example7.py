# Example 4
# อุปกรณ์อิเล็กทรอนิกส์" และตรวจสอบความสัมพันธ์ระหว่าง "อายุการใช้งาน" กับ "ราคาขาย"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# อ่านข้อมูลจากไฟล์ CSV
data = pd.read_csv('/kaggle/input/unit5data2/data.csv')  # ไฟล์ data.csv ควรมีคอลัมน์ 'Years_Used' และ 'Selling_Price'
x = data['Years_Used'].values  # ค่า Years Used
y = data['Selling_Price'].values  # ค่า Selling Price

# คำนวณค่าเฉลี่ยของ x และ y
mean_x = np.mean(x)  # ค่าเฉลี่ยของ Years Used
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
plt.title('Relationship between Years Used and Selling Price of Electronic Devices', fontsize=14)
plt.xlabel('Years Used', fontsize=12)
plt.ylabel('Selling Price', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# แสดงผลลัพธ์
print(f"ค่าเฉลี่ยของ x (Years Used): {mean_x:.2f}")
print(f"ค่าเฉลี่ยของ y (Selling Price): {mean_y:,.2f}")
print(f"ค่าสัมประสิทธิ์สหสัมพันธ์ (r): {r:.5f}")

# อธิบายความสัมพันธ์
if r > 0:
    print("ความสัมพันธ์เชิงบวก: ยิ่งอายุการใช้งานเพิ่มขึ้น ราคาขายมีแนวโน้มเพิ่มขึ้น")
elif r < 0:
    print("ความสัมพันธ์เชิงลบ: ยิ่งอายุการใช้งานเพิ่มขึ้น ราคาขายมีแนวโน้มลดลง")
else:
    print("ไม่มีความสัมพันธ์ระหว่างอายุการใช้งานและราคาขาย")