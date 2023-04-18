import shutil
import sqlite3
import os



def limpar():

    try:
        shutil.rmtree("media/")
        os.mkdir("media/")

    except:
        print("Pasta não localizada")
        os.mkdir("media/")

    conexao = sqlite3.connect('db.sqlite3')
    c = conexao.cursor()

    comando = 'DELETE FROM xmltoexcel_file WHERE id >= 0 '
    c.execute(comando)
    conexao.commit()

    comando = 'DELETE FROM importador_file WHERE id >= 0 '
    c.execute(comando)
    conexao.commit()

    comando = 'VACUUM'
    c.execute(comando)
    conexao.commit()


    c.close()
    conexao.close()
    print("Processo concluído")

limpar()
