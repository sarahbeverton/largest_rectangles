Objective
This short programming activity will help your thought process about how to solve the Molecules programming challenge that is coming up. 

 

Goal
Write a small python function that will generate a list of rectangle tuples with integer dimensions (w, h). The width dimension can vary from 2 to 10 (not including 10). The height dimension should vary between whatever the width is and 10 (not including 10). The resulting list of tuples should be sorted in order from largest enclosed area to smallest.

To sort according to enclosed area, use the formula (w - 1) * (h - 1).  This will compensate for the off-by-1 indexing that is introduced by using the range() function for the w and h values.

Success Criteria
Your function is able to generate the following list of tuples. Ideally, it would take the form of a list comprehension.

[(9, 9), (8, 9), (8, 8), (7, 9), (7, 8), (6, 9), (7, 7), (6, 8), (5, 9),
 (6, 7), (5, 8), (6, 6), (4, 9), (5, 7), (4, 8), (5, 6), (4, 7), (3, 9),
 (5, 5), (4, 6), (3, 8), (3, 7), (4, 5), (3, 6), (4, 4), (2, 9), (3, 5),
 (2, 8), (2, 7), (3, 4), (2, 6), (2, 5), (3, 3), (2, 4), (2, 3), (2, 2)]
 

After studying this list of tuples, you might notice this table is not fully sorted in order of decreasing rectangle areas.  Recall this is because it is sorted by decreasing enclosed areas, which gives a different outcome than sorting by (w * h)

Think about how you might use a static list of rectangle sizes as a first step in your approach to solving the Molecules challenge.

 