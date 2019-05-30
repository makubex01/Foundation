import datetime

#特定の日付から東京オリンピックまで調べる関数
def calc_days(y,m,d):
    #タイムスタンプを得る
    olympic = datetime.datetime(2020,7,24).timestamp() #東京オリンピックのタイムスタンプ

    target = datetime.datetime(y,m,d).timestamp() #引数に指定した日のタイムスタンプ

    #何日なのかを調べる
    perday = 24 * 60 * 60 #1日分の秒数を計算する
    days = (olympic - target) // perday #オリンピックまでの秒数を日に換算
    #計算結果を表示
    s = "{0}/{1}/{2}から{3}日後".format(y,m,d,int(days)) #数を埋め込み
    print(s) #結果を出力

#特定の日付から東京オリンピックまで何日?
calc_days(2017,12,1) #日付を指定して関数を呼び出し
calc_days(2018,3,1)

#今日から何日?
t = datetime.date.today() #プログラムを実行した日を取得
calc_days(t.year,t.month,t.day) #取得した日を引数にして関数を呼び出し