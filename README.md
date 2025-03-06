# Email Service

Проект представляет собой сервис для отправки email-рассылок с использованием Django 1.9.9 и Celery 3.1.26. Сервис поддерживает отправку отложенных рассылок, использование HTML-шаблонов с переменными, а также отслеживание открытий писем.

---

## 📋 **Функциональность**

1. **Создание рассылок**:
   - Использование HTML-шаблонов.
   - Поддержка переменных в шаблонах (имя, фамилия, день рождения).
   - Возможность выбора списка подписчиков.

2. **Отправка писем**:
   - Мгновенная отправка.
   - Отложенная отправка (по расписанию).

3. **Отслеживание открытий писем**:
   - В письмо добавляется прозрачный пиксель для отслеживания.
   - Статистика открытий сохраняется в базе данных.

4. **Интеграция с Celery**:
   - Фоновая обработка задач.
   - Использование Redis как брокера.

---

## 🛠️ **Установка и настройка**

### 1. **Требования**
- Python 2.7
- Redis
- Установленные зависимости (см. `requirements.txt`)

### 2. **Установка зависимостей**
```bash
pip install -r requirements.txt
```

### 3. **Настройка базы данных**
Создайте и примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. **Запуск Redis**
Убедитесь, что Redis запущен:
```bash
redis-server
```

### 5. **Запуск Celery**
```bash
celery -A email_service worker -l info --pool=solo
```

### 6. **Запуск сервера Django**
```bash
python manage.py runserver
```

---

## 🚀 **Использование**

### 1. **Создание рассылки**
- Откройте модальное окно для создания рассылки.
- Заполните форму:
  - Тема письма.
  - HTML-шаблон.
  - Список подписчиков.
  - Время отправки (для отложенной рассылки).

### 2. **Отслеживание открытий**
- Каждое письмо содержит прозрачный пиксель для отслеживания.
- Статистика открытий доступна в админке Django.

### 3. **Пример HTML-шаблона**
```html
<h1>Привет, {{ first_name }} {{ last_name }}!</h1>
<p>Ваш день рождения: {{ birthday }}</p>
```

---

## ⚙️ **Конфигурация**

### 1. **Настройка SMTP**
Добавьте в `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourserver.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@email.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
```

### 2. **Настройка Celery**
```python
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

---

## 📝 **Примеры API**

### Создание рассылки (AJAX)
```javascript
$.ajax({
    url: '/create/',
    method: 'POST',
    data: {
        subject: 'Test Subject',
        html_template: '<h1>Hello, {{ first_name }}</h1>',
        subscribers: [1, 2, 3],
        scheduled_time: '2023-10-01T12:00'
    },
    success: function(response) {
        console.log('Рассылка создана!');
    }
});
```

### Отслеживание открытий
```html
<img src="http://yourdomain.com/tracking/{{ uuid }}.png" width="1" height="1" />
```
