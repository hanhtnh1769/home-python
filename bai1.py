a1 = 40

name = "Tran Ngoc Hong Hanh"

print(a1)
print(name)

gio_hang = a1 + 50

if gio_hang > 100:
    khuyen_mai = gio_hang * 0.1
    thanh_tien = gio_hang - khuyen_mai
else:
    thanh_tien = gio_hang


print("Gio hang co gia tri la: ", gio_hang)
print("Ten cua ban la:", name)
print("Tong tien: ", thanh_tien)


da_thit = 100
gia_rau = 50
gia_trąi_cay = 80
gia_xp = 30

gio_hang = ["thit", "rau", "trai cay", "xaphong"]
tong_tien = 0

def tinh_tien(name, gio_hang):
    for item in gio_hang:
        if item == "thit":
            tong_tien = tong_tien + gia_thit*0.5
        elif item == "rau":
            tong_tien = tong_tien + gia_rau*0.6
        elif item == "trai cay":
            tong_tien = tong_tien + gia_trai_cay*0.7