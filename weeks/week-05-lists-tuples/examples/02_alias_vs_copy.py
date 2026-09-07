"""Compare a list alias with a shallow copied list."""

original = ["learn", "build"]
alias = original
copied = original.copy()

alias.append("test")

print(f"original={original}")
print(f"alias={alias}")
print(f"copied={copied}")
print(f"alias shares changes: {alias == original}")
