FROM python:3.12.4-slim-bullseye

WORKDIR /quantum_mind

RUN pip3 install poetry
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry export --only main --output requirements.txt
RUN pip3 uninstall -y poetry
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]