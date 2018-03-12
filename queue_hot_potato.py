from queue import Queue


def hot_potato(name_list, num):
    """ A general simulation of Hot Potato. The program will input a list of
    names and a constant, call it “num” to be used for counting. It will
    return the name of the last person remaining after repetitive counting
    by num.

    Args:
        name_list (list(str)) : list of strings representing each player
        num (int) : the counting amount

    Returns:
        str : the name of the last person remaining after repetitive counting
        by num.
    """
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
        while sim_queue.size() > 1:
            for i in range(num):
                sim_queue.enqueue(sim_queue.dequeue())
            sim_queue.dequeue()
    return sim_queue.dequeue()


print(hot_potato(["Tom", "Nicola", "Tracy", "Baratham", "Bob", "Ben"], 7))
