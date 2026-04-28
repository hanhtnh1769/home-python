if __name__ == "__main__":
    print("=" * 40)
    print("BÀI 1:")
    def filter_available(products):
        available_products = []

        for product in products:
            if product["stock"] > 0 and product["is_active"] == True:
                available_products.append(product)

        return available_products


    products = [
    {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
    {"id": 3, "name": "Giày sneaker", "stock": 5, "is_active": False},
    {"id": 4, "name": "Nón baseball", "stock": 3, "is_active": True}
    ]

    result = filter_available(products)
    print(result)
    
    print("=" * 40)
    print("BÀI 2:")
    def cart_total(cart, discount=10):
        total = 0

        for item in cart:
            total = total + item["price"] * item["quantity"]

        final_total = total * (1 - discount / 100)

        return final_total


    cart = [
    {"name": "Áo thun", "price": 120000, "quantity": 2},
    {"name": "Quần dài", "price": 350000, "quantity": 1},
    {"name": "Tất", "price": 25000, "quantity": 3}
    ]

    result = cart_total(cart, discount=10)
    print(int(result))
    
    print("=" * 40)
    print("BÀI 3:")
    def related_products(product_id, products, limit=3):
        target_category = ""

        for product in products:
            if product["id"] == product_id:
                target_category = product["category"]
                break

        related = []

        for product in products:
            if product["id"] != product_id and product["category"] == target_category:
                related.append(product)

        related.sort(key=lambda x: x["rating"], reverse=True)

        return related[:limit]

    products = [
    {"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
    {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
    {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
    {"id": 4, "name": "Quần jeans", "category": "quan", "rating": 4.7},
    {"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6}
    ]
    result = related_products(product_id=1, products=products, limit=3)
    print(result)
    
    print("=" * 40)
    print("BÀI 4:")
    def detect_anomalies(orders, threshold=2.5):
        total_sum = 0

        for order in orders:
            total_sum = total_sum + order["total"]

        average = total_sum / len(orders)

        anomalies = []

        for order in orders:
            if order["total"] > threshold * average:
                anomalies.append(order)

        return anomalies


    orders = [
    {"id": 101, "total": 250000},
    {"id": 102, "total": 180000},
    {"id": 103, "total": 920000},
    {"id": 104, "total": 210000},
    {"id": 105, "total": 195000}
    ]

    result = detect_anomalies(orders, threshold=2.5)
    print(result)
    
    print("=" * 40)
    print("BÀI 5:")
    def top_selling(order_items, top_n):
        products = {}

        for item in order_items:
            product_id = item["product_id"]
            name = item["name"]
            qty = item["qty"]
            price = item["price"]

            if product_id not in products:
                products[product_id] = {
                    "product_id": product_id,
                    "name": name,
                    "total_qty": 0,
                    "revenue": 0
                }

            products[product_id]["total_qty"] += qty
            products[product_id]["revenue"] += qty * price

        result = list(products.values())

        result.sort(key=lambda x: x["total_qty"], reverse=True)

        return result[:top_n]


    items = [
    {"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
    {"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
    {"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
    {"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
    {"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},
    ]

    print(top_selling(items, top_n=2))
    
    print("=" * 40)
    print("BÀI 6:")
    def build_catalog(products):
        catalog = {}

        for product in products:
            product_id = product["id"]
            catalog[product_id] = product

        return catalog


    products = [
        {"id": "SP001", "name": "Áo thun basic", "price": 120000, "category": "ao"},
        {"id": "SP002", "name": "Quần jogger", "price": 280000, "category": "quan"},
        {"id": "SP003", "name": "Nón bucket", "price": 95000, "category": "phu_kien"},
    ]

    print(build_catalog(products))
    
    print("=" * 40)
    print("BÀI 7:")
    def count_by_status(statuses):
        result = {}

        for status in statuses:
            if status not in result:
                result[status] = 0

            result[status] += 1

        return result

    statuses = [
    "confirmed", "pending", "shipped", "confirmed", "delivered",
    "pending", "cancelled", "confirmed", "shipped", "delivered"
    ]

    print(count_by_status(statuses))
    
    print("=" * 40)
    print("BÀI 8:")
    def apply_coupon(cart_total, code, coupon_db):
        if code not in coupon_db:
            return {
                "valid": False,
                "discount_amount": 0,
                "final_price": cart_total,
                "message": "Mã không tồn tại"
            }

        coupon = coupon_db[code]

        if cart_total < coupon["min_order"]:
            return {
                "valid": False,
                "discount_amount": 0,
                "final_price": cart_total,
                "message": "Đơn hàng chưa đủ điều kiện"
            }

        if coupon["type"] == "percent":
            discount_amount = cart_total * coupon["value"] // 100
            message = f"Áp dụng thành công {code} (-{coupon['value']}%)"
        else:
            discount_amount = coupon["value"]
            message = f"Áp dụng thành công {code} (-{discount_amount})"

        final_price = cart_total - discount_amount

        return {
            "valid": True,
            "discount_amount": discount_amount,
            "final_price": final_price,
            "message": message
        }


    coupon_db = {
        "SALE20": {"type": "percent", "value": 20, "min_order": 200000},
        "SHIP50K": {"type": "fixed", "value": 50000, "min_order": 150000},
        "VIP30": {"type": "percent", "value": 30, "min_order": 500000},
    }

    print(apply_coupon(cart_total=350000, code="SALE20", coupon_db=coupon_db))
    
    print("=" * 40)
    print("BÀI 9:")
    def daily_report(transactions):
        report = {}

        for transaction in transactions:
            date = transaction["date"]
            amount = transaction["amount"]

            if date not in report:
                report[date] = {
                    "total": 0,
                    "count": 0,
                    "avg": 0
                }

            report[date]["total"] += amount
            report[date]["count"] += 1

        for date in report:
            report[date]["avg"] = report[date]["total"] / report[date]["count"]

        return report

    transactions = [
        {"date": "2024-01-15", "amount": 320000},
        {"date": "2024-01-15", "amount": 185000},
        {"date": "2024-01-16", "amount": 450000},
        {"date": "2024-01-15", "amount": 270000},
        {"date": "2024-01-16", "amount": 390000},
    ]

    print(daily_report(transactions))

    
    print("=" * 40)
    print("BÀI 11:")
    def can_access(role, resource, action, rbac):
        if role not in rbac:
            return False

        if resource not in rbac[role]:
            return False

        if action not in rbac[role][resource]:
            return False

        return True

    rbac = {
        "admin": {
        "products": ["read", "create", "update", "delete"],
        "orders": ["read", "update", "delete"]
        },
        "seller": {
        "products": ["read", "create", "update"],
        "orders": ["read"]
        },
        "customer": {
        "orders": ["read", "create"]
        }
    }

    print(can_access("seller", "products", "delete", rbac))
    print(can_access("admin", "orders", "delete", rbac))
    print(can_access("customer", "products", "read", rbac))
    
    print("=" * 40)
    print("BÀI 12:")
    def calc_shipping(city, weight_kg, order_total, zones):
        # nếu city không tồn tại thì fallback sang "other"
        zone = zones.get(city, zones["other"])

        # miễn phí ship nếu đủ điều kiện
        if order_total >= zone["free_threshold"]:
            return {
                "fee": 0,
                "free_shipping": True,
                "message": f"Miễn phí vận chuyển đến {city}"
            }

        # tính phí theo công thức
        fee = zone["zone_rate"] * weight_kg

        # đảm bảo không thấp hơn min_fee
        if fee < zone["min_fee"]:
            fee = zone["min_fee"]

        return {
            "fee": int(fee),
            "free_shipping": False,
            "message": f"Phí ship đến {city}: {int(fee):,}đ"
        }

    shipping_zones = {
        "HN": {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
        "HCM": {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
        "DN": {"zone_rate": 20000, "free_threshold": 350000, "min_fee": 20000},
        "other": {"zone_rate": 30000, "free_threshold": 500000, "min_fee": 30000},
    }

    print(calc_shipping(city="DN", weight_kg=1.5, order_total=200000, zones=shipping_zones))
    
    print("=" * 40)
    print("BÀI 13:")
    def is_wishlisted(product_id, wishlist):
        return product_id in wishlist

    wishlist = {"SP001", "SP005", "SP012", "SP018", "SP024"}

    print(is_wishlisted("SP005", wishlist))  # True
    print(is_wishlisted("SP999", wishlist))  # False
    
    print("=" * 40)
    print("BÀI 14:")
    def get_unviewed(all_products, viewed_products):
        return all_products - viewed_products

    all_products = {"SP001", "SP002", "SP003", "SP004", "SP005", "SP006"}
    viewed_products = {"SP001", "SP003", "SP005"}

    print(get_unviewed(all_products, viewed_products))
    
    print("=" * 40)
    print("BÀI 15:")
    def unique_categories(products):
        categories = set()

        for product in products:
            categories.add(product["category"])

        return categories

    products = [
    {"name": "Áo thun", "category": "ao"},
    {"name": "Quần jean", "category": "quan"},
    {"name": "Áo khoác", "category": "ao"},
    {"name": "Giày", "category": "giay"},
    {"name": "Áo polo", "category": "ao"},
    ]

    print(unique_categories(products))
    
    print("=" * 40)
    print("BÀI 16:")
    def cross_sell(product_id, order_history, current_cart):
        suggestions = set()

        for order in order_history:
            items = set(order["items"])

            if product_id in items:
                suggestions = suggestions | items

        suggestions.discard(product_id)

        suggestions = suggestions - current_cart

        return suggestions


    order_history = [
    {"items": ["SP001", "SP002", "SP005"]},
    {"items": ["SP001", "SP003"]},
    {"items": ["SP001", "SP002", "SP004"]},
    {"items": ["SP006", "SP002"]},
    ]

    current_cart = {"SP001", "SP003"}

    print(cross_sell("SP001", order_history, current_cart))
    
    print("=" * 40)
    print("BÀI 17:")
    def sale_diff(old_sale, new_sale):
        return {
            "removed": old_sale - new_sale,
            "added": new_sale - old_sale,
            "kept": old_sale & new_sale
        }


    old_sale = {"SP001", "SP002", "SP003", "SP004", "SP005"}
    new_sale = {"SP002", "SP004", "SP005", "SP006", "SP007"}

    print(sale_diff(old_sale, new_sale))
    
    print("=" * 40)
    print("BÀI 18:")
    def filter_verified_reviews(reviews, verified_buyers):
        result = []

        for review in reviews:
            if review["user_id"] in verified_buyers:
                result.append(review)

        return result


    verified_buyers = {"U001", "U003", "U005", "U007"}

    reviews = [
    {"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
    {"user_id": "U002", "rating": 1, "comment": "Kém chất lượng"},
    {"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
    {"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
    ]

    print(filter_verified_reviews(reviews, verified_buyers))
    
    print("=" * 40)
    print("BÀI 19:")
    def segment_users(order_counts):
        segments = {
            "one_time": set(),
            "repeat": set(),
            "vip": set()
        }

        for user_id, count in order_counts.items():
            if count == 1:
                segments["one_time"].add(user_id)
            elif 2 <= count <= 4:
                segments["repeat"].add(user_id)
            elif count >= 5:
                segments["vip"].add(user_id)

        return segments


    order_counts = {
        "U001": 1, "U002": 7, "U003": 3, "U004": 1,
        "U005": 5, "U006": 2, "U007": 9, "U008": 4,
    }

    print(segment_users(order_counts))
    
    print("=" * 40)
    print("BÀI 20:")
    active_campaigns = {
    "clearance": {"SP001", "SP005", "SP009"},
    "bundle_deal": {"SP003", "SP007", "SP011"},
    "new_arrival": {"SP013", "SP015"},
    }

    flash_sale_items = {"SP001", "SP003", "SP007", "SP020", "SP025"}
def check_conflicts(flash_sale_items, active_campaigns):
    conflicts = []
    safe_items = []
    has_conflict = False

    for item in flash_sale_items:
        item_conflict = False
        for key, value in active_campaigns.items():
            if item in value:
                conflicts.append(item)
                has_conflict = True
                item_conflict = True
                break
        if item_conflict == False:
            safe_items.append(item)

    # safe_items = flash_sale_items - conflicts

    return {
        "has_conflict": has_conflict,
        "conflicts": conflicts,
        "safe_items": safe_items
    }
print(check_conflicts(flash_sale_items, active_campaigns))