Para executar o projeto com Docker basta executar o comando abaixo para criar uma imagem

    sudo docker-compose run web django-admin startproject candidates .

Após isso basta executar o docker-compose para fazer uso do projeto

    docker-compose up --build

os endepoints utilizados no projeto estão na raiz do projeto com o nome Worc.postman_collection.json basta apenas importa no POSTMAN.

Pelo terminal criar um superuser para utilizar os dados já cadastrado no sqlit3.

