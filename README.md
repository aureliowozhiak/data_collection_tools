# Data collection tools
This is a projeto with many data collection tools.

You can test the web version of the tool here:
http://datatools.jvmsolutions.tech/

# Installing

## Data Collection Tools

> git clone https://github.com/aureliowozhiak/data_collection_tool

> cd data_collection_tool

> pip install -r requirements.txt


## CherryPy
This project has CherryPy dependency to run in web version

### Supported python version
CherryPy supports Python 3.5 through to 3.8.
CherryPy can be easily installed via common Python package managers such as setuptools or pip.

> easy_install cherrypy

> pip install cherrypy

You may also get the latest CherryPy version by grabbing the source code from Github:

*This need to be run, inside the "data_collection_tools" folder*

> git clone https://github.com/cherrypy/cherrypy

> cd cherrypy

> python setup.py install

# Project Architectural
This project has a MVC (Model–view–controller) software architectural, so the folders inside "src" has this structure:
![Model–view–controller - software architectural](docs/mvc.png)

<!-- Blog post -->

# [Data Tools] - Ferramenta [em desenvolvimento] para trabalhar com Dados [Projeto GitHub]

## A motivação pra criar o projeto
Esse projeto é um sonho que eu sempre tive de implementar algo útil para a comunidade dev e que fosse algo prático para pessoas sem conhecimento técnico, mas até então não tinha muita ideia do que fazer e que realmente pudesse agregar valor para a comunidade dessa forma.

O projeto se iniciou devido a uma grande dor encontrei na área de dados das empresas que trabalhei: **coletar**, **tratar** e **visualizar** dados de **forma rápida**! 

Sempre que eu precisava coletar dados de um site ou precisava conectar com uma API de terceiro para baixar dados era aquele trabalho repetitivo de criar e recriar a roda diversas vezes para chegar em um resultado parecido, mas com fontes de dados totalmente diversas. 

Dado isso, resolvi criar uma biblioteca para ser um "toolkit" para trabalhar com dados, e a ideia desse kit de ferramentas é não só extrair dados externos, mas também facilitar a visualização e pós processamento desses dados, seja propondo gráficos de forma inteligente com base nos dados ou seja sugerindo um modelo matemático para encontrar padrões nesses dados.

De qualquer forma, a ideia do projeto foi crescendo e crescendo e hoje o objetivo é não só fazer um toolkit para pessoas técnicas, mas sim evoluir isso e criar uma ferramenta para que pessoas leigas possam ter acesso a mais dados de forma desburocratizada.

 


## Links úteis 
Demonstração da primeira versão do site: http://datatools.jvmsolutions.tech/

GitHub com instruções de instalação: https://github.com/aureliowozhiak/data_collection_tools



![Home page of Data Tools](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/home_page.PNG)

 



### Funcionalidades já implementadas 
---
#### Extração de dados (em desenvolvimento)
Nessa página, a idéia é você passar a url de uma página HTML e o Data Tools irá retornar diversos dados e informações relevantes sobre o conteúdo da página.
⚠️ Por enquanto a ferramenta só retorna o título da página informada com uma lista de todos os links encontrados dentro dessa página, mas a idéia é ter um mini relatório de dados extraído de forma automática! ⚠️

http://datatools.jvmsolutions.tech/tools/web_scraping/

![Web Srapping page](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/web_scrapping.PNG)

![Web Scrapping result page](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/web_scrapping_result.PNG)
 
![Links result page](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/link_encontrados.PNG)
 
 


---
#### Extração de tabelas HTML 
Essa funcionalidade é simples, você informa uma URL, de um site que contenha uma ou mais tabelas em HTML, e passa a "posição" da tabela na página, e o retorno é essa tabela carregada dentro do Data Tools, junto de um botão para download em formato CSV:
http://datatools.jvmsolutions.tech/tools/table_scraping/


![Table scrapping page](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/table_scrapping.PNG)

![Table scrapping result page](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/download_table_scrapping.PNG)


![CSV generated](https://raw.githubusercontent.com/aureliowozhiak/data_collection_tools/main/docs/datatools_v1/csv.PNG)
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
---
#### Funcionalidade extra

Inspirado no post: [Seu portifólio/blog a partir da API do TabNews](https://www.tabnews.com.br/evertonribas/blog-pessoal-a-partir-das-apis-tabnews), implementei um blog super simples, com lista dos meus posts + visualização de um post em aba separada: http://datatools.jvmsolutions.tech/blog/
