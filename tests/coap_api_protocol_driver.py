import asyncio
import aiocoap import Context, Message, GET, POST


class CoapApiProtocolDriver(Context, Message):
    async def __init__(self):
        protocol = await Context.create_client_context()

    async def show_measurement_sample(self, measurement_type):
        request = Message(code=GET, uri="coap://localhost:5683/" + measurement_type)

        try:
            response = await self.protocol.request(request).response
        except Exception as e:
            sys.exit(1)
        pass
    
    def send_measurement_sample(self, measurement_type, measurement_value):
        pass