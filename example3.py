# โจทย์ฝึกหัด หน้า 44 
# List ของค่าความสัมพันธ์ (correlation coefficients)
correlations = [0.29, -0.63, 0.15, -0.34, 0.04]

# หา correlation ที่แข็งแรงที่สุด (strongest)
# เราพิจารณาค่าที่มีขนาดใหญ่ที่สุด โดยไม่สนเครื่องหมาย (absolute value)
strongest = max(correlations, key=abs)

# หา correlation ที่อ่อนที่สุด (weakest)
# เราพิจารณาค่าที่มีขนาดเล็กที่สุด โดยไม่สนเครื่องหมาย (absolute value)
weakest = min(correlations, key=abs)

# แสดงผล
print("The strongest correlation is:", strongest)
print("The weakest correlation is:", weakest)

# ข้อมูลค่าความสัมพันธ์: เราเก็บค่าความสัมพันธ์ทั้งหมดไว้ในรูปแบบของ list คือ [0.29, -0.63, 0.15, -0.34, 0.04]
# การหา correlation ที่แข็งแรงที่สุด: ใช้ฟังก์ชัน max() โดยกำหนดคีย์ key=abs เพื่อพิจารณาค่าที่มีขนาดใหญ่ที่สุดในแง่ของค่าสัมบูรณ์ 
# 𝑟 ไม่สนว่าเป็นบวกหรือลบ
# การหา correlation ที่อ่อนที่สุด: ใช้ฟังก์ชัน min() โดยกำหนดคีย์ key=abs เพื่อพิจารณาค่าที่มีขนาดเล็กที่สุดในแง่ของค่าสัมบูรณ์ 
# 𝑟 แสดงผล: ใช้ print() แสดงค่า correlation ที่แข็งแรงที่สุดและอ่อนที่สุด
