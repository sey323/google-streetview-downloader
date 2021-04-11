import requests

import google_streetview.api
from bs4 import BeautifulSoup

# デバック用パッケージ
from icecream import ic


class StreetViewRepository:
    def __init__(self, api_key, size=(600, 300)):
        self.api_key = api_key
        self.size = str(size[0]) + "x" + str(size[1])

    def _create_param(
        self, location: str, pitch: int, heading: int, fov: int = 90
    ) -> {}:
        params = [
            {
                "size": self.size,  # max 640x640 pixels
                "location": location,
                "pitch": str(pitch),  # 上下の角度 -90~90 (-90: 真下, 90: 真上)
                "heading": str(heading),  # 方位 0~360 (0:北, 90:東, 180:南, 270:西)
                "fov": str(fov),  # ズーム 0~120
                "key": self.api_key,
            }
        ]
        return params

    def get_pano(self, location: str, pitch: int, heading: int, fov: int = 90):
        """緯度経度からGoogleStreetViewの画像を返すプログラム

        Args:
            location (str): 検索対象の緯度経度
            pitch (int): 上下方向の角度
            heading (int): 水平方向の角度
            fov (int): ズーム
        """
        params = self._create_param(location, pitch, heading)
        ic(params)

        results = google_streetview.api.results(params)
        ic(results.preview())
        results.download_links("downloads")

    def get_pano_for_address(
        self, address: str, pitch: int, heading: int, fov: int = 90
    ):
        """住所からGoogleStreetViewの画像を返すプログラム

        Args:
            address (str): 検索対象の住所
            pitch (int): 上下方向の角度
            heading (int): 水平方向の角度
            fov (int): ズーム
        """
        ic(address)
        target_coodinate = self._coordinate(address)

        location = str(target_coodinate[0]) + "," + str(target_coodinate[1])
        ic(location)
        self.get_pano(location, pitch, heading)

    def _coordinate(self, address) -> []:
        """
        addressに住所を指定すると緯度経度を返す。

        >>> coordinate('東京都文京区本郷7-3-1')
        ['35.712056', '139.762775']
        """
        URL = "http://www.geocoding.jp/api/"  # Geocording Apiを利用する。
        payload = {"q": address}
        html = requests.get(URL, params=payload)
        soup = BeautifulSoup(html.content, "html.parser")
        if soup.find("error"):
            raise ValueError(f"Invalid address submitted. {address}")
        latitude = soup.find("lat").string
        longitude = soup.find("lng").string
        return [latitude, longitude]
