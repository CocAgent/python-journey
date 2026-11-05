"""Official solutions for string methods."""


def normalize_email(email: str) -> str:
    return email.strip().lower()


def name_parts(full_name: str) -> tuple[str, str]:
    parts = full_name.split()
    return parts[0], parts[-1]


def supported_filename(filename: str) -> bool:
    return filename.endswith((".py", ".txt", ".csv"))
