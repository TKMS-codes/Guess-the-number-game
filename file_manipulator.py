import sys

#コマンドライン引数を要素とするリストを取得する
args = sys.argv

#コマンドごとに処理を分岐
#「reverse」コマンドの処理
if args[1] == "reverse":
    if len(args)!=4:
        print("引数の数が不正です。再度プログラムを実行してください。")
        print("Usage: python3 file_manipulator.py reverse [inputPath] [outputPath]")
    else:
        inputPath = args[2]
        outputPath = args[3]
        inputContents = ""
        reverseContents = ""

        with open(inputPath, "r") as f:
            inputContents = f.read()

        #反転させた文字列を作成する処理
        index = len(inputContents)-1
        while(index >= 0):
            reverseContents += inputContents[index]
            index -= 1

        with open(outputPath, "w") as f:
            f.write(reverseContents)

        print("ファイルへの書き込みが完了しました。")
        
elif args[1] == "copy":
    if len(args)!=4:
        print("引数の数が不正です。再度プログラムを実行してください。")
        print("Usage: python3 file_manipulator.py copy [inputPath] [outputPath]")
    else:
        inputPath = args[2]
        outputPath = args[3]
        inputContents = ""

        with open(inputPath, "r") as f:
            inputContents = f.read()

        with open(outputPath, "w") as f:
            f.write(inputContents)

        print("ファイルへの書き込みが完了しました。")

elif args[1] == "duplicate-contents":
    if len(args)!=4:
        print("引数の数が不正です。再度プログラムを実行してください。")
        print("Usage: python3 file_manipulator.py duplicate-contents [inputpath] [n]")
    else:
        inputPath = args[2]
        inputContents = ""
        addContents = ""

        with open(inputPath, "r") as f:
            inputContents = f.read()

        #文字列を指定の個数追加する処理
        for n in range(int(args[3])):
            addContents += inputContents

        with open(inputPath, "a") as f:
            f.write(addContents)

        print("ファイルへの書き込みが完了しました。")

elif args[1] == "replace-string":
    if len(args)!=5:
        print("引数の数が不正です。再度プログラムを実行してください。")
        print("Usage: python3 file_manipulator.py replace-string [inputpath] [needle] [newstring]")
    else:
        inputPath = args[2]
        inputContents = ""
        needle = args[3]
        newString = args[4]
        outputContents = ""

        with open(inputPath, "r") as f:
            inputContents = f.read()

        #文字列の置き換え処理
        outputContents = inputContents.replace(needle, newString)

        with open(inputPath, "a") as f:
            f.write(outputContents)
        print("ファイルへの書き込みが完了しました。")

else:
    print("不正なコマンドです。再度プログラムを実行してください。")