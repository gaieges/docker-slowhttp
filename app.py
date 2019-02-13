import time
import os
import random

from aiohttp import web

SLOW_CALL = 5 #s
PERCENTAGE_SLOW = .1

async def handle(request):
  if random.random() < PERCENTAGE_SLOW:
    time.sleep(SLOW_CALL)

  return web.json_response({'success': True})


if __name__ == '__main__':
  app = web.Application()
  app.add_routes([web.get('/', handle)])
  web.run_app(app, port=os.getenv('PORT', '8000'), host='0.0.0.0')

