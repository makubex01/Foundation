from tkinter import *

#ウィンドウを作成
win = Tk()

#描画のためキャンパスを作成
cv = Canvas(win, width = 400, height = 300)
cv.pack() #ウィンドウ全体に載せる

#メインループを実行
win.mainloop()