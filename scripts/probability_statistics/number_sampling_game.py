
import numpy as np

def run_game():
    s = 0
    while s < 100:
        x = np.random.rand() * 100
        s += x
    while s < 200:
        y = np.random.rand() * 100
        s += y 

    return 1 if y > x else 0

def compute_probability(n=100000):
    y_wins = 0
    for _ in range(n):
        y_wins += run_game()
    return y_wins / n


if __name__ == '__main__':
    print(compute_probability())
