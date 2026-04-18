def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Nolga bo'lish xatosi")
        return None

print(div(10, 2))
print(div(10, 0))