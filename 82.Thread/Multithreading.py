from threading import *
from time import sleep

class One(Thread):
   def run(self):
        for i in range(5):
            print("Zakir")
            sleep(1)


class Two(Thread):
    def run(self):
        for j in range(5):
            print("Keya")
            sleep(1)

t1=One()
t2=Two()

t1.start()
sleep(0.2)
t2.start()

t1.join()

t2.join()

print("Bye")