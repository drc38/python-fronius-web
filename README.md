# fronius_solarweb

Python client for the Fronius Solar.web API.

## Features 

- Talks to your Fronius Solar.web PV system via Cloud API
- Automatic retries with exponential backoff
- Optionally pass in a `httpx` client

## Usage

```python
import asyncio
from pydantic import BaseSettings, SecretStr
from fronius_solarweb.api import Fronius_Solarweb


class AuthDetails(BaseSettings):
    ACCESS_KEY_ID: SecretStr
    ACCESS_KEY_VALUE: SecretStr
    PV_SYSTEM_ID: str


async def main():
    creds = AuthDetails()
    fronius = Fronius_Solarweb(access_key_id=creds.ACCESS_KEY_ID.get_secret_value(),
                  access_key_value=creds.ACCESS_KEY_VALUE.get_secret_value(),pv_system_id=creds.PV_SYSTEM_ID)

    pv_system_data = await fronius.get_pvsystem_meta_data()
    devices_data = await fronius.get_devices_meta_data()
    flow_data = await fronius.get_system_flow_data()

    print("Getting PV system meta data for ", creds.PV_SYSTEM_ID)
    print(pv_system_data)

    print("Getting Devices meta data")
    print(devices_data)

    print("Getting power flow data")
    print(flow_data)


if __name__ == '__main__':
    asyncio.run(main())
```

## Examples

`python-fronius-solarweb` is intended as a library.

Providing authentication for the examples is via environment variables, e.g. on nix systems:

```
export ACCESS_KEY_ID=FKIAFEF58CFEFA94486F9C804CF6077A01AB
export ACCESS_KEY_VALUE=47c076bc-23e5-4949-37a6-4bcfcf8d21d6
export PV_SYSTEM_ID=20bb600e-019b-4e03-9df3-a0a900cda689

```


