# 1. Берем готовый веб-сервер Nginx. Он идеально подходит для раздачи простых HTML страничек.
FROM nginx:alpine

# 2. Копируем наш index.html в ту папку, откуда Nginx раздает файлы по умолчанию
COPY index.html /usr/share/nginx/html/index.html

# Nginx сам запустится, поэтому команду CMD писать не нужно, она есть в базовом образе