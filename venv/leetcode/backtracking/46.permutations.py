def permute(nums):
    # Start with a list containing one empty permutation
    perms = [[]]

    for n in nums:
        new_perms = []
        for existing_perm in perms:
            for i in range(len(existing_perm) + 1):
                # Create a copy to avoid modifying the original
                new_perm = existing_perm.copy()
                new_perm.insert(i, n)
                new_perms.append(new_perm)

        # Update permutations for the next iteration
        perms = new_perms

    return perms


print(permute([1, 2, 3]))

# Time Complexity: O(n! * n)
# n! (n factorial) permutations are generated
# For each permutation, we perform O(n) work (copying and inserting)
# Therefore, total time is O(n! * n)

# Space Complexity: O(n! * n)
# We store all n! permutations
# Each permutation has n elements
# Therefore, total space is O(n! * n)
