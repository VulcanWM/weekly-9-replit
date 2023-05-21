from flask import Flask, render_template, request
from functions import first, second, questions, twovariablesequation, threevariablesequation, fourvariablesequation, slope_intercept
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/first")
def firstpage():
  return render_template("first.html")

@app.route("/first", methods=['POST', 'GET'])
def firstfunc():
  if request.method == 'POST':
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    func = first(a, b, c)
    if isinstance(func, (int, float)) == False:
      return render_template("first.html", error=func)
    else:
      answer = f"x is {str(func)} in {str(a)}x + {str(b)} = {str(c)}"
      return render_template("first.html", answer=answer)

@app.route("/second")
def secondpage():
  return render_template("second.html")

@app.route("/second", methods=['POST', 'GET'])
def secondfunc():
  if request.method == 'POST':
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    func = second(a, b, c, d)
    if isinstance(func, (int, float)) == False:
      return render_template("second.html", error=func)
    else:
      answer = f"x is {str(func)} in {str(a)}x + {str(b)} = {str(c)}x + {str(d)}"
      return render_template("second.html", answer=answer)

@app.route("/questions/easy")
def easyquestionpage():
  thequestion = questions("easy")
  return render_template("questions.html", equation=thequestion[2], question=thequestion[0], type="easy")

@app.route("/questions/hard")
def hardquestionpage():
  thequestion = questions("hard")
  return render_template("questions.html", equation=thequestion[2], question=thequestion[0], type="hard")

@app.route("/questions/medium")
def questionpage():
  thequestion = questions("medium")
  return render_template("questions.html", equation=thequestion[2], question=thequestion[0], type="medium")

@app.route("/answer/<equation>", methods=['POST', 'GET'])
def answerpage(equation):
  if request.method == 'POST':
    answer = first(equation.split(",")[0], equation.split(",")[1], equation.split(",")[2])
    guess = request.form['answer']
    try:
      if float(answer) == float(guess):
        return render_template("answer.html", status="You got it right!", word="Correct")
      else:
        return render_template("answer.html", status=f"You got it wrong! The answer was {str(answer)} and you wrote {str(guess)}", word="Wrong")
    except:
      return render_template("answer.html", status="You didn't enter a number as your answer", word="Error")

@app.route("/twovar")
def twovarpage():
  return render_template("twovar.html")

@app.route("/twovar", methods=['POST', 'GET'])
def twovarfunc():
  if request.method == 'POST':
    try:
      a = int(request.form['a'])
      b = int(request.form['b'])
      c = int(request.form['c'])
      d = int(request.form['d'])
      e = int(request.form['e'])
      f = int(request.form['f'])
      func = twovariablesequation([a, b], [d, e], [c, f])
      return render_template("twovar.html", answer=func)
    except Exception as e:
      e = str(e)
      if e.startswith("invalid literal"):
        return render_template("twovar.html", error="You didn't enter numbers!")
      else:
        return render_template("twovar.html", error=e)

@app.route("/threevar")
def threevarpage():
  return render_template("threevar.html")

@app.route("/threevar", methods=['POST', 'GET'])
def threevarfunc():
  if request.method == 'POST':
    try:
      a = int(request.form['a'])
      b = int(request.form['b'])
      c = int(request.form['c'])
      d = int(request.form['d'])
      e = int(request.form['e'])
      f = int(request.form['f'])
      g = int(request.form['g'])
      h = int(request.form['h'])
      i = int(request.form['i'])
      j = int(request.form['j'])
      k = int(request.form['k'])
      l = int(request.form['l'])
      func = threevariablesequation([a, b, c], [e, f, g], [i, j, k], [d,h, l])
      return render_template("threevar.html", answer=func)
    except Exception as e:
      e = str(e)
      if e.startswith("invalid literal"):
        return render_template("threevar.html", error="You didn't enter numbers!")
      else:
        return render_template("threevar.html", error=e)

@app.route("/fourvar")
def fourvarpage():
  return render_template("fourvar.html")

@app.route("/fourvar", methods=['POST', 'GET'])
def fourvarfunc():
  if request.method == 'POST':
    try:
      a = int(request.form['a'])
      b = int(request.form['b'])
      c = int(request.form['c'])
      d = int(request.form['d'])
      e = int(request.form['e'])
      f = int(request.form['f'])
      g = int(request.form['g'])
      h = int(request.form['h'])
      i = int(request.form['i'])
      j = int(request.form['j'])
      k = int(request.form['k'])
      l = int(request.form['l'])
      m = int(request.form['m'])
      n = int(request.form['n'])
      o = int(request.form['o'])
      p = int(request.form['p'])
      q = int(request.form['q'])
      r = int(request.form['r'])
      s = int(request.form['s'])
      t = int(request.form['t'])
      func = fourvariablesequation([a, b, c, d], [f, g, h, i], [k, l, m, n], [p, q, r, s], [e,j,o,t])
      return render_template("fourvar.html", answer=func)
    except Exception as e:
      e = str(e)
      if e.startswith("invalid literal"):
        return render_template("fourvar.html", error="You didn't enter numbers!")
      else:
        return render_template("fourvar.html", error=e)

@app.route("/slope_intercept")
def sipage():
  return render_template("slope_intercept.html")

@app.route("/slope_intercept", methods=['POST', 'GET'])
def sifunc():
  if request.method == 'POST':
    try:
      x1 = int(request.form['x1'])
      y1 = int(request.form['y1'])
      x2 = int(request.form['x2'])
      y2 = int(request.form['y2'])
      func = slope_intercept(x1, y1, x2, y2)
      answer = f"The equation for the line which goes through ({str(x1)}, {str(y1)}) and ({str(x2)}, {str(y2)}) is y = {str(func[0])}x + {str(func[1])}. The slope in the line is {str(func[0])} and the intercept is {str(func[1])}."
      return render_template("slope_intercept.html", answer=answer)
    except Exception as e:
      e = str(e)
      if e.startswith("invalid literal"):
        return render_template("slope_intercept.html", error="You didn't enter numbers!")
      else:
        return render_template("slope_intercept.html", error=e)
