#次の夏季オリンピックの開催年を調べる関数を定義
def show_next_olympic(year):
    i = 4 - year % 4 #対象の年を4で割った余りを4から引いてiに代入
    year2 = year + i #対象の年にiを足す
    #出力メッセージを生成
    s = "{0}年の次のオリンピックは{1}年".format(year,year2)
    print(s)

#いろいろな西暦年を指定して関数を呼び出す
show_next_olympic(2016)
show_next_olympic(2018)
show_next_olympic(2020)