# Fronius Solar.web

Python client for the Fronius [Solar.web API documentation](https://www.fronius.com/~/downloads/Solar%20Energy/User%20Information/SE_UI_API_InterfaceDocumentation_EN.pdf). 
Fronius [test site](https://api.solarweb.com/swqapi/index.html).

## Features 

- Talks to your Fronius Solar.web PV system via Cloud API
- Automatic retries with exponential backoff
- Optionally pass in a `httpx` client
- If a login and password is provided login with a bearer token can be used

## Usage

Although intended as a library [`fronius_key_example.py`](https://github.com/drc38/python-fronius-web/blob/main/examples/fronius_key_example.py) is provided for testing purposes.

Authentication and PV system id for the example is provided via environment variables, e.g. on nix systems:

```
export ACCESS_KEY_ID=FKIAFEF58CFEFA94486F9C804CF6077A01AB
export ACCESS_KEY_VALUE=47c076bc-23e5-4949-37a6-4bcfcf8d21d6
export LOGIN_NAME=abc@email.com
export LOGIN_PASSWORD=xxxxx
export PV_SYSTEM_ID=20bb600e-019b-4e03-9df3-a0a900cda689
```