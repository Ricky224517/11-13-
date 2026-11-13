v = {}

while True:
    x = input()
    if x == "-999":
        break
    else:
        if x in v:
            print(v[x])
        else:
            b = input("請輸入英文單字的中文意思:") 
            v[x] = b