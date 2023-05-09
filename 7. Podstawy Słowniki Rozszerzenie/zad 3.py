zdanie = (
    "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of "
    "forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently "
    "rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this,"
    " and nothing more.")

# zdanie = """
#     fwgegegegg
#     gwegewgewgvwvwv er
#     """


zdanie_nowe = zdanie.split()
print(zdanie)
print(zdanie_nowe)

slownik = dict()
for slowo in zdanie_nowe:
    if slowo not in slownik.keys():
        slownik[slowo] = 1
    else:
        slownik[slowo] += 1
print(slownik)
