#設定初始值
high = 100
distance = 0
cnt = 10

#計算過程
for i in range(1,cnt+1) :
  if i == 1:
    #第一次落下經過的距離
    distance += high
    high /= 2
  else:
    #第二次開始，落下經過的距離為high*2(彈到高點&從高點落下)
    distance += high*2
    high /= 2

#列印結果
print("總共%f" % distance)
print("第十次%f" % high)