import asyncio
import logging
from aiocoap import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CoapApiProtocolDriver(Context, Message):
    async def __init__(self):
        self.protocol = await Context.create_client_context()

    async def show_measurement_sample(self, measurement_type):
        request = Message(code=GET, uri="coap://datacollector:5683/" + measurement_type)

        try:
            response = await self.protocol.request(request).response
        except Exception as e:
            logger.error(f"Failed to fetch resource: {e} with response code {response.code}")
    
    def send_measurement_sample(self, measurement_type, measurement_value):
        pass