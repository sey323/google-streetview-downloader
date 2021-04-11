import argparse
from StreetViewRepository import StreetViewRepository


def download_photo(
    api_key: str, address: str, pitch: int = 0, heading: int = 0, fov: int = 90
):
    """住所からGoogleStreetViewの画像を保存する

    Args:
        api_key (str): GoogleStreetViewから取得するAPIキー
        address (str): 検索対象の住所
        pitch (int): 上下方向の角度
        heading (int): 水平方向の角度
        fov (int): ズームの割合
    """
    # 初期化
    sr = StreetViewRepository(api_key=api_key)

    # 画像のダウンロード処理
    sr.get_pano_for_address(
        address=address,
        pitch=pitch,
        heading=heading,
        fov=fov,
    )


if __name__ == "__main__":
    # 引数の設定
    parser = argparse.ArgumentParser()

    parser.add_argument("api_key", help="GoogleStreetViewから取得するAPIキー")
    parser.add_argument("address", help="検索対象の住所")
    parser.add_argument("--pitch", default=0, help="上下方向の角度")
    parser.add_argument("--heading", default=0, help="水平方向の角度")
    parser.add_argument("--fov", default=0, help="ズームの割合")

    args = parser.parse_args()

    download_photo(
        api_key=args.api_key,
        address=args.address,
        pitch=args.pitch,
        heading=args.heading,
        fov=args.fov,
    )
