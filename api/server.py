from flask import Flask, request, jsonify

import json, requests, time

app = Flask(__name__)

@app.route('/busca/cpf_cnpj/<id>', methods=['GET'])
def busca_cpf_cnpj(id):
    data = get_data_from_json()
    for item in data:
        if str(item['nu_CPFCNPJ']) == id:
            return jsonify({'empresa': item}), 200
    return "Erro: Empresa/Pessoa Fisica nao encontrada", 404

@app.route('/ranking/<ordem>', methods=['GET'])
def ranking(ordem):
    data = get_data_from_json()
    if ordem == "crescente":
        ranking = sorted(data, key=lambda k: k['confianca'])
        return jsonify({'ranking': ranking}), 200
    elif ordem == "decrescente":
        ranking = sorted(data, key=lambda k: k['confianca'], reverse=True)
        return jsonify({'ranking': ranking}), 200
    else:
        return "Erro: tipo de ordenacao invalida!", 404

@app.route('/incluir_nome/', methods=['GET'])
def include_name():
    data = get_data_from_json()
    for item in data:
        request_url = 'https://www.receitaws.com.br/v1/cnpj/' + str(item['nu_CPFCNPJ'])
        if 'nome' not in item:
            try:
                request = requests.get(request_url)
                nome = request.json()['nome']
                print nome
            except:
                return jsonify({'data': data}), 200
            try:
                item['nome'] = nome
            except:
                item['nome'] = None

    return jsonify({'data': data}), 200

def get_data_from_json():
    data_file = open('data/features.json', 'rb')
    data = json.load(data_file)['data']
    return data

if __name__ == '__main__':
    app.run()
