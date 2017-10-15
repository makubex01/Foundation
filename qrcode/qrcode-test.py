#パッケージをインポート
import qrcode
#QRコードを生成
img = qrcode.make("https://www.fudemame.co.jp/")
#ファイルに保存
img.save("qrcode-test.png")