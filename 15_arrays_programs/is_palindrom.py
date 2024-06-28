def isPalindrome(s: str) -> bool:
    str_ = ""

    for c in s:
        if c.isalnum():
            str_ += c.lower()

    reverse_str = str_[::-1]

    return str_ == reverse_str


s = "Was it a car or a cat I saw?"
print(isPalindrome(s))
