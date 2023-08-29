#!/usr/bin/env python3
"""Script that random awaits and eventually
returns the value"""

import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    random_delay = await wait_random()
    print(f"Waited for {random_delay: .2f} seconds.")

if __name__ == '__main__':
    asyncio.run(main())
    