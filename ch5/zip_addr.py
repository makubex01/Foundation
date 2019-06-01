#郵便番号APIのURL
yubin_api = "http://api.aoikujira.com/zip/json/"

#URLからJSONデータをダウンロードする関数
def get_json(url):
    import urllib.request as req, json
    res = req.urlopen(url) #データをダウンロード
    json_data = res.read()
    return json.loads(json_data) #JSONデータを変換

#郵便番号を指定して住所を調べる関数
def get_addr(zip_code):
    url = yubin_api + zip_code
    a = get_json(url)
    return a["state"] + a["city"] + a["address"]

#郵便番号を調べて表示
if __name__ == "__main__":
    print(get_addr("110-0006"))