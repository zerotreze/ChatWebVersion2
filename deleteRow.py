import sqlite3

# Conectar ao banco de dados ou criar banco de dados
def connect(db_name='db.sqlite3'):
    conn = sqlite3.connect(db_name)
    return conn

# # Função para deletar uma linha
# def delete_row(user_id, table_name='chat_message'):
#     conn = connect()
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"DELETE FROM {table_name} WHERE user_id = ?", (user_id,))
#         conn.commit()
#         print(f"Linha com id {user_id} removida com sucesso.")
#     except sqlite3.Error as err:
#         print(f"Erro: {err}")
#     finally:
#         cursor.close()
#         conn.close()

# # Exemplo de uso
# delete_row(user_id=1)

def update_primary_key(conn, old_id, new_id):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE chat_message
            SET id = ?
            WHERE id = ?
        ''', (new_id, old_id))
        conn.commit()
        print(f"Chave primária alterada de {old_id} para {new_id} com sucesso.")
    except sqlite3.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()

def main():
    conn = connect()
    update_primary_key(conn, 1, 0)
    conn.close()

if __name__ == '__main__':
    main()