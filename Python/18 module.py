Ticket = int(input("Введите число желаемых билетов?: "))
price = 0

for i in range(Ticket):
    age = int(input("Введите возраст каждого участника по порядку: "))
    if age < 18:
        price = price + 0
    if 18 <= age <= 25:
        price += 990
    if age > 25:
        price += 1390
if Ticket > 3:
    price = price * 0.9
print("к оплате:", round(price), "рублей")
