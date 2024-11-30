import time
from concurrent.futures import ProcessPoolExecutor

def print_letters(letter):
    print(letter)

letters = ["a", "b", "c", "d"]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = executor.map(print_letters, letters)

