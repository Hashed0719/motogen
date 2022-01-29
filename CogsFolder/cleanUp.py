class MessageCleanUp:
    def __init__(self, ctx) -> None:
        self.ctx = ctx

    async def __aenter__(self) -> None:
        pass 
    
    async def __aexit__(self, *args) -> None:
        await self.ctx.message.delete(delay=4.0)
        