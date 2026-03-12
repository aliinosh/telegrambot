from aiohttp import web

async def health(request):

    return web.Response(text="Bot is running")

app = web.Application()

app.router.add_get("/health", health)

if __name__ == "__main__":

    web.run_app(app)
