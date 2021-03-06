import unicodedata as ud
from collections import defaultdict


class AlphabetDetector:
    def __init__(self, no_memory=False):
        self.alphabet_letters = defaultdict(dict)
        self.no_memory = no_memory

    # def chr_in_alphabet(self, uchr, alphabet):
    #     if self.no_memory:
    #         return alphabet in ud.name(uchr)
    #     try:
    #         return self.alphabet_letters[alphabet][uchr]
    #     except KeyError:
    #         return self.alphabet_letters[alphabet].setdefault(
    #             uchr, alphabet in ud.name(uchr))

    ## Let's first try a lightweight memory-less chr_in_alphabet
    def chr_in_alphabet(self, uchr, alphabet):
        return alphabet in ud.name(uchr)

    def chr_english(self, uchr):
        i = ord(uchr)
        return (i>=65 and i<=90) or (i>=97 and i<=122)


    def only_alphabet_chars(self, unistr, alphabet, ignore_nl=False):
        """
        In this fork, all types of language testing default to return False if the string contains
        non-alphabetic non-whitespace charaters, such as punctuation marks.

        To ignore non-letter characters, set `ignore_nl=True`.

        CAUTION: If `ignore_nl=False`, existence of numbers will also make the function
        return to false.
        """
        
        unistr = ''.join(unistr.strip().split())
        if ignore_nl:
            return all(self.chr_in_alphabet(uchr, alphabet)
                       for uchr in unistr if uchr.isalpha())
        else:
            return all(self.chr_in_alphabet(uchr, alphabet)
                       for uchr in unistr)

    def only_english(self, unistr, ignore_nl=False):
        unistr = ''.join(unistr.strip().split())
        if ignore_nl:
            return all(self.chr_english(uchr)
                       for uchr in unistr if uchr.isalpha())
        else:
            return all(self.chr_english(uchr)
                       for uchr in unistr)


    def detect_alphabet(self, unistr):
        return set(ud.name(char).split(' ')[0]
                   for char in unistr if char.isalpha())

    def is_greek(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'GREEK') else False

    def is_cyrillic(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'CYRILLIC') else False

    def is_latin(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'LATIN') else False

    def is_arabic(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'ARABIC') else False

    def is_hebrew(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'HEBREW') else False

    # NOTE: this only detects Chinese script characters (Hanzi/Kanji/Hanja).
    # it does not detect other CJK script characters like Hangul or Katakana
    def is_cjk(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'CJK') else False

    def is_hangul(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'HANGUL') else False

    def is_hiragana(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'HIRAGANA') else False

    def is_katakana(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'KATAKANA') else False

    def is_thai(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'THAI') else False

    def is_english(self, unistr):
        return self.only_english(unistr)

    def is_latin_nonenglish(self, unistr):
        """
        Check whether all non-whitespace characters in unistr are latin but
        contains at least one non-English character.
        """
        return self.is_latin(unistr) and (not self.is_english(unistr))
