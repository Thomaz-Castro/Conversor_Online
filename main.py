from flask import Flask, render_template, request, jsonify
from defs_copy import XXceRf697, ff7946

app = Flask(__name__)

def convert_visualg_to_c(codigo):
    # Implemente sua função de conversão de Visualg para C aqui
    # Substitua esse exemplo pela sua função real
    return XXceRf697(codigo)

def convert_c_to_visualg(codigo):
    # Implemente sua função de conversão de C para Visualg aqui
    # Substitua esse exemplo pela sua função real
    return ff7946(codigo)

@app.route('/')
def index():
    user_agent = request.user_agent.string
    if 'Mobile' in user_agent:  # Verifica se o usuário está usando um dispositivo móvel
        return render_template('index_mobile.html')
    else:
        return render_template('index.html')


@app.route('/converter', methods=['POST'])
def converter():
    data = request.get_json()
    codigo = data['codigo']
    conversion_type = data['conversionType']

    if conversion_type == 'visualgToC':
        converted_code = convert_visualg_to_c(codigo)
    elif conversion_type == 'cToVisualg':
        converted_code = convert_c_to_visualg(codigo)
    else:
        converted_code = "Tipo de conversão inválido"

    return jsonify({"convertedCode": converted_code})

if __name__ == '__main__':
    app.run(debug=False)
