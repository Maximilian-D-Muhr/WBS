first_name = "Max"
last_name = "Muhr"
bio = """ich bin ein Lebenslauf
aber habe mehrehere
zeilen"""

print(first_name[0]) 
print(last_name[-1]) 
print(bio[:10]) 

# Kommentar commnand /
# --- Durch String iterieren ---
for char in first_name:
    print(char)

# Test
for char in last_name:
    print(char)

# --- Länge eines Strings ---
print(len(bio))

# --- Substrings prüfen ---
print("Python" in bio)       # True oder False
print("Java" not in bio)     # True oder False

# --- Strings modifizieren ---
print(first_name.upper())    # MAX
print(last_name.lower())     # muhr

bio = bio.strip().replace("Python", "coding")
print(bio)

print(bio.split())           # Liste der Wörter

# --- Strings verketten ---
full_name = first_name + " " + last_name
print(full_name)

# --- String Formatting ---
age = 41
print(f"Hello, my name is {full_name} and I love Python!")
print("My full name is {} and I am {} years old.".format(full_name, age))

# --- Escape Characters ---
quote = "He said, \"Python's great!\""
print(quote)

# --- Bonus ---
print(bio.center(50))                 # bio zentriert auf 50 Zeichen
print(full_name.count("a"))           # Anzahl der Buchstaben 'a' im Namen