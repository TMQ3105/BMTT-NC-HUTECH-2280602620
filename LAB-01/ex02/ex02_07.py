# Nhập các chữ cái hoặc số vào danh sách
print("Nhập các chữ cái hoặc số (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == "done":
        break
    lines.append(line)

# Chuyển các chữ cái thành chữ hoa và in ra màn hình
print("Các chữ cái đã nhập sau khi chuyển thành chữ hoa:")
for line in lines:
    print(line.upper())