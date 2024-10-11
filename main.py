
import random
def game():
    number_to_guess = random.randint(1, 10)
    guess = None
    tries = 0
    while guess != number_to_guess:
        guess = int(input("Угадай число от 1 до 10"))
        tries +=1
        if guess < number_to_guess:
            print("Мало.")
        elif guess > number_to_guess:
            print("перебрал,меньше число")
            print(f"Ого ты угадал {number_to_guess} за {tries}.")
    if __name__ == "__main__":
        game()

