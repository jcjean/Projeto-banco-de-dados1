from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
db_config = {
    'host': 'mylibdatabase.c9bopnmijrhe.us-east-1.rds.amazonaws.com',
    'dbname': 'postgres',
    'user': 'libadmin',
    'password': 'libadmin',
    'port': '5432'}

def test_database_connection():
    try:
        conn = psycopg2.connect(**db_config)
        return True
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def execute_select_query(): 
    cursor = None
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # consulta na tabela livro
        cursor.execute("SELECT * FROM lib.livro")

        # recupera os resultados da consulta
        results = cursor.fetchall()

        return results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()


@app.route('/')     # para testar se foi feita a conexão ou não
def check_database_connection():
    if test_database_connection():
        return jsonify({"status": "Conexao bem-sucedida ao banco de dados PostgreSQL!"})
    else:
        return jsonify({"status": "Falha na conexão ao banco de dados PostgreSQL!"})

@app.route('/select')   # para rodar o select
def select_from_table():
    results = execute_select_query()
    if results is not None:
        return jsonify({"data": results})
    else:
        return jsonify({"error": "Erro ao executar a consulta."})

if __name__ == '__main__':
    app.run(debug=True)
