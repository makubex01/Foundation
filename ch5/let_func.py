#関数の定義
def tasu(a,b):
    return a + b

#lambdaで関数の定義
hiku = lambda a,b : a - b

#変数に関数を代入
add = tasu
sub = hiku

#変数に代入した関数を実行
print(add(100,10))
print(sub(50,5))