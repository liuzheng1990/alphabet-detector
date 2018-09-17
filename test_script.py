from alphabet_detector_lz import AlphabetDetector

ad = AlphabetDetector()

print(ad.only_alphabet_chars(u"ελληνικά! ", "GREEK"))
print("d is an English letter:", ad.chr_english(u'd'))
print("d is lattin:", ad.chr_in_alphabet(u"d", "LATIN"))
print("您 is CJK:", ad.chr_in_alphabet(u"您", "CJK"))
print("'ελληνικά νι.' only contains greek letters:", ad.is_greek('ελληνικά νι.'))
print("'Hello world 牛逼' only contains English letters:", ad.only_english('Hello world!'))
print("'det forårsaker første' is latin but contains non-English characters:", 
								ad.is_latin_nonenglish('det forårsaker første'))

print("'Hello world' is latin but contains non-English characters:", 
								ad.is_latin_nonenglish('Hello world'))