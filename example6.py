# Example 3
# ร้านขายร่มในท้องถิ่นจะติดตามปริมาณร่มที่พวกเขาขายเทียบกับปริมาณฝนในวันนั้น นี่คือตัวเลขของพวกเขาในช่วง 500 วันที่ผ่านมา

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# นำเข้าข้อมูลจากไฟล์ .csv
data = pd.read_csv('/kaggle/input/unit5data/umbrella_sales.csv')

# แยกข้อมูล Rainfall และ Umbrella Sales
rainfall = data['Rainfall (mm)'].values
sales = data['Umbrella Sales'].values

# หาค่าเฉลี่ยของ Rainfall (x) และ Umbrella Sales (y)
x_mean = np.mean(rainfall)
y_mean = np.mean(sales)

# คำนวณค่าสัมประสิทธิ์สหสัมพันธ์ (Correlation Coefficient, r)
r = np.corrcoef(rainfall, sales)[0, 1]

# พล็อตกราฟ
plt.figure(figsize=(10, 6))
plt.scatter(rainfall, sales, color='green', label='Data Points') # จุดข้อมูล

# เพิ่มเส้นแนวโน้ม (Trendline)
coefficients = np.polyfit(rainfall, sales, 1) # หาค่าสมการเส้นตรง
trendline = np.poly1d(coefficients)
plt.plot(rainfall, trendline(rainfall), color='orange', label='Trendline')

# ตกแต่งกราฟ
plt.title('Umbrella Sales vs Rainfall')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Umbrella Sales ($)')
plt.legend()
plt.grid()
plt.show()

# แสดงผลค่าเฉลี่ยและค่า r
print(f"ค่าเฉลี่ยของ Rainfall (x̄): {x_mean:.2f} mm")
print(f"ค่าเฉลี่ยของ Umbrella Sales (ȳ): {y_mean:.2f} $")
print(f"ค่าสัมประสิทธิ์สหสัมพันธ์ (r): {r:.5f}")

# อธิบายความสัมพันธ์
if r > 0:
    print("ความสัมพันธ์เชิงบวก: เมื่อปริมาณฝนเพิ่มขึ้น ยอดขายร่มมีแนวโน้มเพิ่มขึ้น")
elif r < 0:
    print("ความสัมพันธ์เชิงลบ: เมื่อปริมาณฝนเพิ่มขึ้น ยอดขายร่มมีแนวโน้มลดลง")
else:
    print("ไม่พบความสัมพันธ์เชิงเส้นที่มีนัยสำคัญระหว่างปริมาณฝนและยอดขายร่ม")