- Nós da Worc, como startup de empregabilidade, preparamos um desafio com foco em um grupo muito importante da nossa plataforma: os candidatos!
Os candidatos desse teste possuem os seguintes atributos:
    Nome
    Email
    CPF
    Idade
    Pretensão salarial
    Disponibilidade imediata para trabalho - Opção de disponível ou não.
    
- O objetivo é desenvolver uma API com as seguintes funcionalidades:
- Criação de candidatos
    Candidatos devem ter mais que 18 anos para finalizar o cadastro
    Email e CPF devem ser únicos
- Atualização do registro de um candidato
    Não possível alterar o CPF
- Listagem de candidatos
    Paginados com limite de 5 por vez
    Possibilidade de filtro por algum ou todos(opcional) atributos do candidato
- Remover um candidato da base

- Recomendações do teste:
    As funcionalidades devem conter as regras mencionadas no objetivo
    - Documentação - O README deve conter:
    - Como executar a aplicação;
    - Estrutura dos arquivos/pacotes;
    - Explique as decisões de design adotadas para a solução;
    - Descreva sua API Rest de forma simplificada.
    - Testes unitários - o teste deve conter pelo menos um teste unitário contendo o fluxo
    de sua escolha, porém fazer mais de um também é bem vindo.
    - Opcional - Caso saiba utilizar docker e docker-compose, super recomendamos que
    utilize nesse projeto! - Não esqueça de mencionar como rodar o projeto com esse
    adicional.
    - Opcional - Logs são muito importantes para a observabilidade do ambiente, seria
    interessante implementar uma configuração básica para monitorar a aplicação.
    Tipos ex: INFO, WARNING, ERROR, FATAL.
    - Boas práticas de desenvolvimento e gitflow também serão avaliados.


- Para executar o projeto com Docker basta executar o comando abaixo para criar uma imagem

        sudo docker-compose run web django-admin startproject candidates . 

- Após isso basta executar o docker-compose para fazer uso do projeto

        docker-compose up --build
        
 - Executar os tests unitários com o comando abaixo dentro do container docker
        
        ./manage.py test candidates.candidate.tests.test_candidate.TestCandidateTestCase

- Os endepoints utilizados no projeto estão na raiz do projeto com o nome Worc.postman_collection.json basta apenas importa no POSTMAN.
- Fiz uso da autenticaçaõ usando JWT
- O Padrão de projeto utilizado, eu particulamente gosto que cada app fica dentro da pasta do projeto django para usar candidates.candidate gosto de usar esse padrão como exibido na imagem abaixo:
![project](https://user-images.githubusercontent.com/1080519/146121006-f66dda87-2133-4b68-9da8-4927f5b57a71.png)


- Pelo terminal criar um superuser para utilizar os dados já cadastrado no sqlit3 e também é preciso está autenticado para realizar as requisições.
- Foi implementado a opção de filtrar por todos os campos
- É possível ver a documentação da API acessando o endereço: http://localhost:8000/ pelo navegador.
- Para monitorar os logs fiz uso da bibliote newrelic onde é possível ter as métricas e logs da aplicação. Porém não sei disponibilizar ela por aqui.
![newrelic](https://user-images.githubusercontent.com/1080519/146029772-0c10553f-1125-4064-9bec-d514b77fc6f8.png)

 
