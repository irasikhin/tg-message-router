# tg-message-router

[![Build Status](https://cloud.drone.io/api/badges/irasikhin/tg-message-router/status.svg)](https://cloud.drone.io/irasikhin/tg-message-router)

## About

tg-message-router helps you route messages from a telegram channel to a specified http URL.

## Usage

Get **api_id** and **api_hash** at https://my.telegram.org.

```shell
docker run \ 
  -e TELEGRAM_FROM_CHANNEL_ID=<some channel id> \
  -e TELEGRAM_API_ID=<api id> \
  -e TELEGRAM_API_HASH=<api hash> \
  -e TELEGRAM_ROUTE_HOOK_URL=<hook url> \
  irasikhin/tg-message-router
```

## License

[MIT](LICENSE)