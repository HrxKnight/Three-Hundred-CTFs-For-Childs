FROM python:2

WORKDIR /usr/src/app

RUN echo "flag{fl4sk_1s_aws0m3}" > /flag.txt

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]