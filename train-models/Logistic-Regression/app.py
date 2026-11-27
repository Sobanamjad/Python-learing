
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template_string, request

BASE = Path(__file__).resolve().parent

try:
    model = joblib.load(BASE / "churn_model.pkl")
    scaler = joblib.load(BASE / "scaler.pkl")
    encoders = joblib.load(BASE / "encoders.pkl")
except FileNotFoundError as e:
    raise SystemExit(
        f"Model file not found: {e.filename}\n"
        "Notebook mein joblib.dump wale cells chalayein aur .pkl files is app.py ke folder mein rakhein."
    )

app = Flask(__name__)

# Order must match the columns the scaler was fitted on.
FEATURES = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
    "PhoneService", "MultipleLines", "Contract", "TotalCharges",
]


def pretty(col, value):
    """Display label for an encoder class."""
    if col == "SeniorCitizen":
        return {"0": "No", "1": "Yes"}.get(str(value), str(value))
    return str(value)


# {column: [(index, label), ...]}: the form sends the index, the server maps it back.
OPTIONS = {
    col: [(i, pretty(col, v)) for i, v in enumerate(enc.classes_)]
    for col, enc in encoders.items()
}


@app.get("/")
def home():
    return render_template_string(PAGE, options=OPTIONS)


@app.post("/predict")
def predict():
    data = request.get_json(silent=True) or {}
    row = {}

    try:
        for col, enc in encoders.items():
            idx = int(data[col])
            row[col] = enc.classes_[idx]
        row["tenure"] = int(data["tenure"])
        row["TotalCharges"] = float(data["TotalCharges"])
    except (KeyError, ValueError, TypeError, IndexError):
        return jsonify(error="Form ki koi value galat ya missing hai. Sab fields check karein."), 400

    if not (0 <= row["tenure"] <= 100) or row["TotalCharges"] < 0:
        return jsonify(error="Tenure 0 se 100 ke beech aur Total Charges 0 ya zyada hona chahiye."), 400

    df1 = pd.DataFrame([row])[FEATURES]
    for col, enc in encoders.items():
        df1[col] = enc.transform(df1[col])
    scaled = scaler.transform(df1)

    prob = float(model.predict_proba(scaled)[0][1])  # class 1 = Churn
    churn = bool(model.predict(scaled)[0] == 1)
    risk = "low" if prob < 0.30 else "medium" if prob < 0.60 else "high"

    return jsonify(churn=churn, probability=prob, risk=risk)


PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Customer Churn Predictor</title>
<style>
  :root {
    --bg: #e9eef2;
    --surface: #ffffff;
    --ink: #12202e;
    --muted: #55677a;
    --line: #c7d2dc;
    --accent: #0f5c8e;
    --accent-ink: #ffffff;
    --low: #1b7f5c;
    --medium: #a86a0b;
    --high: #b3261e;
    --off: #d5dde4;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #0e161e;
      --surface: #16212c;
      --ink: #e6edf3;
      --muted: #9aa9b7;
      --line: #2a3846;
      --accent: #5aa9e6;
      --accent-ink: #08131c;
      --low: #4cc194;
      --medium: #e0a43a;
      --high: #ff7b72;
      --off: #2a3846;
      color-scheme: dark;
    }
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: "Segoe UI", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
  }
  main {
    max-width: 960px;
    margin: 0 auto;
    padding: 40px 20px 56px;
  }
  h1 { font-size: 2rem; line-height: 1.15; margin: 0 0 8px; letter-spacing: -0.01em; }
  .lead { color: var(--muted); margin: 0 0 28px; max-width: 56ch; }

  .layout { display: grid; grid-template-columns: 1.4fr 1fr; gap: 20px; align-items: start; }
  @media (max-width: 760px) { .layout { grid-template-columns: 1fr; } }

  form, .result {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 24px;
  }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 480px) { .grid { grid-template-columns: 1fr; } }

  label { display: block; font-size: 0.875rem; font-weight: 600; margin-bottom: 6px; }
  select, input {
    width: 100%;
    font: inherit;
    color: var(--ink);
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 9px 10px;
  }
  select:focus-visible, input:focus-visible, button:focus-visible {
    outline: 3px solid var(--accent);
    outline-offset: 2px;
  }

  button {
    width: 100%;
    margin-top: 22px;
    font: inherit;
    font-weight: 600;
    color: var(--accent-ink);
    background: var(--accent);
    border: 0;
    border-radius: 6px;
    padding: 12px 16px;
    cursor: pointer;
  }
  button:disabled { opacity: 0.6; cursor: wait; }

  .result { position: sticky; top: 20px; min-height: 260px; }
  .empty { color: var(--muted); margin: 0; }

  .bars { display: flex; align-items: flex-end; gap: 6px; height: 64px; margin-bottom: 16px; }
  .bars span { width: 14px; border-radius: 3px; background: var(--off); }
  .bars span:nth-child(1) { height: 20%; }
  .bars span:nth-child(2) { height: 40%; }
  .bars span:nth-child(3) { height: 60%; }
  .bars span:nth-child(4) { height: 80%; }
  .bars span:nth-child(5) { height: 100%; }
  .bars span.on { background: var(--tone); }

  .pct { font-size: 3rem; font-weight: 700; line-height: 1; color: var(--tone); font-variant-numeric: tabular-nums; }
  .verdict { font-size: 1.125rem; font-weight: 600; margin: 8px 0 4px; }
  .note { color: var(--muted); font-size: 0.9rem; margin: 0; }
  .error { color: var(--high); margin: 0; font-weight: 600; }

  footer { margin-top: 28px; color: var(--muted); font-size: 0.85rem; }

  @media (prefers-reduced-motion: no-preference) {
    .bars span { transition: background-color 0.25s ease; }
  }
