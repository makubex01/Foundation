import random

#変数の初期化
win = 0 #勝った回数
draw = 0 #引分の回数

#3回勝負
for i in range(3):
    print("■じゃんけん" + str(i + 1) + "回目")
    print(">0:グー、1:チョキ,2:パー")
    #コンピューターの手を決定
    com = random.randint(0,2)
    #自分の手を入力
    you = int(input("あなたの手は?"))
    #結果を表示
    print("コンピューターの手=" + str(com))
    #じゃけんの結果を判定
    n = (com - you + 3) % 3
    if n == 0:
        print("→あいこ")
        draw  = draw + 1
    elif n == 1:
        print("→勝ち")
        win = win + 1
    else:
        print("→負け")
    print("---")

#最終的な対戦結果を表示
print("結果=3戦" + str(win) + "勝" + str(draw) + "引分け")