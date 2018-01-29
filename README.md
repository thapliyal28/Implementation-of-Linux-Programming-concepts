# Implementation-of-Linux-Programming-concepts

It consists of 1 driver program(ece650-a3.cpp) and 3 sub programs attached as 3 files in the repository(rgen.cpp,ece650.a1py,ece650-a2.cpp).
Rgen is written in C++.Which is random street generator and continuously produces streets name and coordinates as its output.Now this output act as a command line input for the second program written in python ece650.a1.py,which in result of these streets produces a graph in form of vertices and edges,according to given specs.

There is a vertex corresponding to: (a) each intersection, and, (b) the end-point of a line segment of a street that intersects with another street.
There is an edge between two vertices if: (a) at least one of them is an intersection, (b) both lie on the same street, and, (c) one is reachable from the other without traversing another vertex.


The output of this program acts as a input for third program written in c++ (ece650-a2.cpp),which utilizes two inputs one from second program as well as other from the user in form of command line argument like s 1 2,where 1 and 2 are vertices.Finally  the third program utlizies these inputs and produces an output which is shortest path between vertex 1 and 2.

The final program ece650-a3.cpp is a driver program.It has the overall control.It consists of fork and pipe and exec commands which are utilized to connect and run other child programs. 

Program can run in following manner using command prompt and cmake file
$ cd build
$ cmake ../
$ make install
$ cd ./run/bin
$ ./ece650-a3 
V = 8
E = {<0,2>,<0,3>,<0,4>,<1,3>,<4,7>,<5,2>,<5,6>}
s 2 4
2-0-4

where V E and S are input and 2-0-4 is the output
