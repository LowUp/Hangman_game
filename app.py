from itertools import repeat
import random

word_bank = open("Words.txt", "r")
word_list = word_bank.readlines()

random_word = random.randint(0, len(word_list))


def play():
    hidden_word = []

    hidden_word += list(repeat("_", len(word_list[random_word]) - 1))

    wrong_counter = 0
    right_counter = 0
    max_tries = 8

    #print(word_list[random_word])
    print(hidden_word)

    while True:

        user_input = input("Enter a letter: ").lower()

        if word_list[random_word].lower().__contains__(user_input):
            index = word_list[random_word].index(user_input)
            hidden_word[index] = user_input
            right_counter += 1
            print(hidden_word)

            if right_counter >= len(word_list[random_word]) - 1:
                print(f"You win !\nThe word was: {word_list[random_word]}")
                break
        else:
            wrong_counter += 1
            print(f"\nWrong guess !\nRemaining tries: {max_tries - wrong_counter}\n")
            print(hidden_word)
            if wrong_counter >= max_tries:
                print(f"\nYou lost !\nThe hidden word was: {word_list[random_word]}")
                break


play()

word_bank.close()