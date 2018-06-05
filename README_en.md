# accountbook_server

> account book server project

## Build steps

### 1. Create a virtual environment and install dependencies
``` bash
$ pipenv install
```

### 2. Create a virtual environment and install dependencies
``` bash
$ pipenv shell
```

### 3. Create database and perform migration
Start `MySQL` service, create a database`accountbook`:
``` sql
CREATE DATABASE accountbook DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```
Check the database connection configuration and perform a table migration:
``` bash
$ python manage.py migrate
```

### 4. Operation service
``` bash
$ python manage.py runserver
```

---
* See details: [`wiki`](https://github.com/JiangInk/accountbook_server/wiki)
