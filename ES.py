import random
import operator
import numpy as np 
import math
import matplotlib.pyplot as plt

def initialisation():
    pop = dict()
    l = list()
    for i in range(1,51):
        for j in range(5):
            l.append(random.randint(1,8))
        for j in range (5):
            l.append(random.normalvariate(0.5,.15))
        l.append(random.normalvariate(0.5,.15))
        pop[i] = l
        l = []
    for obj in list(pop.keys()):
        print( obj ,pop[obj])
    return pop

def check_constraint(chorom):
    alfa = [0.0000233 , 0.0000145 , 0.00000541 , 0.0000805 , 0.0000195]
    WiVi_2 = [1,2,3,4,2]
    Wi = [7,8,8,6,9]
    g1, g2 , g3 = 0 , 0 , 0
    for i in range(5):
        g1 += ((WiVi_2[i]*((chorom[i])**2)) - 110)
        param_1 = 0
        #g2 += ((alfa[i]((-1000/(math.log2(chorom[i+5])))**beta)*(math.exp(0.25*(chorom[i])))) - 175)
        if chorom[i+5] < 1 :
            param_1 = (-1000/(math.log2(chorom[i+5])+0.000005))
        else:
            param_1 = (-1000/(math.log2(chorom[i+5])+ 0.00000005)) 
        param_1 = alfa[i]*((param_1)**1.5) #beta = 1.5
        param_2 = chorom[i] + math.exp(0.25*(chorom[i])) 
        g2 += param_1*param_2 - 175 #C=175
        g3 += ((Wi[i]*chorom[i])*(math.exp(0.25*(chorom[i])) ) - 200 )

    if g1 <= 0 and g2 <= 0 and g3 <= 0 :
        return(1)
    return(0)

def fit_complex(pop):
    R_chorom=dict()
    fit_per_chorom= dict()
    R = list()
    fitness = 0
    for i in list(pop.keys()):
        flag = check_constraint(pop[i])
        for j in range(0,5):
            if flag == 1:
                r = 1 - (1-pop[i][j+5])**pop[i][j]
                R.append(r)
            if flag == 0:
                R.append(0)
        R_chorom[i] = R
        R = []
    for i in list(R_chorom.keys()):
        R = R_chorom[i]
        fitness = R[0]*R[1] + R[2]*R[3] + R[0]*R[3]*R[4] + R[1]*R[2]*R[4]
        fitness = fitness - R[0]*R[1]*R[2]*R[3] - R[0]*R[1]*R[2]*R[4] - R[0]*R[1]*R[3]*R[4] - R[0]*R[2]*R[3]*R[4]
        fitness = fitness - R[1]*R[2]*R[3]*R[4] + 2*R[0]*R[1]*R[2]*R[3]*R[4]
        fit_per_chorom[i] = fitness
    return(fit_per_chorom)

def fit_series(pop):
    fit_per_chorom= dict()
    r=1
    for i in list(pop.keys()):
        flag = check_constraint(pop[i])
        for j in range(0,5):
            if flag == 1:
                r = r*(1 - (1-pop[i][j+5])**pop[i][j])
            if flag == 0:
                r = 0
        fit_per_chorom[i] = r
        r = 1
    return(fit_per_chorom)

def crossover_func(p1 , p2):
    child = []
    for i in range (0,11):
        j = random.randint(0,1)
        if j == 0 :
            child.append(p1[i])
        if j == 1 :
            child.append(p2[i])
    return(child)

def mutation_func (child, max_components):
    p = random.uniform(0,0.99)
    param_t = 1/(5**(0.5))
    if p <0.8:
        normal = random.normalvariate(0,1)
        sigma_new = child[10]*math.exp(param_t*normal)
        for i in range(0,5):
            child[i] += sigma_new*(random.normalvariate(0,1))
            if child[i] > max_components :
                child[i] = max_components
            elif child[i] < 1:
                child[i] = 1
            else:
                child[i] = np.round(child[i])
        for i in range(5,10):
            child[i] += sigma_new*(random.normalvariate(0,1))
            child[i] = np.clip(child[i],0.000005,0.999995)
        child[10] = sigma_new
    return(child)

