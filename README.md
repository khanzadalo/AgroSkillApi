# AgroSkill 
## django rest framework

---
## Настройка
Для начала работы с проектом вам потребуется клонировать репозиторий на свой компьютер. Вы можете сделать это, используя следующие команды:

```bash
git clone https://github.com/khanzadalo/AgroSkillApi.git
cd AgroSkillApi
python -m venv venv
source venv/bin/activate Linux
venv\Scripts\activate   Windows
pip install -r requirements.
```
---
## .env file
Для настройки проекта вам потребуется файл .env, в котором будут храниться ваши переменные окружения. Пример содержимого файла .env:
```
SECRET_KEY=your-secret-key

POSTGRES_DB=your-database-name
POSTGRES_USER=your-database-user
POSTGRES_PASSWORD=your-database-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

EMAIL_USE_SSL=True
EMAIL_PORT=465
EMAIL_HOST=your-email-host
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-email-password
```
---
## Запуск проекта
После создания файла .env, вы можете запустить проект, используя следующие команды:
```bash
python manage.py migrate
python manage.py createsuperuser(insert user name and password)
python manage.py runserver
```
---
# To-Do:
- [x] добавить пользователей и конфигурации
- [x] добавить CORS и конфигурации
- [x] Сделать корзину
- [x] Добавить систему аутентификации JWT
- [x] проверить доступность всех продуктов с помощью метода get
- [x] добавить функцию удаления для корзины
- [x] добавить документацию
- [x] добавить CSRF и конфигурации
- [x] добавить возможность поиска по товару и категории
- [x] добавить возможность добавления товара в корзину
- [x] добавить возможность увеличения и уменьшения товара в корзине
- [x] добавить возможность изменения пароля и изображения профиля
- [x] добавить возможность удаления профиля
- [x] добавить возможность обновления профиля
- [x] добавить возможность выхода из профиля
- [x] добавить возможность обновления токена
- [x] добавить возможность регистрации
- [x] добавить возможность восстановления пароля
- [x] добавить возможность отправки писем
- [x] добавить возможность отправки писем с подтверждением
- [x] добавить возможность отправки писем с восстановлением пароля



## Контакты
Если вы нашли ошибки или у вас есть вопросы или предложения, свяжитесь со мной по адресу https://t.me/nikksiri