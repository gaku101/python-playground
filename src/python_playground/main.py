import datetime
import sys


def hello():
    greet = "Hello from python-playground!"
    print(greet)
    # プラットフォーム標準の文字コードを表示
    print(sys.getfilesystemencoding())


hello()


def export_log():
    file = open("./hoge.log", "a", encoding="UTF-8")
    file.write(f"{datetime.datetime.now()}\n")
    file.close()
    print("現在時刻をファイルに保存しました")


# export_log()


# withを使えば自動でcloseしてくれる
def export_log_using_with():
    with open("./hoge.log", "a", encoding="UTF-8") as file:
        file.write(f"{datetime.datetime.now()}\n")


def read_log():
    with open("./hoge.log", "r", encoding="UTF-8") as file:
        data = file.read()
    print(data)

read_log()
