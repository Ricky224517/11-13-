v = {}

while True:
    x = input()
    if x == "-999":
        break
    else:
        if x in v:
            print(v[x])
        else:
            b = input("請輸入存在的英文單字:") 
            v[x] = b