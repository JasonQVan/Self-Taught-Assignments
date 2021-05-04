
import random
def hangman(word):
  word = word.upper()
  wrong = 0
  stages = ["",
            "__________               ",
            "|                        ",
            "|            |           ",
            "|            0           ",
            "|           /|\          ",
            "|           / \          ",
            "|                        "
  ]
  remaining_letters = list(word)
  board = ["_"] * len(word)
  win = False
  print("Welcome to Hangman")

  while wrong < len(stages)-1:
    print("\n")
    msg = "Guess a letter \n"
    char = input(msg)
    char = char.upper()
    if char in remaining_letters:
      while char in remaining_letters:
        cind = remaining_letters.index(char)
        board[cind] = char 
        remaining_letters[cind] = '$'
    else:
      wrong += 1
    print(" ".join(board))
    e = wrong + 1
    print("\n".join(stages[0:e]))
    if "_" not in board:
      print("You win!")
      print(" ".join(board))
      win = True
      break
  if not win:
    print("\n".join(stages[0: wrong]))
    print("You lose! It was {}".format(word))

word_list = ["free", "outstanding", "tail", "grotesque", "reject", "malicious", "loose", "rhyme"]
# word_list = input("Enter list of words").split()
chosen_word = random.choice(word_list)
hangman(chosen_word)
