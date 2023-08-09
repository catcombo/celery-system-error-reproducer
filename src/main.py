from concurrent import futures

from tasks import add


def celery_task(i: int) -> int:
    result = add.delay(1, i)
    return result.get(timeout=None)


def run():
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            print("start tasks")
            future_to_value = {executor.submit(celery_task, number): number for number in range(500)}
            for future in futures.as_completed(future_to_value):
                number = future_to_value[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print(f'Task {number} generated an exception: {exc}')
                else:
                    print(f'Task {number} result: {data}')


if __name__ == '__main__':
    run()
