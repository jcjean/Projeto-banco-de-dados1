from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [] #Armazenando os usuarios na memoria

class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    data = request.json

    cpf = data['cpf']
    nome = data['nome']
    data_nascimento = data['data_nascimento']

    novoUsuario = Usuario(cpf, nome, data_nascimento)
    usuarios.append(novoUsuario)

    return jsonify({"msg": "Usuario adicionado!"})

@app.route('/get_usuario/<int:cpf>', methods=['GET'])
def get_usuario(cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return jsonify({
                "cpf": usuario.cpf,
                "nome": usuario.nome,
                "data_nascimento": usuario.data_nascimento
                })
    return jsonify({"msg": "Usuario nao encontrado!"}), 404

if __name__ == '__main__':
    app.run(debug=True)