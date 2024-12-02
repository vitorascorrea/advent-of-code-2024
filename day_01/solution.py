def parse_input():
  f = open("day_01/input.txt", "r")
  lines = f.readlines()

  left_numbers = []
  right_numbers = []

  for line in lines:
    split_line = line.split("   ")
    left_numbers.append(int(split_line[0]))
    right_numbers.append(int(split_line[1]))

  return left_numbers, right_numbers


def part_one(left_numbers, right_numbers):
  left_numbers.sort()
  right_numbers.sort()

  total = 0

  for i in range(len(left_numbers)):
    left_number = left_numbers[i]
    right_number = right_numbers[i]

    total += abs(left_number - right_number)

  return total


def part_two(left_numbers, right_numbers):
  right_numbers_frequency = {}

  for number in right_numbers:
    if not number in right_numbers_frequency:
      right_numbers_frequency[number] = 1
    else:
      right_numbers_frequency[number] += 1

  total = 0

  for number in left_numbers:
    if number in right_numbers_frequency:
      total += number * right_numbers_frequency[number]

  return total

if __name__ == "__main__":
  left_numbers, right_numbers = parse_input()
  part_one_total = part_one(left_numbers, right_numbers)
  part_two_total = part_two(left_numbers, right_numbers)

  print(part_one_total)
  print(part_two_total)