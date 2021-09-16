## autoTrasformer

Сервис трансформирует неструктурированный текст в структурированный

## Манипуляции с docker
Сборка проет в docker
`docker build -t docker.io/kudddy/autotrasformer .`

Публикация образа
```
docker push docker.io/kudddy/autotrasformer:latest
```

Запуск проекта
```
docker run -p 8080:8080 docker.io/kudddy/autotrasformer
```
ps данных шаг требуется для деплоя проекта

## Проверка работоспособности сервиса
Можно использовать postman
запрос
```
http://0.0.0.0:8080/get-search-res-from-yandex/
```
Внутри запроса должен лежать json вида:
```
{
    "MESSAGE_NAME": "GET_DUCKLING_RESULT", 
    "data": {
        "text": "хочу бмв 3 в москве"
    }
}
```
где "алалла" - запрос пользователя

ответ
```
{
    "MESSAGE_NAME": "GET_DUCKLING_RESULT",
    "STATUS": true,
    "PAYLOAD": {
        "result": {
            "min_price": 247000,
            "median": 3464899,
            "max_price": 6585100,
            "count": 154,
            "url": "https://sberauto.com/app/cars?brand=48=model=591&rental_car=exclude_rental&city=1"
        },
        "description": "OK"
    }
}
```
## Логирование

В качесте логера используется tlg




