FROM python:3.12.4-slim-bullseye

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /quantum_mind
COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --frozen

COPY . .

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]