FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install --install-option="--prefix=/install" -r requirements.txt
FROM python:3.8-slim
WORKDIR /code
COPY --from=builder /install /root/.local
COPY ./app .
ENV PATH=/root/.local:$PATH
CMD [ "python", "./main.py" ]