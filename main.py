# coding: utf-8
import requests
import json
import subprocess


## ユーザ認証型のAccessToken取得用データ
payload_credential = {'grant_type': 'password',
           'username': "your username",
           'password': "your password",
           'client_id':"your client id",
           'client_secret': "your client secret",
           'scope': 'read_station'}

# ユーザ認証型でAccessTokenを取得する
def get_accessToken(payload_credential):
    try:
        response = requests.post("https://api.netatmo.com/oauth2/token", data=payload_credential)
        response.raise_for_status()
        access_token=response.json()["access_token"]
        return access_token

    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

# device_idで指定した機器のデータを取得する
# jsonのところで、devicesの結果がリストで返ってくるため[0]で指定している
def get_deviceData(access_token):

    payload_device = {'access_token': access_token,
            'device_id': 'your device_id'}

    try:
        response = requests.post("https://api.netatmo.com/api/getstationsdata", data=payload_device)
        response.raise_for_status()
        json = response.json()["body"]["devices"][0]["dashboard_data"]["Temperature"]
        return json

    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

# 実行
def execute_say(temp):
    data = "部屋の温度は" + str(temp) + "どです"
    print(data)
    subprocess.run(["say", data])


# メイン
if __name__ == "__main__":
    # execute only if run as a script
    token = get_accessToken(payload_credential)
    data_temperature = get_deviceData(token)
    execute_say(data_temperature)
