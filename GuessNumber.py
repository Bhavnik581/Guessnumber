import random 

n = random.randrange(1,100)
guess = int(input("Guess the number: "))
while n != guess:
    if guess < n:
        print(" Too Low ")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print(' To high ')
        guess = int(input('Enter number again: '))
    else:
        break
print('you guessed in Right!!')
