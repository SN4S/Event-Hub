FROM python:3.11

ENV PYTHONUNBUFFERED 1
WORKDIR /eventhub
COPY . /eventhub
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "eventhub.wsgi:application", "--bind", "0.0.0.0:8000"]
