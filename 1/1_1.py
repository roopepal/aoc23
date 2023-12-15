with open('input', 'r') as f:
    result = sum(
        [int(''.join((digits[0], digits[-1]))) \
         for digits in \
            ([char for char in line if char.isdigit()] \
             for line in f.readlines())])
    print(result)
