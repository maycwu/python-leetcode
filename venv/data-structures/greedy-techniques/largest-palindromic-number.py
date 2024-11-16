# Statement
# You are given a string num consisting of digits from 0 tom 9. Your task is to return the largest possible palindromic number as a string by using some or all of the digits in num. The resulting palindromic number must not have leading zeros.
#
# Note: You may reorder the digits freely, and you must use at least one digit from the num string.
#
# What is the output for the given input?
#
# nums = “123321”
# Output: "321123" (The largest palindromic number that can be formed using “123321”)
#
#
# What is the output for the given input?
# nums = “50000”
# Output: "5" (The largest palindromic number that can be formed using “50000”)
#
#
# What is the output for the given input?
#
# nums = “77777777777”
# Output: “77777777777” (The largest palindromic number that can be formed using “77777777777”)

from collections import Counter

def largest_palindrome(num):
    # Count the frequency of each digit in the input string
    occureneces = Counter(num)

    # first half and the middle of the palindrome
    first_half = []
    middle = ""

    for digit in range(9, -1, -1):
        digit_char = str(digit)

        if digit_char in occureneces:
            digit_count = occureneces[digit_char]

            # num of pairs of this digit that can be used
            num_pairs = digit_count // 2

            # If pairs available, add them to the first half
            if num_pairs:
                # Avoiding leading zeros
                if not first_half and not digit:
                    occureneces["0"] = 1
                else:
                    first_half.append(digit_char * num_pairs)

            # Checking for a middle element
            if digit_count % 2 and not middle:
                middle = digit_char

    # If all elements are '0'
    if not middle and not first_half:
        return "0"

    # Returning the full palindrome
    return "".join(first_half + [middle] + first_half[::-1])

# Driver code
def main():
    numbers = ["00001", "1234287", "9876545367282", "000000", "146"]

    for i in range(len(numbers)):
        print(i+1, '.', '\tGiven number: "', numbers[i],'"', sep='')
        result = largest_palindrome(numbers[i])
        print('\n\tThe largest palindromic number: "', result,'"', sep='')
        print('-' * 100)

if __name__ == '__main__':
    main()
