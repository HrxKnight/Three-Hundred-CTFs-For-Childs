FROM python:3

WORKDIR /usr/src/app

RUN echo "flag{n0w_fl4sk_m0re_th1ngs_t0_learn}" > /flag.txt

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]