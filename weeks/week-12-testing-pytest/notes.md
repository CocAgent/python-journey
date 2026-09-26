# Week 12 — pytest foundation

## Discovery và assert

Pytest tìm file `test_*.py` và function `test_*`. Một assertion so sánh
actual behavior với expected behavior.

## Arrange → Act → Assert

```python
def test_wait_action_is_legal():
    # Arrange
    state = {"position": 2}

    # Act
    action = choose_action(state)

    # Assert
    assert action in {"left", "right", "wait"}
```

## Case selection

- normal: input điển hình;
- edge: biên hợp lệ như list rỗng hoặc turn cuối;
- invalid: input ngoài contract và expected exception;
- regression: input nhỏ từng làm code sai.

Fixture nhỏ chỉ dùng khi setup chung thực sự làm test rõ hơn. Tuần này không
cần mock framework, patch-heavy tests hay test architecture.

## Đọc một test failure

Khi test fail, đọc theo thứ tự:

1. tên test để biết behavior đang được kiểm tra;
2. expected và actual trong assertion;
3. traceback tới dòng code của mình;
4. input nhỏ đã tái hiện lỗi.

Không sửa expected value chỉ để test xanh. Trước tiên xác nhận contract đúng,
sau đó sửa implementation hoặc sửa test nếu test mô tả sai contract.

## Test phải độc lập

Mỗi test tự chuẩn bị dữ liệu cần thiết và không phụ thuộc test chạy trước. Dùng
`tmp_path` khi cần file tạm để test không tạo rác trong repository.

```python
def test_save_note(tmp_path):
    destination = tmp_path / "note.txt"
    destination.write_text("pytest", encoding="utf-8")
    assert destination.read_text(encoding="utf-8") == "pytest"
```

## Vòng lặp làm việc

```text
Write/choose a case → Run → Read failure → Fix one cause → Re-run
```

Chạy riêng learner tests:

```bash
pytest weeks/week-12-testing-pytest/tests -q
```
