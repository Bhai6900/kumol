from flask import Flask,render_template, request ,request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    return render_template('greet.html',name=request.form.get('name'))

  return render_template("index.html")

if __name__ =='__main__':
  app.run(host='0.0.0.0',debug=True)
