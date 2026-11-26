import pickle
from flask import Flask, render_template_string, request

app = Flask(__name__)
model = pickle.load(open('liner_regression_model.pkl', 'rb'))

# Frontend 
HTML = """<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Sales Predictor</title>
<style>
  * { box-sizing: border-box; font-family: 'Segoe UI', 'Inter', Arial, sans-serif; margin: 0; }
  body {
    min-height: 100vh;
    display: flex; align-items: center; justify-content: center;
    background: #0a0a14;
    background-image:
      radial-gradient(ellipse 80% 60% at 20% 10%, rgba(99,102,241,.25), transparent),
      radial-gradient(ellipse 60% 50% at 80% 90%, rgba(168,85,247,.18), transparent),
      radial-gradient(ellipse 50% 40% at 60% 40%, rgba(34,211,238,.12), transparent);
    padding: 24px;
  }
  .card {
    width: 420px; padding: 44px 40px;
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.1);
    border-radius: 24px;
    backdrop-filter: blur(20px);
    box-shadow: 0 30px 80px rgba(0,0,0,.5),
                inset 0 1px 0 rgba(255,255,255,.08);
  }
  .badge {
    display: inline-block; padding: 5px 14px; margin-bottom: 18px;
    font-size: 12px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase;
    color: #67e8f9; background: rgba(34,211,238,.1);
    border: 1px solid rgba(34,211,238,.25); border-radius: 999px;
  }
  h1 {
    font-size: 30px; font-weight: 800; color: #fff;
    background: linear-gradient(90deg, #a5b4fc, #67e8f9, #f0abfc);
    -webkit-background-clip: text; background-clip: text; color: transparent;
    margin-bottom: 8px;
  }
  p.sub { color: rgba(255,255,255,.5); font-size: 14px; margin-bottom: 32px; }

  .field { margin-bottom: 20px; }
  .field-head {
    display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;
  }
  label { font-size: 14px; font-weight: 600; color: rgba(255,255,255,.85); }
  .val { font-size: 13px; color: #67e8f9; font-weight: 600; font-variant-numeric: tabular-nums; }
  input[type=range] {
    width: 100%; height: 6px; -webkit-appearance: none; appearance: none;
    background: rgba(255,255,255,.12); border-radius: 999px; outline: none;
  }
  input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none; width: 18px; height: 18px; border-radius: 50%;
    background: linear-gradient(135deg, #6366f1, #22d3ee);
    border: 2px solid #fff; cursor: pointer;
    box-shadow: 0 0 12px rgba(99,102,241,.7);
  }
  input[type=range]::-moz-range-thumb {
    width: 18px; height: 18px; border-radius: 50%;
    background: linear-gradient(135deg, #6366f1, #22d3ee);
    border: 2px solid #fff; cursor: pointer;
  }
  input[type=number] {
    width: 100%; padding: 12px 14px; font-size: 15px;
    background: rgba(255,255,255,.06); color: #fff;
    border: 1px solid rgba(255,255,255,.12); border-radius: 12px; outline: none;
    transition: border-color .2s, box-shadow .2s;
  }
  input[type=number]:focus {
    border-color: #6366f1;
    box-shadow: 0 0 0 3px rgba(99,102,241,.25);
  }
  .row { display: flex; align-items: center; gap: 14px; }
  .row input[type=range] { flex: 1; }
  .row input[type=number] { width: 96px; text-align: center; }

  button {
    width: 100%; margin-top: 30px; padding: 15px;
    font-size: 16px; font-weight: 700; letter-spacing: .02em;
    color: #fff; border: none; border-radius: 14px; cursor: pointer;
    background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
    background-size: 200% 200%;
    animation: grad 6s ease infinite;
    box-shadow: 0 10px 30px rgba(168,85,247,.35);
    transition: transform .15s, box-shadow .2s;
  }
  @keyframes grad {
    0%,100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  button:hover { transform: translateY(-2px); box-shadow: 0 14px 40px rgba(168,85,247,.5); }
  button:active { transform: scale(.97); }

  .result {
    margin-top: 26px; padding: 22px; border-radius: 16px;
    background: linear-gradient(135deg, rgba(99,102,241,.15), rgba(34,211,238,.1));
    border: 1px solid rgba(99,102,241,.35);
    text-align: center;
    animation: fadein .5s ease;
  }
  @keyframes fadein { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
  .result .label { font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: rgba(255,255,255,.5); }
  .result .value {
    font-size: 36px; font-weight: 800; margin-top: 4px;
    background: linear-gradient(90deg, #a5b4fc, #67e8f9);
    -webkit-background-clip: text; background-clip: text; color: transparent;
    font-variant-numeric: tabular-nums;
  }
  .result .unit { font-size: 14px; color: rgba(255,255,255,.5); font-weight: 400; }

  .footer { margin-top: 22px; text-align: center; font-size: 11px; color: rgba(255,255,255,.3); }
</style>
</head>
<body>
  <div class="card">
    <span class="badge">AI Powered</span>
    <h1>Sales Predictor</h1>
    <p class="sub">Linear Regression inference engine</p>

    <form method="post">
      <div class="field">
        <div class="field-head">
          <label for="tv">TV Advertising</label>
          <span class="val" id="tvv">0</span>
        </div>
        <div class="row">
          <input type="range" id="tvR" min="0" max="300" step="0.5" value="150"
                 oninput="sync('tv', this.value)">
          <input type="number" id="tv" name="tv" step="0.1" min="0" value="150">
        </div>
      </div>

      <div class="field">
        <div class="field-head">
          <label for="radio">Radio Advertising</label>
          <span class="val" id="radiov">0</span>
        </div>
        <div class="row">
          <input type="range" id="radioR" min="0" max="50" step="0.5" value="20"
                 oninput="sync('radio', this.value)">
          <input type="number" id="radio" name="radio" step="0.1" min="0" value="20">
        </div>
      </div>

      <div class="field">
        <div class="field-head">
          <label for="newspaper">Newspaper Advertising</label>
          <span class="val" id="newsv">0</span>
        </div>
        <div class="row">
          <input type="range" id="newsR" min="0" max="100" step="0.5" value="30"
                 oninput="sync('newspaper', this.value)">
          <input type="number" id="newspaper" name="newspaper" step="0.1" min="0" value="30">
        </div>
      </div>

      <button type="submit">Run Prediction</button>
    </form>

    {% if result is not none %}
    <div class="result">
      <div class="label">Predicted Sales</div>
      <div class="value">{{ result }} <span class="unit">$1000s</span></div>
    </div>
    {% endif %}

    <div class="footer">sklearn LinearRegression &middot; Flask</div>
  </div>

<script>
  function sync(name, val) {
    document.getElementById(name).value = val;
    document.getElementById(name + 'v').innerText = val;
    const r = document.getElementById(name + 'R');
    if (+r.value !== +val) r.value = val;
  }
  ['tv','radio','newspaper'].forEach(n => {
    document.getElementById(n).addEventListener('input', e => sync(n, e.target.value));
    sync(n, document.getElementById(n).value);
  });
</script>
</body>
</html>"""


# Decorator
@app.route('/', methods=['GET','POST'])
# Fuction
def index():
    result = None
    # Condition
    if request.method == 'POST':
    # Prediction Values
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        news = float(request.form['newspaper'])
        # Model now the order
        result = round(model.predict([[tv, radio, news]])[0], 2)
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)