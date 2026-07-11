# 🚀 API Testing Automation Project

![Python API Tests](https://github.com/thiagosilvaqa93/api-testing-project/actions/workflows/python-tests.yml/badge.svg)

## 📌 Overview

This project demonstrates API test automation using **Python**, **Pytest**, and **REST API validation**.

The objective is to validate REST API endpoints through automated tests following QA Automation best practices, including:

* Test organization
* Reusable API client
* Automated regression testing
* Continuous Integration with GitHub Actions
* HTML test reports

---

## 🛠️ Technologies Used

* Python 3.13
* Pytest
* Requests
* pytest-html
* GitHub Actions (CI/CD)
* REST API Testing

---

## 📂 Project Structure

```
api-testing-project/
│
├── tests/
│   └── test_users.py
│
├── utils/
│   └── api_client.py
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🧪 Test Scenarios

The automated tests validate:

✅ API response status codes
✅ Response data validation
✅ User endpoint behavior
✅ REST API communication

---

## ▶️ How to Run Locally

### 1. Clone repository

```bash
git clone https://github.com/thiagosilvaqa93/api-testing-project.git
```

### 2. Navigate to project folder

```bash
cd api-testing-project
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Mac/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run automated tests

```bash
pytest
```

---

## 📊 HTML Test Report

To generate an HTML test report:

```bash
pytest --html=report.html
```

After execution, an HTML file will be generated containing the test results.

---

## 🔄 Continuous Integration (CI/CD)

This project uses **GitHub Actions** for continuous integration.

Every push or pull request to the `main` branch automatically:

* Installs Python
* Installs project dependencies
* Runs automated tests
* Generates HTML test reports
* Stores test reports as workflow artifacts

---

## 📈 Future Improvements

* Add API authentication tests
* Add environment variables using `.env`
* Add negative test scenarios
* Add test data management
* Add Docker support
* Add test coverage reports

---

## 👨‍💻 Author

**Thiago Silva**

QA Engineer | Software Engineering Student

GitHub:
https://github.com/thiagosilvaqa93

