import asyncio
import logging
from aiocoap import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CoapApiProtocolDriver(Context, Message):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.client = self.loop.run_until_complete(Context.create_client_context())

    def show_measurement_sample(self, measurement_type):
        request = Message(code=GET, uri="coap://datacollector:5683/" + measurement_type)
        return self.loop.run_until_complete(self.fetch_resource(request))

    async def fetch_resource(self, request):
        try:
            response = await self.client.request(request).response
        except Exception as e:
            logger.error(f"Failed to fetch resource: {e} with response code {response.code}")
    
    def send_measurement_sample(self, measurement_type, measurement_value):
        pass