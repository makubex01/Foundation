#coding:utf-8
import random

isok = False #isokは全体がOKかどうかを調べるのに使う。最初はFalse設定して、NGであることを示しておく
while isok == False:
    b = input("数を入れてね>")
    if len(b) != 4:
        print("4桁の数字を入力してください")
    else:
        kazuok = True #kazuokは4桁が全部数字かどうかを調べるのに使う。最初はTrueに設定して「たぶんOKだろう」ということを示しておく
        for i in range(4):
            if (b[i] < "0") or (b[i] > "9"):
                print("数字ではありません")
                kazuok = False #数字ではないときはkazuokにFalseを設定する。「最初は数字だと思っていたけど、実際調べたらダメだった。」ということを示す
            if kazuok:
                if kazuok:
                    isok = True #全部が数字だったら全体としてOKであることを示す

print(b[0])
print(b[1])
print(b[2])
print(b[3])