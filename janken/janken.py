#じゃんけんゲーム
import random #randomモジュールの取り込み

#手をリストで表現
hand = ["グー","チョキ","パー","ゲーム終了"]

print("==== じゃんけんをしましょう! ====")
while True:
    #コンピューターの手を決定
    com = random.randint(0,2)
    #ユーザーの手を入力してもらう
    for i,desc in enumerate(hand): #enumerate関数でインデックス番号と手を取得
        print(i, ":" ,desc) #数値とじゃんけんの手の対応を説明
    you = int(input("出す手を数値で入力：　"))
    if you == 3: break
    if you < 0 or you > 2:
        print("0から3の間で入力してね")
        continue
    #手を入力
    print("-----")
    print("自分：", hand[you])
    print("相手：", hand[com])
    input("-----")
    #じゃんけんの勝敗を判定する
    j = (you - com + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("負け")
    else:
        print("勝ち")
    input("-----")