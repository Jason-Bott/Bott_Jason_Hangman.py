import random

lives = 7

num = random.randint(0,99)

file = open('word_list.txt').readlines()
word = file[num]

length = len(word)-1

word_unguessed = "*"*length
print(word_unguessed)
print("")

guess = ""

while "*" in word_unguessed:
    while len(guess) != 1:
        guess = input("Please enter your next guess: ")
        if len(guess) != 1:
            print("Please enter only one letter at a time")
            print("")
        
    if guess in word:
        print("Yes this letter is in the word")

        while guess in word:
            position = word.find(guess)
    
            unword_list = list(word_unguessed)
            unword_list[position] = guess

            word_list = list(word)
            word_list[position] = " "
            word = "".join(word_list)
    
            word_unguessed = "".join(unword_list)

        print("")
        print(word_unguessed)
        print("")

    else:
        lives -= 1
        print("This letter is not in the word")
        lives = str(lives)
        print("You have " + lives + " lives left")
        lives = int(lives)
        print("")
        
        if lives == 0:
            print("you lose")
            exit()
    
    guess = ""
    
print("congratulations you win")
