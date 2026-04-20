if __name__ == "__main__":
    # Bài 1
    print("Bài 1: ")
    products = ["Áo", "Quần", "Giày", "Mũ"]
    index = 1
    for product in products:
        print(f"{index}. {product}")
        index  = index + 1
        
    # Bài 2
    print("")
    print("Bài 2: ")
    prices = [100000, 200000, 150000]
    tong_tien = 0
    for price in prices:
        tong_tien += price
        
    print(f"Tong tien: {tong_tien} VND")
    
    # Bài 3
    print("")
    print("Bài 3: ")
    prices = [100000, 500000, 700000, 200000]
    count = 0
    for price in prices:
        if price > 300000:
            count += 1
            
    print(f"San pham gia cao: {count}")
    
    # Bài 4
    print("")
    print("Bài 4: ")
    prices = [100000, 500000, 700000, 200000]
    max_price = prices[0]  # lấy giá đầu tiên làm mốc ban đầu
    for price in prices:   # duyệt từng giá
        if price > max_price:  # nếu giá hiện tại lớn hơn giá lớn nhất đang có
            max_price = price  # cập nhật lại giá lớn nhất

    print(f"Giá cao nhất: {max_price}")