from itertools import product
from collections import Counter

SIDES = range(1, 7)


def is_scoring_roll(roll):
    """
    Returns True if the roll scores under standard Farkle rules.
    Works for any number of dice.
    """
    n = len(roll)
    counts = Counter(roll)
    freq = sorted(counts.values(), reverse=True)

    # Straight only applies to exactly 6 dice
    if n == 6 and sorted(roll) == [1, 2, 3, 4, 5, 6]:
        return True

    # Any 3+ of a kind
    if freq[0] >= 3:
        return True

    # Three pairs (only possible with 6 dice)
    if n == 6 and freq == [2, 2, 2]:
        return True

    # Two triplets (only possible with 6 dice)
    if n == 6 and freq == [3, 3]:
        return True

    # Single scoring dice
    if 1 in counts or 5 in counts:
        return True

    return False


def farkle_probability(n_dice):
    """
    Computes number of farkles and probability for n_dice.
    """
    total_rolls = 6 ** n_dice
    farkles = 0

    for roll in product(SIDES, repeat=n_dice):
        if not is_scoring_roll(roll):
            farkles += 1

    return farkles, farkles / total_rolls


if __name__ == "__main__":
    for n in range(1, 7):
        num_farkles, farkle_probs = farkle_probability(n)
        print(f"{n} dice -> Num Farkles: {num_farkles} | Probability: {farkle_probs}")
