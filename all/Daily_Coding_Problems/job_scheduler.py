#!/usr/bin/python
"""
Purpose: This problem was asked in Apple.
    Implement a job scheduler which takes in a function f and an integer n,
    and calls f after n milliseconds.
"""


def task_1(args, kwargs):
    print("Hello world !!!", args)
    print("Hello world !!!", kwargs)


def job_scheduler(interval, func, *_args, **_kwargs):
    """
    This Job scheduler function will take as function func  and the time
    interval, interval, and runs that after interval milliseconds.

    As time.sleep expects in seconds, given interval must be converted
    from milliseconds to seconds.
    1 sec == 1000 milliseconds
    1 millisecond = 0.001 second

    :param interval:
    :param func:
    :return:
    """
    import time

    time.sleep(interval * 0.001)
    func(_args, _kwargs)


if __name__ == "__main__":
    job_scheduler(20000, task_1, a="apple")
    job_scheduler(200, task_1, a="apple")
