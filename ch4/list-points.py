#あるクラスの国語の点数
points = [62,58,72,60,47,81,74,65,59,38]

#各点数の合計を求める
total = 0
for pt in points: #繰り返すたびにpointsの要素を1つずつptに代入
    total = total + pt #totalにptの値を足す
print("合計点=" + str(total))

#平均点を求める
ave = total / len(points) #合計を、pointsの要素数(点数の数)で割る
print("平均点=" + str(ave))