import logging

from aiocoap.resource import Resource as AiocoapResource
from aiocoap.message import Message as AiocoapMessage
from aiocoap.numbers import CHANGED

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InterfaceResource(AiocoapResource, AiocoapMessage):
    def __init__(self, resource_name):
        super().__init__()
        self.resource_name = resource_name
        self.content = ""

    def path(self):
        return [self.resource_name]
    
    async def render_get(self, request):
        return AiocoapMessage(payload=self.content.encode("utf-8"))

    async def render_put(self, request):
        self.content = request.payload.decode("utf-8")
        logger.info(f"Resource {self.resource_name} updated with value {self.content}")
        return AiocoapMessage(code=CHANGED, payload=self.content.encode("utf-8"))

class InterfaceAdapter:
    pass

    def add_resource(self, resource):
        pass

    def run_as(self, role):
        pass
