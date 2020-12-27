FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.8-slim AS build-image
RUN pip install --user .
WORKDIR /code
COPY --from=builder /requirements.txt ./
COPY --from=builder /root/.local/bin /root/.local
COPY --from=builder /root/.cache /root/.cache
RUN pip install -r requirements.txt
COPY ./app .
ENV PATH=/root/.local:$PATH
CMD [ "main.py" ]