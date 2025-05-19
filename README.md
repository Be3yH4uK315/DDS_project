# Django DDS Web Service

## 📌 Описание
Веб-приложение для управления движением денежных средств с фильтрацией, справочниками и логическими связями.

## 🚀 Установка

```bash
git clone <repo-url>
cd dds_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
