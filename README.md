<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# HELP MY HAIR

## Conteúdo
- [Descrição do Projeto](#project-description)
- [Sistema de recomendação](#sistema-de-recomendação)
- [Desenvolvimento](#desenvolvimento)
- [Status](#status)
- [Etapas](#etapas)
- [Funcionalidades](#funcionalidades)
- [Autor](#autor)


<a name="project-description"></a>

## Descrição do Projeto
A ideia inicial surgiu do desejo de criar uma ferramenta que pudesse contribuir de alguma forma na empresa que trabalho. Atuo na área comercial de uma multinacional de bens de consumo, detentora de diversas marcas mundialmente conhecidas e que são consumidas diariamente por milhares de pessoas. Pensando na quantidade de marcas e diferentes tipos de produtos que existem no mercado, e sendo apaixonada pela categoria de cuidados pessoais e beleza, decidi criar um sistema de recomendação que sugerisse produtos para cabelos considerando as marcas da empresa em que trabalho. Tal sugestão é baseada na recomendação por similaridade entre conteúdo e input do usuário. 

<a name="sistema-de-recomendação"></a>

## Sistema de recomendação
Em um mundo cada vez mais conectado, dinâmico, repleto de informações e conteúdo, a personalização tem se tornado a mina de ouro nos negócios. Entender a necessidade do consumidor, apresentar um conteúdo relevante, alinhado a seus gostos e hábitos hoje já é visto como algo básico, porém fundamental. O sistema de recomedação como o próprio nome já diz, surge para selecionar aquilo que interessa e é relevante a determinada pessoa de acordo com suas preferências. Sendo possível até personalizar a experiência do usuário com aplicativos e sites por exemplo. 

Para o projeto final usei o sistema de recomendação por filtragem de conteúdo.

<a name="Desenvolvimento"></a>

## Desenvolvimento

Após a escolha do dataset, realizei a exploração e limpeza dos dados com base no conteúdo de interesse ao projeto. A etapa seguinte foi transformar essa informação de uma forma que permitisse entender a correlação entre o input do usuário e os produtos a serem recomendados. Com os dados classificados, usei a biblioteca Scipy e cdist para cálculo da distância entre informações. Com esse dados prontos, usei a plataforma Streamlit  para criar uma aplicação na web.


<a name="status"></a>

## Status
Em desenvolvimento.

<a name="etapas"></a>

## Etapas
  * [x] Sistema de recomendação por filtragem de conteúdo;
  * [ ] Criar um sistema hibrido de filtragem de conteúdo e colaborativo;
  * [ ] Inserir demais categorias e portfolio ampliando as opções de recomendação.

<a name="funcionalidades"></a>

## Funcionalidades
 
  * Além de sugerir o produto ideal para cada tipo de cabelo, o sistema trará 3 opções para que o usuário escolha uma. Ao clicar em uma delas, será direcionado ao shopping do Google onde seu produto será exibido em diversas opções de varejistas permitindo que faça comparações de preço.


<a name="autor"></a>

## Autor

* https://github.com/bruna-de-paula
* https://www.linkedin.com/in/brunadepaula-2020/
* https://www.instagram.com/bru.ni.ta/





