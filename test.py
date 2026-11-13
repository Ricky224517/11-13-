price = {'珍奶':60,'紅茶':30,'冬瓜茶':25}
stock = {'珍奶':5,'紅茶':3,'冬瓜茶':6}
rejected = []
revenue = 0
spent = {}

total = [(1,"小美","珍奶",2),
    (2,"阿明","紅茶",2),
    (3,"小華","珍奶",3),
    (4,"小美","紅茶",2),
    (5,"阿明","冬瓜茶",4),
    (6,"小華","紅茶",1),
    (7,"小美","珍奶",1),]

for number,name,drink,quantity in total:
  if stock[drink] >= quantity:
    stock[drink] -= quantity
    money = price[drink] * quantity
    revenue += money
    if name in spent:
        spent[name] += money
    else:
        spent[name] = money
  else:
    rejected.append(f"{name}-{drink}")
top = None
most = 0

for name in spent:
  if spent[name] > most:
    most = spent[name]
    top = name 

print("剩餘庫存:", stock)
print("總營收:", revenue)
print("每位常客花費:", spent)
print("被拒絕訂單:", rejected)
print("消費王:", top, most, "元")