import time

from DataProcessor import DataProcessor

start_time = time.time()


def main():
    tasks = []
    for number in range(1, 10):
        # answer = await DataProcessor(api_url=f'https://jsonplaceholder.typicode.com/todos',
        #                              number=number).get_answer()
        DataProcessor(api_url=f'https://jsonplaceholder.typicode.com/todos',
                      number=number).get_answer()
    # ioloop = asyncio.get_event_loop()
    # wait_tasks = asyncio.wait(tasks)
    # ioloop.run_until_complete(wait_tasks)
    # ioloop.close()



if __name__ == "__main__":
    main()