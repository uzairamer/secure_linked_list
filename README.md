# Secure Linked List
Secure Linked List allows multiple users to store their data in encrypted form and takes care of the following security principles:
# 1) Confidentiality
The data comes in the encrypted form from the user. So if the user doesn’t leak its key, the data will be remained confidential. Secondly, on every addition of the node, the server sends the ‘previous hash’ to the client. User is advised to make it confidential as well so the adversary will never know what block belongs to what user
# 2) Integrity
Since the data is hosted on a single trusted server, the server is maintaining all the
records. So integrity is there automatically. Of course for a big project, we’ll use some
sort of backup storage as well.
# 3) Availability
Running the server 24/7 will solve the availability principle.
# 4) Immutability
This is a private chain. A particular user can only modify its own data. User can never
access any other node. The trusted server will never attempt to mutate the data of the
users.

# Some Identified Security Threats
- No defenses against denial of service
- Users can try to send faulty packets because project is based on Socket Programming

# Dependencies
```sh
pip install python3
pip install hashlib
pip install pycryptodome
```
# Run Project
With all the dependencies in place, run **server_main.py** and the server will be started. Now run **client_main.py** It will ask some self-explanatory questions. That’s it.

# Features!
- Add new nodes to the Linked List
- Modify existing nodes in the Linked List
- Get your nodes back from the Linked List
- No node can be deleted once it has been inserted in to the Linked Lists