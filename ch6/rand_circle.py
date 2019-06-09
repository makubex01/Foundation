from tkinter import *

#ランダムな色を返す関数
def random_color():
    #ランダムに色の配色を決定
    from random import randint #randomモジュールからrandint()関数をimport
    rnd = lambda : randint(0,255) #0～255から乱数を発生させる関数をrndに代入
    
    r = rnd()
    g = rnd()
    b = 255
    #HTMLの色形式に変換
    f = "#{0:02x}{1:02x}{2:02x}" #3つの値を受け取って16新数にするための指定
    color = f.format(r, g, b) #r,g,bの値を、format()により16新数に変換
    return color

#たくさんの円を描画する
def draw_circles():
    #画面を初期化
    cv.delete("all")
    #繰り返し円を描画
    for y in range(20):
        y1 = y * 20 #1回目は「0」、「2」回目は「20」、20回目は「380」
        y2 = y1 + 20 #1回目は「20」、　2回目は「40」、20回目は「400」
        for x in range(30): #y1,y2を固定したまま30回繰り返す
            x1 = x * 20 #1回目は「0」、2回目は「20」、20回目は「580」
            x2 = x1 + 20 #1回目は「20」、2回目は「40」、20回目は「600」
            #円を描画
            color = random_color()
            cv.create_oval(x1, y1, x2, y2, #(x1,y1)から(x2,y2)への円を描画)
                fill=color, width=0)
    #0.1秒後に再描画
    win.after(100, draw_circles)

#ウィンドウとキャンバスを作成
win = Tk()
cv = Canvas(win, width=600, height=400)
cv.pack()
win.after(1,draw_circles) #円を描画
win.mainloop()