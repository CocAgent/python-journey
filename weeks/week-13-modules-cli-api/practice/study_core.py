"""Phần nghiệp vụ được CUNG CẤP để người học luyện import/CLI/HTTP.

Ngưỡng 5/10 chỉ dùng minh họa, KHÔNG phải quy chế điểm của trường.
"""

from __future__ import annotations

import math


def validate_score(score: int | float) -> int | float:
    """Chỉ nhận số 0..10 hữu hạn; không biến bool thành điểm 0/1."""
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError("Điểm phải là một số")
    if not math.isfinite(score) or not 0 <= score <= 10:
        raise ValueError("Điểm phải từ 0 đến 10")
    return score


def status_for_score(score: int | float) -> str:
    """Phân loại có thể kiểm bằng test, không tự print."""
    validate_score(score)
    return "Đạt" if score >= 5 else "Cần luyện tập"
