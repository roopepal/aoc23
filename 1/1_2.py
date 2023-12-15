def words_with_digits(text):
    result = text
    for (i, word) in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        # e.g. 'one' -> 'on1e'
        word_with_digit = f'{word[:-1]}{str(i+1)}{word[-1:]}'
        result = result.replace(word, word_with_digit)
    return result 

with open('input', 'r') as f:
    lines = list(map(words_with_digits, f.readlines()))
    digits = [[char for char in line if char.isdigit()] for line in lines]
    first_last_joined = [int(''.join((d[0], d[-1]))) for d in digits]
    print(sum(first_last_joined))
