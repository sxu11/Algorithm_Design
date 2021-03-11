from threading import Lock


class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for i in range(5)]

        # call the functions directly to execute, for example, eat()

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        right = (philosopher + 1) % 5
        left = philosopher
        if philosopher % 2 == 0:
            self.locks[right].acquire()
            self.locks[left].acquire()
        else:
            self.locks[left].acquire()
            self.locks[right].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        if philosopher % 2 == 0:
            self.locks[left].release()
            self.locks[right].release()
        else:
            self.locks[right].release()
            self.locks[left].release()

