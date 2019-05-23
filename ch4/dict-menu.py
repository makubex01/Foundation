#レストランのメニュー
menu_dict = {
    "洋風カレー": 900,
    "オムライス": 870,
    "ラザニア": 790,
    "ハンバーグ":920,
    "トマトパスタ":720
}

#すべての料理の値段を1.3倍する
import math
for key in menu_dict: #繰り返すたびにkeyにキーを代入
    v1 = menu_dict[key] #keyに対応する値(単価)を代入
    v2 = math.ceil(v1 * 1.3) #v1に1.3を掛けてv2に代入
    print(key + ": " + str(v1) + "→" + str(v2) + "円")