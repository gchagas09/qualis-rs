import PyPDF2
import shutil
import os
from unidecode import unidecode
import re


def verifica_arquivo_existe(nome_arquivo):
   return os.path.exists(nome_arquivo)

def encontrar_palavras_chave(texto, palavra_chave1, palavra_chave2):
    # Encontre todas as ocorrências das duas palavras-chave no texto
    padrao = re.compile(fr'\b({palavra_chave1}|{palavra_chave2})\b', re.IGNORECASE)
    ocorrencias = [match.start() for match in padrao.finditer(texto)]

    if len(ocorrencias) < 2:
        return False

    # Encontre a primeira ocorrência da primeira palavra-chave
    indice_palavra1 = ocorrencias[0]

    # Encontre a última ocorrência da segunda palavra-chave
    indice_palavra2 = ocorrencias[-1]

    # Determine a posição inicial e final do trecho de texto que você deseja retornar
    inicio = max(0, indice_palavra1 - 50)
    fim = min(len(texto), indice_palavra2 + 50)

    # Extraia o trecho de texto
    trecho = texto[inicio:fim]

    return trecho


def normaliza_texto(texto):
    texto_normalizado = " ".join(texto.split())
    texto_normalizado = texto_normalizado.lower()
    return texto_normalizado


def listar_arquivos_pdf(caminho_da_pasta):
    # Lista para armazenar nomes de arquivos PDF
    nomes_arquivos_pdf = []
    print(caminho_da_pasta)
    # Loop pelos arquivos na pasta
    for nome_arquivo in os.listdir(caminho_da_pasta):
        # Caminho completo do arquivo
        caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo)

        # Verifique se o arquivo é um arquivo PDF
        if nome_arquivo.endswith('.pdf') and os.path.isfile(caminho_completo):
            # Adicione o nome do arquivo à lista
            nomes_arquivos_pdf.append(nome_arquivo)

    return nomes_arquivos_pdf


def escrever_em_arquivo(nome_arquivo, texto):
    try:
        # Abre o arquivo no modo de append (acrescentar)
        with open(nome_arquivo, 'a') as arquivo:
            # Escreve a string no arquivo
            arquivo.write(texto)
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {str(e)}")

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
def find_keywords_in_pdf(pdf_file, relatory_file, palavras_chave, keywords, diretorio_se_contem, diretorio_se_nao_contem, pdf_file_name):
    # Abra o arquivo PDF
    global n_texto
    contem_algo = False
    pdf = PyPDF2.PdfReader(pdf_file)
    novo_caminho = diretorio_se_contem+"/"+pdf_file_name
    texto = "\n<h2>ARQUIVO:</h2> <a href='../"+novo_caminho+"' target=_blank>"+ pdf_file_name +"</a>\n"

    # Loop através de todas as páginas do PDF
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        page_text = page.extract_text()
        page_text = normaliza_texto(page_text)

        # Loop através das palavras-chave
        for keyword in keywords:
            keyword = keyword.lower()
            # Use expressões regulares para encontrar a palavra-chave e 50 palavras ao redor dela
            pattern = re.compile(r'.{0,50}\b' + re.escape(keyword) + r'\b.{0,50}', re.DOTALL | re.IGNORECASE)
            matches = pattern.findall(page_text)

            # Imprima os resultados
            if matches:
                texto = texto + "<h3>Nº: "+ str(n_texto) +" | <a href='../"+novo_caminho+"#page="+str(page_num+1)+"' target=_blank> Página: " + str(page_num+1) + "</a> | Palavra-chave: <strong>" + keyword + "</strong></h3>\n"
                contem_algo = True
                n_texto = n_texto+1
                for match in matches:
                    texto = texto + "<blockquote>"
                    texto = texto + match.strip()+"\n"
                    texto = texto + "</blockquote>"

    if contem_algo:
        texto = texto+"\n"+"<hr>"
        escrever_em_arquivo(relatory_file, texto)
        mover_arquivo_para_subdiretorio(pdf_file, diretorio_se_contem)
    elif not matches:
        mover_arquivo_para_subdiretorio(pdf_file, diretorio_se_nao_contem)


keywords=["prêmio por inovação",
"incentivo à eficiência organizacional",
"bonificação por mérito em inovação",
"reconhecimento por eficácia comunitária",
"promoção por impacto positivo",
"recompensa por liderança eficaz",
"gratificação por projetos comunitários",
"incentivo por resultados excepcionais",
"bonificação por excelência em projeto",
"reconhecimento por transformação organizacional",
"bonificação por projeto",
"reconhecimento por inovação",
"incentivo a projetos inovadores",
"promoção por liderança em projeto",
"gratificação por impacto organizacional",
"recompensa por melhorias significativas",
"incentivo por projeto de impacto",
"reconhecimento por melhorias comunitárias",
"bonificação por eficácia organizacional",
"promoção por mérito em projeto",
"incentivo à inovação organizacional",
"gratificação por projetos de alto impacto",
"reconhecimento por projetos estratégicos",
"bonificação por resultados significativos",
"promoção por projetos de sucesso",
"incentivo por liderança inovadora",
"gratificação por contribuição significativa",
"recompensa por projetos estratégicos",
"incentivo por melhorias na comunidade",
"reconhecimento por impacto comunitário"]
palavras_chave = ['atualizacao', 'trabalho', 'horario escolar', 'servidor', 'trabalhador', 'promocao', 'desempenho', 'merecimento', 'atualizaçao', 'promoçao', 'incentivo', 'qualificacao', 'qualificaçao', 'curso', 'capacitacao', 'capacitaçao']

caminho_da_pasta = 'files'
se_contem = "contem"
nao_contem = "nao_contem"
# Exemplo de uso da função
index = 'index.html'
texto = "<head><link rel='stylesheet' type='text/css' href='stylesheet.css' /></head>"

escrever_em_arquivo(index, texto)


nomes_arquivos_pdf = listar_arquivos_pdf(caminho_da_pasta)

n_texto = 1
lista_letras = []
for i in range (len(nomes_arquivos_pdf)):
    if(nomes_arquivos_pdf[i][0] not in lista_letras):
        lista_letras.append(nomes_arquivos_pdf[i][0])

if verifica_arquivo_existe("index.html"):
    for letra in lista_letras:
        texto = "<head><link rel='../stylesheet' type='text/css' href='stylesheet.css' /></head>"
        relatorio = "paginas/"+normaliza_texto(letra).lower()+".html"
        escrever_em_arquivo(relatorio, texto)
        texto = "<br><a href=" + relatorio + " target=_blank>Letra " + normaliza_texto(letra).lower() + "</a>"
        escrever_em_arquivo(index, texto)

for pdf_file in nomes_arquivos_pdf:
    relatorio = "paginas/"+normaliza_texto(pdf_file[0]).lower()+".html"
    file = caminho_da_pasta+"/"+pdf_file
    find_keywords_in_pdf(file, relatorio, palavras_chave, keywords, se_contem, nao_contem, pdf_file)
