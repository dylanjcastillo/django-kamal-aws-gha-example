FROM python:3.10-slim AS base

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.8.3
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && poetry --version

FROM base AS builder

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.in-project true && \
    poetry install --only main --no-interaction

FROM base AS runner

WORKDIR /app
COPY --from=builder /app/.venv/ /app/.venv/

COPY . /app
RUN mkdir -p /data /db

RUN chmod +x /app/src/entrypoint.sh

FROM runner AS production

EXPOSE 8000

ARG user=django
ARG group=django
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group} && \
    useradd -u ${uid} -g ${group} -s /bin/sh -m ${user} && \
    chown -R ${uid}:${gid} /app /data /db

USER ${uid}:${gid}

WORKDIR /app/src
CMD [ "/app/src/entrypoint.sh" , "app"]
