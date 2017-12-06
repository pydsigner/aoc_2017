def get_sum(chars):
    result = 0
    for i, comp in enumerate(chars):
        # For the first char, this will give char -1, which is the last one.
        # We're basically going about this backwards because it gives the 
        # same result.
        n = chars[i - 1]
        if n == comp:
            result += int(n)
    return result


one_line = lambda chars: sum(int(comp) for i, comp in enumerate(chars) if comp == chars[i - 1])
