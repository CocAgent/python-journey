"""Official solution for list operations."""


def add_subject(subjects: list[str], subject: str) -> list[str]:
    updated = subjects.copy()
    updated.append(subject)
    return updated


def remove_subject(subjects: list[str], subject: str) -> list[str]:
    updated = subjects.copy()
    if subject in updated:
        updated.remove(subject)
    return updated
