# 🚀 Downloads Organizer API

A modular, layered-architecture backend utility built with **FastAPI**, **Python (Pathlib / Shutil)**, and **Pydantic**. Designed to automatically inspect local directories, organize messy files into clean category folders, and detect duplicate files.

---

## 🏗️ Architecture & Flow
This project strictly separates concerns into a clean 3-layer design:
1. **API Layer (`main.py`)**: Handles FastAPI HTTP routes (`GET`, `POST`), query parameters, Pydantic request models, and `HTTPException` error handling.
2. **Logic Layer (`logic.py`)**: Manages core business rules such as extension counting, category mapping (`Docs`, `Img`, `Archive`), and size-based duplicate detection.
3. **Data Layer (`data.py`)**: Interfaces directly with the operating system file system using `pathlib` and `shutil` to read folders and move files safely.

```text
[ Client / Frontend / Swagger UI ]
       │  (Sends HTTP GET / POST requests)
       ▼
[ FastAPI App / main.py ]  ──► Handles HTTP routes, Pydantic validation, & errors
       │  (Calls functions)
       ▼
[ Business Logic / logic.py ]  ──► Counts extensions, maps categories, tracks sizes
       │  (Calls functions)
       ▼
[ Data Layer / data.py ]  ──► Interacts with OS via Pathlib and Shutil