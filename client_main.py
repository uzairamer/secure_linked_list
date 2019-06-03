from models import DataNode
from multiprocessing.connection import Client
from cryptography.fernet import Fernet


def get_user_key():
    key = None
    print('Do you have a key? Press y or Y for yes otherwise n or N')
    have_a_key = input()
    if have_a_key == 'y' or have_a_key == 'Y':
        with open('mykey.secret', 'rb') as my_secret_key:
            key = my_secret_key.read()
            print('Key acquired')
    else:
        print('Please enter a secure password: ')
        password = input()
        with open('mykey.secret', 'wb') as my_secret_key:
            key = Fernet.generate_key()
            my_secret_key.write(key)
            print('Your secret key is ', key)
    return key


def create_new_node(key):
    print('Enter data for node: ')
    user_input = input()
    user_fern = Fernet(key)
    user_data_encrypted = user_fern.encrypt(user_input.encode('utf-8'))
    return DataNode(data=user_data_encrypted)


if __name__ == '__main__':
    address = ('localhost', 1470)
    client = Client(address, authkey=b'secureLinkedListProject')

    # get user key
    key = get_user_key()

    # filter user's request
    print('To add a node type "a", to modify a node type "m", to get a node type"g"')
    user_input = input()

    final_send_request = None

    if user_input == 'm':
        print('Enter that node\'s previous_hash')
        previous_hash = input()
        d = create_new_node(key)
        final_send_request = ('m', d, previous_hash)

    elif user_input == 'a':
        d = create_new_node(key)
        final_send_request = ('a', d)

    elif user_input == 'g':
        print('Enter that node\'s previous_hash')
        previous_hash = input()
        final_send_request = ('g', previous_hash)

    client.send(final_send_request)
    previous_hash = client.recv()
    print('Please keep this private: Hash to lookup your node is ', previous_hash)
    client.close()

