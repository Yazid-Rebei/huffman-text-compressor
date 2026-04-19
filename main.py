from haffman import compresser_fichier, decomprimer_fichier


while True:
    print("1. Compress a file")
    print("2. Decompress a file")
    print("3. Exit")

    choix = int(input("Your choice: "))

    if choix == 1:
        compresser_fichier("input.txt", "compressed.yazid")

    elif choix == 2:
        decomprimer_fichier("compressed.yazid", "output.txt")

    elif choix == 3:
        exit()

    else:
        print("Invalid choice!")