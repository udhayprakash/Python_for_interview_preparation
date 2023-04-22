Variables: In computer science programming, we need something for holding data, and variables
is the way to do that.

Data Type: A data type in a programming language is a set of data with predefined values.
Ex: integer, floating point, unit number, character, string, etc.
Computer memory is all filled with zeros and ones.
As it is difficult to code with 0s & 1s, programming languages & compilers provide
us with data types.

    		bits   - 0 , 1
    		nibble - 4 bits - 0101
    		byte   - 8 bits - 0101 0011


    		int     - 2 bytes  - 16 bits
    		float   - 4 bytes  - 32 bits
    		char    - 1 byte

       At top level, there are two types of data types:
    	1) System-defined data types (also called Primitive data types)
    		: int, float, char, double, bool, etc
    		: The number of bits allocated for each primitive data type depends on the
    		   programming languages, the compiler and the OS
    		: For the same primitive data type, different languages may use different
    		   sizes. Depending on the size of the data types, the total available values
    		   (domain) will also change.
    		  int - 2 bytes - 16 bits ->(-2^15 to 2^15 -1)-> -32,768 to 32,767
    			  - 4 bytes - 32 bits ->(-2^31 to 2^31 -1)-> -2,147,483,648 to -2,147,483,647
    	2) User-defined data types
    		: structures in C/C + + and classes in Java/python

    			class MyClass:
    				class_var1 = 123
    				class_var2 = 123.123
    				def __init__(self):
    					pass

    			struct newType{
    				int data1;
    				float data2;
    			}

Data Structures:
It is a particular way of storing and organizing data in a computer so that it can
be used efficiently.
It is a special format for organizing and storing data.
General data structure types include arrays, files, linked lists, stacks, queues,
trees, graphs and so on.

        Analogy
            drinking                - glass of water            - glass
            watering plants         - mug of water              - mug
            taking shower           - bucket of water           - bucket
            farming your field      - container of water        - container

        Depending on the organization of the elements, data structures are classified into two types:
        1) Linear data structures:
                Elements are accessed in a sequential order but it is not compulsory to store all elements sequentially.
                Examples: Linked Lists, Stacks and Queues.

        2) Non – linear data structures:
                Elements of this data structure are stored/accessed in a non-linear order.
                Examples: Trees and graphs.

                       12         preorder, postorder, inorder
                      /    \
                      3
                    /   \
                    1    2

Abstract Data Types (ADTs): - user defined data types are defined along with their operations - ADT contains two parts:
a) Declaration of data
b) Declaration of operations

                class MyClass:
                    def __init__(self):
                        self.a = 1121
                        self.b = 1232

                    def __add__(self, object):
                        pass

                        ....

    - Commonly used ADTs include: Linked Lists, Stacks, Queues, Priority Queues, Binary Trees,
        Dictionaries, Disjoint Sets (Union and Find), Hash Tables, Graphs, and many others.
    - Ex: For stack,
        - creating the stack
        - pushing an element onto the stack
        - popping an element from stack
        - finding the current top of the stack
        - finding number of elements in the stack, etc.
    - Different kinds of ADTs are suited to different kinds of applications, and some are highly specialized to specific tasks.

Algorithms: - An algorithm is the step-by-step unambiguous instructions to solve a given problem. - Quality of Algorithm can be expression as its - correctness - solving the problem - Efficiency - how much resources ( time & memory) are used - Algo analyses - Algorithm analysis helps us to determine which algorithm is most efficient in terms of time and space consumed - Why Algo analysis - For traveling from city A to city B - by flight - by bus - by bike - by bicycle - by walk - Algorithm analysis helps us to determine which algorithm is most efficient in terms of time and space consumed.

    - Goal of Algo Analysis
        - To compare algorithms (or solutions) mainly in terms of running time but also
          in terms of other factors (e.g., memory, developer effort, etc.)

Running Time Analyses:
It is the process of determining how processing time increases as the size of the problem (input size) increases.
Input size is the number of elements in the input, and depending on the problem type, the input may be of different types.
The following are the common types of inputs.
• Size of an array
• Polynomial degree
• Number of elements in a matrix
• Number of bits in the binary representation of the input
• Vertices and edges in a graph.

