a_file = open("test.txt",encoding="sjis",mode="w")
try:
    a_file.write("私は失敗したことがない。\n")
    a_file.write("ただ、一万通りの方法を\n見つけただけだ。\n")
finally:
    a_file.close()