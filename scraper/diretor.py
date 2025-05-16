from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def extrair_diretor(driver, url):
    diretor = "Diretor não encontrado"
    if url:
        driver.execute_script("window.open(arguments[0]);", url)
        driver.switch_to.window(driver.window_handles[1])

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            container = soup.find("div", class_="ipc-metadata-list-item__content-container")
            if container:
                links_diretores = container.find_all("a", href=True)
                nomes_diretores = [a.text.strip() for a in links_diretores if "/name/" in a["href"]]
                diretor = ", ".join(nomes_diretores) if nomes_diretores else diretor
        except Exception as e:
            print(f"Erro ao buscar diretor: {e}")
        finally:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    return diretor
