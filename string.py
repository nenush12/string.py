mport re
from collections import Counter

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def are_anagrams(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

def count_words(sentence):
    words = sentence.lower().split()
    return dict(Counter(words))

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print("1. Reverse 'hello':", reverse_string("hello"))
print("2. Vowels in 'hello world':", count_vowels("hello world"))
print("3. Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))
print("   Are 'hello' and 'world' anagrams?", are_anagrams("hello", "world"))

sentence = "the quick brown fox jumps over the lazy dog"
word_counts = count_words(sentence)
print("4. Word counts:")
for word, count in word_counts.items():
    print(f"   '{word}': {count}")

text = "Hello, World!"
shift = 3
encrypted =Ca