How to compare Algorithms - Parameters - Execution Times? - But, it depends on particular computer, so cant use it. - Number of statements executed? - Not a good measure, since the number of statements varies with the programming language as well as the style of the individual programmer

    			n1 = 12
    			n2 = 34
    			n3 = n1 + n2
    			print(n3)

    			n3 = 12 + 34
    			print(n3)

    			print(12 + 34)

    - Ideal Solution
    	-> we express the running time of a given algorithm as a function of the input
    	   size n (i.e., f(n)) and compare these different functions corresponding to running times.
    	-> This kind of comparison is independent of machine time, programming style, etc

Rate of Growth - The rate at which the running time increases as a function of input. - Ex1:
TotalCost = cost_of_car + cost_of_bicyle
TotalCost ~= cots_of_car(approximation)
as cost of bicycle is very small in order compared to that of car - Ex2:
n^4 + 2n^2 + 100n + 500 ~= n^4

- Decreasing rate of Growth
  - 2 ^ 2 ^ n
  - n!
  - 4 ^ n
  - 2 ^ n
  - n^2
  - n log n
  - log(n!)
  - n
  - 2 ^ (log n)
  - log^2 n
  - sqrt(log n)
  - log log n
  - 1

Time complexity - TODO - fail=r

Types of Analyses - To analyze the given algorithm, we need to know with which inputs the algorithm takes less time (performing wel1) and with which inputs the algorithm takes a long time.

    - Worst case
        ○ Defines the input for which the algorithm takes a long time (slowest
        time to complete).
        ○ Input is the one for which the algorithm runs the slowest.
    -  Best case
        ○ Defines the input for which the algorithm takes the least time (fastest
        time to complete).
        ○ Input is the one for which the algorithm runs the fastest.
    -  Average case
        ○ Provides a prediction about the running time of the algorithm.
        ○ Run the algorithm many times, using many different inputs that come
        from some distribution that generates these inputs, compute the total
        running time (by adding the individual times), and divide by the
        number of trials.
        ○ Assumes that the input is random

    - Lower Bound <= Average Time <= Upper Bound

Asymptotic Notation - The word Asymptotic means approaching a value or curve arbitrarily closely
(i.e., as some sort of limit is taken). - Asymptotic notations are the mathematical notations used to describe the running time of an algorithm when the input tends towards a particular value or a limiting value. - There are three types of asymptotic notations to represent the growth of any
algorithm, as input increases: - Big Oh(O) - Best case - upper bound - Big Omega (Ω) - worst case - - Big Theta (Θ) - Average case

    - Big-O Notation [Upper Bounding Function]
        - f(n) = n^4 + 100n^2 + 10n + 50
        - f(n) = O(g(n))

f(n) = 3n + 8
f(1) = 3(1) + 8 = 11 :- 4n = 4(1) = 4
f(5) = 3(5) + 8 = 23 :- 4n = 4(5) = 20
f(8) = 3(8) + 8 = 32 :- 4n = 4(8) = 32
f(1000) = 3(1000) + 8 = 3008 :- 4n = 4(1000) = 4000

    3n + 8 ≤ 4n, for all n ≥ 8

so, 3n + 8 = O(n) with c = 4 and n0 = 8

Q) f(n) = n^2 + 1

f(0) = 0^2 + 1 = 1 :- 2n^2 = 2(0)^2 = 0
f(1) = 1^2 + 1 = 2 :- 2n^2 = 2(1)^2 = 2
f(5) = 5^2 + 1 = 26 :- 2n^2 = 2(5)^2 = 50

n^2 + 1 ≤ 2n^2, for all n ≥ 1
so, n^2 + 1, for all n ≥ 1

Q) f(n) = n^4 + 100n^2 + 50

n^4 + 100n^2 + 50, for n ≥ 11
So, n^4 + 100n^2 + 50 = O(n^4) with c = 2 and n0 = 11

NO Uniqueness
There is no unique set of values for n0 and c in proving the asymptotic bounds.

Omega-Q Notation [Lower Bounding Function]

    f(n) = Ω(g(n))
    at larger values of n, the tighter lower bound of f(n) is g(n)

f(n) = 100n^2 + 10n + 50 => g(n)= Ω(n^2)

Theta-Θ Notation [Order Function]
This notation decides whether the upper and lower bounds of a given function (algorithm) are the same. The average running time of an algorithm is always between the lower bound and the upper bound. If the upper bound (O) and lower bound (Ω) give the same result, then the Θ notation will also have the same rate of growth.

Θ(g(n)) = {f(n): there exist positive constants c1,c2 and n0 such that
0 ≤ c1g(n) ≤ f(n) ≤ c2g(n) for all n ≥ n0}
