#bmiを計算する関数を定義
def calc_bmi(weight, height):
    return weight / (height / 100) ** 2

#キーワード引数を用いて関数を呼び出す
bmi1 = calc_bmi(weight = 65, height = 150)
print("bmi1=" + str(bmi1))

bmi2 = calc_bmi(weight = 150, height = 65)
print("bmi2=" + str(bmi2))