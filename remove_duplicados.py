import os
import shutil


def deletar_arquivos_repetidos(pasta1, pasta2):
    # Lista de arquivos na pasta1
    arquivos_pasta1 = os.listdir(pasta1)

    # Lista de arquivos na pasta2
    arquivos_pasta2 = os.listdir(pasta2)

    # Itera pelos arquivos na pasta2
    for arquivo_pasta2 in arquivos_pasta2:
        if arquivo_pasta2 in arquivos_pasta1:
            # Constrói o caminho completo do arquivo na pasta2
            caminho_arquivo_pasta2 = os.path.join(pasta2, arquivo_pasta2)

            # Remove o arquivo da pasta2
            os.remove(caminho_arquivo_pasta2)
            print(f"Arquivo {arquivo_pasta2} foi removido da pasta2.")


# Exemplo de uso da função
pasta2 = "contem"
pasta1 = "contem_antigo"
deletar_arquivos_repetidos(pasta1, pasta2)
