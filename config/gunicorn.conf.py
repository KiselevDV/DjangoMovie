"""
gunicorn.conf.py (Веб-сервер) - более надёжный локальный сервер, для прода
movie.conf (supervisor) - программа, которая следит за тем, что бы процесс
всегда работал и если процесс упал, то он автоматическт поднимет этот
процесс - gunicorn.conf.py
"""
bind = '127.0.0.1:8000'
workers = 3  # выделение 'ресурса', от 1 до ...
user = "dima"  # username
timeout = 120  # время ожидание ответа клиентом от сервера
