#cording: utf-8

from flask import Flask, render_template

#appという名前でオブジェクトをインスタンス化
app = Flask(__name__)

# -- View側の設定 --

#ルートディレクトリにアクセスした場合の挙動を定義
@app.route('/')
def index():
    #return 'Hello World!'
    return render_template('index.html')

# エントリーポイントの設計
if __name__ == '__main__':
    app.run()

