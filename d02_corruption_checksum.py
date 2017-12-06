def parse_array(string):
    return [[int(i) for i in row.split('\t')] for row in string.split('\n')]

# Part 1

def get_checksum(array):
    return sum(max(row) - min(row) for row in array)

# Part 2

def get_divisible_checksum(array):
    total = 0
    for row in array:
        row = set(row)
        for first in row:
            for second in row - {first}:
                result = first / second
                if result == round(result):
                    total += int(result)
                    break
            else:
                continue
            break
            
    return total
