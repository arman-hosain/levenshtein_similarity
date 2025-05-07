import Levenshtein

def levenshtein_similarity(s1, s2):
    distance = Levenshtein.distance(s1, s2)
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    return 1 - (distance / max_len)

# Load file contents
with open('file1.txt', 'r', encoding='utf-8') as f1:
    text1 = f1.read()

with open('file2.txt', 'r', encoding='utf-8') as f2:
    text2 = f2.read()

# Compute similarity
similarity = levenshtein_similarity(text1, text2)
print(f"Levenshtein Similarity: {similarity:.4f}")
