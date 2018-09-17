from alphabet_detector import AlphabetDetector

ad = AlphabetDetector()
print("[ is an English letter:", ad.chr_english(u'['))
print(ad.only_alphabet_chars(u"ελληνικά ", "GREEK"))
print("刘 is lattin:", ad.chr_in_alphabet(u"刘", "LATIN"))
print("刘 is CJK:", ad.chr_in_alphabet(u"刘", "CJK"))
print("'ελληνικά νι.' only contains greek letters:", ad.is_greek('ελληνικά νι.'))