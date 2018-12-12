from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch
import pprint


async def get_page():
    browser = await launch()
    # context = await browser.createIncognitoBrowserContext()
    # page = await context.newPage()
    page = await browser.newPage()
    await page.goto("https://hackernoon.com/a-simple-introduction-to-pythons-asyncio-595d9c9ecf8c")
    html = await page.content()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    await browser.close()


# this is the event loop
loop = asyncio.get_event_loop()

# schedule both the coroutines to run on the event loop
loop.run_until_complete(asyncio.gather(get_page()))
