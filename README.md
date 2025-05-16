# Simple_Database_GUI

A desktop application that demonstrates essential skills in GUI design, database integration, and basic data security. This project is built using Python's `tkinter` for the interface, `sqlite3` for the database layer, and includes SHA-256 hashing for secure data handling.

## 🚀 Project Overview

**Simple_Database_GUI** is a portfolio-level project that showcases the integration of multiple core software development concepts:
- Building desktop applications with a graphical user interface (GUI)
- Managing local databases using SQLite
- Applying cryptographic hashing (SHA-256) for basic data protection

## ✨ Features

- Add, update, delete, and view records
- Store sensitive data securely using SHA-256 hashing
- Simple and clean interface built with Tkinter
- Lightweight and self-contained (no external dependencies)

## 🔐 SHA-256 Hashing

This application uses Python's `hashlib` library to securely hash sensitive data (e.g., passwords) before storing it in the database. This ensures that raw values are never stored directly, improving data security even in local applications.

Example:
```python
import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
 ```
## 🛠 Technologies Used
Python 3.x

Tkinter (GUI)

SQLite3 (Database)

hashlib (for SHA-256 hashing)

## 📸 Screenshots

### Entry Window
![Entry Window](https://github.com/YasinAk37/Simple_Database_GUI/blob/d1e066e8db6af283ff5b9c97969ba1a466a5c3f3/Pictures/app1.png)

### Database Window
![Database Window](https://github.com/YasinAk37/Simple_Database_GUI/blob/8e3e951bec4a74051bef507fd6c352acaa27ebc9/Pictures/app2.png)

