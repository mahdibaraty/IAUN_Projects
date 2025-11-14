def funcStrip(s):
    start = 0
    while start < len(s) and s[start] == " ":
        start += 1

    end = len(s) - 1
    while end >= 0 and s[end] == " ":
        end -= 1

    return s[start:end+1]


Str = input(" Enter a string :")

print(f"\033[92m{funcStrip(Str)}\033[0m")