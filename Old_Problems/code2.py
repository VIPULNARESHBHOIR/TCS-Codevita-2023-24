def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def rotate_string(s, direction, magnitude):
    n = len(s)
    magnitude = magnitude % n  # Adjust magnitude to avoid unnecessary rotations

    if direction == 'L':
        return s[magnitude:] + s[:magnitude]
    elif direction == 'R':
        return s[-magnitude:] + s[:-magnitude]

def check_anagram_substring(s, rotations):
    first_char_string = ''
    for direction, magnitude in rotations:
        rotated_string = rotate_string(s, direction, magnitude)
        first_char_string += rotated_string[0]

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_anagram(first_char_string, substring):
                return "YES"
    return "NO"

# Input
original_string = "programming"
q = 3
rotations = [('L', 3), ('R', 2), ('L', 4)]

# Output
result = check_anagram_substring(original_string, rotations)
print(result)
