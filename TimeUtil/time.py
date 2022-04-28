from time import time_ns, sleep


class Time:
    SECOND = 10 ** 9
    delta: float = 0

    @staticmethod
    def get_time() -> int:
        return time_ns()

    @staticmethod
    def get_delta() -> float:
        return Time.delta

    @staticmethod
    def set_delta(delta: float) -> None:
        Time.delta = delta

    @staticmethod
    def sleep_thread(amount: float) -> None:
        sleep(amount)
