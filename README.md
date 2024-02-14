# Data Structures Coursework

## Overview

In this Data Structures course, I delve into the intricacies of abstract data types such as arrays, stacks, queues, lists, trees, and graphs. My approach combines the design of data structures and algorithms to implement them effectively, using Python as the primary language. Throughout this journey, I emphasize the practical application of these data structures to design solutions for complex problems, while also focusing on the critical analysis of space and time complexity. This ensures not only a deep understanding of data structures but also the ability to evaluate and optimize the efficiency of algorithms.

Leveraging Python for its readability and the extensive support of its libraries, I aim to make the learning process both intuitive and impactful. This choice facilitates a clear demonstration of data structure principles and algorithmic strategies, making it accessible for learners at various levels. By the end of the course, I expect to have developed a solid foundation in both fundamental and advanced data structures, honed my skills in algorithm design and implementation, and gained proficiency in computational complexity analysis. This knowledge will empower me to apply data structures creatively and efficiently in solving real-world problems, enhancing my capabilities in software development and computational problem-solving.

## Objective 

- Master Abstract Data Types with Python
- Design and Implement Efficient Data Structures and Algorithms
- Solve Real-world Problems Using Data Structures
- Exploit Python for Effective Data Structure Implementation
- Strengthen Problem-solving with Appropriate Data Structures
- Build Foundation for Advanced Computational Challenges

## Assignment 1 (Theatre Seats Calculator)

The Yorktown theatre has 300 hall seats and 100 mezzanine seats. A hall seat costs $10 for an adult and $7 for a child. A mezzanine seat costs $8 for an adult and $5 for a child. Write a program to REPEATEDLY prompt the user to enter the required seating (1 for hall, 2 for mezzanine), the number of adults and children in the party, and the print out a receipt and the number of remaining seats in Hall and Mezzanine. An order will be refused if there are not enough seats in the required area. The program loops until there are no more seats in either hall or mezzanine.  

Sample interaction:

```
Enter 1 for Hall and 2 for Mezzanine: 1
Number of adults? 2
Number of children? 3
 
Great, You got 2 adult tickets for $20 and 3 child tickets for $21 so your total is $41
Remaining seats: Hall 295 Mezzanine 100

Enter 1 for Hall and 2 for Mezzanine: 2
Number of adults? 1
Number of children? 4
 
Great, You got 1 adult tickets for $8 and 4 child tickets for $20 so your total is $28
Remaining seats: Hall 295 Mezzanine 95
```

## Assignment 2 (Binary and Linear Search)

Write a program that:
```
a.	Generates 5000 random numbers and puts them in an array.
b.	Sorts the numbers using any sorting technique (Selection sort is fine, but you can try another one).  
c.	Ask the user for a number between 0 and 20,000 and search for it in your sorted array using a simple linear search. Is this a good idea?
d.	Ask the user for a number between 0 and 20,000 and search for it in your sorted array using a binary search.
```

Hint: To generate random numbers you need to include this module:
import random
To get a random number w :  

```
w = random.randint(0,20000) 
```

This will give w a random value between 0 and 20,000


## Assignment 3 (Product Linked List)

A greengrocer would like to maintain a linked lists about his products. For each product he saves it name, price and stock amount.
Write a program that creates an empty linked list and then prompts to user to do one of the following:

1. Add a product to the list (anywhere)
2. Print all products in the LinkedList
3. Print all products above a certain price
4. Print all low-stock products ( Less than 20 pounds)
5. Exit

Hint: The trick here is to make a node with 4 parts: one for the produce name, one for the price, one for the stock and one a ref to the next node.
```
class Node:
     def __init__(self, nm, pr, st):
         self.name = nm
         self.price = pr
         self.stock = st
         self.ref = None
```


## Assignment 4 (Stacks: Check Brackets)

Stacks are used to check that parentheses match in an equation.
Write a program that asks the user to input a string containing parentheses of the three types:   "( )",  "[  ]", and "{  }" and then tell him/her whether they are right or wrong.

For example:

```
Abc(xyz)mnv             Correct
Abc(xyz]bnm             Wrong mismatched brackets
Abc( xcvbnm,m           Wrong bracket opened but never closed
Abc(cvb{bgt}vde)dfg     Correct
Abc(fgfd{gg)dfg}nn      Wrong mismatched brackets
Abc)nmg                 Wrong bracket closed but never opened 

```

Hint: The trick here is to  push an “open” bracket to the stack and pop when you find a “closed” bracket 


## Assignment 5 (University Record Hashing)

The university registrar uses hash tables to find student records quickly.  It is a small university with about 4000 students. Write a  program for hashing (use either chaining or probing) to save the records in. Have a menu with the following options:
```
1.	Add a new student number to the hash table 
2.	Print out the hash table
3.	Find a student’s record using his/her number
4.	(optional) Delete a student record (careful if you use probing!)
5.	Exit
```
