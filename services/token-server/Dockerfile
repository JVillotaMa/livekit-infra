FROM python:3.12

WORKDIR /usr/src/app

RUN pip install uv
COPY . .
RUN uv sync

EXPOSE 8000

CMD ["uv","run","fastapi","run","token-server.py","--port","8000"]