from selenium.webdriver.common.by import By

def extrair_dados_filme(elemento):
    try:
        raw_titulo = elemento.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text.strip()
        numero, titulo = raw_titulo.split(". ", 1)
    except:
        numero, titulo = "?", "Título não encontrado"

    try:
        nota = elemento.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text.strip()
    except:
        nota = "Nota não encontrada"

    ano, duracao = "Ano não encontrado", "Duração não encontrada"
    try:
        metadatas = elemento.find_elements(By.CSS_SELECTOR, 'span.cli-title-metadata-item')
        for item in metadatas:
            texto = item.text.strip()
            if "h" in texto or "m" in texto:
                duracao = texto
            elif texto.isdigit() and len(texto) == 4:
                ano = texto
    except:
        pass

    try:
        link = elemento.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        link = None

    return numero, titulo, ano, nota, duracao, link

