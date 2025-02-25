# 📌 PricePilot - AI-Powered Dynamic Pricing API

### 🚀 About the Project
PricePilot is an AI-powered **dynamic pricing API** that optimizes product pricing using **competitor analysis** and **machine learning (Random Forest Regressor)**.

### 🔥 Features
- **Web scraping** (eBay competitor prices)
- **Database storage** (SQLite)
- **Machine Learning model** (Random Forest for price optimization)
- **FastAPI-powered API**
- **Automated price updates**
- **Deployment-ready**

---

## 📌 Setup & Installation

### 1️⃣ Clone the Repository
Download the project from GitHub and navigate into the directory.

### 2️⃣ Create a Virtual Environment & Install Dependencies
Set up a virtual environment and install required libraries from the requirements file.

### 3️⃣ Run the FastAPI Server
Start the server locally to test the API.

### 4️⃣ Test the API
Once the server is running, visit the provided link to access API documentation and test endpoints interactively.

---

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|------------|
| **POST** | `/products/` | Add a new product |
| **GET** | `/products/{id}` | Get product details |
| **GET** | `/fetch-competitor-prices/` | Fetch & store competitor prices |
| **GET** | `/optimized-price/` | Get AI-optimized price |
| **GET** | `/update-competitor-prices/` | Run competitor price updates in the background |

---

## 📌 Deployment on Render

### 1️⃣ Prepare for Deployment
Ensure all dependencies are listed in the requirements file and modify the application to bind to the correct host and port.

### 2️⃣ Push to GitHub
Commit and push the latest changes to GitHub.

### 3️⃣ Deploy on Render
- Create a new web service on Render.
- Connect the repository and set the build and start commands.
- Deploy the API and obtain the public URL.

### 4️⃣ Test the Deployed API
Visit the deployment URL followed by `/docs` to access the API documentation.

---

## 📌 How to Use the API
- **Adding a Product:** Submit product details to the `/products/` endpoint.
- **Fetching Competitor Prices:** Call `/fetch-competitor-prices/` with a product ID.
- **Getting Optimized Prices:** Request `/optimized-price/` to receive AI-driven price recommendations.
- **Automating Updates:** Use `/update-competitor-prices/` to refresh competitor prices in the background.

---

## 📌 Contributing
Contributions are welcome! Feel free to submit PRs or report issues.

---
## 📌 License
MIT License. Free to use.
