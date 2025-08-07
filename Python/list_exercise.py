# Step 1: Liste erstellen und ausgeben
my_list = ["apple", "banana", "cherry", "mango", "grape"]
print(my_list)

# Step 2: Auf Elemente per Index und negativen Index zugreifen
print(my_list[0])     # Erstes Element
print(my_list[-1])    # Letztes Element
print(my_list[-2])    # Vorletztes Element

# Step 3: Liste slicen (Teilbereiche anzeigen)
print(my_list[1:4])   # Index 1 bis 3 (4 ist exklusiv)
print(my_list[:2])    # Von Anfang bis Index 1
print(my_list[2:])    # Von Index 2 bis zum Ende

# Step 4: Prüfen, ob ein Element enthalten ist
if "apple" in my_list:
    print("Apple is in the list!")
else:
    print("Apple is NOT in the list!")

# Step 5: Elemente hinzufügen
my_list.append("pear")           # Hängt ein Element ans Ende
my_list.insert(2, "orange")      # Fügt ein Element an Position 2 ein
print(my_list)

# Step 6: Elemente verändern
my_list[0] = "lemon"                     # Ersetzt erstes Element
my_list[1:3] = ["peach", "melon"]        # Ersetzt mehrere Elemente
print(my_list)

# Step 7: Elemente entfernen
my_list.remove("pear")                  # Entfernt das erste Vorkommen
removed_item = my_list.pop(1)           # Entfernt Element bei Index 1
print(f"Removed item: {removed_item}")
temp_list = my_list.copy()
temp_list.clear()                       # Macht die Liste leer
print("Cleared list:", temp_list)

# Step 8: Liste kopieren
copy_list = my_list.copy()
my_list.append("pineapple")
print("Original list:", my_list)
print("Copied list  :", copy_list)

# Step 9: Listen zusammenfügen und erweitern
list_a = ["a", "b"]
list_b = ["c", "d"]
combined_plus = list_a + list_b
print("Combined with + :", combined_plus)

list_a.extend(list_b)                   # Fügt Elemente von list_b zu list_a hinzu
print("Extended with extend():", list_a)

# Step 10: Liste sortieren und umdrehen
numbers = [5, 3, 8, 1, 4]
numbers.sort()                          # Sortiert in-place (aufsteigend)
print("Sorted list:", numbers)

numbers.reverse()                       # Kehrt Reihenfolge um
print("Reversed list:", numbers)

new_sorted = sorted(numbers)            # Gibt eine neue sortierte Liste zurück
print("New sorted (via sorted()):", new_sorted)

# Count und Index verwenden
print("Count of 'a' in list_a:", list_a.count("a"))
print("Index of 'b' in list_a:", list_a.index("b"))

# Bonus: List Comprehension
fruits = ["apple", "banana", "kiwi", "pineapple"]
upper_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]  # Groß schreiben, wenn >5 Buchstaben
print("Uppercase fruits (len > 5):", upper_fruits)
