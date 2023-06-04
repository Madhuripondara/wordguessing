import random
words = ['madhu', 'siri', 'sireesha', 'rohini',
         'sreelalitha', 'vanaja', 'bhavana', 'lalitha',
         'anitha', 'venky', 'poornima', 'vijay']
def fun():
    word = random.choice(words)
    print("Guess the characters")
    guesses = ''
    turns = 5
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("\nYou Win")
            print("The word is: ", word)
            break
        print()
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")
fun()
ask=input("do want to playagain(yes/no):")
while ask=="yes":
    fun()
    ask=input("do want to playagain(yes/no):")
else:
    print("thankyou")

