from models import DataNode, SecureLinkedList
from multiprocessing.connection import Listener
import threading


# Globals
sll = None


def listener_thread():
    address = ('localhost', 1470)  # family is deduced to be 'AF_INET'
    while True:
        with Listener(address, authkey=b'secureLinkedListProject') as listener:
            with listener.accept() as conn:
                print('Connection established with ', listener.last_accepted)
                recv = conn.recv()

                if recv[0] == 'a':
                    print('It\'s an add request')
                    sll.insert(recv[1])
                    conn.send(sll.get_head_node().get_previous_hash())
                elif recv[0] == 'm':
                    print('It\'s a modification request')
                    previous_hash = sll.modify_node(recv[2], recv[1])
                    conn.send(previous_hash)
                elif recv[0] == 'g':
                    print('It\'s a get request')
                    conn.send(sll.find_node(recv[1]))

                print(sll.get_count())
                print(sll.get_head_node().get_previous_hash())


if __name__ == '__main__':
    sll = SecureLinkedList()
    listener_th = threading.Thread(target=listener_thread)
    listener_th.start()
    print('We started the thread')
    # basically WaitForSingleObject() as in Windows System Programming ;)
    listener_th.join()
