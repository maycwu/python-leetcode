def reverse_words(str):
    str = str.split(' ')
    updated_str = []

    for i in range(len(str)):
        if str[i] != '':
            updated_str.append(str[i])

    left = 0
    right = len(updated_str) - 1

    while left < right:
        current = updated_str[left]
        end = updated_str[right]
        updated_str[right] = current
        updated_str[left] = end

        left += 1
        right -= 1
        
    return ' '.join(updated_str)


print(reverse_words("To be or not       to be"))
print(reverse_words("Hurray 3 2 1"))
print(reverse_words("We love Java "))
