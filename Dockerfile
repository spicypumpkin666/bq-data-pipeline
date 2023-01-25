FROM python:3.9.10-alpine3.15

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

# RUN crontab crontab

# CMD ["crond", "-f"]

CMD ["python3", "main.py"]
