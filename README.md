# Сервис для работы со статистикой
____

## Документация сервиса
`
http://127.0.0.1:8000/docs/
`
____

## Развернуть контейнер Docker
`
docker-compose up -d --build
`
____

## Запустить тесты
`
pytest
`
____

## Метод сохранения статистики
`
POST http://127.0.0.1:8000/stats/
`
```json

{
  "date": Date,
  "views": int,
  "clicks": int,
  "cost": float
}
```
____

## Метод получения статистики
`
POST http://127.0.0.1:8000/stats/show_stats
`
```json

{
  "from_date": Date,
  "to_date": Date
}
```
____

## Метод удаления статистики
`
GET http://127.0.0.1:8000/stats/delete_stats
`
