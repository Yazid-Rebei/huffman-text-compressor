```markdown
# HuffmanCompress

**A pure Python implementation of the Huffman coding algorithm for lossless text file compression.**

---

## Overview

HuffmanCompress implements the Huffman coding algorithm, an optimal prefix-free compression method that assigns shorter codes to more frequent characters. This project was developed as part of the **Multimedia Course (ICE 3)** to demonstrate fundamental compression concepts.

| Property | Description |
|----------|-------------|
| **Lossless** | Original data perfectly recoverable |
| **Optimal** | Achieves Shannon's entropy limit for symbol coding |
| **Prefix-free** | No code is a prefix of another → unambiguous decoding |

---

## Algorithm


Input Text → Frequency Analysis → Huffman Tree → Code Generation → Bit Packing → Compressed File
```



*where n = text length, k = number of distinct characters*

---

## File Format (.yazid)
```

┌────────────────────────────────────────────────────────────────┐
│ Bytes          │ Content                                       │
├────────────────┼───────────────────────────────────────────────┤
│ 0-3            │ Header length (uint32, big-endian)            │
│ 4 to 4+H       │ JSON header: {freqs: [[codepoint, freq]],     │
│                │              padding: N}                      │
│ 4+H to EOF     │ Compressed binary data                        │
└────────────────┴───────────────────────────────────────────────┘
```

---

## API Reference

### `compresser_fichier(txt_path, bin_path)`

Compresses a text file using Huffman coding.

| Parameter | Type | Description |
|-----------|------|-------------|
| `txt_path` | `str` | Path to input text file (UTF-8) |
| `bin_path` | `str` | Path for compressed output |

### `decomprimer_fichier(bin_path, txt_out_path)`

Decompresses a `.yazid` file back to original text.

| Parameter | Type | Description |
|-----------|------|-------------|
| `bin_path` | `str` | Path to compressed file |
| `txt_out_path` | `str` | Path for decompressed output |

### Usage Example

```python
# Compress
compresser_fichier("document.txt", "document.yazid")

# Decompress
decomprimer_fichier("document.yazid", "document_restored.txt")
```

---

## Performance

Test results on a 2KB text file:

| Metric | Value |
|--------|-------|
| Original size | 1,984 bytes |
| Compressed size | 1,185 bytes |
| Compression ratio | 40.3% |
| Effective bits/char | ~4.5 |

---

## Project Structure

```
HuffmanCompress/
├── main.py              # Core implementation
├── input.txt            # Source file
├── compressed.yazid     # Compressed output
├── output.txt           # Decompressed output
└── README.md            # Documentation
```

### Core Components

| Function | Responsibility |
|----------|----------------|
| `calcule_frequence()` | Character frequency analysis |
| `Noeud` | Binary tree node structure |
| `construire_arbre()` | Huffman tree construction |
| `gener_code()` | Recursive code generation |
| `bits_vers_octets()` | Bit packing with padding |
| `decode_bits_avec_arbre()` | Tree traversal decoding |

---

## Requirements

- Python 3.6+
- No external dependencies (standard library only: `json`, `os`)

---

## Author

**Mohamed Yazid Rebei**  
ICE 3 - Multimedia Course

---

## License

Educational project. Free for use and modification.

---

## References

1. Huffman, D. A. (1952). *A Method for the Construction of Minimum-Redundancy Codes*
2. Shannon, C. E. (1948). *A Mathematical Theory of Communication*
```
