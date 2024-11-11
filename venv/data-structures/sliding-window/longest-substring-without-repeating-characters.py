# Statement
# Given a string, input_str, return the length of the longest substring without repeating characters.


# What should be the output if the following string is given as an input?

# str = “conceptoftheday”
# Output: 8 (The longest substring without any repeating characters is “oftheday”, with a length of 8.)

# str = “bbbbbbbbbbbbbbbb”
# Output: 1 (The longest substring without any repeating characters is the “b”, with a length of 1. Since all the characters in the input string are the same,
# we can’t find a substring with a length greater than 1.)

# str = “racecar”
# Output: 4 (The longest substring without any repeating characters is “ecar” or “race”, with a length of 4.)

# str = “bankrupted”
# Output: 10 (The longest substring without any repeating characters is “bankrupted”, with a length of 10.
# Since all the characters in the input string are unique, the entire input string is the output)

def find_longest_substring(input_str):
    # Check the length of input_str
    if len(input_str) == 0:
        return 0

    window_start, longest, window_length = 0, 0, 0

    last_seen_at = {}

    # Traverse str to find the longest substring
    # without repeating characters.
    for index, val in enumerate(input_str):
        # If the current element is not present in the hash map,
        # then store it in the hash map with the current index as the value.
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            # If the current element is present in the hash map,
            # it means that this element may have appeared before.
            # Check if the current element occurs before or after `window_start`.
            if last_seen_at[val] >= window_start:
                window_length = index - window_start
                if longest < window_length:
                    longest = window_length
                window_start = last_seen_at[val] + 1

            # Update the last occurrence of
            # the element in the hash map
            last_seen_at[val] = index

    index += 1
    # Update the longest substring's
    # length and starting index.
    if longest < index - window_start:
        longest = index - window_start

    return longest


# Driver code
def main():
    string = [
        "abcabcbb",
        "pwwkew",
        "bbbbb",
        "ababababa",
        "",
        "ABCDEFGHI",
        "ABCDEDCBA",
        "AAAABBBBCCCCDDDD",
    ]
    for i in range(len(string)):
        print(i + 1, ". \t Input String: ", string[i], sep="")
        print("\t Length of longest substring: ",
              (find_longest_substring(string[i])))
        print("-" * 100)


if __name__ == "__main__":
    main()