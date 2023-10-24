# beekin_backend


Requirements and installation

Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.

In our case, we have one single resource, crud, so we will use the following URLS - /api/crud/ and /api/crud/<id> for collections and elements, respectively:

Endpoint	HTTP Method	CRUD Method	Result
crud	GET	READ	Get all user details
crud/:id	GET	READ	Get a single user details
crud	POST	CREATE	Create a new user details
crud/:id	PUT	UPDATE	Update a user details
crud/:id	DELETE	DELETE	Delete a user details
First, we have to start up Django's development server:

python manage.py runserver
Any users can use the API services, for that reason if we try this:

http://localhost:8000/api/crud/
