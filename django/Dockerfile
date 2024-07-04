# syntax = docker/dockerfile:1.4
FROM python:3

EXPOSE 8000

WORKDIR /project

COPY ./project ./

RUN <<EOF
pip3 install --upgrade pip
python3 -m venv /venv
EOF

ENV PATH="/venv/bin:$PATH"

RUN <<EOF
pip3 install -r ./requirements.txt --no-cache-dir
python3 manage.py makemigrations
python3 manage.py migrate
EOF

ENTRYPOINT [ "python3" ]

CMD [ "manage.py", "runserver", "0.0.0.0:8000"]
