import logging
import asyncio

from aiocoap.resource import Resource as AiocoapResource
from aiocoap.resource import WKCResource as AiocoapWKCResource
from aiocoap.resource import Site as AiocoapSite
from aiocoap.message import Message as AiocoapMessage
from aiocoap.numbers import CHANGED
from aiocoap import Context as AiocoapContext

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

class InterfaceAdapter(AiocoapSite, AiocoapWKCResource):
    def __init__(self):
        self.site_root = AiocoapSite()
        self._add_well_known_core_resource()

    def _add_well_known_core_resource(self):
        self.site_root.add_resource([".well-known", "core"],
                                    AiocoapWKCResource(self.site_root.get_resources_as_linkheader))

    def add_resource(self, resource):
        self.site_root.add_resource(resource.path(), resource)

    async def run_as(self, role):
        if role == "server":
            await AiocoapContext.create_server_context(self.site_root)
        return await asyncio.get_event_loop().create_future()
