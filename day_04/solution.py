def parse_input():
  f = open("day_04/input.txt", "r")
  lines = f.readlines()

  word_search = []

  for line in lines:
    word_search.append(list(line.replace("\n", "")))

  return word_search


def part_one(word_search):
  total = 0

  for i in range(len(word_search)):
    for j in range(len(word_search[i])):
      if word_search[i][j] == "X":
        total += find_horizontal_and_vertical_xmas(word_search, i, j)
        total += find_diagonal_word(word_search, i, j)

  return total


def part_two(word_search):
  total = 0

  for i in range(len(word_search) - 2):
    for j in range(len(word_search[i]) - 2):
      occurrences = 0
      occurrences += word_search[i][j] == "M" and find_upper_left_to_bottom_right_diagonal(word_search, i, j, "MAS")
      occurrences += word_search[i][j+2] == "M" and find_upper_right_to_bottom_left_diagonal(word_search, i, j+2, "MAS")
      occurrences += word_search[i][j] == "S" and find_upper_left_to_bottom_right_diagonal(word_search, i, j, "SAM")
      occurrences += word_search[i][j+2] == "S" and find_upper_right_to_bottom_left_diagonal(word_search, i, j+2, "SAM")

      if occurrences == 2:
        total += 1

  return total


def find_horizontal_and_vertical_xmas(word_search, i, j):
  total = 0

  # print("Finds for X in position " + str(i) + " " + str(j))

  # left to right
  if j < len(word_search[i]) - 3 and word_search[i][j:j+4] == list("XMAS"):
    # print("found left to right")
    total += 1

  # right to left
  if j >= 3 and word_search[i][j-3:j+1] == list("SAMX"):
    # print("found right to left")
    total += 1

  # top to bottom
  if i < len(word_search) - 3 and [c[j] for c in word_search[i:i+4]] == list("XMAS"):
    # print("found top to bottom")
    total += 1

  # bottom to top
  if i >= 3 and [c[j] for c in word_search[i-3:i+1]] == list("SAMX"):
    # print("found bottom to top")
    total += 1

  return total


def find_diagonal_word(word_search, i, j, word="XMAS"):
  total = 0
  word_len = len(word)

  # upper left to right diagonal
  if find_upper_left_to_bottom_right_diagonal(word_search, i, j, word):
      total += 1

  # upper right to left
  if find_upper_right_to_bottom_left_diagonal(word_search, i, j, word):
      total += 1

  # bottom left to right diagonal
  if j < len(word_search[i]) - (word_len - 1) and i >= (word_len - 1):
    diagonal_word = [word_search[i-x][j+x] for x in range(word_len)]
    if diagonal_word == list(word):
      total += 1

  # bottom right to left diagonal
  if j >= (word_len - 1) and i >= (word_len - 1):
    diagonal_word = [word_search[i-x][j-x] for x in range(word_len)]
    if diagonal_word == list(word):
      total += 1

  return total


def find_upper_left_to_bottom_right_diagonal(word_search, i, j, word="XMAS"):
  word_len = len(word)

  # upper left to right diagonal
  if j < len(word_search[i]) - (word_len - 1) and i < len(word_search) - (word_len - 1):
    diagonal_word = [word_search[i+x][j+x] for x in range(word_len)]

    return diagonal_word == list(word)


def find_upper_right_to_bottom_left_diagonal(word_search, i, j, word="XMAS"):
  word_len = len(word)

  if j >= (word_len - 1) and i < len(word_search) - (word_len - 1):
    diagonal_word = [word_search[i+x][j-x] for x in range(word_len)]

    return diagonal_word == list(word)


if __name__ == "__main__":
  word_search = parse_input()
  # part_one_total = part_one(word_search)
  # print(part_one_total)

  part_two_total = part_two(word_search)
  print(part_two_total)
