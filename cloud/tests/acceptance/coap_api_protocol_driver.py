import asyncio
import logging

from aiocoap import *
from aiocoap.numbers import GET, PUT

from util.util import create_coap_uri

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HOST_ADDRESS = "datacollector" #"127.0.0.1" never stops with this address

class TransportTuner(TransportTuning):
    def __init__(self):
        super().__init__()
        self.MAX_RETRANSMIT = 0

class CoapApiProtocolDriver(Context, Message):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.client = self.loop.run_until_complete(Context.create_client_context())

    def show_measurement_sample(self, measurement_type):
        request = Message(code=GET,
                        uri=create_coap_uri(resource_path=measurement_type, address=HOST_ADDRESS),
                        transport_tuning=TransportTuner())
        return self.loop.run_until_complete(self.request_resource(request))

    async def request_resource(self, request):
        try:
            response = await self.client.request(request).response
            return response.payload.decode("utf-8")
        except Exception as e:
            logger.error(f"Failed to request resource: {e}")
        
    
    def send_measurement_sample(self, measurement_type, measurement_value):
        request = Message(code=PUT,
                        uri=create_coap_uri(resource_path=measurement_type, address=HOST_ADDRESS),
                        payload=str.encode(measurement_value),
                        transport_tuning=TransportTuner())
        self.loop.run_until_complete(self.request_resource(request))