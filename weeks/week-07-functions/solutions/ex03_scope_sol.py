"""Official solution for Exercise 03 — local scope."""


def them_ghi_chu(danh_sach: list[str], noi_dung: str) -> bool:
    """Thêm ghi chú hợp lệ và báo thao tác có thành công hay không."""
    ghi_chu = noi_dung.strip()
    if not ghi_chu:
        return False
    danh_sach.append(ghi_chu)
    return True


def tim_ghi_chu(danh_sach: list[str], tu_khoa: str) -> list[str]:
    """Trả về các ghi chú chứa từ khóa, không phân biệt hoa thường."""
    tu_khoa_thuong = tu_khoa.lower()
    ket_qua = []
    for ghi_chu in danh_sach:
        if tu_khoa_thuong in ghi_chu.lower():
            ket_qua.append(ghi_chu)
    return ket_qua


def dem_ghi_chu(danh_sach: list[str]) -> int:
    """Trả về số ghi chú trong list được truyền vào."""
    return len(danh_sach)


def main() -> None:
    """Chạy ví dụ với state local."""
    ghi_chu_cua_toi: list[str] = []
    them_ghi_chu(ghi_chu_cua_toi, "Học return")
    them_ghi_chu(ghi_chu_cua_toi, "Luyện scope")
    print(tim_ghi_chu(ghi_chu_cua_toi, "scope"))
    print(f"Số ghi chú: {dem_ghi_chu(ghi_chu_cua_toi)}")


if __name__ == "__main__":
    main()
