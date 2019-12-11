import threading
from time import sleep

num_of_philosophers = int(input("Enter number of Philosophers"))
forks = [] 
for i in range(num_of_philosophers):
    forks.append(threading.Lock())
    forks.append(i+1)

class Philosopher(threading.Thread):
    def __init__(self, name, counter, forks = [], *args):
        threading.Thread.__init__(self)
        self.__name = name
        self.__counter = counter
        if(counter == len(forks) / 2 - 1):
            self.__lock_left_fork = forks[counter + counter]
            self.__lock_right_fork = forks[0]
            self.__left_fork = forks[counter + counter + 1]
            self.__right_fork = forks[1]
        else:
            self.__lock_left_fork = forks[counter + counter]
            self.__lock_right_fork = forks[counter + counter + 2]
            self.__left_fork = forks[counter + counter + 1]
            self.__right_fork = forks[counter + counter + 3]

    def take_forks(self):
        self.__lock_left_fork.acquire()
        self.__lock_right_fork.acquire()   
        print(self.__name, self.__counter + 1, "is hungry")
        print(self.__name, self.__counter + 1, "picks forks", self.__left_fork, "and", self.__right_fork); 
        print(self.__name, self.__counter + 1, "is eating")

    def put_forks(self):
        self.__lock_left_fork.release()
        self.__lock_right_fork.release()
        print(self.__name, self.__counter + 1, "puts down forks", self.__left_fork, "and", self.__right_fork)
        print(self.__name, self.__counter + 1, "is thinking")

    def run(self):
        while(True):
            sleep(self.__counter + 3)
            self.take_forks()       
            sleep(self.__counter + 3)
            self.put_forks()

def diningPhilosophers():
    threads = []
    philosophers = []

    for i in range(num_of_philosophers):
        philosophers.append(Philosopher("philosopher", i, forks))

    for i in range(len(philosophers)):
        philosophers[i].start()
        sleep(1)

    for i in range(len(philosophers)):
        threads.append(philosophers[i])

    for thread in threads:
        thread.join()

diningPhilosophers() 