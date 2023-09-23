FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PORT 5000

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 5000

CMD python main.py
