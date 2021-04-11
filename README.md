# Google StreetView Downloader

Google StreetView Apiを利用して画像をダウンロードするサンプルです。

## Usage

### 1. 必要ライブラリのインストール

``
pip install -r requirements.txt
``

### 2. コマンド

以下のコマンドを実行することで、`${対象の住所}`のストリートビュー画像をダウンロードし、`downloads/`以下フォルダに保存する。

``
python main.py ${api_key} ${対象の住所}
``

必須の引数

- ${api_key}: [こちら](https://developers.google.com/maps/documentation/streetview/overview)で取得したapi_key
- ${対象の住所}: ダウンロードする対象の住所

オプション  
- pitch: 上下の角度 -90~90 (-90: 真下, 90: 真上)
- heading: 方位 0~360 (0:北, 90:東, 180:南, 270:西)
- fov: ズーム 0~120