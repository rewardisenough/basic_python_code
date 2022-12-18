from IPython.display import clear_output 
import random

arr_1 = ['person1','person2','person3','person4'] # four people in this case, but could be any number.

for i in range(10):
  random.shuffle(arr_1) # shuffle the list 10 times but also could shuffle any number of times.

index_arr = [] # array to hold index to use for output.

for i in range(4): # range in four since arr_1 contained four elements.
  random_num = random.randint(0,3) # random integer from 0 to 3.
  while(random_num in index_arr or random_num==i): # first case checks if random_num has been generated in the past. This avoids duplicates. Second case prevents a person from choosing their ownself.
    random_num = random.randint(0,3) # generates until satifies the conditional statements.
  index_arr.append(random_num) # appends the used number to leave a history.

for i in range(4): # range in 4 since it's going to output to 4 different people.
  user = input("What's your name?: ") # ask their name could be any value out of (person1,person2,person3,person4).
  index = arr_1.index(user) # gets the index value of the user in arr_1. i.e. if user is person1, then index is equal to 0.
  chosen = index_arr[index] # gets the value that corresponds to same index in the index_arr as with value of 'index'. i.e. if index=2, and index_arr = [3,1,0,2], then chosen = 0 since index_arr[2] = 0.
  print(arr_1[chosen]) # print the person's name that user gets.
  done = input("Print done: ") # After user sees the name, it requires user input 'done'.
  if(done=="done"): # checks if user inputted 'done'.
    clear_output() # if so, clears the output so that next person doesn't see anyone elses.
