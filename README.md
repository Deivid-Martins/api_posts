# Como usar?
1 - Clone o repositório na sua própria máquina.

2 - habilite sua venv com o comando "pip -m venv venv", após isso será criado um pasta com nome "venv" na raiz do seu projeto, ative o "venv/Scripts/activate usando" o comando do seu sistema operacional.

3 - instale os requisitos presentes em requirements.txt, verifique se estão presentes com o comando "pip freeze".

4 - após isso, execute "py manage.py runserver" para iniciar a API no seu localhost.

Bonus - Caso queira ver seu banco de dados sqlite dentro do próprio Vs Code, utilize alguma extensão, como a "SQLite Viewer"


# EndPoints
AVISO: Utilize algum software que faça requisições HTTP, pois essa API não possui Front-End. Como o imsomnia ou postman


Isso é um exemplo de objeto no banco de dados dessa API(JSON):

    
    "id": “number primary key”, // Ele auto-incrementa conforme mais um objeto é gerado
    
    "username": "string",
    
    "created_datetime": "datetime",
   
    "title": "string",
   
    "content": "string"
    


1 - 

GET - "{hostUrl}/careers"

return: retorna todos os items do banco de dados em JSONs


2 - 

POST - "{hostUrl}/careers"

requisição(JSON):


		"username": "string",
  
		"title": "string",
  
		"content": "string"
  

ao enviar esse JSON, ele é armazenado no Banco de Dados


3 -
PUT - {hostUrl}/careers/{object_id}

requisição(JSON): 


		"title": "string",
  
		"content": "string"
  

Pode ser alterado apenas o "title" e o "content", ao enviar a requisição em JSON, ele busca pelo "id" do objeto e altera caso o mesmo exista no Banco de Dados.


4 -

DELETE - {hostUrl}/careers/{object_id}

Não é necessário um body nessa requisição, ele simplesmente procura o "id" passado na URL e se existir algum objeto com esse "id", o mesmo é excluido do banco de dados.

