"""Lab 04: except vs else vs finally; log every attempt.

valid_score(raw, audit) returns int 0..10 or None. For invalid
text append "invalid", for successful conversion append "converted".
Always append "attempt:<raw>" in finally, even if TypeError propagates.
"""


def valid_score(raw: str, audit: list[str]) -> int | None:
    """Parse score and record events in a caller-owned list."""
    # TODO: try score = int(raw)
    # TODO: except ValueError: audit.append("invalid"); return None
    # TODO: else: audit.append("converted"); check 0..10, return int/None
    # TODO: finally: audit.append(f"attempt:{raw!r}")
    # Do NOT catch TypeError, and do NOT return from finally.
    raise NotImplementedError("Hoàn thiện valid_score")


if __name__ == "__main__":
    print("Hoàn thiện TODO; dùng self-check để xác nhận event order.")
