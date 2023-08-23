# Acompanhamento de Ações com Python e Power BI

Este repositório contém um projeto de acompanhamento de ações utilizando Python para a extração de dados financeiros e integração com o Power BI para a criação de um dashboard interativo. O objetivo desse projeto é permitir que os usuários possam acompanhar o desempenho de diferentes ações de maneira eficiente e visualmente atrativa.

<div align="center">
    <img src="https://github.com/catianemarinho/escola2/assets/97571709/915aa79d-5da3-4258-bd41-6be02cafa8cb">
</div>

## Funcionalidades

- Extração de Dados: Utilizamos a biblioteca `yfinance` para extrair dados financeiros de ações diretamente da internet. Isso inclui preço atual, máxima, mínima e outros indicadores relevantes.

- Pré-processamento: Os dados extraídos são pré-processados para garantir que estejam em um formato adequado para análise. Isso pode incluir tratamento de valores ausentes, cálculo de retornos ou outros indicadores personalizados.

- Integração com Power BI: Os dados pré-processados são importados para o Power BI, uma ferramenta de visualização de dados poderosa. O Power BI nos permite criar gráficos, tabelas e outros elementos visuais para construir um dashboard interativo.

- Criação de Dashboard: No Power BI, criamos um dashboard interativo que exibe os dados financeiros de forma clara e compreensível. Os usuários podem filtrar os dados por ação, período de tempo ou outros critérios, permitindo uma análise detalhada.

## Estrutura do Repositório

O repositório está organizado da seguinte maneira:

- `script.py`: Este arquivo contém o código em Python responsável por extrair e pré-processar os dados das ações utilizando a biblioteca `yfinance`.

- `dashboard_acoes`: Aqui você encontrará o arquivo do Power BI que contém o dashboard interativo criado com base nos dados extraídos. Este arquivo pode ser aberto no Power BI Desktop.

- `README.md`: O arquivo que você está lendo agora, fornecendo informações sobre o projeto, sua finalidade e instruções básicas de uso.

## Como Utilizar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Instale as bibliotecas necessárias. Você pode fazer isso executando o seguinte comando:

   ```bash
   pip install yfinance
3. Vá para a pasta e execute o script de extração de dados, por exemplo:
    ```bash
    piython script.py
4. Abra o arquivo power_bi_dashboard/dashboard.pbix usando o Power BI Desktop.
5. No Power BI Desktop, atualize a fonte de dados para refletir os dados extraídos no passo 3.
6. Explore o dashboard interativo criado no Power BI. Use filtros e gráficos para analisar o desempenho das ações ao longo do tempo.

## Contribuições

Contribuições para este projeto são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para enviar um pull request.

## Aviso Legal

Este projeto é apenas para fins educacionais e informativos. Não oferece aconselhamento financeiro nem recomendações de investimento. Sempre realize sua própria pesquisa antes de tomar decisões financeiras.

## Contato

- **mail**: cat.50@hotmail.com





