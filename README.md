# tg-message-router

[![Build Status](https://cloud.drone.io/api/badges/irasikhin/tg-message-router/status.svg)](https://cloud.drone.io/irasikhin/tg-message-router)

## About

**tg-message-router** helps you route messages from a telegram channel to a specified http URL.

## Usage

Get **api_id** and **api_hash** at https://my.telegram.org.

```shell
docker run \ 
  -i \
  -t \
  -e TELEGRAM_SESSION_PATH=<session path> \
  -e TELEGRAM_FROM_CHANNEL_TITLE=<channel title> \
  -e TELEGRAM_API_ID=<api id> \
  -e TELEGRAM_API_HASH=<api hash> \
  -e TELEGRAM_ROUTE_HOOK_URLS=<hook url> \
  irasikhin/tg-message-router
```

Example:

```shell
docker run \ 
  -i \
  -t \
  -e TELEGRAM_SESSION_PATH='/data' \
  -e TELEGRAM_FROM_CHANNEL_TITLE='ForkLog' \
  -e TELEGRAM_API_ID='123' \
  -e TELEGRAM_API_HASH='123456' \
  -e TELEGRAM_ROUTE_HOOK_URLS='http://localhost:8080' \
  -v ./data:/data
  irasikhin/tg-message-router
```

## License

[MIT](LICENSE)