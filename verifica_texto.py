import fitz

import shutil
import os

def listar_arquivos_pdf(caminho_da_pasta):
    # Lista para armazenar nomes de arquivos PDF
    nomes_arquivos_pdf = []

    # Loop pelos arquivos na pasta
    for nome_arquivo in os.listdir(caminho_da_pasta):
        # Caminho completo do arquivo
        caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo)

        # Verifique se o arquivo é um arquivo PDF
        if nome_arquivo.endswith('.pdf') and os.path.isfile(caminho_completo):
            # Adicione o nome do arquivo à lista
            nomes_arquivos_pdf.append(nome_arquivo)

    return nomes_arquivos_pdf


def mover_arquivo_para_subdiretorio(nome_arquivo, subdiretorio):
    # Verifica se o arquivo existe
    if not os.path.isfile(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' não existe.")
        return

    # Verifica se o subdiretório existe; se não, cria o subdiretório
    if not os.path.exists(subdiretorio):
        os.makedirs(subdiretorio)

    # Obtém o caminho completo para o novo local do arquivo
    novo_caminho = os.path.join(subdiretorio, os.path.basename(nome_arquivo))

    try:
        # Move o arquivo para o subdiretório
        shutil.move(nome_arquivo, novo_caminho)
        print(f"Arquivo '{nome_arquivo}' movido para '{novo_caminho}' com sucesso.")
    except Exception as e:
        print(f"Erro ao mover o arquivo: {str(e)}")


def verifica_pdf_texto_ou_imagens(nome_arquivo, nm):
    try:
        pdf_documento = fitz.open(nome_arquivo)
        num_paginas = len(pdf_documento)

        texto_encontrado = False

        for pagina_num in range(num_paginas):
            pagina = pdf_documento[pagina_num]
            texto_pagina = pagina.get_text()

            if texto_pagina.strip():
                texto_encontrado = True
                break

        pdf_documento.close()

        if texto_encontrado:
            print(f"Arquivo {nome_arquivo} contem texto")
            mover_arquivo_para_subdiretorio(caminho, "files/com_texto")
        else:
            print(f"Arquivo {nome_arquivo} nao contem texto")
            mover_arquivo_para_subdiretorio(caminho, "files/so_imagens")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

caminho_da_pasta = "files"

nomes_arquivos_pdf = listar_arquivos_pdf(caminho_da_pasta)

for nome_arquivo_pdf in nomes_arquivos_pdf:
    caminho = "files/"+nome_arquivo_pdf
    print(nome_arquivo_pdf)
    verifica_pdf_texto_ou_imagens(caminho, nome_arquivo_pdf)
