word = "Programming"

print(word[::-1])
print(word[:3], word[-3:])
print(word.count("m"))

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("level"))
print(is_palindrome("python"))