from string import ascii_lowercase as low, ascii_uppercase as up


def caesar(s, shift):
    result = []
    for a in s:
        if a.isalpha():
            if a.islower():
                result.append(low[(low.index(a) + shift) % 26])
            else:
                result.append(up[(up.index(a) + shift) % 26])
        else:
            result.append(a)
    return ''.join(result)


assert caesar("Abcd", 2) == "Cdef"
assert caesar("message", -1) == "ldrrzfd"
assert caesar("ZZ Top", 3) == "CC Wrs"
