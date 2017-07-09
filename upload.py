from flask import Flask, render_template, request
from werkzeug import secure_filename
import string
from without import *
from Resultado import *
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

      input = open(f.filename, "r")
      resultado=resultados(input)
      aparicoes=resultado.aparicoes
      return render_template("/result.html", aparicoes=aparicoes, numero=resultado.numero)


if __name__ == '__main__':
   app.run(debug = True)
