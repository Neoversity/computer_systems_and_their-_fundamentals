# import asyncio
# import concurrent.futures
# from time import time

# def blocks(n):
#     counter = n
#     start = time()
#     while counter > 0:
#         counter -= 1
#     return time() - start

# async def monitoring():
#     while True:
#         await asyncio.sleep(2)
#         print(f'Monitoring {time()}')

# async def run_blocking_tasks(executor, n):
#     loop = asyncio.get_event_loop()
#     print('waiting for executor tasks')
#     result = await loop.run_in_executor(executor, blocks, n)
#     return result

# async def main():
#     asyncio.create_task(monitoring())
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         futures = [run_blocking_tasks(executor, n) for n in [50_000_000, 60_000_000, 70_000_000]]
#         results = await asyncio.gather(*futures)
#         return results

# if __name__ == '__main__':
#     result = asyncio.run(main())
#     for r in result:
#         print(r)



# import requests
# from time import time

# urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']

# def preview_fetch(url):
#     r = requests.get(url)
#     return url, r.text[:150]

# if __name__ == '__main__':
#     start = time()
#     for url in urls:
#         r = preview_fetch(url)
#         print(r)
#     print(time() - start)


# import asyncio
# import requests
# from concurrent.futures import ThreadPoolExecutor
# from time import time

# urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']

# def preview_fetch(url):
#     r = requests.get(url)
#     return url, r.text[:150]

# async def preview_fetch_async():
#     loop = asyncio.get_running_loop()

#     with ThreadPoolExecutor(3) as pool:
#         futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
#         result = await asyncio.gather(*futures, return_exceptions=True)
#         return result

# if __name__ == '__main__':
#     start = time()
#     r = asyncio.run(preview_fetch_async())
#     print(r)
#     print(time() - start)






import asyncio
from aiofile import async_open

async def main():
    async with async_open("hello.txt", 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world\\n")
        await afp.write("Hello from - async world!")

if __name__ == '__main__':
    asyncio.run(main())
