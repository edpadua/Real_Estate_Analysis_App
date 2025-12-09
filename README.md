![image](https://github.com/edpadua/Real_Estate_Analysis_App/blob/main/capture.gif)

# 🏡 Real Estate Analysis and Recommendation App

A full-stack project (Web + Data Science) built in Python that uses a Machine Learning model to estimate the **“Fair Price”** of a property based on its characteristics and provides a clear investment recommendation.

---

## ✨ Main Features

* **Price Prediction:** Uses a **Multiple Linear Regression** model (Scikit-learn) to calculate the expected market value (Fair Price) of a property.
* **Investment Recommendation:** Compares the user-provided sale price with the model’s predicted price, classifying the property as an **"Excellent Opportunity"**, **"Fair Price"**, or **"Overpriced"**.
* **Interactive Web Interface:** Presents data and results in a dynamic, user-friendly web dashboard built with **Streamlit**.
* **Model Transparency:** Displays the **Statistical Influence** of different features (Area, Bedrooms, Distance from City Center) on the final price.

---

## 🛠️ Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Main logic, data analysis, and back-end. |
| **Modeling** | Scikit-learn (Linear Regression) | Training the price prediction model. |
| **Web Framework** | Streamlit | Building the interactive web interface (Front-end). |
| **Data Handling** | Pandas & NumPy | Dataset simulation/loading and preprocessing. |
| **Packaging** | joblib | Saving and loading the trained model. |

---

## 🚀 How to Run the Project Locally

Follow the steps below to run the application on your machine.

### 1. Requirements

Make sure Python (version 3.8+) is installed.

### 2. Installing Dependencies

Create a `requirements.txt` file with the following libraries and install them:

```bash
# requirements.txt
pandas
numpy
scikit-learn
streamlit
joblib
