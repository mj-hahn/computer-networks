## ELEC 373 Computer Networks - Course Project Final Report
Kevin Huang 10104718 - Matt Hahn  10104772 - Noam Hacker 10106436

### Task 1
`python task1.py`

Task 1 is organized as a separate function for each layer of the OSI model. A user inputs a message and the program passes it to the top layer (Application Layer), which then passes it down layer by layer to the bottom layer (Physical Layer). Each function performs the layer's duties and prints the progress along the way. Some notable layers are the Transport and Network Layers, which add a port and IP to the message's headers, and the Data Link Layer, which utilizes a find and replace to implement Bit Stuffing and converts the message into bytes using ascii-to-bytes with padding to ensure there are always eight 1s or 0s per letter.

![task1 image](https://github.com/MHahn37/cachemoney/blob/master/readme%20source%20images/Screen%20Shot%202017-03-31%20at%206.59.10%20PM.png)
<hr>

### Task 2

<hr>

### Task 3
`python task3.py`

Task 3 implements a undirected graph in python to act as network. There are six nodes in the current implementation with each connection being and edge with an associated delay. Nodes are labeled A, B, C, D, E, F and each delay for each node connection was abitrarily chosen. In the main function of the python program the graph is instantiated and a undirected graph is created (see below). Dijkstra's algorithm was created and called in main using dijkstra(g, 'a', 'e'), where 'a' is the starting node and 'e' is the destination node. An output of the of Dijksta's algorithm being used on the graph is shown below.

![task3 image](https://github.com/MHahn37/cachemoney/blob/master/readme%20source%20images/373%20graph.png)
![task3 image](https://github.com/MHahn37/cachemoney/blob/master/readme%20source%20images/Screen%20Shot%202017-03-31%20at%207.35.48%20PM.png)
<hr>

### Task 4
`python task4_server.py` `python task4_client.py`

Task 4 comprises of two programs: the server and the client. When the server is run, a socket is created and the server listens for text to enter the buffer. When the client is run, it connects to the same socket. As seen in the program output below, there are several stages of the program labeled alphabetically. 
* A: The client sends HELLO / the server listens for HELLO.
* B: The server sends an ACK / the client listens for an ACK.
* C: The client sends a requested filename / the server listens for a filename.
* D: The server sends the file (from the source folder) to the client / the client receives the file and saves it (in the destination folder).
* E: The client sends an ACK / the server listens for an ACK. Both programs terminate.

The programs consider both UDP and TCP.

![task4_image](https://github.com/MHahn37/cachemoney/blob/master/readme%20source%20images/Screen%20Shot%202017-03-31%20at%207.02.43%20PM.png)
