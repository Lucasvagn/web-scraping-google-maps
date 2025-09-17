# Web Scraper de Locadoras de Motos no Google Maps

Este é um script em Python que automatiza a busca e a coleta de dados de locadoras de motos em São Paulo, usando o Google Maps como fonte. O objetivo é extrair informações como **nome, endereço e telefone** das empresas listadas.

## Funcionalidades

- Acessa automaticamente o Google Maps.
- Realiza uma busca pelo termo: `"locadoras de motos em São Paulo"`.
- Extrai informações como **nome, endereço e telefone** dos resultados.
- Rola a página para carregar mais resultados.
- Salva os dados coletados em um arquivo Excel (`empresas_google_maps.xlsx`).

## Requisitos

Você precisa ter as seguintes bibliotecas instaladas no seu ambiente Python:

```bash
pip install pandas playwright
playwright install
💡 O segundo comando (playwright install) é necessário para instalar os navegadores usados pela automação.

Como Usar
Baixe o arquivo main.py para o seu computador.

Abra o terminal na pasta onde o arquivo foi salvo.

Execute o script com o comando:

bash
Copiar código
python main.py
O navegador será aberto automaticamente e a automação vai iniciar.
Ao final, um arquivo Excel com os dados será criado na mesma pasta.

yaml
Copiar código
