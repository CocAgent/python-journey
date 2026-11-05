"""Classify a score with ordered branches."""

score = 7.5

if score < 0 or score > 10:
    result = "invalid"
elif score >= 8:
    result = "good"
elif score >= 5:
    result = "pass"
else:
    result = "practice more"

print(result)
