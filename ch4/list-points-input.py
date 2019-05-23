#点数を初期化
points = [] #値を何も入れないリストの変数を用意

#繰り返し点数を入力
while True:
    s = input("点数は?")
    if (s == "") or (s == "q"): break
    v = int(s)
    points.append(v) #入力された値をpointsに入れる

#点数を集計する
total = 0
for v in points:
    total = total + v
print("合計=" + str(total))
ave = total / len(points)
print("平均点=" + str(ave))