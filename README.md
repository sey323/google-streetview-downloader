# Google StreetView Downloader

Google StreetView Apiを利用して画像をダウンロードするサンプル。本リポジトリは、下記の記事で利用したリポジトリです。

- [PythonでGoogleStreetViewから画像をダウンロードする - Qiita](https://qiita.com/sey323/items/6339767bd289c9be7112)

## Usage

### 1. 必要ライブラリのインストール

```sh:
pip install -r requirements.txt
```

### 2. コマンド

以下のコマンドを実行することで、`${対象の住所}`のストリートビュー画像をダウンロードし、`downloads/`以下フォルダに保存する。

```sh:
python main.py ${api_key} ${対象の住所}
```

必須の引数

- ${api_key}: [こちら](https://developers.google.com/maps/documentation/streetview/overview)で取得したapi_key
- ${対象の住所}: ダウンロードする対象の住所

オプション  
- pitch: 上下の角度 -90~90 (-90: 真下, 90: 真上)
- heading: 方位 0~360 (0:北, 90:東, 180:南, 270:西)
- fov: ズーム 0~120
