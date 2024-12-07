import aiohttp
import asyncio

class AsyncAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def fetch_users(self):
        url = f"{self.base_url}/users"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to fetch users: {response.status}")

async def main():
    client = AsyncAPIClient("https://jsonplaceholder.typicode.com")
    try:
        users = await client.fetch_users()
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
