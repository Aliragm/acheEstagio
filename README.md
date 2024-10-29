# acheEstagio - Web Scraping para Oportunidades de Estágio

Este projeto tem como objetivo centralizar e organizar oportunidades de estágio, coletando dados automaticamente de um site específico (em breve mais sites!). Utilizamos técnicas de web scraping com Python, Selenium, BeautifulSoup e Pandas.

## Status do Projeto
**Desenvolvimento em Andamento**: Novas funcionalidades serão implementadas em breve, incluindo filtros personalizáveis e parâmetros específicos para refinar a busca.

## Tecnologias Utilizadas
- **Python**: Linguagem principal
- **Selenium**: Automação de navegação e interação
- **BeautifulSoup**: Parsing e extração de dados HTML
- **Pandas**: Manipulação e armazenamento de dados

## Funcionalidades
- **Extração de Oportunidades**: Captura títulos e links das vagas.
- **Rolagem Automática**: A função `scroll_down` carrega mais conteúdo dinâmico.
- **Filtros de Estado**: Seleção de vagas por estado, com uma escolha interativa.
- **Filtros Personalizáveis** *Coming Soon*: Implementação de parâmetros customizados para buscas mais precisas.

## Observação sobre o Driver

Atualmente, o projeto utiliza o **SafariDriver**, mas essa escolha é temporária. O driver será alterado para o do **Google Chrome**, **Edge** ou **Firefox** nas futuras atualizações.

## Formato dos Resultados
Por enquanto, os resultados estão sendo gerados em uma tabela HTML salva na mesma pasta do projeto. No entanto, está em estudo a opção de exportar os dados para um arquivo **Excel** ou formato similar, proporcionando uma manipulação mais prática dos resultados.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias:
   ```bash
   pip install selenium beautifulsoup4 pandas
3. Baixe o driver da versão atual(https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)
4. Execute o script:
    ```bash
    python finder.py
