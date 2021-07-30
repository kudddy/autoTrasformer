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
localhost:8080/getnearesttoken/
```
Внутри запроса должен лежать json вида:
```
{
    "MESSAGE_NAME": "GET_DUCKLING_RESULT",
    "data": {
        "text": "лалалал"
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
            "min_price": 17170436,
            "max_price": 887000,
            "count": 100,
            "url": "https://sberauto.com/cars?brand=48&city=1&rental_car=exclude_rental"
        },
        "description": "OK"
    }
}
```





