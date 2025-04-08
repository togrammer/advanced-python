import aiohttp
import aiofiles
import asyncio
import os


async def download_image(session, filename):
    async with session.get(url="https://thispersondoesnotexist.com/") as response:
        if response.status == 200:
            async with aiofiles.open(filename, "wb") as f:
                await f.write(await response.content.read())
            print("Downloaded:", filename)
        else:
            print("Failed to download:", filename)


async def download_all(num_images, folder):

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_images):
            filename = os.path.join(folder, f"image_{i}.jpg")
            tasks.append(download_image(session, filename))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    num_images = int(input("Enter number of images to download: "))
    folder = "artifacts"
    if not os.path.exists(folder):
        os.makedirs(folder)
    asyncio.run(download_all(num_images, folder))
