# Sales Prediction Web App — Project Report

## Overview

A machine learning web application that predicts product **Sales** based on three advertising channels — **TV**, **Radio**, and **Newspaper** — using a trained **Linear Regression** model served through a **Flask** web interface.

## Dataset

- **File:** `datasets/advertising.csv` (located in `Scikit-learn/datasets/`)
- **Features (inputs):** TV, Radio, Newspaper (advertising spend in $1000s)
- **Target (output):** Sales (in $1000s)

## Model Training

- **Algorithm:** Linear Regression (`sklearn.linear_model.LinearRegression`)
- **Trained in:** Jupyter notebook (`Scikit-learn/linear-regression.ipynb`)
- **Learned coefficients:**

  | Feature    | Coefficient |
  |------------|-------------|
  | TV         | 0.0545      |
  | Radio      | 0.1009      |
  | Newspaper  | 0.0043      |
  | Intercept  | 4.7141      |

- **Saved model:** `liner_regression_model.pkl` (via Python `pickle`)

## Web Application (`app.py`)

### Backend — Flask

- Loads the pickled model at startup: `pickle.load(open('liner_regression_model.pkl', 'rb'))`
- Single route `/` accepting **GET** (show form) and **POST** (run prediction)
- Reads form values `tv`, `radio`, `newspaper`, calls `model.predict([[tv, radio, news]])`, rounds result to 2 decimals
- Renders HTML via `render_template_string`

### Frontend — HTML/CSS/JavaScript

- **Dark AI-style theme:** gradient glow background, glassmorphism card with `backdrop-filter: blur()`
- **Gradient typography:** animated gradient text on the title
- **"AI Powered" badge** and footer credit
- **Inputs:** each feature has a range slider synced with a numeric input (live value display via JS `sync()` function)
- **Animated gradient button** with hover/active states
- **Result card:** fade-in animation, large gradient numbers showing predicted sales

## How to Run

```bash
cd train-models
pip install flask        # one-time setup
python app.py            # or: python3 app.py
```

Then open `http://127.0.0.1:5000` in a browser.

## Files

| File                          | Purpose                        |
|-------------------------------|--------------------------------|
| `train-models/app.py`         | Flask app + embedded HTML UI   |
| `train-models/liner_regression_model.pkl` | Trained model (pickle) |
| `Scikit-learn/linear-regression.ipynb`    | Model training notebook |
| `Scikit-learn/datasets/advertising.csv`   | Training dataset      |

## Key Concepts Covered

- Data loading with **pandas** (`read_csv`)
- Exploratory analysis & visualization (**matplotlib**, **seaborn**)
- Model training & evaluation (**scikit-learn**)
- Model persistence (**pickle**)
- Web deployment (**Flask**), form handling (`GET`/`POST`, `request.form`)
- Frontend design: CSS gradients, glassmorphism, sliders, vanilla JS
