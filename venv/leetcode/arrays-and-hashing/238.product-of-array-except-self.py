# answer = [2*3*4, 1*3*4, 1*2*4, 1*2*3]
#        = [24, 12, 8, 6]
#
# Think of each element nums[i] as being in the middle of two groups:
#
# [ left side ] * nums[i]  * [ right side ]
# product_of_left_side * product_of_right_side
#
# Let’s compute the product of numbers before each index.
#
# For nums = [1, 2, 3, 4]:
#
# “Prefix” = Product of all elements to the left
#
# Index	nums[i]	 Product of elements to the left (prefix)
# 0	     1	     1 (nothing on the left)
# 1	     2	     1
# 2	     3	     1×2 = 2
# 3	     4	     1×2×3 = 6
# prefix = [1, 1, 2, 6]
#
# “Postfix” = Product of all elements to the right
#
# Index	nums[i]	 Product of elements to the right (postfix)
# 3	     4	     1 (nothing on the right)
# 2	     3	     4
# 1	     2     	 3×4 = 12
# 0	     1	     2×3×4 = 24
# postfix = [24, 12, 4, 1]
#
# Multiply prefix and postfix for each index:
# answer[i] = prefix[i] * postfix[i]


def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # initialize output array with 1 i.e [1, 1, 1, 1]

    # prefix pass — multiply products from the left
    prefix = 1
    for i in range(n):
        answer[i] = prefix  # store product of all elements before i
        prefix *= nums[i]  # update prefix product

    # postfix pass — multiply products from the right
    postfix = 1
    for i in reversed(range(n)):  # loop from right to left
        answer[i] *= postfix
        postfix *= nums[i]
    return answer


def productExceptSelf_v2(nums):
    n = len(nums)

    left_products = [1] * n
    right_products = [1] * n
    products = [1] * n

    left_running_product = 1
    for i in range(n):
        left_products[i] = left_running_product
        left_running_product *= nums[i]

    right_running_product = 1
    for i in reversed(range(n)):
        right_products[i] = right_running_product
        right_running_product *= nums[i]

    print("left products", left_products)
    print("right products", right_products)

    for i in range(n):
        products[i] = left_products[i] * right_products[i]

    return products


# print(productExceptSelf([1, 2, 3, 4]))  # Output: [24,12,8,6]
# print(productExceptSelf([-1, 0, 1, 2, 3]))  # Output: [0,-6,0,0,0]

print(productExceptSelf_v2([1, 2, 3, 4]))  # Output: [24,12,8,6]
# print(productExceptSelf_v2([-1, 0, 1, 2, 3]))  # Output: [0,-6,0,0,0]
