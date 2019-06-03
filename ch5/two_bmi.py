#BMIを計算する関数を定義(ただし、判定結果付き)
def calc_bmi(weight,height):
    bmi = weight / (height / 100) ** 2
    res = "普通"
    if bmi < 18.5: res = "痩せ型"
    if bmi >= 25: res = "肥満"
    return bmi, res #二つの値を返す　

#関数を呼び出す
bmi,res = calc_bmi(weight = 80, height = 160)
print("BMI=" + str(bmi))
print("判定=" + res)