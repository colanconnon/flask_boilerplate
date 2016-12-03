# flask_boilerplate

A basic flask boilerplate using docker-compose postgres, sql alchemy and nginx

To start just type 
```
docker-compose up -d
```

visit http://localhost in a browser


# To run migrations

To create a migration from your models
```
python3 manage.py db migrate
```

To run apply the migrations to your database
```
python3 manage.py upgrade
```
