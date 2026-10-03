"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
# TODO: update the first subject.
# TODO: remove one known subject and pop the last subject.
# TODO: print the first, last and middle slice after each safe operation.

print(subjects)
subjects.append('Ly')
subjects.insert(1, 'Hoa')
print(subjects)
subjects[0] = 'Sinh'
subjects(subjects)
subjects.remove('Van')
print(subjects)
last = subjects.pop()
print(subjects)
print('Mon vua lay ra:', last)
print('fist', subjects[0])
print('last', subjects[-1])
print('middle', subjects[1:2])