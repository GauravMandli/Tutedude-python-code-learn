# Tutedude-python-code-learn

# 🧮 Tkinter Calculator (Python)

A simple GUI-based calculator built using **Python Tkinter (ttk)**.  
This project helps beginners understand GUI development, button handling,
and basic calculator logic in Python.

---

## 📌 Features

- Clean GUI using **tkinter + ttk**
- Number buttons (0–9)
- Operators:
  - Addition (+)
  - Subtraction (−)
  - Multiplication (×)
  - Division (÷)
- Clear button
- Entry display aligned to the right
- Grid-based layout (calculator-style)

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter**
- **ttk (Themed Tkinter)**

---

## 🧠 How the Calculator Works

### Number Input
- Number buttons trigger the `click(num)` function.
- Each digit is appended to the Entry widget to form a number.

### Operator Handling
- When an operator button is clicked:
  - The first number is stored internally.
  - The selected operator is saved.
  - The Entry field is cleared to accept the next number.

### Equal (`=`) Button
- Executes the calculation based on the selected operator.
- Displays the computed result in the Entry widget.

### Clear Button
- Clears all input from the Entry field.

---

## ⚠️ Limitations

- Does not follow the BODMAS rule.
- Supports only two numbers per calculation.
- Decimal number operations are not supported yet.

---

## 🚀 Future Improvements

- Implement BODMAS rule using expression evaluation.
- Add support for decimal numbers.
- Enable keyboard input for calculations.
- Improve error handling (e.g., divide-by-zero cases).
- Enhance UI styling for a better user experience.
