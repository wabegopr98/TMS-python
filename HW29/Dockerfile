FROM python:3.9

#устанавливаем рабочую директорию
WORKDIR /app

#копируем файлы внутри контейнера
COPY script.py .

CMD ["python", "script.py"]


FROM python:3.9
WORKDIR /tests
COPY test_script.py .
RUN pip install pytest
CMD ["pytest", "-s", "test_script.py"]