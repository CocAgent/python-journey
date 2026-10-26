"""Exercise 04: separate success handling from guaranteed final work."""

def parse_score(raw: str, audit_log: list[str]) -> int | None:
    score = None
    try:
        score = int(raw)
    except ValueError:
        score = None
    else:
        if not (0 <= score <= 10):
            score = None
    finally:
        audit_log.append(f"parsed={raw!r}")
    return score


if __name__ == "__main__":
    events: list[str] = []
    print(parse_score("8", events))     
    print(parse_score("eight", events))  
    print(parse_score("12", events))    
    print(events)                       

