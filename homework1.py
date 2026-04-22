if __name__ == "__main__":
    # Bài 1
    print("Bài 1: ")
    price = 120000
    quantity = 3
    Total = price * quantity
    print("Tong_tien: ", Total , "VND")
    
    # Bài 2
    print("Bài 2: ")
    price = 500000
    discount_percent = 10
    Discount = price * discount_percent / 100
    Total = price - Discount
    print("So tien duoc giam: ", int(Discount), "VND")
    print("Gia cuoi cung: ", int(Total), "VND")
    
    # Bài 3
    print("Bài 3: ")
    salary_per_day = 300000
    working_days = 22
    Total = salary_per_day * working_days
    print("Luong thang: ", Total, "VND")
    
    # Bài 4
    print("Bài 4: ")
    distance_km = 12
    cost_per_km = 5000
    Total = distance_km * cost_per_km
    print("Tong phi van chuyen: ", Total, "VND")
    
    # Bài 5
    print("Bài 5: ")
    total_storage = 256
    used_storage = 180
    Total = total_storage - used_storage
    print("Dung luong con lai: ", Total)
    
    # Bài 6
    print("Bài 6: ")
    balance = 200000
    item_price = 150000
    if balance >= item_price:
        print("Thanh toan thanh cong")
    else:
        print("Ban khong du tien trong tai khoan")
        
    # Bài 7
    print("Bài 7: ")
    order_value = 250000
    shipping_fee = 200000
    if order_value >= shipping_fee:
        print("Ban duoc free ship")
    else:
        print("Don hang khong duoc free ship")
        
    # Bài 8
    print("Bài 8: ")
    is_logged_in = True
    is_admin = False
    if is_logged_in == True:
        print("Da login vao he thong")
        if is_admin == True:
            print ("Chinh la admin")
        else:
            print("Khong phai la admin")
    
    # Bài 9
    print("Bài 9: ")
    hour = 18
    if hour >= 9:
        if hour <= 18:
            print("Nam trong gio lam viec")
        else:
            print("Khong nam trong gio lam viec")
            
    # Bài 10
    print("Bài 10: ")
    email = "user@gmail.com"
    if "@" in email and "." in email:
        print("true")
    else:
        print("false")
        
    # Bài 11
    print("Bài 11: ")
    order_value = 180000
    limit = 200000
    total = order_value + 30000
    if order_value >= limit:
        print("Free ship")
    else:
        print("Tong tien phai tra: ", total)
        
    # Bài 12
    print("Bài 12: ")
    performance_score = 9
    if performance_score == 9:
        print("Thuong 5000000")
    if performance_score == 7:
        print("Thuong 2000000")
    if performance_score < 7:
        print("Khong thuong")
        
    # Bài 13
    print("Bài 13: ")
    status_code = 2
    if status_code == 1:
        print("Pending")  
    elif status_code == 2:
        print("Shipping")  
    elif status_code == 3:
        print("Delivered")
    else:
        print("Unknown")
        
    # Bài 14
    print("Bài 14: ")
    age = 15
    if age < 12:
        print(50000)
    elif age <= 17:
        print(70000)
    else:
        print(100000)
        
    # Bài 15
    print("Bài 15: ")
    total_spent = 1200000
    if total_spent >= 1000000:
        print("VIP")
    elif total_spent >= 500000:
        print("Gold")
    else:
        print("Normal")
        
    # Bài 16
    print("Bài 16: ")
    kwh = 135
    total = 0
    if kwh <= 50:
        total = kwh * 1678
    elif kwh <= 100:
        total = 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        total = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    print(total)
    
    # Bài 17
    print("Bài 17: ")
    base_salary = 10000000
    kpi = 0.85
    if kpi >= 0.9:
        total = base_salary * 1.3
    elif kpi >= 0.8:
        total = base_salary * 1.1
    else:
        total = base_salary
    print(int(total))
    
    # Bài 18
    print("Bài 18: ")
    distance = 12
    total = 0
    if distance <= 1:
        total = 15000
    elif distance <= 10:
        total = 15000 + (distance - 1) * 12000
    else:
        total = 15000 + 9 * 12000 + (distance - 10) * 10000
    print(total)
    
    # Bài 19
    print("Bài 19: ")
    income = 15000000
    debt = 3000000
    if income >= 10000000 and debt <= income * 0.5:
        print("Duoc vay")
    else:
        print("Khong du dieu kien")
    
    # Bài 20
    print("Bài 20: ")
    price = 1000000
    is_member = True
    voucher = 100000
    if is_member:
        price = price * 0.9
    price = price - voucher
    if price < 0:
        price = 0
    print(int(price))