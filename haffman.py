import json
import os


def calcule_frequence(chain):
    t = {}
    for c in chain:
        if c in t:
            t[c] += 1
        else:
            t[c] = 1
    return t


class Noeud:
    def __init__(self, char, freq, gauche=None, droite=None):
        self.char = char
        self.freq = freq
        self.gauche = gauche
        self.droite = droite


def construire_arbre(freqs):
    tab_noeud = []

    for char, freq in freqs.items():
        tab_noeud.append(Noeud(char, freq))

    if len(tab_noeud) == 0:
        return None

    if len(tab_noeud) == 1:
        return tab_noeud[0]

    while len(tab_noeud) > 1:
        tab_noeud.sort(key=lambda n: n.freq)

        n1 = tab_noeud.pop(0)
        n2 = tab_noeud.pop(0)

        parent = Noeud(None, n1.freq + n2.freq, n1, n2)
        tab_noeud.append(parent)

    return tab_noeud[0]


def gener_code(noeud, code="", tab_code=None):
    if tab_code is None:
        tab_code = {}

    if noeud is None:
        return tab_code

    if noeud.char is not None:
        tab_code[noeud.char] = code if code != "" else "0"
    else:
        gener_code(noeud.gauche, code + '0', tab_code)
        gener_code(noeud.droite, code + '1', tab_code)

    return tab_code


def compresse_text(code, text):
    ch = ""
    for c in text:
        ch += code[c]
    return ch


def bits_vers_octets(bitstring):
    padding = (8 - len(bitstring) % 8) % 8
    bitstring_padded = bitstring + ("0" * padding)

    data = bytearray()
    for i in range(0, len(bitstring_padded), 8):
        octet = bitstring_padded[i:i+8]
        data.append(int(octet, 2))

    return bytes(data), padding


def octets_vers_bits(data):
    bits = ""
    for b in data:
        bits += format(b, "08b")
    return bits


def decode_bits_avec_arbre(racine, bits):
    if racine is None:
        return ""

    if racine.char is not None:
        return racine.char * len(bits)

    resultat = ""
    courant = racine

    for bit in bits:
        if bit == '0':
            courant = courant.gauche
        else:
            courant = courant.droite

        if courant.char is not None:
            resultat += courant.char
            courant = racine

    return resultat


def compresser_fichier(txt_path, bin_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    freqs = calcule_frequence(text)
    racine = construire_arbre(freqs)
    code = gener_code(racine)

    bits = compresse_text(code, text)
    donnees_binaires, padding = bits_vers_octets(bits)

    # on stocke les fréquences avec ord() pour éviter les problèmes JSON
    header = {
        "freqs": [[ord(char), freq] for char, freq in freqs.items()],
        "padding": padding
    }

    header_bytes = json.dumps(header).encode("utf-8")
    header_len = len(header_bytes)

    with open(bin_path, "wb") as f:
        f.write(header_len.to_bytes(4, byteorder="big"))
        f.write(header_bytes)
        f.write(donnees_binaires)

    taille_avant = os.path.getsize(txt_path)
    taille_apres = os.path.getsize(bin_path)

    print("Compression terminée")
    print("Fichier source :", txt_path)
    print("Fichier compressé :", bin_path)
    print("Taille avant :", taille_avant, "octets")
    print("Taille après :", taille_apres, "octets")
    print("Nombre de bits Huffman utiles :", len(bits))


def decomprimer_fichier(bin_path, txt_out_path):
    with open(bin_path, "rb") as f:
        header_len = int.from_bytes(f.read(4), byteorder="big")
        header_bytes = f.read(header_len)
        data = f.read()

    header = json.loads(header_bytes.decode("utf-8"))
    padding = header["padding"]

    freqs = {}
    for codepoint, freq in header["freqs"]:
        freqs[chr(codepoint)] = freq

    racine = construire_arbre(freqs)

    bits = octets_vers_bits(data)
    if padding > 0:
        bits = bits[:-padding]

    texte = decode_bits_avec_arbre(racine, bits)

    with open(txt_out_path, "w", encoding="utf-8") as f:
        f.write(texte)

    print("Décompression terminée")
    print("Fichier compressé :", bin_path)
    print("Fichier texte reconstruit :", txt_out_path)




#main : 

compresser_fichier("input.txt", "compressed.yazid")
decomprimer_fichier("compressed.yazid", "output.txt")