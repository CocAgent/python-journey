"""Combine comparison results with boolean operators."""

age = 20
has_ticket = True
is_closed = False

can_enter = age >= 18 and has_ticket and not is_closed
needs_help = age < 18 or not has_ticket

print(f"can_enter={can_enter}")
print(f"needs_help={needs_help}")
