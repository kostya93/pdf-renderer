## pdf-renderer

### Установка
```
git clone https://github.com/kostya93/pdf-renderer.git
cd pdf-renderer
```
Заполнить необходнимые поля в [db/.env](db/.env) и [web/.env](web/.env)


### Запуск
```
docker-compose up -d
```

### API

- **Файл**

Создадим html-файл

`/path/to/file.html`:
```html
<!DOCTYPE html>
<html>
<body>

<h1>Heading</h1>

</body>
</html>
```

Сделаем запрос на создание pdf из html-файла

Запрос:
```
curl -X POST http://localhost/api/pdfrenders/ -F html_file=@/path/to/file.html
```
Ответ:
```json
{
  "id":"450d62d9-618b-49f1-a199-3a2566e074e0",
  "url":null,
  "status":"pending",
  "html_file":"http://localhost/media/html/450d62d9-618b-49f1-a199-3a2566e074e0.html",
  "pdf_file":null
}
```

Статус `pending` значит, что процесс создания pdf запущен. Чтобы проверить результат (используем `id` из предыдущего ответа):

Запрос:
```
curl http://localhost/api/pdfrenders/450d62d9-618b-49f1-a199-3a2566e074e0/
```
Ответ:
```json
{
  "id":"450d62d9-618b-49f1-a199-3a2566e074e0",
  "url":null,
  "status":"success",
  "html_file":"http://localhost/media/html/450d62d9-618b-49f1-a199-3a2566e074e0.html",
  "pdf_file":"http://localhost/media/pdf/450d62d9-618b-49f1-a199-3a2566e074e0.pdf"
}
```
Видим, что `"status":"success"` и появилась ссылка на pdf.

Если `"status":"pending"` -- нужно ещё подождать

Если `"status":"failed"` -- что-то пошло не так

- **URL**

Всё аналогично за исключением того, что в первом запросе передаём не `html_file`, а `url`:

Запрос:
```
curl -X POST http://localhost/api/pdfrenders/ -F url=https://en.wikipedia.org/wiki/Quebec_Agreement
```
Ответ:
```json
{
  "id":"3abaa7eb-c09f-4dbe-8145-affb8e6d5121",
  "url":"https://en.wikipedia.org/wiki/Quebec_Agreement",
  "status":"pending",
  "html_file":null,
  "pdf_file":null
}
```
Запрос:
```
curl http://localhost/api/pdfrenders/3abaa7eb-c09f-4dbe-8145-affb8e6d5121/
```
Ответ:
```json
{
  "id":"3abaa7eb-c09f-4dbe-8145-affb8e6d5121",
  "url":"https://en.wikipedia.org/wiki/Quebec_Agreement",
  "status":"success",
  "html_file":null,
  "pdf_file":"http://localhost/media/pdf/3abaa7eb-c09f-4dbe-8145-affb8e6d5121.pdf"
}
```
### Завершение работы
```
docker-compose down -v
```
