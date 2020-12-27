FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.8-slim AS build-image
COPY app/ .
RUN pip install --user .
WORKDIR /code
COPY --from=builder /root/.local/bin /root/.local
ENV PATH=/root/.local:$PATH
CMD [ "app" ]