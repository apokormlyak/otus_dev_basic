# otus_dev_project

## Проектная работа на тему "Складские операции"


### запуск приложения

Создаем файл окружения по примеру environment.example
```
ln -s environment.example environment
```

```
docker-compose up --build
```

### Приложение доступно по адресу: http://localhost:8000/warehouses/

### тесты
```
docker-compose run --rm  backend pytest
```
