# You are given 20 jobs. Each job takes a different amount of time to process. Implement
# a function process_job which will do the following:

# 1. Print when Job starts.
# 2. Wait for random duration between 1 and 3 seconds
# 5. Print when job completes
# 6. Return the process job id


import asyncio
import random
import time

async def process_job(job_id: int) -> int:
   
    print(f"Job {job_id} started.")

    duration: float = random.uniform(1, 3)

    await asyncio.sleep(duration)

    print(
        f"Job {job_id} completed "
        f"in {duration:.2f} seconds."
    )

    return job_id


# Now create an async job runner func run_jobs . The following conditions must be met.

# 1. All 20 jobs must eventually be processed.
# 2. A maximum of 3 jobs may run simultaneously.
# 3. Collect and return the results of all completed jobs.
# 4. Print the total execution time.


async def run_jobs(job_ids: list[int]) -> list[int]:

    semaphore = asyncio.Semaphore(3)

    async def run_with_limit(job_id: int) -> int:

        async with semaphore:
            return await process_job(job_id)

    start_time: float = time.time()

    tasks = [
        run_with_limit(job_id)
        for job_id in job_ids
    ]

    results: list[int] = await asyncio.gather(*tasks)

    end_time: float = time.time()

    total_time: float = round(end_time - start_time)

    print("\nAll jobs completed.")
    print(f"Total execution time: {total_time:.2f} seconds.")

    return results


async def main() -> None:

    jobs: list[int] = list(range(1, 21))

    results: list[int] = await run_jobs(jobs)

    print(f"\nCompleted Job IDs: {results}")


if __name__ == "__main__":
    asyncio.run(main())
