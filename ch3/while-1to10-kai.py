v = 0 #合計値
i = 0 #繰り返しごとに1を加算する
while i <= 10:
    v += i
    print("i=" + str(i) + ", v=" + str(v))
    i += 1
print("----")
print("合計=" + str(v))