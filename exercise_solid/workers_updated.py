from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    
class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    
    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorker, Workable, Eatable):
    def __init__(self):
        super(Worker, self).__init__()

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker, Workable, Eatable):
    def __init__(self):
        super(SuperWorker, self).__init__()

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class WorkManager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()



class BreakManager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker, Workable):
    def __init__(self):
        super(Robot, self).__init__()

    def work(self):
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

