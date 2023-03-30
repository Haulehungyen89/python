import math
try:
    # Nhập bán kính đường tròn dưới dạng thập phân 
    r=float(input("Nhập bán kính đường tròn: "))
    cv=2*math.pi*r            # math.pi khai báo giá trị "pi" trong toán học 
    dt= pow(r,2)*math.pi      # tương đương với r**2 
    print("Chu vi hình tròn là: ",cv)
    print("Diện tích hình tròn là: ",dt)
except:
    print("Lỗi rồi !")        # Hiển thị với input là str,bool,complex
