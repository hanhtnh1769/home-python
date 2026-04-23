if __name__ == "__main__":
    print("=" * 40)
    print("BÀI 1: In danh sách sản phẩm (có index)")
    print("=" * 40)
    
    products = ["Áo", "Quần", "Giày", "Mũ"]
    
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 2: Tính tổng tiền giỏ hàng")
    print("=" * 40)
    
    prices = [100000, 200000, 150000]
    
    tong = 0
    for p in prices:
        tong = tong + p
    
    print(f"Tổng tiền: {tong} VND")
    
    
    print("\n" + "=" * 40)
    print("BÀI 3: Đếm sản phẩm giá cao")
    print("=" * 40)
    
    prices = [100000, 500000, 700000, 200000]
    
    dem = 0
    for p in prices:
        if p > 300000:
            dem = dem + 1
    
    print(f"Sản phẩm giá cao: {dem}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 4: Tìm giá lớn nhất")
    print("=" * 40)
    
    prices = [100000, 500000, 700000, 200000]
    
    lon_nhat = prices[0]
    for p in prices:
        if p > lon_nhat:
            lon_nhat = p
    
    print(f"Giá cao nhất: {lon_nhat}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 5: Tổng số chẵn")
    print("=" * 40)
    
    numbers = [1, 2, 3, 4, 5, 6]
    
    tong_chan = 0
    for n in numbers:
        if n % 2 == 0:
            tong_chan = tong_chan + n
    
    print(f"Tổng chẵn: {tong_chan}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 6: Bảng cửu chương mini")
    print("=" * 40)
    
    for i in range(2, 6):       # từ 2 đến 5
        for j in range(1, 11):  # từ 1 đến 10
            print(f"{i} x {j} = {i * j}")
        print()  # dòng trống giữa các bảng
    
    
    print("=" * 40)
    print("BÀI 7: Kiểm tra số nguyên tố")
    print("=" * 40)
    
    n = 17
    
    la_nguyen_to = True
    
    if n < 2:
        la_nguyen_to = False
    else:
        for i in range(2, n):
            if n % i == 0:
                la_nguyen_to = False
    
    if la_nguyen_to:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải số nguyên tố")
    
    
    print("\n" + "=" * 40)
    print("BÀI 8: Đếm số lần xuất hiện")
    print("=" * 40)
    
    orders = ["A", "B", "A", "C", "A"]
    
    dem_a = 0
    for o in orders:
        if o == "A":
            dem_a = dem_a + 1
    
    print(f"A xuất hiện: {dem_a} lần")
    
    
    print("\n" + "=" * 40)
    print("BÀI 9: Hàm tính tổng tiền")
    print("=" * 40)
    
    def calculate_total(price, quantity):
        return price * quantity
    
    ket_qua = calculate_total(50000, 3)
    print(f"Tổng tiền: {ket_qua}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 10: Hàm kiểm tra đăng nhập")
    print("=" * 40)
    
    def check_login(is_logged_in):
        if is_logged_in:
            return "Đã đăng nhập"
        else:
            return "Chưa đăng nhập"
    
    print(check_login(True))
    print(check_login(False))
    
    
    print("\n" + "=" * 40)
    print("BÀI 11: Hàm giảm giá")
    print("=" * 40)
    
    def apply_discount(price, percent):
        giam = price * percent / 100
        gia_moi = price - giam
        return gia_moi
    
    print(f"Giá sau giảm: {apply_discount(200000, 20)}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 12: Hàm free ship")
    print("=" * 40)
    
    def is_free_shipping(order_value):
        if order_value >= 500000:
            return True
        else:
            return False
    
    ket_qua = is_free_shipping(600000)
    print(f"Free ship: {ket_qua}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 13: Phân loại khách hàng")
    print("=" * 40)
    
    def classify_customer(total_spent):
        if total_spent >= 5000000:
            return "VIP"
        elif total_spent >= 2000000:
            return "Gold"
        else:
            return "Normal"
    
    print(classify_customer(6000000))
    print(classify_customer(3000000))
    print(classify_customer(500000))
    
    
    print("\n" + "=" * 40)
    print("BÀI 14: Validate email")
    print("=" * 40)
    
    def is_valid_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False
    
    email = "test@gmail.com"
    if is_valid_email(email):
        print("Email hợp lệ")
    else:
        print("Email không hợp lệ")
    
    
    print("\n" + "=" * 40)
    print("BÀI 15: Tổng doanh thu")
    print("=" * 40)
    
    orders = [100000, 200000, 300000]
    
    def total_revenue(orders):
        tong = 0
        for o in orders:
            tong = tong + o
        return tong
    
    print(f"Tổng doanh thu: {total_revenue(orders)}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 16: Lọc giá cao")
    print("=" * 40)
    
    prices = [100000, 500000, 700000, 200000]
    
    def filter_prices(prices):
        ket_qua = []
        for p in prices:
            if p > 300000:
                ket_qua.append(p)
        return ket_qua
    
    print(filter_prices(prices))
    
    
    print("\n" + "=" * 40)
    print("BÀI 17: Đếm đơn hợp lệ")
    print("=" * 40)
    
    orders = [100000, 0, 200000, -50000]
    
    def check_orders(orders):
        dem = 0
        for o in orders:
            if o > 0:
                dem = dem + 1
        return dem
    
    print(f"Số đơn hợp lệ: {check_orders(orders)}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 18: Tổng sau giảm giá")
    print("=" * 40)
    
    prices = [100000, 200000, 300000]
    
    def apply_discount(price):
        return price * 0.9  # giảm 10%
    
    tong_sau_giam = 0
    for p in prices:
        tong_sau_giam = tong_sau_giam + apply_discount(p)
    
    print(f"Tổng sau giảm: {tong_sau_giam}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 19: Lọc khách VIP")
    print("=" * 40)
    
    cart = [200000, 1500000, 800000]
    
    def vip_checker(cart):
        tong = 0
        for c in cart:
            tong = tong + c
        if tong >= 3000000:
            return True
        else:
            return False
    
    print(f"Khách VIP: {vip_checker(cart)}")
    
    
    print("\n" + "=" * 40)
    print("BÀI 20: Hệ thống thanh toán (mini backend)")
    print("=" * 40)
    
    cart = [100000, 200000, 150000]
    balance = 500000
    
    def checkout(cart, balance):
        tong = 0
        for item in cart:
            tong = tong + item
    
        if balance >= tong:
            so_du = balance - tong
            return {"status": "Thanh toán thành công", "Số dư còn lại": so_du}
        else:
            so_du = balance - tong
            return {"status": "Không đủ tiền", "Số dư còn lại": so_du}
    
    ket_qua = checkout(cart, balance)
    print(ket_qua)