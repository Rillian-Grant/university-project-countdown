import random
import threading
import os

# !!! Should probably be changed into a single function doing operations on two sets of data
def letters_to_chose_from():
    # Define data
    constanants_dist = [2,3,6,2,3,2,1,1,5,4,8,4,1,9,9,9,1,1,1,1,1]
    constanants = "b c d f g h j k l m n p q r s t v w x y z"
    constanants = constanants.split(" ")

    vowels_dist = [15,21,13,13,5]
    vowels = "a e i o u"
    vowels = vowels.split(" ")

    # Create arrays with elements repeated a number of times defined in the dist variable
    constanants_total = []
    for i in range(0, len(constanants)):
        for k in range(0, constanants_dist[i]):
            constanants_total.append(constanants[i])

    vowels_total = []
    for i in range(0, len(vowels)):
        for k in range(0, vowels_dist[i]):
            vowels_total.append(vowels[i])
    return constanants_total, vowels_total

def select_characters():
    # Get choices from the user
    types = []
    for i in range(0,9):
        successful = False
        while not successful:
            choice = input("Letter " + str(i+1) + " Input c for a constanant or v for a vowel: ")
            if choice == "c" or choice == "v":
                successful = True
            else:
                print("you must either enter c or v")
        types.append(choice)

    letters = []
    constanants, vowels = letters_to_chose_from()

    # Pick random letters from the sets defined by the user
    for type in types:
        if type == "c":
            letters.append(random.choice(constanants))
        elif type == "v":
            letters.append(random.choice(vowels))
    return letters

def dictionary_reader():
    words = []
    with open("words.txt", "r") as file:
        for word in file:
            words.append(word.strip())
    return words

# Check if the chosen word is a valid choice. i.e. can be made up of the letters.
def word_lookup(chosen_letters):
    results = []
    all_words = dictionary_reader()
    for word in all_words:
        if set(word).issubset(set(chosen_letters)):
            results.append(word)

    return results

# !!! To be run if the user runs out of time. I should probably exit the thread and then use more conventional exit methods but that would require restructuring.
def times_up():
    print("\nToo late!")
    os._exit(0)

def main():
    # Load data
    words = dictionary_reader()
    ascii_welcome = ''.join([line for line in open("ascii_art/welcome.txt", "r")])

    # Chose the letters
    print(ascii_welcome)
    letters = select_characters()
    print("\n")
    print("Your letters are: "+ "".join(letters))
    print("\n\n")

    # Get the possible solutions
    words = word_lookup(letters)
    words = sorted(words, key=len, reverse=True)

    # Get guesses and check their validity
    timer = threading.Timer(30, times_up)
    timer.start()
    guess = input("Enter your guess: ")
    while guess not in words:
        print("You can't make {} with {}".format(guess, "".join(letters)))
        guess = input("Enter your guess: ")
    timer.cancel()
    
    # Print points and possible better answers
    print("You scored {} points".format(len(guess)))
    print("\n\n")

    print("...but you could have scored:")
    for word in words:
        if len(word) > len(guess):
            print("{} points for {}".format(len(word), word))

    print("\n\nThanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os._exit(0)