import string
import random
from imdb import Cinemagoer


def pick_movie():
    ia = Cinemagoer()
    movies = ia.get_top250_movies()
    movie = random.choice(movies)
    return movie.data["title"]


class Hangman:
    def __init__(self, movie_title):
        self.movie_title = movie_title.upper()
        self.wrong_guesses = 6
        self.right_guesses = len(movie_title)
        self.correct_letters = []
        self.incorrect_letters = []

    def print_score(self):
        if self.wrong_guesses == 6:
            print("________\n       |\n")                                             # 6 guesses remaining
        elif self.wrong_guesses == 5:
            print("________\n       |\n       O\n")                                   # 5 guesses remaining
        elif self.wrong_guesses == 4:
            print("________\n       |\n       O\n      \|\n")                         # 4 guesses remaining
        elif self.wrong_guesses == 3:
            print("________\n       |\n       O\n      \|/\n")                        # 3 guesses remainin
        elif self.wrong_guesses == 2:
            print("________\n       |\n       O\n      \|/\n       |\n      /\n")     # 2 guesses remaining
        elif self.wrong_guesses == 1:
            print("________\n       |\n       O\n      \|/\n       |\n      / \ \n")  # 1 guess remaining
        else:
            print("________\n       |\n       X\n      \|/\n       |\n      / \ \n")  # 0 guesses remaining

    def print_guesses(self):
        print(*self.title_display, sep="")               # print correct guesses
        print("Correct Guesses:", self.correct_letters)  # print which letters are correct guesses
        print("Incorrect Guesses:", self.incorrect_letters)  # print which letters are wrong guesses

    def initiate_game(self):
        self.title_hidden = [char for char in self.movie_title]  # creates list with each letter of movie title, not to be shown
        self.title_display = []                                  # list with title that will be shown
        for letter in self.movie_title:
            if letter == " ":                                    # if space, leave as space
                self.title_display.append(" ")
                self.right_guesses -= 1
            elif letter.isdigit():                               # if number, replace with "#"
                self.title_display.append("#")
            elif letter in string.punctuation:                   # if punctuation, leave as punctuation
                self.title_display.append(letter)
                self.right_guesses -= 1
            else:                                                # if letter, replace with "_ "
                self.title_display.append("_ ")

    def play_game(self):           
        print("\n" * 50)
        print("\nWelcome to Hangman! \n________\n       |\n\n\nHere is your title: \n")    # welcome text with hanging thingy and title, title is "__"
        print(*self.title_display, sep="")
        while (self.wrong_guesses > 0 and self.right_guesses > 0):                         # while the user has not gone bust or guessed correctly
            choice = input("\nWould you like to guess a letter or the title? L or T: \n")  # asks user if they wanna guess letter or title
            choice = choice.upper()
            if choice == "T":                                              # user chooses to guess title
                title_guess = input("\nPlease guess the movie title: \n")  # user is asked to guess title
                title_guess = title_guess.upper()
                if (title_guess == self.movie_title):                      # correct title guess, game over, user wins
                    break
                elif title_guess in self.incorrect_letters:
                    print("You already guessed that title!")
                else:                                                      # incorrect title guess
                    self.wrong_guesses -= 1                                # wrong guesses -1
                    self.incorrect_letters.append(title_guess)             # wrong title guess is added to list of wrong guesses
                    print("\n" * 50)
                    print("\nSorry, wrong guess.\n")
                    self.print_score()                                 # print current hang man
                    self.print_guesses()                               # print wrong and right guesses
            elif choice == "L":                                        # user chooses to guess letter
                letter_guess = input("\nPlease guess a letter: \n")    # user is asked to guess letter
                letter_guess = letter_guess.upper()                    # letter is upper cased
                if (letter_guess in self.correct_letters):             # check if user guess this letter already
                    print("You already guesed that letter!")
                elif (letter_guess in self.incorrect_letters):         # check if user guess this letter already
                    print("You already guesed that letter!")
                elif letter_guess in self.title_hidden:                # letter is found in title
                    for i, n in enumerate(self.title_hidden):          # finding the correct spot the guessed letter is in and replacing it with guessed letter
                        if n == letter_guess:
                            self.title_display[i] = letter_guess
                            self.right_guesses -= 1                    # right guesses -1
                    print("\n" * 50)
                    print("\nCorrect!\n")
                    self.correct_letters.append(letter_guess)          # correct letter guess is added to list of right guesses
                    self.print_score()                           # print current hang man
                    self.print_guesses()                         # print wrong and right guesses
                else:                                            # letter is not found in title
                    self.wrong_guesses -= 1                      # wrong guesses -1
                    self.incorrect_letters.append(letter_guess)  # incorrect letetr guess is added to list of wrong guesses
                    print("\n" * 50)
                    print("\nSorry, wrong guess.\n")
                    self.print_score()                           # print current hang man
                    self.print_guesses()                         # print wrong and right guesses
            else:                                                # user did not input "L" or "T"
                print("\nPlease choose 'L' or 'T'!")
        
    def declare_winner(self):    
        if self.wrong_guesses == 0:                              # user goes bust, they lose
            print("\n" * 50)
            self.print_score()                                   # print final hang man
            self.print_guesses()                                 # print wrong and right guesses
            print("\nSorry, you lose!\nMovie title was: " + self.movie_title)
        elif self.right_guesses == 0:                            # user guesses all letters correctly, they win
            print("\n" * 50)
            print(*self.title_display, sep="")
            print("\nCongradulations! You won!\n")
        else:                                                    # user gueses the title correctly, they win
            print("\n" * 50)
            print(self.movie_title)
            print("\nCongradulations! You won!\n")


game = Hangman(pick_movie())
game.initiate_game()
game.play_game()
game.declare_winner()
