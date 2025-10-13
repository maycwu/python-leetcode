from collections import defaultdict


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    # Create character count for s1
    s1_count = defaultdict(int)

    for char in s1:
        s1_count[char] += 1

    # Initialize window
    window_count = defaultdict(int)
    window_size = len(s1)

    # Initialize first window
    for i in range(window_size):
        char = s2[i]
        window_count[char] += 1

    # Check first window
    if window_count == s1_count:
        return True

    # Slide window through s2, the window is the size of s1
    for i in range(window_size, len(s2)):
        # Remove leftmost character of previous window
        left_char = s2[i - window_size]

        current_window = s2[i - window_size:i]
        print("Printing current window: ", current_window)

        if window_count[left_char] == 1:
            del window_count[left_char]
        else:
            window_count[left_char] -= 1

        # Add new character to window
        right_char = s2[i]
        window_count[right_char] += 1

        # Check if current window matches s1's character count
        if window_count == s1_count:
            return True
    return False


# Indices: 0 1 2 3 4 5 6
# s2:      l e c a b e e
#          |---|          # Initial window (indices 0-2), processed before loop
#            |---|        # i=3: window is indices 1-3 ("eca")
#              |---|      # i=4: window is indices 2-4 ("cab") ← match found here!
#                |---|    # i=5: window is indices 3-5 ("abe")
#                   |---|  # i=6: window is indices 4-6 ("bee")
print(checkInclusion("abc", "lecabee"))  # Output: true

print(checkInclusion("abc", "lecaabee"))  # Output: false
print(checkInclusion("ab", "ab"))  # Output: true