# alphabet-detector
[![Build Status](https://travis-ci.org/EliFinkelshteyn/alphabet-detector.svg?branch=master)](https://travis-ci.org/EliFinkelshteyn/alphabet-detector)
[![Coverage Status](https://coveralls.io/repos/EliFinkelshteyn/alphabet-detector/badge.svg?branch=master&service=github)](https://coveralls.io/github/EliFinkelshteyn/alphabet-detector?branch=master)

A library to detect what alphabet something is written in. **Works on Python 2.7+ and 3.3+**

## Author
Original: Eli Finkelshteyn (founder [constructor.io](http://www.constructor.io))
Forked: Liu Zheng (personal blog: [liutheprogrammer.wordpress.com](http://liutheprogrammer.wordpress.com))

## Installation (original version)
<code>pip install alphabet-detector</code>  

For now, this forked version does not support PyPI install, before the author understands all the copyright issues. To use this fork, please clone the repository, copy the `alphabet_detector_lz` directory to the project directory and import it locally.

## Usage
To instantiate an AlphabetDetector (the object is used for speed optimization):

```python
from alphabet_detector_lz import AlphabetDetector
ad = AlphabetDetector()
```

In general, you can just use the `only_alphabet_chars(unicode_str, alphabet)` method and expect a boolean response:

```python
ad.only_alphabet_chars(u"ελληνικά means greek", "LATIN") #False
ad.only_alphabet_chars(u"ελληνικά", "GREEK") #True
ad.only_alphabet_chars(u'سماوي يدور', 'ARABIC') #True
ad.only_alphabet_chars(u'שלום', 'HEBREW') #True
ad.only_alphabet_chars(u"frappé", "LATIN") #True
ad.only_alphabet_chars(u"hôtel lœwe 67", "LATIN") #True
ad.only_alphabet_chars(u"det forårsaker første", "LATIN") #True
ad.only_alphabet_chars(u"Cyrillic and кириллический", "LATIN") #False
ad.only_alphabet_chars(u"кириллический", "CYRILLIC") #True
```

**Change in this fork**:

Unlike the original version, where non-whitespace non-alphabetic characters (such as numerical digits, punctuation symbols, etc.) were ignored, in this thread, the `only_alphabet_chars` method dafaults not
to ignore them. One can set `ignore_nl=True` ("nl" short for "non letter") to ignore them if needed. See the examples below:

```python
ad.only_alphabet_chars(u"Hello world!", "LATIN") #False in this fork, while True in original version
ad.only_alphabet_chars(u"Hello world!", "LATIN", ignore_nl=True) #True
```

As a result, the following `is_*` functions all default not to ignore the non-alphabetic characters.

You can also request free-style detection of any unicode string:

```python
ad.detect_alphabet(u'Cyrillic and кириллический') #{'CYRILLIC', 'LATIN'}
```

Convenience methods are also provided for some major languages:

```python
ad.is_cyrillic(u"Привет") #True  
ad.is_latin(u"howdy") #True
# NOTE: this only detects Chinese script characters (Hanzi/Kanji/Hanja).
# it does not detect other CJK script characters like Hangul or Katakana
ad.is_cjk(u"hi") #False
ad.is_cjk(u'汉字') #True
```

**New in this fork**:

In this fork, a function called `only_english` is added to explicitly check whether a string contains only English letters (again, a `ignore_nl=False` by default). Examples:

```python
print("'Hello world 牛逼' only contains English letters:", ad.only_english('Hello world!'))
print("'det forårsaker første' is latin but contains non-English characters:", 
								ad.is_latin_nonenglish('det forårsaker første'))

print("'Hello world' is latin but contains non-English characters:", 
								ad.is_latin_nonenglish('Hello world'))
```


**NOTE: all strings are expected to be unicode to keep things consistent. Conversion is *never* done for you, and errors are thrown when a string is not unicode.**
