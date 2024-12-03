import re

def part_one():
  f = open("day_03/input.txt", "r")
  input = f.read()

  total = 0
  occurrences = re.findall("mul\(\d+,\d+\)", input)

  for occ in occurrences:
    total += parse_mul_string(occ)

  return total


def part_two():
  f = open("day_03/input.txt", "r")
  return calculate_total_from_input(f.read())


def calculate_total_from_input(input):
  total = 0
  enabled = True

  occurrences = re.findall("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", input)

  for occ in occurrences:
    if enabled and occ[0] != "":
      total += parse_mul_string(occ[0])
      continue

    enabled = occ[1] == "do()"

  return total


def parse_mul_string(string):
  split_occ = string.replace("mul(", "").replace(")", "").split(",")
  numbers = list(map(lambda x: int(x), split_occ))

  return numbers[0] * numbers[1]


if __name__ == "__main__":
  part_one_total = part_one()
  print(part_one_total)

  print("Part two test cases (input, expected total)")
  cases = [
    ["mul(1,2)", 2],
    ["mul(1,2)mul(1,2)", 4],
    ["mul(1,2)randomthingsmul(1,2)", 4],
    ["mul[1,2)", 0],
    ["mul(1,2", 0],
    ["nada", 0],
    ["do()", 0],
    ["do()don't()", 0],
    ["mul(1,2)don't()mul(1,3)", 2],
    ["mul(1,2)don't()do()mul(1,3)", 5],
    ["don't()mul(1,2)", 0],
    ["mul(1,2)randomthingsdon't()mul(1,2)", 2],
    ["mul(1,2)do()don't()mul(1,2)", 2],
    ["mul(1,2)do()don't()mul(1,2)mul(1,2)mul(1,2)undo()", 2],
    ["mul(1,2)do()don't()mul(1,2)mul(1,2)mul(1,2)undo()mul(1,2)", 4],
    ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48],
    ["select blabla mul(1,3)~asdijasdi()()()mul(2,2)", 7],
    ["select blabla mul(1,3)~asdijasdi()()()mul(2,2)don't()mul(1,2)", 7],
    ["select()} <*mul(1,2)mul(1,2)mul(1,2)mul(1,2)mul(1,2)mul(1,2)don't()mul(1,2)mul(1,2)do()mul(1,2)", 14],
    ["mul(mul(1,2))", 2],
    ["mul(mul(1,2), 1)", 2],
    ["mul(mul(1,2), mul(don't()mul(1,2))", 2],
    ["select don't(mul(1,1))", 1],
    ["select don't(mul(1,1)do()mul(1,1))", 2],
    ["don't(do(don't(do(mul(1,2)))))", 2],
  ]

  for case in cases:
    print(case)
    print("actual: " + str(calculate_total_from_input(case[0])))
    assert(calculate_total_from_input(case[0]) == case[1])

  part_two_total = part_two()
  print(part_two_total)