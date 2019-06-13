from drivegame_info import ginfo
from drivegame_map import create_map_line
from drivegame_draw import *
import tkinter.messagebox as msgbox

#ゲームの初期化処理 ---(*1)
def init_game():
    global win
    #ウィンドウやキャンバスの生成と、走行コースも生成
    win = create_window(ginfo)
    #キーボードイベントを設定 --- (*2)
    win.bind("<Left>",key_event_left) #「←」キーが押されたらkey_event_left()を実行

    win.bind("<Right>",key_event_right) #「→」キーが押されたら、key_event_right()を実行
    
    #ゲームを開始する ---(*3)
    game_loop()
    win.mainloop()

#カーソルキーを押したときの処理 ---(*4)
def key_event_left(e):
    if ginfo["car"] > 0: #車が画面左端より右にいれば
        ginfo["car"] -= 1 #車を1つ左に移動
def key_event_right(e):
    if ginfo["car"] <= ginfo["cols"] -1: #車が画面右端より左にいれば
        ginfo["car"] += 1 #車を1つ右に移動

#ゲームループ ---(*5)
def game_loop():
    #走行コースと自動車の描画
    draw_map(ginfo) #maze_show.pyのdraw_map()で迷路を描画
    win.title("ドライブゲーム スコア = " + str(ginfo["score"])) #タイトルバーに設定
    #ゲームオーバー判定 ---(*6)
    map_data = ginfo["map_data"]
    v = map_data[ginfo["rows"] - 2][ginfo["car"]] #車が位置のマップデータの値を取得
    if v != 0: #道路ではない
        msgbox.showinfo(
                title="ゲームオーバー",
                message="コースアウトしました\n" +
                        "スコア=" + str(ginfo["score"]))
        quit() #ゲーム終了
    #スコアを加算
    ginfo["score"] += 10
    #過ぎた道路を消して新たに道路を足す
    del(map_data[ginfo["rows"] -1]) #map_dataの一番下の行を削除
    line = create_map_line(ginfo)
    map_data.insert(0,line) #map_dataの一番上の行を追加
    #一定時間後に、再びこの関数を実行
    win.after(100,game_loop)

if __name__ == "__main__": init_game()                             
        