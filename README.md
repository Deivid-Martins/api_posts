# How to use it?
1 - Clone the repository on your own machine.

2 - enable your venv with the command “pip -m venv venv”, after which a folder named “venv” will be created in the root of your project, activate “venv/Scripts/activate using” your operating system's command.

3 - install the requirements in requirements.txt, check that they are present with the “pip freeze” command.

4 - after that, run “py manage.py runserver” to start the API on your localhost.

Bonus - If you want to view your sqlite database within Vs Code itself, use an extension such as “SQLite Viewer”.


# EndPoints
ALERT: Use software that makes HTTP requests, as this API has no Front-End. Like imsomnia or postman

This is an example of an object in this API's database (JSON):

    
    "id": “number primary key”, // It auto-increments as more objects are generated
    
    "username": "string",
    
    "created_datetime": "datetime",
   
    "title": "string",
   
    "content": "string"
    


1 - 

GET - "{hostUrl}/careers"

return: returns all database items in JSONs



2 - 

POST - "{hostUrl}/careers"

request(JSON):


		"username": "string",
  
		"title": "string",
  
		"content": "string"
  

when you send this JSON, it is stored in the database



3 -
PUT - {hostUrl}/careers/{object_id}

request(JSON): 


		"title": "string",
  
		"content": "string"
  

Only the “title” and “content” can be changed. When sending the JSON request, it searches for the object's “id” and changes it if it exists in the database.



4 -

DELETE - {hostUrl}/careers/{object_id}

There is no need for a body in this request, it simply looks for the “id” passed in the URL and if there is an object with that “id”, it is deleted from the database.
