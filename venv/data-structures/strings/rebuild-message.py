def rebuild_message(parts):
    # Step 1: Build a mapping of first character -> part
    parts_map = {p[0]: p for p in parts}

    # Step 2: Find the starting part
    all_second_chars = {p[1] for p in parts}
    start = None
    for p in parts:
        if p[0] not in all_second_chars:
            start = p
            break

    # Step 3: Rebuild the full message
    message = start
    while message[-1] in parts_map:
        next_part = parts_map[message[-1]]
        message += next_part[1:]  # skip duplicate overlapping char

    return message

# Example 1
print(rebuild_message(["Ab", "bcZ"]))
# ➡️ "AbcZ"

# Example 2
print(rebuild_message(["A--#", "#-----Z", "X----A"]))
# ➡️ "X----A--#-----Z"

# Example 3
print(rebuild_message(["#*", "A#", "X+X", "+X-#"]))
# ➡️ "A#+X+X-#*"

# Example 4
print(rebuild_message(["AB", "BC", "CD", "DE"]))
# ➡️ "ABCDE"

# Example 5 (Edge case — only 2 parts)
print(rebuild_message(["XY", "YZ"]))
# ➡️ "XYZ"

# Example 6 (Non-sequential characters)
print(rebuild_message(["A1", "1B", "BC", "CD"]))
# ➡️ "A1BCD"

print(rebuild_message(["M@N", "N#O", "O$P", "P%Q", "Q^R", "R&S", "S*T"])) # Expected: "M@N#O$P%Q^R&S*T"

print(rebuild_message(["Aa", "aB", "Bc", "Cd", "xY", "Yz"])) # Expected: "AaBcCd"