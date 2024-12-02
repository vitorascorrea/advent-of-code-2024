def parse_input():
  f = open("day_02/input.txt", "r")
  lines = f.readlines()

  report = []

  for line in lines:
    split_line = line.split(" ")
    report.append(list(map(lambda x: int(x), split_line)))

  return report


def part_one(report):
  total = 0

  for line in report:
    if line_is_safe(line):
      total += 1

  return total


def part_two(report):
  total = 0

  for line in report:
    if line_is_safe(line):
      total += 1
    else:
      for i in range(len(line)):
        sliced_line = line[:i] + line[i+1:]
        if line_is_safe(sliced_line):
          total += 1
          break

  return total


def line_is_safe(line):
  safe = True
  sorted_line = sorted(line)

  if line != sorted_line:
    reversed_sorted_list = sorted_line[::-1]
    if line != reversed_sorted_list:
      safe = False

  if safe:
    for i in range(len(line) - 1):
      diff = abs(line[i] - line[i + 1])
      if diff < 1 or diff > 3:
        safe = False
        break

  return safe


if __name__ == "__main__":
  report = parse_input()
  part_one_total = part_one(report)
  print(part_one_total)

  part_two_total = part_two(report)
  print(part_two_total)