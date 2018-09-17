from alphabet_detector import AlphabetDetector

ad = AlphabetDetector()
print(ad.only_alphabet_chars(u"ελληνικά ", "GREEK"))
print("刘 is lattin:", ad.is_in_alphabet(u"刘", "LATIN"))
print("刘 is CJK:", ad.is_in_alphabet(u"刘", "CJK"))