#main

no_of_sub_sys = 5
max_components = 8
population = initialisation()
fitness_for_complex = fit_complex (population)
fitness_for_series = fit_series (population)

for obj in list(fitness_for_complex.keys()):
    print( obj ,fitness_for_complex[obj] , '\t' , fitness_for_series[obj])

best_fit_complex_per_iteration=dict()
best_fit_series_per_itration = dict()
avg_fit_complex = []
avg_fit_series = []
worst_fit_complex=[]
worst_fit_series = []
generation_number = 1
while (generation_number <100):
    i = 350
    j = 51
    while i > 0:
        #random_selection
        sys_1 = population[random.randint(1,50)]
        sys_2 = population[random.randint(1,50)]

        #cross_over and mutation
        child_1 = crossover_func(sys_1 , sys_2)
        child_1 = mutation_func (child_1, max_components)
        population[j] = child_1
        j += 1
        i -= 1
    fitness_for_complex = fit_complex (population)
    fitness_for_series = fit_series (population)   
    avg_fit_complex.append(sum(fitness_for_complex.values())/400)
    avg_fit_series.append(sum(fitness_for_series.values())/400)

    sorted_fit_complex = sorted(fitness_for_complex.items(),key=lambda kv: kv[1])
    sorted_fit_series = sorted(fitness_for_series.items(),key=lambda kv: kv[1])
    best_fit_complex_per_iteration[generation_number]= sorted_fit_complex[399][1]
    best_fit_series_per_itration [generation_number]= sorted_fit_series[399][1]

    this_obj = 0
    while sorted_fit_complex[this_obj][1] == 0:
        this_obj += 1
    worst_fit_complex.append(sorted_fit_complex[this_obj][1])

    this_obj = 0
    while sorted_fit_series[this_obj][1] == 0:
        this_obj += 1
    worst_fit_series.append(sorted_fit_series[this_obj][1])
    
    best_choroms_complex = []
    best_choroms_series = []
    for i in range(344,399):
        best_choroms_complex.append(sorted_fit_complex[i][0])
        best_choroms_series.append(sorted_fit_series[i][0])
    
    next_pop = dict()
    count = 1
    for obj in range(50):
        #if best_choroms_complex[obj] in best_choroms_series and len(next_pop)<50:
        next_pop[count] = population[best_choroms_complex[obj]]
        #next_pop[count] = population[best_choroms_complex[obj]]
        count += 1
    
   # if len(next_pop) < 51:
    #    for obj in range(len(next_pop)+1 , 51):
            #next_pop[i] = population[random.randint(1,350)]
     #       p = random.randint(0,1)
      #      if p == 0:
       #         next_pop[obj] = population[best_choroms_complex[random.randint(40,54)]]
        #    else:
         #       next_pop[obj] = population[best_choroms_series[random.randint(40,54)]] 

    population = {}
    population = next_pop
    generation_number += 1

print ('best fit for complex: ', best_fit_complex_per_iteration[99])
print('best fit for series:', best_fit_series_per_itration[99])
print('worst fit for complex:',worst_fit_complex[98])
print('worst fit for series:',worst_fit_series[98])
print('avg fit for complex:',avg_fit_complex[98])
print('avg fit for series:',avg_fit_series[98])
plt.plot(list(best_fit_complex_per_iteration.keys()) , list (best_fit_complex_per_iteration.values()), c = 'green')
plt.plot(list(best_fit_complex_per_iteration.keys()), list (best_fit_series_per_itration.values()), c = 'blue')
plt.plot(list(best_fit_complex_per_iteration.keys()) , worst_fit_complex, c = 'red')
plt.plot(list(best_fit_complex_per_iteration.keys()), worst_fit_series, c = 'orange')
plt.grid()
plt.show()

plt.plot(list(best_fit_complex_per_iteration.keys()) , avg_fit_complex, c = 'violet')
plt.plot(list(best_fit_complex_per_iteration.keys()), avg_fit_series, c = 'yellow')
plt.grid()
plt.show()