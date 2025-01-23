# โจทย์ฝึกหัด หน้า 45
# เพื่อวิเคราะห์ความสัมพันธ์ระหว่างค่าใช้จ่ายโฆษณา x และยอดขาย y 
# สำหรับธุรกิจค้าปลีกขนาดเล็ก 
# การคำนวณค่าสถิติต่าง ๆ เช่น ค่าสัมประสิทธิ์สหสัมพันธ์ (Correlation Coefficient) 
# และสร้างแบบจำลองการถดถอยเชิงเส้น (Linear Regression) เพื่อทำนายยอดขายจากค่าใช้จ่ายโฆษณา

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# ข้อมูลค่าใช้จ่ายโฆษณา (x) และยอดขาย (y)
x = np.array([1.4, 1.6, 1.6, 2.0, 2.0, 2.2, 2.4, 2.6])
y = np.array([180, 184, 190, 220, 186, 215, 205, 240])

# สร้าง DataFrame เพื่อความสะดวกในการจัดการข้อมูล
data = pd.DataFrame({'Advertising Expenditure (x)': x, 'Sales (y)': y})

# ทำนายยอดขายจากค่าใช้จ่ายโฆษณา
y_pred = model.predict(x.reshape(-1, 1))
# พล็อตกราฟแสดงข้อมูลและเส้นถดถอย
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('Ad spend (x)')
plt.ylabel('circulation (y)')
plt.title('Relationship between ad spend and sales')
plt.legend()
plt.show()

# คำนวณค่าสัมประสิทธิ์สหสัมพันธ์
correlation_coefficient, _ = pearsonr(x, y)
print(f"ค่าสัมประสิทธิ์สหสัมพันธ์: {correlation_coefficient:.2f}")

# สร้างแบบจำลองการถดถอยเชิงเส้น
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# คำนวณค่าความชัน (slope) และค่าตัดแกน y (intercept)
slope = model.coef_[0]
intercept = model.intercept_
print(f"สมการถดถอยเชิงเส้น: y = {slope:.2f}x + {intercept:.2f}")