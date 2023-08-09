from tasks import add


def run():
    while True:
        result = add.delay(2, 3)
        result.get(timeout=0)


if __name__ == '__main__':
    run()
