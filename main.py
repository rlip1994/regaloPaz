from flask import Flask, redirect, request, render_template
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/", methods=['POST'])
def search():
    webbrowser.open_new_tab('http://siabuc.asamblea.go.cr/CatalogoAsamblea/home/BusquedaSimple?SearchString=ley+'+request.form['text'])
    webbrowser.open_new_tab('http://www.pgrweb.go.cr/scij/main.aspx')
    return redirect('http://www.asamblea.go.cr/Centro_de_Informacion/Consultas_SIL/Pginas/Detalle%20Leyes.aspx?Numero_Ley='+request.form['text'])
    
if __name__ == "__main__":
    app.run(debug=True)
