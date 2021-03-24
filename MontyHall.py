import numpy as np
import random
import matplotlib.pyplot as plt

number_of_cases=1000

results = np.zeros((number_of_cases,3), dtype=int)

for icases in range(1,number_of_cases):
    
    results[icases,0]=icases

    # Prize location

    prize_location = np.random.randint(0, 3, icases)

    # print("Price Location  ", prize_location)

    # Stick

    stick_choice = np.random.randint(0, 3, icases)

    # print("Stick choice    ", stick_choice)

    stick_success = prize_location == stick_choice

    # print("Success if stuck to first chosen door", stick_success)

    # print("Success count if stuck to first chosen door:", stick_success.tolist().count(True))
    
    results[icases,1]=stick_success.tolist().count(True)

    # Switch 

    aux = np.array([2,0,1,2,0])

    # Cases when any door can be open. The car was chosen in the first election.
    
    switch_decision = (np.random.randint(0, 2, icases))

    # print("Switch decision ", switch_decision)
    
    switch_choice = np.zeros((icases,), dtype=int)+9

    switch_choice[stick_success,] = aux[stick_choice[stick_success,] + switch_decision[stick_success,] * 2,]
    
    # Cases when only one door can be open. The car was not chosen in the first election.
    
    switch_choice[~stick_success,] = prize_location[~stick_success,]

    # print("Switch choice   ", switch_choice)

    switch_success = prize_location == switch_choice

    # print("Success if switch chosen door", switch_success)

    # print("Success count if switch chosen door:", switch_success.tolist().count(True))

    results[icases,2]=switch_success.tolist().count(True)
    
    
plt.plot(results[:,0],results[:,1],label=('Stick'))
plt.plot(results[:,0],results[:,2],label=('Switch'))
plt.title('Success simulation whether Sticking to the first decision or Switching doors')
plt.ylabel('Success')
plt.xlabel('Cases')
plt.legend(loc='best', ncol=2, borderaxespad=0.) 
plt.show()