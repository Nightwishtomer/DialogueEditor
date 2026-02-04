# Dialogue Editor

A powerful and flexible **Dialogue Editor** built in Python, designed for creating, editing, and managing complex dialogue trees for games, simulations, or interactive applications.

---

## 🚀 Features

- **Modular Architecture**  
  The project is structured into clear modules for `core` logic, `GUI`, `libraries`, and `tools`. Each module is self-contained and follows clean coding principles.

- **Dialogue Management**  
  Create, edit, and organize dialogues using a JSON-based data structure. Supports hierarchical dialogues, branching options, and conditional logic.

- **Library System**  
  Maintain reusable phrases and dialogue nodes through a dedicated library module. Supports importing, editing, and saving structured and non-structured phrase collections.

- **Interactive GUI**  
  A PyQt/PySide-based interface with:
  - Tree view for dialogue nodes
  - Context menus for node actions (add, edit, delete)
  - Popup dialogs for editing node content
  - Toolbar for quick actions and workflow optimization

- **Data Integrity & Parsing**  
  Built-in parsers ensure proper validation and handling of dialogue data. Easy serialization to JSON or proprietary `.plib` formats for external use.

- **Extensibility**  
  Designed with future expansions in mind:
  - Add new node types, conditions, or actions
  - Integrate with game engines or custom runtime environments
  - Support for additional file formats

---

## 🏗️ Project Structure
   ```bash
   DialogueEditor/
   ├── core/ # Core logic: dialog handling, parsing, libraries
   ├── gui/ # Graphical interface components and windows
   ├── libraries/ # Predefined dialogues, phrases, and libraries
   ├── tools/ # Utility scripts and helpers
   ├── main.py # Entry point of the application
   └── dialog.json # Example dialogue file
   ```


---

## ⚡ Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Run the editor:**
   ```bash
   python main.py

3. **Load a dialogue library from the libraries/ folder and start editing nodes, phrases, and dialogue trees.**

---

## 🛠️ Technologies
- Python 3.13+
- PyQt/PySide (GUI)
- **JSON & custom .plib** formats for dialogue storage
- Modular OOP design for maintainability and scalability

---

## 💡 Use Cases

Game development: interactive storylines, branching dialogues

Simulation & training apps: scenario-based conversations

Rapid prototyping of dialogue systems

---

## 📂 Contributions

Contributions are welcome! Please follow the modular structure and ensure all new nodes, parsers, or GUI features maintain compatibility with existing libraries and dialogue data.



