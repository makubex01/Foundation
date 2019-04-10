#coding:utf-8

for a in range(1,51):
    print(a)
    if (a % 12 == 0):
        #12の倍数のとき
        print("〇")
    elif(a % 4 == 0):
        #4の倍数のとき
        print("△")
    elif(a % 2 == 0):
        #2の倍数のとき
        print("×")
    else:
        #どれでもないとき
        print("☆")