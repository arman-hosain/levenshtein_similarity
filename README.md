
# 🔤 Levenshtein Similarity Between Two Files

This project computes the **Levenshtein similarity** between the contents of two text files using Python. Levenshtein similarity is a normalized score derived from the number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another.

---

## 📁 Files

- `Levenshtein_similarity.py` – Main Python script
- `file1.txt` – First input text file
- `file2.txt` – Second input text file

---

## ⚙️ Requirements

- Python 3.x
- `python-Levenshtein` package

Install the required package:

```bash
pip install python-Levenshtein
```

---

## ▶️ Usage

1. Clone the repository or copy the script into your project.
2. Make sure your two text files are named `file1.txt` and `file2.txt`.
3. Run the script:

```bash
python Levenshtein_similarity.py
```

4. Sample output:

```
Levenshtein Similarity: 0.8732
```

---

## 📌 Example

If:

**file1.txt**
```
hello world
```

**file2.txt**
```
hallo word
```

Then output:
```
Levenshtein Similarity: 0.8182
```

---

## 🧠 How It Works

The script:
- Reads both files into strings.
- Uses `Levenshtein.distance()` to calculate edit distance.
- Normalizes it using:

```python
similarity = 1 - (distance / max(len(s1), len(s2)))
```

A similarity of `1.0` means the files are identical. A value closer to `0.0` means they are highly different.

---

## ✅ License

This project is open source and free to use under the MIT License.
