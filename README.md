# Fronius Solar.web

Python client for the Fronius [Solar.web API](https://www.fronius.com/~/downloads/Solar%20Energy/User%20Information/SE_UI_API_InterfaceDocumentation_EN.pdf).

## Features 

- Talks to your Fronius Solar.web PV system via Cloud API
- Automatic retries with exponential backoff
- Optionally pass in a `httpx` client

## Usage

Although intended as a library a `fronius_sw_example.py` is provided for testing purposes.

To provide authentication and system id for the example is done via environment variables, e.g. on nix systems:

```
export ACCESS_KEY_ID=FKIAFEF58CFEFA94486F9C804CF6077A01AB
export ACCESS_KEY_VALUE=47c076bc-23e5-4949-37a6-4bcfcf8d21d6
export PV_SYSTEM_ID=20bb600e-019b-4e03-9df3-a0a900cda689
```