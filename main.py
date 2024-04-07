from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Função para conectar ao banco de dados PostgreSQL
def conectar_bd():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='senha.100',
        host='my-database.cnu4266qsk28.us-east-1.rds.amazonaws.com',
        port='5432'
    )
    conn.set_session(autocommit=True)
    return conn


# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios(): 
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clinica.Usuario')
    usuarios = cur.fetchall()
    conn.close()
    usuarios_list = []
    for usuario in usuarios:
        usuario_dict = {
            'cpf': usuario[0],
            'Cargo': usuario[1],
            'Nome': usuario[2]
        }
        usuarios_list.append(usuario_dict)
    return jsonify(usuarios_list)

# Rota para buscar um usuário por CPF
@app.route('/usuarios/<int:cpf>', methods=['GET'])
def buscar_usuario(cpf): 
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clinica.Usuario WHERE cpf = %s', (cpf,))
    usuario = cur.fetchone()
    conn.close()
    if usuario:
        colunas = [desc[0] for desc in cur.description]
        usuario_dict = dict(zip(colunas, usuario))
        return jsonify(usuario_dict)
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404


# Rota para criar um novo usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario(): 
    novo_usuario = request.json
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('INSERT INTO clinica.Usuario (cpf, cargo, nome) VALUES (%s, %s, %s)',
                (novo_usuario['cpf'], novo_usuario['cargo'], novo_usuario['nome']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário criado com sucesso'}), 201

# Rota para atualizar um usuário
@app.route('/usuarios/<int:cpf>', methods=['PUT'])
def atualizar_usuario(cpf): 
    usuario_atualizado = request.json
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('UPDATE clinica.Usuario SET cargo = %s, nome = %s WHERE cpf = %s', 
                (usuario_atualizado['cargo'], usuario_atualizado['nome'], cpf))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário atualizado com sucesso'})

# Rota para deletar um usuário
@app.route('/usuarios/<int:cpf>', methods=['DELETE'])
def deletar_usuario(cpf): 
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('DELETE FROM clinica.Usuario WHERE cpf = %s', (cpf,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Usuário deletado com sucesso'})


# Rota para listar todas as enfermidades
@app.route('/enfermidades', methods=['GET'])
def listar_enfermidades():
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clinica.Enfermidade')
    enfermidades = cur.fetchall()
    conn.close()
    enfermidades_list = []
    for enfermidade in enfermidades:
        enfermidade_dict = {
            'nome': enfermidade[0],
            'codigo_cid': enfermidade[1]
        }
        enfermidades_list.append(enfermidade_dict)
    return jsonify(enfermidade_dict)

# Rota para buscar uma enfermidade por Código CID
@app.route('/enfermidades/<string:codigo_cid>', methods=['GET'])
def buscar_enfermidade(codigo_cid):
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clinica.Enfermidade WHERE codigo_cid = %s', (codigo_cid,))
    enfermidade = cur.fetchone()
    conn.close()
    if enfermidade:
        colunas = [desc[0] for desc in cur.description]
        enfermidade_dict = dict(zip(colunas, enfermidade))
        return jsonify(enfermidade_dict)
    else:
        return jsonify({'mensagem': 'Enfermidade não encontrada'}), 404

# Rota para criar uma nova enfermidade
@app.route('/enfermidades', methods=['POST'])
def criar_enfermidade():
    nova_enfermidade = request.json
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('INSERT INTO clinica.Enfermidade (nome, codigo_cid) VALUES (%s, %s)',
                (nova_enfermidade['nome'], nova_enfermidade['codigo_cid']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Enfermidade criada com sucesso'}), 201

# Rota para atualizar uma enfermidade
@app.route('/enfermidades/<string:codigo_cid>', methods=['PUT'])
def atualizar_enfermidade(codigo_cid):
    enfermidade_atualizada = request.json
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('UPDATE clinica.Enfermidade SET nome = %s WHERE codigo_cid = %s', 
                (enfermidade_atualizada['nome'], codigo_cid))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Enfermidade atualizada com sucesso'})

# Rota para deletar uma enfermidade
@app.route('/enfermidades/<string:codigo_cid>', methods=['DELETE'])
def deletar_enfermidade(codigo_cid):
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('DELETE FROM clinica.Enfermidade WHERE codigo_cid = %s', (codigo_cid,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Enfermidade deletada com sucesso'})


# Rota para listar todas as consultas
@app.route('/consultas', methods=['GET'])
def listar_consultas():
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clinica.Consulta')
    consultas = cur.fetchall()
    conn.close()
    consulta_list = []
    for consulta in consultas:
        consulta_dict = {
            'data_consulta': consulta[0],
            'id_consulta': consulta[1],
            'id_equipe': consulta[2],
            'id_prontuario': consulta[3],
            'id_procedimentos': consulta[4],
            'id_solicitacao': consulta[5],
            'id_paciente': consulta[6],
            'id_receituario': consulta[7]
        }
        consulta_list.append(consulta_dict)
    return jsonify(consulta_list)

# Rota para buscar uma consulta por ID
@app.route('/consultas/<string:id_consulta>', methods=['GET'])
def buscar_consulta(id_consulta):
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('SELECT * FROM clinica.Consulta WHERE id_consulta = %s', (id_consulta,))
    consulta = cur.fetchone()
    conn.close()
    if consulta:
        colunas = [desc[0] for desc in cur.description]
        consulta_dict = dict(zip(colunas, consulta))
        return jsonify(consulta_dict)
    else:
        return jsonify({'mensagem': 'Consulta não encontrada'}), 404

# Rota para criar uma nova consulta
@app.route('/consultas', methods=['POST'])
def criar_consulta():
    nova_consulta = request.json
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('INSERT INTO clinica.Consulta (data_consulta, id_consulta, id_equipe, id_prontuario, id_procedimentos, id_solicitacao, id_paciente, id_receituario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (nova_consulta['data_consulta'], nova_consulta['id_consulta'], nova_consulta['id_equipe'], nova_consulta['id_prontuario'], nova_consulta['id_procedimentos'], nova_consulta['id_solicitacao'], nova_consulta['id_paciente'], nova_consulta['id_receituario']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Consulta criada com sucesso'}), 201

# Rota para atualizar uma consulta
@app.route('/consultas/<string:id_consulta>', methods=['PUT'])
def atualizar_consulta(id_consulta):
    consulta_atualizada = request.json
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('UPDATE clinica.Consulta SET data_consulta = %s, id_equipe = %s, id_prontuario = %s, id_procedimentos = %s, id_solicitacao = %s, id_paciente = %s, id_receituario = %s WHERE id_consulta = %s', 
                (consulta_atualizada['data_consulta'], consulta_atualizada['id_equipe'], consulta_atualizada['id_prontuario'], consulta_atualizada['id_procedimentos'], consulta_atualizada['id_solicitacao'], consulta_atualizada['id_paciente'], consulta_atualizada['id_receituario'], id_consulta))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Consulta atualizada com sucesso'})

# Rota para deletar uma consulta
@app.route('/consultas/<string:id_consulta>', methods=['DELETE'])
def deletar_consulta(id_consulta):
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute('DELETE FROM clinica.Consulta WHERE id_consulta = %s', (id_consulta,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Consulta deletada com sucesso'})



if __name__ == '__main__':
    app.run(debug=True)
