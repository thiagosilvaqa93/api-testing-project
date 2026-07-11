# 🚀 API Testing Project

Automated API testing project developed with **Python**, **Pytest**, and **Requests**.
The goal of this project is to demonstrate API test automation practices, clean project structure, and reusable API client implementation.

---

## 🛠️ Technologies

* **Python 3.13**
* **Pytest** - Test framework
* **Requests** - HTTP client library
* **Virtual Environment (venv)**

---

## 📂 Project Structure

```text
api-testing-project/
│
├── tests/
│   └── test_users.py          # API test cases
│
├── utils/
│   ├── __init__.py
│   └── api_client.py           # Reusable API client
│
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Project dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd api-testing-project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

Execute the test suite with:

```bash
python -m pytest
```

Expected result:

```text
4 passed
```

---

## 📌 Test Coverage

Current automated tests include:

✅ GET requests validation
✅ HTTP status code verification
✅ API response validation
✅ User endpoint testing

---

## 🔌 API Client

The project uses a reusable API client located at:

```text
utils/api_client.py
```

This approach centralizes API requests and improves:

* Code reuse
* Maintenance
* Test readability
* Scalability

Example:

```python
from utils.api_client import APIClient

client = APIClient()

response = client.get("/users")

assert response.status_code == 200
```

---

## ⚙️ Pytest Configuration

The project uses `pytest.ini`:

```ini
[pytest]
pythonpath = .
```

This allows internal modules to be imported correctly during test execution.

---

## 👨‍💻 Author

**Thiago Silva**

QA Automation / API Testing Project

---

## 📄 License

This project is created for learning purposes and portfolio demonstration.

