# Simple NLP program for practice

# Sample text
text = "Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from data. These systems improve their performance over time without being explicitly programmed. With the rise of big data, machine learning techniques have become essential in many fields, including healthcare, finance, and marketing.."

# 1. Tokenization: split text into words
words = text.split()
print("Tokens:", words)

# 2. Convert words to lowercase for uniformity
words_lower = [word.lower().strip(".,!'") for word in words]
print("Lowercase tokens:", words_lower)

# 3. Count frequency of each word
word_freq = {}
for word in words_lower:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
