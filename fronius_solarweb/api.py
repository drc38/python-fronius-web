import logging

from httpx import AsyncClient
from pydantic import ValidationError
from tenacity import (
    retry,
    retry_if_not_exception_type,
    wait_random_exponential,
    stop_after_attempt,
)
from typing import List

from .errors import NotAuthorizedException, NotFoundException

from .schema.pvsystem import (
    PvSystemMetaData,
    PvSystemsMetaData,
    PvSystemFlowData,
    PvSystemAggrDataV2,
)
from .schema.device import DeviceMetaData, DevicesMetaData
from .schema.service import ReleaseInfo

_LOGGER = logging.getLogger(__name__)
SW_BASE_URL = "https://api.solarweb.com/swqapi"
MAX_ATTEMPTS = 5


class Fronius_Solarweb:
    def __init__(
        self,
        access_key_id: str,
        access_key_value: str,
        pv_system_id: str = None,
        httpx_client: AsyncClient = None,
    ):
        """
        Create an Fronius Solarweb API client.

        :param access_key_id:  unique ID for the API key, e.g.
            "FKIAFEF58CFEFA94486F9C804CF6077A01AB". Access keys are 36
            characters long and start with the "FKIA" prefix.
        :param access_key_value: A secret value (GUID),
            e.g. "47c076bc-23e5-4949-37a6-4bcfcf8d21d6", which
            you need to know for authorization of API calls.
        :param pv_system_id (optional): Unique PV system ID,
            this can be provided or determined from a call to
            get_pvsystems_meta_data()
        :param httpx_client (optional)
        """
        self.access_key_id = access_key_id
        self.access_key_value = access_key_value
        self.pv_system_id = pv_system_id
        self.httpx_client = httpx_client or AsyncClient()

    @property
    def _common_headers(self):
        return {
            "Accept": "application/json",
            "AccessKeyId": self.access_key_id,
            "AccessKeyValue": self.access_key_value,
        }

    async def _check_api_response(self, response):
        if response.status_code == 401:
            _LOGGER.debug("Access unauthorised check solar.web access key values")
            raise NotAuthorizedException()
        if response.status_code == 404:
            _LOGGER.debug("Item not found check your PV system ID")
            raise NotFoundException()

        response.raise_for_status()
        # returns dict type not string
        return response.json()

    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        retry=retry_if_not_exception_type(
            (ValidationError, NotAuthorizedException, NotFoundException)
        ),
        stop=stop_after_attempt(MAX_ATTEMPTS),
    )  # raises tenacity.RetryError if max attempts reached
    async def get_api_release_info(self) -> ReleaseInfo:
        _LOGGER.debug("Listing SolarWeb api release info")
        r = await self.httpx_client.get(
            f"{SW_BASE_URL}/info/release",
            headers=self._common_headers,
        )
        json_data = await self._check_api_response(r)
        try:
            model_data = ReleaseInfo.model_validate(json_data)
        except ValidationError as e:
            _LOGGER.error(
                f"Unable to validate data receieved from SolarWeb api: '{json_data}'"
            )
            _LOGGER.error(e)
        return model_data

    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        retry=retry_if_not_exception_type(
            (ValidationError, NotAuthorizedException, NotFoundException)
        ),
        stop=stop_after_attempt(MAX_ATTEMPTS),
    )  # raises tenacity.RetryError if max attempts reached
    async def get_pvsystems_meta_data(self) -> list[PvSystemMetaData]:
        _LOGGER.debug("Listing PV systems meta data")
        r = await self.httpx_client.get(
            f"{SW_BASE_URL}/pvsystems",
            headers=self._common_headers,
        )
        json_data = await self._check_api_response(r)
        try:
            model_data = PvSystemsMetaData.model_validate(json_data).pvSystems
        except ValidationError as e:
            _LOGGER.error(
                f"Unable to validate data receieved from SolarWeb api: '{json_data}'"
            )
            _LOGGER.error(e)
        return model_data

    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        retry=retry_if_not_exception_type(
            (ValidationError, NotAuthorizedException, NotFoundException)
        ),
        stop=stop_after_attempt(MAX_ATTEMPTS),
    )  # raises tenacity.RetryError if max attempts reached
    async def get_pvsystem_meta_data(self) -> PvSystemMetaData:
        _LOGGER.debug("Listing PV system meta data")
        r = await self.httpx_client.get(
            f"{SW_BASE_URL}/pvsystems/{self.pv_system_id}",
            headers=self._common_headers,
        )
        json_data = await self._check_api_response(r)
        try:
            model_data = PvSystemMetaData.model_validate(json_data)
        except ValidationError as e:
            _LOGGER.error(
                f"Unable to validate data receieved from SolarWeb api: '{json_data}'"
            )
            _LOGGER.error(e)
        return model_data

    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        retry=retry_if_not_exception_type(
            (ValidationError, NotAuthorizedException, NotFoundException)
        ),
        stop=stop_after_attempt(MAX_ATTEMPTS),
    )
    async def get_devices_meta_data(self) -> list[DeviceMetaData]:
        _LOGGER.debug("Listing Devices meta data")
        r = await self.httpx_client.get(
            f"{SW_BASE_URL}/pvsystems/{self.pv_system_id}/devices",
            headers=self._common_headers,
        )
        json_data = await self._check_api_response(r)
        try:
            model_data = DevicesMetaData.model_validate(json_data).devices
        except ValidationError as e:
            _LOGGER.error(
                f"Unable to validate data receieved from SolarWeb api: '{json_data}'"
            )
            _LOGGER.error(e)
        return model_data

    @retry(
        wait=wait_random_exponential(multiplier=2, max=60),
        retry=retry_if_not_exception_type(
            (ValidationError, NotAuthorizedException, NotFoundException)
        ),
        stop=stop_after_attempt(MAX_ATTEMPTS),
    )
    async def get_system_flow_data(self, tz: str = "zulu") -> PvSystemFlowData:
        _LOGGER.debug("Listing PV system flow data")
        r = await self.httpx_client.get(
            f"{SW_BASE_URL}/pvsystems/{self.pv_system_id}/flowdata?timezone={tz}",
            headers=self._common_headers,
        )
        json_data = await self._check_api_response(r)
        try:
            model_data = PvSystemFlowData.model_validate(json_data)
        except ValidationError as e:
            _LOGGER.error(
                f"Unable to validate data receieved from SolarWeb api: '{json_data}'"
            )
            _LOGGER.error(e)
        return model_data

    async def get_system_aggr_data_v2(
        self, period: str = "total", channels: List[str] | None = None
    ) -> PvSystemAggrDataV2:
        _LOGGER.debug("Listing PV system aggregated v2 data")
        _url = f"{SW_BASE_URL}/pvsystems/{self.pv_system_id}/aggrdata?period={period}"
        if channels is not None:
            _url += f"&channel={','.join(channels)}"
        r = await self.httpx_client.get(
            _url,
            headers=self._common_headers,
        )
        json_data = await self._check_api_response(r)
        try:
            model_data = PvSystemAggrDataV2.model_validate(json_data)
        except ValidationError as e:
            _LOGGER.error(
                f"Unable to validate data receieved from SolarWeb api: '{json_data}'"
            )
            _LOGGER.error(e)
        return model_data
