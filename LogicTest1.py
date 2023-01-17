import math

def calculate(name,score):
  #以另一個變數儲存原始分數
  OriginalScore = score
  #計算出原分數的下一個最接近的5的倍數
  score /= 5
  score = math.floor(score)
  NextScore = (score+1)*5
  #如果原分數的下一個最接近的5的倍數跟原分數的差在3以下，新分數則為下一個最接近的5的倍數
  if NextScore-OriginalScore<3 :
    NewScore = NextScore
  #如果新分數小於40分，不予加分(保持原分數)
  if NewScore<40 :
    NewScore = OriginalScore
  print("%s %d" % (name,NewScore))

#設定原始分數
Derek = 33
Sean = 73
Jeff = 63
Mackey = 39

#將值帶入函數進行運算並列印結果
calculate("德瑞克",Derek)
calculate("尚恩",Sean)
calculate("傑夫",Jeff)
calculate("馬基",Mackey)