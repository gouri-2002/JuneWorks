#create a function is_paindrome(word) return True if word is a palindrome string
#else return False


def is_palinddrome(word):
    
    reversed_str=word[::-1]
    return word==reversed_str

print(is_palinddrome("madam"))


