import asyncio
from pydantic import BaseSettings, SecretStr
from fronius_solarweb.api import Fronius_Solarweb


class AuthDetails(BaseSettings):
    ACCESS_KEY_ID: SecretStr
    ACCESS_KEY_VALUE: SecretStr
    PV_SYSTEM_ID: str


async def main():
    creds = AuthDetails()
    fronius = Fronius_Solarweb(
        access_key_id=creds.ACCESS_KEY_ID.get_secret_value(),
        access_key_value=creds.ACCESS_KEY_VALUE.get_secret_value(),
        pv_system_id=creds.PV_SYSTEM_ID,
    )

    print("Getting SolarWeb api release info:")
    release_info = await fronius.get_api_release_info()
    print(f"{release_info}\n")

    print("Getting PV systems meta data:")
    pv_systems_data = await fronius.get_pvsystems_meta_data()
    print(f"{pv_systems_data}\n")

    print(f"Getting PV system meta data for {creds.PV_SYSTEM_ID}:")
    pv_system_data = await fronius.get_pvsystem_meta_data()
    print(f"{pv_system_data}\n")

    print("Getting Devices meta data:")
    devices_data = await fronius.get_devices_meta_data()
    print(f"{devices_data}\n")

    print("Getting power flow data:")
    flow_data = await fronius.get_system_flow_data()
    print(f"{flow_data}\n")


if __name__ == "__main__":
    asyncio.run(main())
