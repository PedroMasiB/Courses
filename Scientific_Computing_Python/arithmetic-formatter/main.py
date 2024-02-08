from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

values = arithmetic_arranger(problems, True)
combined_lines = [
  "    ".join(lines) for lines in zip(*[value.split('\n') for value in values])
]

for line in combined_lines:
  print(line)
