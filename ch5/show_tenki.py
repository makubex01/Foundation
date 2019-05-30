#東京の天気をJSONで取得できるURL
url = "http://weather.livedoor.com/forecast/webservice/json/v1"
url += "?city=130010"

#webから天気情報を取得する
import urllib.request as req
res = req.urlopen(url)
json_data = res.read()

#JSONデータをpythonのデータ型(今回は辞書型)に変換
import json
data = json.loads(json_data)

#結果を表示
for row in data["forecasts"]: #dataの「forcast」を1行ずつ読み込む
    label = row["dateLabel"] #読み込んだ行の「datalabel」の値を代入
    telop = row["telop"] #読み込んだ行の「telop」の値を代入
    print(label + " : " + telop)