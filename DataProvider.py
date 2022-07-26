import time

from DataProcessor import DataProcessor
from DataPrinter import DataPrinter

start_time = time.time()


def main():
    for number in range(1, 10):
        DataProcessor(api_url=f'https://jsonplaceholder.typicode.com/todos',
                      number=number).get_answer()
        DataPrinter(DataProcessor(api_url=f'https://jsonplaceholder.typicode.com/todos',
                                  number=number).get_answer(),
                    "/home/tech/Documents/Tasks/trash",#"C:/Projects/trash",
                    "test.csv").write_to_csv()


if __name__ == "__main__":
    main()
