#今回集計するデータ
s = """
サンマ,カツオ,サンマ,サンマ,マグロ,フグ,マグロ,マグロ,マグロ,サンマ,ニシン,イワシ,
サンマ,サンマ,カツオ,サンマ,カツオ,サンマ,カツオ,サンマ,マグロ,マグロ,マグロ,ニシン
"""

#データの前後にある空白を除去
s = s.strip()
#カンマでデータを区切る
s_list = s.split(",")

#集計用の辞書型を生成
result = {} #空の辞書型の変数を作成
for name in s_list: #繰り返すたびにS_listの要素をnameに代入
    name = name.strip() #空白を除去
    #キー(nameの値)がresultに存在するか確認
    if not name in result: #「key in DICT」と「not」で調べる
        result[name] = 0 #nameをキーとして追加し、値を「0」とする
    #辞書型のnameのキーの値を1加算
    result[name] = result[name] + 1 #nameがあれば、値を1つ加算

#結果を表示
for name, v in result.items(): #resultのkeyと価を1つずつ代入
    print(name + "=" + str(v))