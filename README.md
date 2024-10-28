# Projeto acheEstagio - Web Scraping para Oportunidades de Estágio

Este projeto tem como objetivo reunir e organizar oportunidades de estágio disponíveis em um site específico, utilizando técnicas de web scraping com Python, Selenium e BeautifulSoup.

## Status do Projeto

🔄 **Desenvolvimento em Andamento**  
Este projeto está em sua fase inicial. Funcionalidades adicionais e melhorias serão implementadas nas próximas versões.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Selenium**: Para automação do navegador e interação com páginas da web.
- **BeautifulSoup**: Para parsing e extração de dados HTML.
- **Pandas**: Para manipulação e armazenamento de dados.

## Funcionalidades

- **Extração de Oportunidades**: O projeto permite a extração de títulos e links de oportunidades de estágio disponíveis na página especificada.
- **Rolagem Automática**: A função de rolagem automática permite carregar mais conteúdo dinamicamente enquanto navega na página.
- **Filtros e Parâmetros**: **Coming Soon**: Implementação de filtros e parâmetros passados pelo usuário para refinar a busca por oportunidades.

## Observação sobre o Driver

Atualmente, o projeto utiliza o **SafariDriver**, mas essa escolha é temporária. O driver será alterado para o do **Google Chrome** ou **Edge** nas futuras atualizações.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias:
   ```bash
   pip install selenium beautifulsoup4 pandas
3. Baixe o driver da versão atual(https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)
4. Execute o script:
    ```bash
    python finder.py
