# Evolution Strategy (ES) based approach to system reliability optimization
System reliability optimization is very important in real-world applications. To design a highly reliable system, there are two main approaches: 1) Add redundant components and 2) Increase the component reliability.
For financial reasons, it has to establish a balance between reliability and other resources during designing a highly reliable system. 
In this project, have tried to design an Evolution Strategy (ES) based approach to reach this goal.
Well-known benchmarks
The notations used in this project are listed in the table (1):
![image](https://user-images.githubusercontent.com/14861041/210171131-2dcb83a4-0c40-4802-903b-1cd70e166260.png)

The reliability–redundancy allocation problem can be modeled in general form as follow:

Max Rs = f (ri, ni).
subject to g (ri, ni) ≤ predefinedValue

Where f (.) is the objective function (fitness function) for the overall system and g(.) is the set of constraint functions (e.g., constraints are on system weight, volume and cost). For more information, see: 
P. Wu, L. Gao, D. Zou, and S. Li, “An improved particle swarm optimization algorithm for reliability problems,” ISA Trans., vol. 50, no. 1, pp. 71–81, 2011.

# A) Complex (bridge) system (P1): 
Figure 1 represent a complex system that consists of five subsystems. The objective function for complex system is:

![image](https://user-images.githubusercontent.com/14861041/210171201-7e516fe1-34fc-4123-83db-ca4d375cd2bf.png)

# B) Series system (P2): 
Figure 2 represents a series system consisting of five subsystems. The objective function for series system is:
![image](https://user-images.githubusercontent.com/14861041/210171215-160cdbab-b197-4c37-adb5-665a8aa8321f.png)

Parameter used for complex (bridge) system (P1) and series system (P2) are listed in the below table:
![image](https://user-images.githubusercontent.com/14861041/210171228-5b00faf8-20aa-4f87-b884-ebdae68cb311.png)

![image](https://user-images.githubusercontent.com/14861041/210171235-d9abae49-689c-4c58-b87d-015e09519f10.png)

