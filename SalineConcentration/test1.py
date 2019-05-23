#coding:utf-8

#食塩水を計算するクラス
class saline:
    def __init__(self,salt,water):
        self.salt = salt
        self.water = water
        self.calcSaline()

    def calcSaline(self):
        ''' 食塩水を計算する '''
        self.saline = self.salt + self.water

    def printCount(self):
        ''' 結果を表示する '''
        print("食塩水の重さ(g)=",self.saline)
    
#1
q1 = saline(salt = 8, water = 100)
q1.printCount()