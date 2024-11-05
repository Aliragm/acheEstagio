# acheEstagio - Web Scraping para Oportunidades de Estágio

Este projeto tem como objetivo centralizar e organizar oportunidades de estágio, coletando dados automaticamente de um site específico (em breve mais sites!). Utilizei técnicas de web scraping com Python, Selenium, BeautifulSoup e Pandas.

## Status do Projeto
**Desenvolvimento em Andamento**: Novas funcionalidades serão implementadas em breve, incluindo filtros personalizáveis e parâmetros específicos para refinar a busca.

## Tecnologias Utilizadas
- **Python**: Linguagem principal
- **Selenium**: Automação de navegação e interação
- **BeautifulSoup**: Parsing e extração de dados HTML
- **Pandas**: Manipulação e armazenamento de dados

## Funcionalidades
- **Extração de Oportunidades**: Captura títulos e links das vagas.
- **Filtros de Estado**: Seleção de vagas por estado, com uma escolha interativa.
- **Filtros Personalizáveis** *Coming Soon*: Implementação de parâmetros customizados para buscas mais precisas.

## Observação sobre o Driver

Atualmente, o projeto utiliza o **SafariDriver** e **EdgeDriver**, por enquanto, essas serão as escolhas do projeto, visto que são navegadores bem gerais. Para poder utilizar o projeto, baixe o driver do edge pelo link da seção *como executar* e coloque o arquivo executável na mesma pasta do projeto, para utilizar o driver do safari, ative a automatização do navegador pelas opções de desenvolvedor do safari. A utilização do Edge é mais rápida, pois, é utilizada em modo *headless*, coisa que não é feita com o safari.

## Formato dos Resultados
Por enquanto, os resultados estão sendo gerados em uma tabela HTML e um arquivo JSON salvos na mesma pasta do projeto. No entanto, está em estudo a opção de exportar os dados para um arquivo **Excel** ou formato similar, proporcionando uma manipulação mais prática dos resultados.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias:
   ```bash
   pip install selenium beautifulsoup4 pandas colorama
3. Baixe o driver da versão atual (https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) ou o driver do microsoft EDGE (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH#downloads)
4. Execute o script:
    ```bash
    python finder.py
