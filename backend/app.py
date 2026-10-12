from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Разрешаем фронтенду (из другого места) делать к нам запросы
CORS(app) 

@app.route('/api/data', methods=['GET'])
def get_data():
    # Эта функция срабатывает, когда кто-то обращается по адресу /api/data
    return jsonify({"message": "Сообщение с бекэнда, проверка связи!"})

if __name__ == '__main__':
    # Запускаем сервер на порту 5000. 0.0.0.0 значит "слушать все входящие подключения"
    app.run(host='0.0.0.0', port=5000)