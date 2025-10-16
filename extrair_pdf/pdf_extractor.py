from tarfile import fully_trusted_filter
import pdfplumber


# Função da extração do texto do PDF com o PDF Plumber
def extrair_texto_pdf(pdf_path):
    full_text = "" # variável em que vai ser armazenado o texto
    tables = [] # 


    with pdfplumber.open(pdf_path) as pdf: # abrindo o PDF
        for page in pdf.pages: # iterando as páginas
            full_text += page.extract_text() or "" # adicionando o texto à variável
            tables.extend(page.extract_tables()) # adicionando as tabelas à lista

    return full_text # retornando o texto completo

