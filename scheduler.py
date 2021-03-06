#!/usr/bin/env python
import time
import schedule
from cases_per_10k_view import update


def main():
    print('running an update now..')
    update()

    schedule.every().day.at("00:00").do(update)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
