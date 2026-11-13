lst = []

for i in range(7):
    x,y = input().split()
    lst.append({'x':x,'y':y})
    
for item in lst:
    x,y = item.values()
    print(x,y,sep = "\t") 
    
#星期一	Monday
#星期二	Tuesday
#星期三	Wednesday
#星期四	Thursday
#星期五	Friday
#星期六	Saturday
#星期日	Sunday       
