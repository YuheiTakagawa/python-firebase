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

# For GPS
pip install git+https://github.com/bsdz/micropyGPS.git
```

## 対応ずみのセンサ達

各センサごとにクラスとファイルを分けてるよ
- タクトスイッチ
- 単色LED
- [温度・湿度(DHT11)](/dht11.py)
- [感圧(ALPHA-MF02-N-221-A01)](/ad_convert.py)
- [加速度・ジャイロ(MPU-6050)](/mpu-6050.py)
- [GPS(AE-GYSFDMAXB)](/gps.py)
- [衝突検出センサ(赤外線)(ML393 IR)](/irml393.py)
- [サーボモータ(SG90)](/sarvo.py)
- [人感センサ(HC-SR501)](/ch-sr501.py) (検討中)

### 感圧センサに関して
アナログ値・デジタル値のどちらかをとることができるよ  
アナログ値を取得するためには、A/Dコンバータを組み込む必要があるよ  
その際、PythonではSPI（Serial Peripheral Interface)を使ってデータを受け取ります。  
デフォルトでは/dev/配下にデバイスが見えたり見えなかったり＾＾；  
/dev/spi0をこのプログラムでは使っているから有効にする必要あり[Qiita](https://qiita.com/7of9/items/49d7a462732cbd41cb82
)  
```shell
sudo raspi-config
8 Advanced Options
A6 SPI
Would you like the SPI interface to be enabled? にて Yes
The SPI interface is enabled にて Ok
Would you like the SPI kernel module to be loaded by default? にて Yes
SPI kernel module will now be loaded by default にて Ok
Finishを選択
```

### 衝突検出センサ(赤外線)について
ML393 IRというセンサを使います。  
可変抵抗がついていてこれを回すこと(要プラスドライバー)で距離を変更できます。  
今の所、1cm~6cmは確認できてますがそれ以上の抵抗になると常に検出中になってしまう。  
検出した場合、GPIO.LOWになります。5/5時点ではデジタル値のみに対応

### サーボモータについて
SG90は180度の回転しかできません。一周することはできない。
ハードの制御なのでPWM(擬似アナログ出力)を使うようなプログラムです。


### 人感センサについて
HC-SR501は人体赤外線感応モジュールである。  
これは、赤外線の変化を読み取り、変化があった際にGPIO.HIGHを出力する仕組みになっている。  
可変抵抗で遅延時間(前回取得した値を何秒間使い回すか))感度を調整することができる。  
5/6時点では、感度があまりにも不安定なため、あまり使いたくないという感じ。人の動きによる赤外線の変化は読み取ることができず、センサの向きを変えることによってのみ、変化を読み取っているようにしか見えない。要検討
