
# HuffmanCompress

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Compression](https://img.shields.io/badge/Compression-Huffman-green)
![Status](https://img.shields.io/badge/Status-Educational_Project-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A Python project that implements **Huffman coding** for **lossless text compression**, enhanced with **password-protected decompression** using **salted SHA-256 hashing**.

---


## Overview

**HuffmanCompress** is an educational implementation of the Huffman coding algorithm developed in Python. It demonstrates how entropy-based compression can reduce the size of text data by assigning shorter binary codes to more frequent characters.

This project also introduces a password verification mechanism: decompression is only allowed when the correct password is provided. The password is not stored in plain text; instead, a **salted SHA-256 hash** is stored in the file header.

---

## Features

- Lossless text compression using Huffman coding
- Prefix-free binary encoding for correct decoding
- Password-protected decompression
- Salted SHA-256 password hashing
- Custom binary compressed file format
- Metadata header stored in JSON
- Automatic size reporting before and after compression
- Simple command-line interface

---

## How the Algorithm Works

### Compression Pipeline

```text id="vpjzvv"
Input Text
   ↓
Character Frequency Analysis
   ↓
Huffman Tree Construction
   ↓
Binary Code Generation
   ↓
Text Encoding into Bitstream
   ↓
Bit Packing into Bytes
   ↓
Password Hash + Metadata Header
   ↓
Compressed File (.yazid)
````

### Decompression Pipeline

```text id="kf1wjy"
Compressed File
   ↓
Header Parsing
   ↓
Password Verification
   ↓
Byte-to-Bit Conversion
   ↓
Huffman Tree Reconstruction
   ↓
Bitstream Decoding
   ↓
Original Text Recovery
```

---

## Project Structure

```text id="4r74ag"
project/
│── main.py
│── huffman.py
│── input.txt
│── compressed.yazid
│── output.txt
│── README.md
```

### File Description

| File               | Role                                                         |
| ------------------ | ------------------------------------------------------------ |
| `main.py`          | Handles the user menu and program flow                       |
| `huffman.py`       | Contains compression, decompression, hashing, and file logic |
| `input.txt`        | Example input file to compress                               |
| `compressed.yazid` | Generated compressed file                                    |
| `output.txt`       | Reconstructed file after decompression                       |
| `README.md`        | Project documentation                                        |

---

## Compressed File Format

Compressed files use a custom `.yazid` format.

### Binary Structure

```text id="jf0qwi"
[4 bytes: header length] → [JSON header] → [compressed binary data]
```

### Header Example

```json id="xek774"
{
  "freqs": [[97, 12], [98, 4], [99, 7]],
  "padding": 3,
  "password_salt": "a1b2c3d4e5f6...",
  "password_hash": "9f86d081884c7d65...",
  "original_length": 245
}
```

### Header Fields

| Field             | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `freqs`           | Character frequencies used to rebuild the Huffman tree  |
| `padding`         | Number of padding bits added to complete the final byte |
| `password_salt`   | Random salt used during password hashing                |
| `password_hash`   | Salted SHA-256 hash of the password                     |
| `original_length` | Length of the original text                             |

---

## Core Functions

### Compression Functions

| Function                | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `calcule_frequence()`   | Counts character frequencies in the input text    |
| `construire_arbre()`    | Builds the Huffman tree from the frequency table  |
| `gener_code()`          | Generates binary Huffman codes for each character |
| `compresse_text()`      | Encodes the input text into a Huffman bitstream   |
| `bits_vers_octets()`    | Packs the bitstream into bytes                    |
| `creer_hash_password()` | Generates a salted SHA-256 password hash          |
| `compresser_fichier()`  | Main compression routine                          |

### Decompression Functions

| Function                   | Description                          |
| -------------------------- | ------------------------------------ |
| `octets_vers_bits()`       | Converts bytes back into a bitstring |
| `decode_bits_avec_arbre()` | Decodes the Huffman bitstream        |
| `verifier_password()`      | Validates the entered password       |
| `decomprimer_fichier()`    | Main decompression routine           |

---

## Data Structure

### `Noeud` Class

The Huffman tree is represented using the `Noeud` class:

```python id="naruls"
class Noeud:
    def __init__(self, char, freq, gauche=None, droite=None):
        self.char = char
        self.freq = freq
        self.gauche = gauche
        self.droite = droite
```

### Attributes

| Attribute | Description                                  |
| --------- | -------------------------------------------- |
| `char`    | Stored character (`None` for internal nodes) |
| `freq`    | Character frequency or subtree sum           |
| `gauche`  | Left child                                   |
| `droite`  | Right child                                  |

---

## Security Model

This project uses **salted SHA-256 hashing** to protect decompression access.

### What is implemented

* a password is requested during compression
* a random 16-byte salt is generated
* the password hash is computed using the salt
* the salt and hash are stored in the header
* decompression is denied if the password is incorrect

### Important clarification

This project does **not implement full file encryption**.

That means:

* the password is protected correctly
* decompression access is restricted
* but the compressed binary content itself is not encrypted with an algorithm such as AES

So the project should be described as:

* **password-protected decompression**
* not **full encrypted compression**

This distinction is technically important.

---


## Limitations

* supports text files only
* uses fixed file names in the current menu
* does not encrypt compressed data
* tree construction uses repeated sorting instead of a priority queue
* no graphical interface
* limited input validation in the current version

---

## Future Improvements

Possible future enhancements include:

* custom input and output file paths
* file existence validation before processing
* better exception handling
* compression ratio calculation
* faster Huffman tree construction using `heapq`
* full encryption of compressed data
* graphical interface
* support for additional file types
* multilingual user interface
* modular unit testing

---

## Author

Developed as part of the **Multimedia Course (ICE 3)* by Moahemed Yazid Rebei*.

---



