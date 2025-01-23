# โจทย์ฝึกหัด หน้า 46
# คำนวณค่าสถิติต่าง ๆ เช่น ค่าเฉลี่ย, ความแปรปรวน, และค่าสัมประสิทธิ์สหสัมพันธ์ (correlation coefficient)

import numpy as np

# กำหนดค่าต่าง ๆ จากข้อมูลที่ให้มา
n = 50
sum_x = 112.5
sum_y = 4.83
sum_xy = 15.255
sum_x2 = 356.25
sum_y2 = 0.667

# คำนวณค่าเฉลี่ยของ x และ y
mean_x = sum_x / n
mean_y = sum_y / n

# คำนวณความแปรปรวนของ x และ y
var_x = (sum_x2 / n) - (mean_x ** 2)
var_y = (sum_y2 / n) - (mean_y ** 2)

# คำนวณค่าสัมประสิทธิ์สหสัมพันธ์ (correlation coefficient)
cov_xy = (sum_xy / n) - (mean_x * mean_y)
corr_coef = cov_xy / (np.sqrt(var_x) * np.sqrt(var_y))

# แสดงผลลัพธ์
print(f"ค่าเฉลี่ยของ x: {mean_x:.4f}")
print(f"ค่าเฉลี่ยของ y: {mean_y:.4f}")
print(f"ความแปรปรวนของ x: {var_x:.4f}")
print(f"ความแปรปรวนของ y: {var_y:.4f}")
print(f"ค่าสัมประสิทธิ์สหสัมพันธ์: {corr_coef:.4f}")