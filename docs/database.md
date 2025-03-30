# O BANCO DE DADOS | ORM. 🌵

The database modeling must have three tables: User, Plants and Flowers.

```mermaid
erDiagram
    User {
        int id PK
        string email UK
        string username UK
        string senha
    }


    Plantas {
        int id PK
        string Nome UK
        string Nome_Cientifico UK
        string Classe 
        string Ordem 
        string Familia
        string Genero
    }

    Flores {
        int id PK
        string Nome UK
        string Nome_Cientifico UK
        string Classe 
        string Ordem 
        string Familia
        string Genero
    }
```

## Extração dos dados. 🌱

This project used web scraping to extract taxonomic information about plants from [Wikipedia](https://pt.wikipedia.org/wiki/Lista_de_plantas_do_Brasil). Using the `BeautifulSoup` library to parse the HTML, data such as scientific name, class, order, family and genus of several plants were collected. This data was then stored in a database using SQLAlchemy, facilitating future queries and ensuring the persistence of the extracted information.

<div align='center'>
<img src=assets/images/image.png width=30%>
</div>


**AVISO ⚠️**
> Much of the data was taken raw. Without proper cleaning or source verification. In case there are broken values ​​or unrealistic values.
