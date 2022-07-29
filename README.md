# microservices-products-list-app
## This is my first app built using the microservices architecture.
This project is made based on 2 microservices, the 'admin' one and the 'main' one.
The first is built with Django, and the second with Flask, they communicate with each other through a RabbitMQ layer, and each one has it's own MySQL database.


### Microservice 1 - ADMIN - Built with Django:
To run this service, you will have to have Docker installed.
Steps:
- Go inside the admin/ folder
- Run: docker-compose up 
- See the magic!

### Microservice 2 - MAIN - Built with Flask:
Steps:
- Go inside the main/ folder
- Run: docker-compose up
- See the magic!

### Frontend 
Steps:
- Go inside the react-frontend/ folder
- Run: npm start
- The app will run, and you can access the admin page with 'localhost:3000/admin/products' and the main page with 'localhost:3000'.

### Extras:
If you make any change that need to be applied on the databases, access the terminal of the correct Docker container with:
- docker exec -it <CONTAINER-ID> /bin/bash

Then, for the ADMIN app (Django one), you can run:
- python manage.py migrate
- python manage.py makemigrations

For the MAIN app (Flask one), run:
- flask db init
- flask db migrate
- flask db upgrade