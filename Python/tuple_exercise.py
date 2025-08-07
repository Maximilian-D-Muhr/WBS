# 1. Tupel erstellen
my_tuple = ("apple", "banana", "cherry", "banana", "kiwi")
print("Tuple:", my_tuple)

# 2. Tupel ausgeben
print("Full tuple:", my_tuple)

# 3. Auf Tupel-Elemente zugreifen
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# 4. Tupel slicen (Teilausschnitte anzeigen)
print("Middle items:", my_tuple[1:4])     # Index 1 bis 3
print("Start to index 3:", my_tuple[:3])  # Von Anfang bis Index 2
print("Index 2 to end:", my_tuple[2:])    # Ab Index 2 bis Ende

# 5. Prüfen, ob ein Element enthalten ist
if "banana" in my_tuple:
    print("Yes, 'banana' is in the tuple.")
else:
    print("No, 'banana' is not in the tuple.")

# 6. count() und index() verwenden
print("Count of 'banana':", my_tuple.count("banana"))
print("Index of 'cherry':", my_tuple.index("cherry"))

# 7. Tupel packen und entpacken
# Packen war bereits oben
(a, b, c, d, e) = my_tuple
print("Unpacked:", a, b, c, d, e)

# Asterisk beim Entpacken
(fruit1, *middle_fruits, fruit_last) = my_tuple
print("With * unpacking:", fruit1, middle_fruits, fruit_last)

# 8. Tupel zusammenfügen (joining)
another_tuple = ("orange", "melon")
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple)

repeated_tuple = another_tuple * 2
print("Repeated tuple:", repeated_tuple)
