import asyncio
from server import Server
from aiocoap_adapter import InterfaceResource, InterfaceAdapter


async def main():
    interface = InterfaceAdapter()
    server = Server(interface)
    server.add_resource_to_interface(InterfaceResource("temperature"))
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())