# Computational_Biology_Exe1

## **Overview:**
This program is a simulation that models the spread of rumors in a population,
using various parameters such as population density, waiting time between rumors, and belief probabilities. 

## **Usage:**
1. Download the main.exe file.
2. Double-click the file to start the simulation.
3. A new window will open, and the user will be prompted to enter the desired simulation parameters in the following panel:
![image](https://user-images.githubusercontent.com/111457277/236135595-b868439e-4fa8-4f77-87c6-134cb0bc912a.png)  
The parameters are:  
* P: population density (a number between 0 and 1 inclusive).
* L: waiting time between rumors (an integer).
* S1: percentage of people who believe each rumor.
* S2: percentage of people who believe a rumor with a probability of 2/3.
* S3: percentage of people who believe a rumor with a probability of 1/3.
* S4: percentage of people who do not believe any rumors.  
Default values are provided if the user chooses not to enter their own parameters (The default values are shown in the picture.)
4. Once the parameters have been entered, click "Run Simulation" to start the simulation. A 100x100 display of squares will appear on the screen as follows:  
![image](https://user-images.githubusercontent.com/111457277/236136535-37f8bb8b-cc5a-4161-82bf-0fe0cd6cebc1.png)  
* Green squares represent people who have not heard the rumor.
* Red squares represent people who have heard the rumor.
* White squares represent areas with no people.  
On the left side of the screen, the selected parameters are displayed.
Below the simulation display, the percentage of people exposed to the rumor out of the total number of people, and the number of generations that have passed, are shown.
These data change as the simulation progresses.
5. To close the simulation while it is running, click the "Quit" button that appears on the left side below the parameter panel.
