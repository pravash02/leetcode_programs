from collections import Counter


def checkInclusion(s1, s2):
    window = len(s1)
    s1_c = Counter(s1)
    print(s1_c)

    for i in range(len(s2) - window + 1):
        s2_c = Counter(s2[i:i + window])
        if s2_c == s1_c:
            return True

    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
