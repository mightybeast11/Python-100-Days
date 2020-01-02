from time import time, localtime, sleep

# A class method is a method which is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and
#   not the object instance.
# It can modify a class state that would apply across all the instances of the class.
#   For example it can modify a class variable that will be applicable to all the instances.

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):  # default values are 0.
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
        # set the class parameters: _hour = ctime.tm_hour
        #                           _minute = ctime.tm_min
        #                           _second = ctime.tm_sec

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
