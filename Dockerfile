FROM python:3.12

WORKDIR /usr/src/app

COPY ./app /usr/src/app/

COPY api_info.json /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ARG TABLE_NAME
ENV TABLE_NAME ${TABLE_NAME}

CMD ["python", "./app.py"]
