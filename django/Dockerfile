# syntax = docker/dockerfile:1.4
FROM python:3

EXPOSE 8000

WORKDIR /project

COPY ./project/ ./
COPY --chmod=755 ./tools/docker-entrypoint.sh ./.

ENV DJANGO_SETTINGS_MODULE config.settings.deployment
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN <<EOF
pip3 install --upgrade pip
python3 -m venv /venv
EOF

ENV PATH "/venv/bin:$PATH"

RUN pip3 install -r ./requirements.txt --no-cache-dir

ENTRYPOINT [ "./docker-entrypoint.sh" ]
