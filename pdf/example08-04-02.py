#クラスのインポート
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

#フォントの登録
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

#PDFを作る
