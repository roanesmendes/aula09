from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_desconto', methods=['POST'])
def calcular_desconto():
    if request.method == 'POST':
        preco = float(request.form['preco'])
        desconto = float(request.form['desconto'])
        
        preco_com_desconto = preco - (preco * (desconto / 100))

        return render_template('resultado.html', preco_com_desconto=preco_com_desconto)

if __name__ == '__main__':
    app.run(debug=True)
