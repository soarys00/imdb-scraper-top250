# IMDb Top 250 Scraper

Este é um projeto em Python que coleta dados dos 250 melhores filmes do site IMDb.  
Ele utiliza Selenium, BeautifulSoup e pandas para extrair os dados e salvar em um arquivo CSV.

---

## Tecnologias usadas

- Python 3
- Selenium
- BeautifulSoup (bs4)
- pandas

---

## Funcionalidades

- Coleta título, ano, nota, duração e diretor de cada filme.
- Exporta os dados para o arquivo `imdb_top_250.csv`.

---

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/soarys00/imdb-scraper.git
cd imdb-scraper
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script:

```bash
python main.py
```
