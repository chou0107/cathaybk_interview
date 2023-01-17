def calculate(name,score):
  NewScore = (score//5 +1)*5
  #如果原分數的下一個最接近的5的倍數跟原分數的差在3以下，新分數則為下一個最接近的5的倍數
  if NewScore-score<=3 and NewScore>=40:
    print("%s %d" % (name,NewScore))
  #如果新分數小於40分，不予加分(保持原分數)
  else:
    print("%s %d" % (name,score))

#將值帶入函數進行運算並列印結果
calculate("德瑞克",33)
calculate("尚恩",73)
calculate("傑夫",63)
calculate("馬基",39)