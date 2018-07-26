__author__ = 'Preston Sheppard'
import multiprocessing as mp
import time
def worker(number):
    name = mp.current_process().name
    print(name, "is starting")
    time.sleep(5)
    print(name, "is exiting")
    return 5

if __name__ == "__main__":
    pool = mp.Pool(processes=5)
    done1 = pool.map(worker, range(2))
    # for i in range(5):
    #     p = mp.Process(target=worker, args=(i,), name="worker " + str(i)) #args must be serializable with pickle
    #     jobs.append(p)
    #
    # for job in jobs:
    #     job.start()
    #
    # for job in jobs:
    #     a = job.join()
    #     print(a)
    #
    # print("this should happen at the end")