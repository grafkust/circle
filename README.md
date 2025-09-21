# Circle
Получает из чата видео и конвертирует его в telegram кружок

### Запуск приложения
1. Создаем .env файл в корневой папке и указываем токен для доступа к боту `HTTP_TOKEN=token`
2. Устанавливаем виртуальное окружение `python -m venv venv`
3. Активируем окружение 
   - Windows - `venv\Scripts\activate`
   - Linux/macOS - `source venv/bin/activate`
4. Устанавливаем зависимости `pip install -r requirements.txt`
5. Запускаем основной файл `python src\main\python\Application.py`

p.s. Приложение разрабатывалось на Python 3.13.2

### Ограничения бота
- Принимает только файлы до 20МБ (внутреннее ограничение telegram)
- Обрезает исходник до 240*240px (формат кружков в telegram)

