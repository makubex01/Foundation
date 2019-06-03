def show_keywords(**args):
    for key, value in args.items(): #argsのキーとvalueに代入
        print(key + "=" + str(value)) #1つずつkeyとvalueを出力
    print("---")

show_keywords(a=55,b=87)
show_keywords(c=55,d=87,e=62)