</style>
</head>
<body>
<main>
  <h1>Will this customer stay?</h1>
  <p class="lead">Enter the customer's plan details. The model estimates how likely they are to cancel their service.</p>

  <div class="layout">
    <form id="form" autocomplete="off">
      <div class="grid">
        <div>
          <label for="gender">Gender</label>
          <select id="gender" name="gender">
            {% for i, label in options["gender"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="SeniorCitizen">Senior citizen</label>
          <select id="SeniorCitizen" name="SeniorCitizen">
            {% for i, label in options["SeniorCitizen"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="Partner">Has a partner</label>
          <select id="Partner" name="Partner">
            {% for i, label in options["Partner"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="Dependents">Has dependents</label>
          <select id="Dependents" name="Dependents">
            {% for i, label in options["Dependents"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="PhoneService">Phone service</label>
          <select id="PhoneService" name="PhoneService">
            {% for i, label in options["PhoneService"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="MultipleLines">Multiple lines</label>
          <select id="MultipleLines" name="MultipleLines">
            {% for i, label in options["MultipleLines"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="Contract">Contract</label>
          <select id="Contract" name="Contract">
            {% for i, label in options["Contract"] %}<option value="{{ i }}">{{ label }}</option>{% endfor %}
          </select>
        </div>
        <div>
          <label for="tenure">Tenure (months)</label>
          <input id="tenure" name="tenure" type="number" min="0" max="100" step="1" value="1" required>
        </div>
        <div>
          <label for="TotalCharges">Total charges</label>
          <input id="TotalCharges" name="TotalCharges" type="number" min="0" step="0.01" value="29.85" required>
        </div>
      </div>
      <button id="submit" type="submit">Predict churn</button>
    </form>

    <section class="result" aria-live="polite" id="result">
      <p class="empty">Fill in the form and select Predict churn to see the result here.</p>
    </section>
  </div>

  <footer>Logistic Regression model trained on the Telco customer churn dataset.</footer>
</main>

<script>
  const form = document.getElementById("form");
  const btn = document.getElementById("submit");
  const out = document.getElementById("result");

  const TONE = { low: "var(--low)", medium: "var(--medium)", high: "var(--high)" };
  const LIT = { low: 1, medium: 3, high: 5 };

  function showError(msg) {
    out.innerHTML = "";
    const p = document.createElement("p");
    p.className = "error";
    p.textContent = msg;
    out.appendChild(p);
  }

  function showResult(r) {
    const lit = LIT[r.risk];
    let bars = "";
    for (let i = 1; i <= 5; i++) bars += '<span class="' + (i <= lit ? "on" : "") + '"></span>';
    const pct = (r.probability * 100).toFixed(1);
    const verdict = r.churn ? "Likely to churn" : "Likely to stay";
    const note = r.risk === "high"
      ? "High risk. Consider reaching out with a retention offer."
      : r.risk === "medium"
        ? "Moderate risk. Worth keeping an eye on."
        : "Low risk of cancelling.";

    out.style.setProperty("--tone", TONE[r.risk]);
    out.innerHTML =
      '<div class="bars" aria-hidden="true">' + bars + "</div>" +
      '<div class="pct">' + pct + "%</div>" +
      '<div class="verdict">' + verdict + "</div>" +
      '<p class="note">' + note + "</p>";
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    btn.disabled = true;
    btn.textContent = "Predicting\u2026";
    try {
      const payload = Object.fromEntries(new FormData(form).entries());
      const res = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      if (!res.ok) showError(data.error || "Something went wrong. Try again.");
      else showResult(data);
    } catch (err) {
      showError("Could not reach the server. Make sure app.py is still running.");
    } finally {
      btn.disabled = false;
      btn.textContent = "Predict churn";
    }
  });
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)