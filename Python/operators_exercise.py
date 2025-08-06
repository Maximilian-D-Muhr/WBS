# --- Arithmetic Operators ---
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)          # normales Teilen
print("Floor Division:", a // b)   # ganzzahliges Teilen
print("Modulus:", a % b)           # Rest
print("Exponentiation:", a ** b)   # Potenzierung

# --- Assignment Operators ---
x = 10
x += 5
print("x after += 5:", x)
x -= 3
print("x after -= 3:", x)
x *= 2
print("x after *= 2:", x)
x /= 4
print("x after /= 4:", x)

# --- Comparison Operators ---
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# --- Logical Operators ---
is_python_fun = True
is_java_fun = False

print("Python and Java fun:", is_python_fun and is_java_fun)
print("Python or Java fun:", is_python_fun or is_java_fun)
print("Not Python fun:", not is_python_fun)

# --- Identity Operators ---
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)       # True
print("list1 is not list2:", list1 is not list2) # False
print("list1 is list3:", list1 is list3)       # False (andere Objekte mit gleichem Inhalt)

# --- Membership Operators ---
text = "Python programming is fun!"
print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)

# --- Bitwise Operators (Bonus) ---
a = 5   # 0101 in binär
b = 3   # 0011 in binär

print("a & b:", a & b)   # Bitwise AND
print("a | b:", a | b)   # Bitwise OR
print("a ^ b:", a ^ b)   # Bitwise XOR
print("a << 1:", a << 1) # Linksverschiebung
print("b >> 1:", b >> 1) # Rechtsverschiebung

# --- Operator Precedence ---
expr1 = 2 + 3 * 2 ** 2
expr2 = (2 + 3) * (2 ** 2)

print("Without parentheses:", expr1)
print("With parentheses:", expr2)
