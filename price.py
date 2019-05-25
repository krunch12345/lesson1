def format_price(price):
    price = 'Цена: ' + str(int(price)) + ' руб.' 
    return price

print(format_price(56.24))