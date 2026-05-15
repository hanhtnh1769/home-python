if __name__ == "__main__":
    print("=" * 40)
    print("BÀI 1:")
    
class BrowserHistory:

    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    # truy cập trang mới
    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url

        # vào trang mới thì xóa forward history
        self.forward_stack = []

    # quay lại
    def back(self, steps):

        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1

        return self.current

    # đi tới
    def forward(self, steps):

        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1

        return self.current


# test
h = BrowserHistory("trang-chu")

h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")

print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))


print("=" * 40)
print("BÀI 2:")
def is_valid_brackets(s):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:

        # gặp ngoặc mở
        if char in "([{":
            stack.append(char)

        # gặp ngoặc đóng
        elif char in ")]}":

            # stack rỗng -> sai
            if not stack:
                return False

            top = stack.pop()

            # không khớp
            if top != pairs[char]:
                return False

    # cuối cùng stack phải rỗng
    return len(stack) == 0


print(is_valid_brackets('{"name": "An", "items": [1, 2]}'))
print(is_valid_brackets('{"data": [{"id": 1}'))
print(is_valid_brackets('()'))
print(is_valid_brackets('{"data": [{"id": 1]]'))


print("=" * 40)
print("BÀI 3:")
def validate_transaction_order(events):

    states = {}
    errors = []
    completed = 0

    for item in events:

        txn_id = item["txn_id"]
        event = item["event"]

        # chưa có transaction
        if txn_id not in states:

            if event != "INIT":
                errors.append(f"{txn_id} thieu buoc INIT")
                continue

            states[txn_id] = ["INIT"]

        else:
            states[txn_id].append(event)

    # kiểm tra flow
    for txn_id, history in states.items():
        if history[0] != "INIT":
            errors.append(f"{txn_id} sai INIT")

        elif len(history) < 2 or history[1] != "PROCESSING":
            errors.append(f"{txn_id} thieu buoc PROCESSING")

        elif history[-1] not in ["COMPLETED", "FAILED"]:
            errors.append(f"{txn_id} chua done")

        elif history[-1] == "COMPLETED" or history[-1] == "FAILED":
            completed += 1

    return {
        "valid": len(errors) == 0,
        "completed": completed,
        "errors": errors
    }


events1 = [
    {"txn_id": "1", "event": "INIT"},
    {"txn_id": "2", "event": "INIT"},
    {"txn_id": "2", "event": "PROCESSING"},
    {"txn_id": "2", "event": "COMPLETED"},
    {"txn_id": "1", "event": "PROCESSING"},
    {"txn_id": "1", "event": "FAILED"},
]

events2 = [
    {"txn_id": "3", "event": "INIT"},
    {"txn_id": "3", "event": "COMPLETED"},
]

print(validate_transaction_order(events1))
print(validate_transaction_order(events2))

print("=" * 40)
print("BÀI 4:")
import heapq

class PriorityShippingQueue:

    def __init__(self):

        self.queue = []
        self.counter = 0

        self.priority_map = {
            "express": 1,
            "vip": 2,
            "normal": 3
        }

    def enqueue(self, order):

        priority = self.priority_map[order["type"]]

        heapq.heappush(
            self.queue,
            (priority, self.counter, order)
        )

        self.counter += 1

    def dequeue(self):

        if not self.queue:
            return None

        return heapq.heappop(self.queue)[2]


psq = PriorityShippingQueue()

psq.enqueue({"id": "S1", "type": "normal", "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip", "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})

print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())


print("=" * 40)
print("BÀI 5:")
from collections import deque


def simulate_checkout(customers, n_counters):

    counters = {}

    # tạo quầy
    for i in range(1, n_counters + 1):

        counters[f"counter_{i}"] = {
            "queue": deque(),
            "total_items": 0
        }

    # chia khách luân phiên
    counter_index = 1

    for customer in customers:

        counter_name = f"counter_{counter_index}"

        counters[counter_name]["queue"].append(customer["id"])

        counters[counter_name]["total_items"] += customer["items"]

        # đổi quầy
        counter_index += 1

        if counter_index > n_counters:
            counter_index = 1

    # format output
    result = {}

    for name, data in counters.items():

        result[name] = {
            "customers": list(data["queue"]),
            "total_items": data["total_items"]
        }

    return result


customers = [
    {"id": "C1", "items": 5},
    {"id": "C2", "items": 12},
    {"id": "C3", "items": 3},
    {"id": "C4", "items": 8},
    {"id": "C5", "items": 1},
]

print(simulate_checkout(customers, 2))