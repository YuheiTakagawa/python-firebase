# python-firestore

Pythonを使ってfirestoreにデータを格納するプログラム
主にRapsberry Piで取得したセンサ値を入れる

## 認証

firebaseへのアクセスには認証が必要
認証のための鍵の作成は以下を参考に
[参考](http://i-yusuke.com/entry/python-firestore/)

このプログラムでは鍵(json)へのパスを環境変数で渡します

```shell
FIREBASE_AUTH_KEY=<path to your key>
```

## install

```shell
pip install firebase-admin
pip install google-cloud-firestore
```
