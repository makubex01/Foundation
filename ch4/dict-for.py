test_dict = {"田中":48,"佐藤":78,"井上":49}
for key in test_dict: #繰り返すたびにキーをkeyに代入
    value = test_dict[key] #keyに対応する値をvalueに代入
    print(key + "=" + str(value)) #keyとvalueを「=」でつなげて出力