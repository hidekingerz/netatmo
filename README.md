# netatmo
netatmo weather stationのメインモジュール側の検知温度を取得し、Macのsayコマンドで温度を発話するコード。

## 仕様
- python3.6
  - subprocess
  - requests
  - json

- say

## 利用準備
main.py の中にある下記のパラメータを個人のものに変更してください。

```
## ユーザ認証型のAccessToken取得用データ
payload_credential = {'grant_type': 'password',
           'username': "your username",
           'password': "your password",
           'client_id':"your client id",
           'client_secret': "your client secret",
           'scope': 'read_station'}
```

device_idにはメインモジュールのMacアドレスを記載してください。
```
def get_deviceData(access_token):

    payload_device = {'access_token': access_token,
            'device_id': 'your device_id'}
```

## 使い方

```
$ python3 main.py
```
