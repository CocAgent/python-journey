"""Ví dụ Week 13: gọi API dự báo thời tiết Open-Meteo."""

import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def lay_json(url, tham_so):
    """Gửi GET với timeout và đọc JSON trả về."""
    duong_dan = url + "?" + urlencode(tham_so)
    with urlopen(duong_dan, timeout=10) as phan_hoi:
        return json.load(phan_hoi)


def tim_thanh_pho(ten):
    du_lieu = lay_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        {"name": ten, "count": 5, "language": "vi", "format": "json"},
    )
    ket_qua = du_lieu.get("results", [])
    if not ket_qua:
        raise ValueError("Không tìm thấy thành phố. Thử nhập tên khác.")
    return next((x for x in ket_qua if x.get("country_code") == "VN"), ket_qua[0])


def du_bao_thoi_tiet(thanh_pho):
    return lay_json(
        "https://api.open-meteo.com/v1/forecast",
        {
            "latitude": thanh_pho["latitude"],
            "longitude": thanh_pho["longitude"],
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "forecast_days": 3,
            "timezone": "auto",
        },
    )


def main():
    ten = input("Nhập tên thành phố (Enter = Ho Chi Minh City): ").strip() or "Ho Chi Minh City"
    try:
        thanh_pho = tim_thanh_pho(ten)
        thoi_tiet = du_bao_thoi_tiet(thanh_pho)
        hien_tai = thoi_tiet["current"]
        hang_ngay = thoi_tiet["daily"]
        print(f"\n🌤 Thời tiết: {thanh_pho['name']} ({thanh_pho.get('country', '')})")
        print(f"Nhiệt độ: {hien_tai['temperature_2m']}°C")
        print(f"Độ ẩm: {hien_tai['relative_humidity_2m']}%")
        print(f"Gió: {hien_tai['wind_speed_10m']} km/h")
        print("\nDỰ BÁO 3 NGÀY:")
        for ngay, cao, thap, mua in zip(
            hang_ngay["time"],
            hang_ngay["temperature_2m_max"],
            hang_ngay["temperature_2m_min"],
            hang_ngay["precipitation_probability_max"],
        ):
            print(f"{ngay}: {thap}–{cao}°C | Khả năng mưa cao nhất: {mua}%")
        print("Nguồn: Open-Meteo.com (CC BY 4.0)")
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as loi:
        print(f"Lỗi khi lấy dự báo: {loi}")


if __name__ == "__main__":
    main()
