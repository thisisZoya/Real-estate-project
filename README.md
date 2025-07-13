# Real-estate-project
# 🏠 

This project is a simple, object-oriented **real estate management system** developed in Python **without any external frameworks**. It allows users to view, filter, and report property listings through a command-line interface.

The core of this system is built using **OOP principles** including **inheritance**, **composition**, and **abstraction** — providing flexibility and extensibility for real-world scenarios.

---

## 📌 Features

- View all property listings
- Filter listings by:
  - Region (neighborhood)
  - Price (min/max range)
  - Number of rooms
- Support for different deal types:
  - 🏷 Sale (price per square meter, discount, exchange)
  - 📄 Rent (mortgage, rent, convertible, discount)
- Display count reports per listing type
- Clean CLI-based user interaction
- Data handled purely in-memory (no database)

---

## 🏗 Project Structure

| File           | Purpose                                               |
|----------------|--------------------------------------------------------|
| `main.py`      | Entry point to the system / CLI loop                   |
| `sample.py`    | Generates sample property listings for demonstration   |
| `manager.py`   | Implements object search, filtering, and count logic   |
| `advertisement.py` | Deal type implementations (Rent/Sell)             |
| `deal.py`      | Encapsulates deal-specific options                     |
| `estate.py`    | Defines property types (Apartment, Villa, Store)       |
| `base.py`      | Base classes using abstraction                         |
| `user.py`      | Seller/owner information (name, contact)               |

---

## 🧠 OOP Concepts Used

- **Inheritance** – For property/deal type hierarchies  
- **Composition** – Combining behaviors across objects  
- **Abstraction** – Base classes like `BaseEstate`, `BaseAdvertisement`  
- **Polymorphism** – Shared interfaces like `show_description()`  
- **Encapsulation** – Logical separation between data and behavior  

---

## 🔍 Sample Usage

```python
# Filter apartment listings in a price range
ApartmentSell.manager.search(price_per_meter__min=10000, price_per_meter__max=15000)

# Filter villas with 3 bedrooms in specific neighborhood
VillaRent.manager.search(region="Zafaranieh", rooms=3)
```

---

## 🧪 Running the App

Make sure you have Python 3 installed.

Clone the repository or download the project.

Run the program from terminal:

```bash
python main.py
```

You'll be prompted to choose between viewing reports or all listings.

---

## ⚙️ Implementation Notes

- Each ad must have a **unique ID**.
- A single property listed for both **rent and sale** must be registered separately.
- Each model has an `objects_list` to simulate persistent storage.
- No database is used — data is fully stored and processed in-memory.
- Sample listings are preloaded using `create_samples()`.

---

## 🚀 Potential Future Improvements

- Add graphical interface (GUI)
- Connect to a database (SQLite, PostgreSQL, etc.)
- Enable full-text search (`contains`, `startswith`, etc.)
- Edit or delete ads from the CLI
- Add user authentication

---

## 🔍 SEO Keywords

```
real estate CLI python, OOP real estate project, property listing search Python, inheritance abstraction composition Python, command-line real estate system
```

---

## 👤 Author

- Developed by: [Your Name]
- GitHub: [your-username]
- Contact: [your-email@example.com]

---
