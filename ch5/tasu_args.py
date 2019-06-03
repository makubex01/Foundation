#引数すべてを足し合わせる関数を定義
def tasu(*args):
    r = 0
    for v in args: #argsから1つずつ要素を取り出してvに代入
        r += v
    return r
#関数を利用
print(tasu(1,2))
print(tasu(1,2,3))
print(tasu(1,2,3,4,5))