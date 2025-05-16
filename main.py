from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

from scraper.imdb import extrair_dados_filme
from scraper.diretor import extrair_diretor

def main():
    driver = webdriver.Chrome()
    url = "https://www.imdb.com/chart/top/"
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item'))
    )
    filmes = driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item')

    dados = []

    for filme in filmes:
        numero, titulo, ano, nota, duracao, link = extrair_dados_filme(filme)
        diretor = extrair_diretor(driver, link)

        print(f"{numero}. {titulo} ({ano}) - Nota: {nota} - Duração: {duracao} - Diretor: {diretor}")

        dados.append({
            "Rank": numero,
            "Título": titulo,
            "Ano": ano,
            "Nota": nota,
            "Duração": duracao,
            "Diretor": diretor
        })

    df = pd.DataFrame(dados)
    df.to_csv("imdb_top_250.csv", index=False, encoding='utf-8-sig')
    driver.quit()

if __name__ == "__main__":
    main()
