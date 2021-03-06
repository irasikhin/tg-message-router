FROM python:3.8 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.8-slim AS build-image
WORKDIR /code
COPY --from=builder /requirements.txt ./
COPY --from=builder /root/.local/bin /root/.local
COPY --from=builder /root/.cache /root/.cache
RUN pip install -r requirements.txt
COPY ./app .
ENV PATH=/root/.local:$PATH
CMD ["python", "main.py" ]