from tkinter import *
import tkinter.messagebox as messagebox

def main():
    global cv
    #ウィンドウとキャンバスを作成
    win = Tk()
    cv = Canvas(win,width=400,height=300)
    cv.pack()
    #イベントを設定
    cv.bind("<1>",canvas_click)
    win.mainloop()

#クリックしたときに実行するイベント
def canvas_click(e):
    global cv
    mx = e.x #マウスのx座標
    my = e.y #マウスのy座標
    #円を描画
    cv.create_oval(
        mx - 10, my -10, mx + 10, my + 10,
        fill="red")

main()