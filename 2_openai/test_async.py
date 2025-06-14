import asyncio

async def do_some_processing():
    await asyncio.sleep(1)
    return "Some"

async def do_other_processing():
    await asyncio.sleep(2)
    return "Other"

async def do_more_processing():
    return "More"

async def do_yet_more_processing():
    result = await do_more_processing()
    return result + ", " + "Yet More"

async def main():
    results = await asyncio.gather(
        do_some_processing(),
        do_other_processing(),
        do_yet_more_processing()
    )
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
