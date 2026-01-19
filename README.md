# Farkle Probability by Number of Dice
This project computes the probability of farkling (rolling no scoring dice) in the game Farkle, parameterized by the number of dice rolled. The implementation exhaustively enumerates all possible dice rolls and classifies each roll according to standard Farkle scoring rules.


## What Is a Farkle?
In standard Farkle rules, a roll scores if any of the following conditions are met:

**Single-Die Scoring**
- At least one 1
- At least one 5

**Combination Scoring**
- Three or more of a kind
- Three pairs (six dice only)
- Two triplets (six dice only)
- Straight (1–6, six dice only)

A farkle is a roll that satisfies none of these conditions.


## Methodology
For a given number of dice $n$:
1. All $6^n$ possible rolls are generated.
2. Each roll is evaluated against the scoring rules.
3. Rolls with no scoring patterns are counted as farkles.
4. The farkle probability is computed as: $P(farkle)=\frac{num\_of\_farkles}{6^n}$.

This approach guarantees an exact result for small values of $n$.


## Scope and Limitations
- Designed for 1–6 dice.
- Uses a brute-force enumeration approach.
- Performance scales exponentially with the number of dice.
- Exact results depend on the chosen scoring rules (house rules may vary).

## Usage
Run: ```python count_farkles.py```

## Example Results
```
1 dice -> Farkles:       4 | Probability: 0.666667
2 dice -> Farkles:      16 | Probability: 0.444444
3 dice -> Farkles:      60 | Probability: 0.277778
4 dice -> Farkles:     204 | Probability: 0.157407
5 dice -> Farkles:     600 | Probability: 0.077160
6 dice -> Farkles:    1080 | Probability: 0.023148
```

## Possible Extensions
1. Expected value per roll
2. Optimal reroll strategies
3. Alternative or custom scoring rules
4. Monte Carlo simulation for larger dice counts#