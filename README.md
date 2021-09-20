# Virtual File System

### How install and run

- Clone the project
```bash
git clone git@github.com:Zhyzhkunets/virtual_file_system.git
```

#### To use virtualenv

- Create venv and activate 
```bash
python3 -m venv env
source env/bin/activate 
```

- Install requirements
```bash
pip install -r requirements.txt
```

- Create DB (approach is up to you)
```bash
createdb file_manager -U postgres
```

- Make migrations
```bash
./manage.py migrate
```

- Create superuser
```bash
./manage.py createsuperuser 
```

- Run server 
```bash
./manage.py runserver
```

- Run tests 
```bash
./manage.py test 
```

#### To use docker

- Run the docker-compose up command 
```bash
docker-compose up
```

- Run migrations
```bash
docker-compose run web python manage.py migrate
```

- Create superuser
```bash
docker-compose run web python manage.py createsuperuser
```

- Run test
```bash
docker-compose run web python manage.py createsuperuser
```