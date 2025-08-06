# --- Variablen erstellen ---
name = "Max"
age = 41
height = 1.82

# --- Variablen ausgeben ---
print("Name:", name)
print("Age:", age)
print("Height:", height)

# --- Typen prüfen ---
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))

# --- Casting ---
age_str = str(age)
print("My name is " + name + " and I am " + age_str + " years old.")

# --- Bonus: Globale Variable ---
global_message = "This is the original message."

def change_message():
    global global_message
    global_message = "This is the modified global message."

change_message()  # Funktion aufrufen, um die globale Variable zu ändern
print(global_message)
