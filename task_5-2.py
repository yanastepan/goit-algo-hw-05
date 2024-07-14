from typing import Callable, Generator
from decimal import Decimal


# the function must accept the string as an argument and return a generator that iterates over all real numbers in the text.
# real numbers in the text are considered to be written without errors and are clearly separated by spaces on both sides.
def generator_numbers(text: str) -> Generator[Decimal, None, None]:
    words = text.split()            # split the sentence into words
    for word in words:              # look at each word
        try:                        # if the word is a number, save it into the generator
            yield Decimal(word)
        except:                     # if it's not a number, skip it
            continue


# the function must use the generator_numbers generator to calculate the total sum of the numbers in each row
# and take it as an argument when called.
def sum_profit(text: str, func: Callable) -> Decimal:
    total = 0                       # start with a total of 0
    for number in func(text):       # take each value from the generator one by one
        total += number             # adding taken value to the total
    return total                    # return the result

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

