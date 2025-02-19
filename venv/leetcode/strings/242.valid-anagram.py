def isAnagram(s: str, t: str):
        s_map = {}
        t_map = {}

        for letter in s:
                s_map[letter] = s_map.get(letter, 0) + 1

        for letter in t:
                t_map[letter] = t_map.get(letter, 0) + 1

        if t_map == s_map:
            return True

        print(s_map)
        print(t_map)
        return False

    
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'c': 3, 'b': 2}
print(dict1 == dict2)

print(isAnagram("jaar","jaam"))