#coding:utf-8
import random

a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)
    ]

#テストのための答えを表示
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

while True:
    #4桁の数字かどうかを判定する
    isok = False #ユーザの入力が4桁の数字かどうかを判定する変数
    while isok == False:
        b = input("数を入れてね>")
        if len(b) != 4:
            print("4桁の数字を入力してください")
        else:
            kazuok = True
            for i in range(4):
                if (b[i] < "0") or (b[i] > "9"):
                    print("数字ではありません")
                    kazuok = False
                    break
            if kazuok:
                isok = True

    #4桁の数字であったとき
    #ヒットを判定
    hit = 0
    for i in range(4):
        if a[i] == int(b[i]): 
            hit = hit + 1
    
    #ブローを判定
    blow = 0
    for j in range(4):
        for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                blow = blow + 1
                break
    
    #ヒット数とブロー数を表示
    print("ヒット" + str(hit))
    print("ブロー" + str(blow))

    #ヒットが4なら当たりで終了
    if hit == 4:
        print("当たり!")
        break