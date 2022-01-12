# Assignment: Solve NQueens Problem
## Objectives:
###Objective 1 : Using the steepest Hill climb algorithm
###Objective 2: Using the Genetic algorithm

###Solution:
- genetic.py : Executes the genetic algorithm
- nqueens_common.py: Contains some common utilities 
- hillclimb_new.py : Executes steepest ascend (no side passes allowed)


#Execution :
- genetic.py and hillclimb_new.py can be executed individually but both needs nqueens_common.py
- install all the dependencies in the import statement.

#Controls :
Two parameters you need to control
1. No of Queens :- you know what this is
2. No. of Episodes :
   1. This decides how many attempts your algorithm is going to make to get a solution
   2. For Genetic Algo, the higher the number of episodes more time it takes for the run, but it never fails
   3. Hill climb may fail with a small number of episodes choose higher numbers wisely.
   4. The count of episodes in the output report starts from 0(only for reporting)

#Output : 
1. A sample output of hill climb
- Enter the number of Queens : 6
- Enter the number of Episodes : 10
- Episode: 0
- Number of episodes: 10
- Number of successful episodes: 2
- Average step per successful episode: 2.0
- Success Percentage: 50.0
- Number of unsuccessful episodes: 8
- Average step per unsuccessful episode: 2.25
- [[0 0 0 1 0 0]
-  [1 0 0 0 0 0]
-  [0 0 0 0 1 0]
-  [0 1 0 0 0 0]
-  [0 0 0 0 0 1]
-  [0 0 1 0 0 0]]
- [[0 1 0 0 0 0]
-  [0 0 0 1 0 0]
-  [0 0 0 0 0 1]
-  [1 0 0 0 0 0]
-  [0 0 1 0 0 0]
-  [0 0 0 0 1 0]]
- Total Time in seconds : 0.0506289005279541


2. A sample output of genetic algo:-
Enter Number of Queens: 6
Enter Number of Episodes: 1
Episode: 0
Generation: 0
Generation: 1
Generation: 2
Generation: 3
Generation: 4
Generation: 5
Generation: 6
Generation: 7
Generation: 8
Generation: 9
Generation: 10
Generation: 11
Generation: 12
Generation: 13
Generation: 14
Generation: 15
Generation: 16
Generation: 17
Generation: 18
Generation: 19
Generation: 20
Generation: 21
Generation: 22
Generation: 23
Generation: 24
Generation: 25
Generation: 26
Generation: 27
Generation: 28
Generation: 29
Generation: 30
Generation: 31
Generation: 32
Generation: 33
Generation: 34
Generation: 35
Generation: 36
Generation: 37
Generation: 38
Generation: 39
Generation: 40
Generation: 41
Generation: 42
Generation: 43
Generation: 44
Generation: 45
Generation: 46
Generation: 47
Generation: 48
Generation: 49
Generation: 50
Generation: 51
Generation: 52
Generation: 53
Generation: 54
Generation: 55
Generation: 56
Generation: 57
Generation: 58
Generation: 59
Generation: 60
Generation: 61
Generation: 62
Generation: 63
Generation: 64
Generation: 65
Generation: 66
Generation: 67
Generation: 68
Generation: 69
Generation: 70
Generation: 71
Generation: 72
Generation: 73
Generation: 74
Generation: 75
Generation: 76
Generation: 77
Generation: 78
Generation: 79
Generation: 80
Generation: 81
Generation: 82
Generation: 83
Generation: 84
Generation: 85
Generation: 86
Generation: 87
- Solution found
- [3, 0, 4, 1, 5, 2]. Score: 15.0
- Number of episodes: 1
- Number of successful episodes: 1
- Average step per successful episode: 88.0
- Success Percentage: 1.1363636363636365
- Number of unsuccessful episodes: 0
- Average step per unsuccessful episode: Undefined
- [[0 0 0 0 1 0]
-  [0 0 1 0 0 0]
-  [1 0 0 0 0 0]
-  [0 0 0 0 0 1]
-  [0 0 0 1 0 0]
-  [0 1 0 0 0 0]]
- Total Time in seconds : 3.936737060546875


   

