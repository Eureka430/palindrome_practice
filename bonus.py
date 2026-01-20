"""
409. Longest Palindrome

Given a string text which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

For this question, letters are case-sensitive, for example, "Aa" is not considered a palindrome.
"""
def longest_palindrome_length(text):
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter]= counts[letter] + 1
        elif letter not in counts:
            counts[letter] = 1
    length = 0
    value_odd = False

    for letter in counts:
        if counts[letter] % 2 == 0:
            length = length + counts[letter]
        else:
            length = length + counts[letter] -1
            value_odd = True
    if value_odd:
        length = length + 1
    return length


if __name__ == '__main__':
    test_cases = [('abccccdd', 7),      # dccaccd / dccbccd
                  ('a', 1),             # a
                  ('school', 3)]        # oso / oco / oho / olo

    for test_text, expected in test_cases:
        result = longest_palindrome_length(test_text)
        msg = 'Correct' if expected == result else 'Wrong'
        print(f'[{msg:7s}] longest_palindrome_length("{test_text}") should be {expected}')
