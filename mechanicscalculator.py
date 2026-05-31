#Importing libraries to access later on for calculations or functions.
import math
import statistics
import inspect

#Defining gravitational constant that will be used later on
gravAcceleration = 9.8

#A global dictionary for the known values that will be changed as user inputs values/answers questions, manages all known values and allows us to access them for calculations in every calculation function.
knowns = {}

#Global variables that will be used/changed/accessed throughout multiple functions for calculations, storing and looping.
solution = None
equation = ""
originalEquation = ""
typeWork = ""
wantToContinue = True
chapterNum = ""

#Defining values that will be used later for calculations-- some values will be used for multiple functions, hence making them global variables

#Creating Kinematic Variables
vi = None
vf = None
v = None
d = None
t = None
a = None

#Creating Forces Variables
Fa = None
Ff = None
weight = None
Fn = None
Fnet = None
mu = None
mass = None

#Creating Momentum Variables
p = None
pf = None
pi = None
changeOfp = None
J = None

#Creating Collision Variables
m1 = None
m2 = None
v1i = None
v2i = None
v1f = None
v2f = None
pf1 = None
pf2 = None
pfc = None

#Creating Energy Variables
KE = None
Ug = None
Uspring = None
dy = None
k = None
dspring = None
Fspring = None

#Creating Work Variables
KW = None
KEi = None
KEf = None
UgW = None
Ugi = None
Ugf = None
UspringW = None
Uspringi = None
Uspringf = None
ei = None
ef = None
dyi = None
dyf = None
dspringi = None
dspringf = None
W = None
P = None
hp = None
costheta = None

#Creating Rotational Kinematics Variables
theta_rot = None
omega_i = None
omega_f = None
omega = None
alpha = None
arc = None
r = None

#Creating Rotational Dynamics Variables
tau = None
I = None
alpha_dyn = None
L = None
Li = None
Lf = None
changeOfL = None
KErot = None
r_dyn = None
F_tang = None
F_cent = None
omega_dyn = None
mass_dyn = None
v_tang = None

#Creating Oscillations Variables
A = None
omega_osc = None
T_osc = None
f_osc = None
x_osc = None
v_osc = None
a_osc = None
k_osc = None
mass_osc = None
L_pend = None
T_pend = None
f_pend = None
phi = None
E_osc = None

#Creating Calculus Kinematics Variables
x_t = None
v_t = None
a_t = None
t_calc = None
x0 = None
v0 = None
a_const = None

#Creating Calculus Rotational Variables
theta_t = None
omega_t = None
alpha_t = None
omega0_calc = None
theta0_calc = None

#Creating Calculus Work-Energy Variables
W_calc = None
F_calc = None
dx_calc = None
KE_calc = None
PE_calc = None
E_total_calc = None

#Creating Calculus Oscillation Variables
x_calc = None
v_calc = None
a_calc = None
t_osc_calc = None
A_calc = None
omega_calc = None
phi_calc = None

#List that is used to looping for all the possible calculable values that do not yet have known values, in case the user needs to input one of these values and our scenario finders didn't cover them.
kinematicsVariables = ["vi", "vf", "v", "a", "d", "t"]
forcesVariables = ["Fa", "Ff", "mu", "weight", "Fn", "Fnet", "mass", "a", "vi", "vf", "t"]
momentumVariables = ["p", "pi", "pf", "changeOfp", "J", "vi", "vf", "v", "mass", "t", "Fa"]
#Seperating Elastic and Inelastic collisions to not overload user with so many inputs, some of which unnecessary
collisionVariablesElastic = ["v1i", "v2i", "v1f", "v2f", "pi1", "pi2", "pf1", "pf2", "m1", "m2"]
collisionVariablesInelastic = ["v1i", "v2i", "vf", "pi1", "pi2", "pfc", "m1", "m2"]

energyVariables = ["KE", "Ug", "Uspring", "dy", "mass", "v", "k", "dspring", "Fspring"]

#Seperating Work types to not overload user with so many inputs, some of which unnecessary
kineticWorkVariables = ["KW", "KEi", "KEf", "vi", "vf", "mass"]
gravPotentialWorkVariables = ["UgW", "Ugi", "Ugf", "dyi", "dyf", "mass"]
elastPotentialWorkVariables = ["UspringW", "Uspringi", "Uspringf", "dspringi", "dspringf", "k"]          
workVariables = ["W", "ei", "ef", "Fa", "d", "P", "hp", "t"]

#Rotational Kinematics variable list
rotKinematicsVariables = ["theta_rot", "omega_i", "omega_f", "omega", "alpha", "arc", "r", "t"]

#Rotational Dynamics variable lists
rotDynamicsVariables = ["tau", "I", "alpha_dyn", "L", "Li", "Lf", "changeOfL", "KErot", "r_dyn", "F_tang", "F_cent", "omega_dyn", "mass_dyn", "v_tang"]

#Oscillations variable lists - separating by type for clarity
simpleHarmonicVariables = ["x_osc", "v_osc", "a_osc", "A", "omega_osc", "T_osc", "f_osc", "k_osc", "mass_osc", "phi", "E_osc"]
pendulumVariables = ["T_pend", "f_pend", "L_pend"]

#Calculus-based variable lists - separated by topic
calculusKinematicsVariables = ["x0", "v0", "a_const", "t_calc", "x_t", "v_t", "a_t"]
calculusRotationalVariables = ["theta0_calc", "omega0_calc", "alpha_t", "t_calc", "theta_t", "omega_t"]
calculusWorkEnergyVariables = ["W_calc", "F_calc", "dx_calc", "KE_calc", "PE_calc", "E_total_calc", "mass", "v", "k", "dspring"]
calculusOscillationVariables = ["A_calc", "omega_calc", "phi_calc", "t_osc_calc", "x_calc", "v_calc", "a_calc"]

#An entire dictionary for all the shortened variable names that corresponds to their longer name, used for printing final values and asking for input variables. This dictionary is used to match simplified inputs to the full name of the value, to ensure there is no confusion for what is being asked/presented. This allows for a more simplified and abstract coding process as well.
variableFullNames = {
  "vi": "Initial Velocity (m/s)",
  "vf": "Final Velocity (m/s)",
  "v": "Velocity (m/s)",
  "d": "Displacement (Δx) (m)",
  "t": "Time (Δt) (s)",
  "a": "Acceleration (m/s^2)",
  "Fa": "Applied Force (N)",
  "Ff": "Friction (N)",
  "mu": "Mu (μ)",
  "weight": "Weight (mg) (N)",
  "Fnet": "Net Force (ΣF) (N)",
  "Fn": "Normal Force (N)",
  "mass": "Mass (kg)",
  "p": "Momentum (kgm/s)",
  "pi": "Initial Momentum (kgm/s)",
  "pf": "Final Momentum (kgm/s)",
  "changeOfp" : "Change of Momentum (Δp) (Ns)",
  "J": "Impulse (Ns)",
  "v1i": "Initial Velocity of the First Object (m/s)",
  "v2i": "Initial Velocity of the Second Object (m/s)",
  "v1f": "Final Velocity of the First Object (m/s)",
  "v2f": "Final Velocity of the Second Object (m/s)",
  "pi1": "Initial Momentum of Object 1 (kgm/s)",
  "pi2": "Initial Momentum of Object 2 (kgm/s)",
  "pf1": "Final Momentum of Object 1 (kgm/s)",
  "pf2": "Final Momentum of Object 2 (kgm/s)",
  "pfc": "Final Momentum of Inelastic Collision (kgm/s)",
  "m1": "Mass of Object 1 (kg)",
  "m2": "Mass of Object 2 (kg)",
  "KE": "Kinetic Energy (J)",
  "Ug": "Gravitational Potential Energy (J)",
  "Uspring": "Elastic Potential Energy (J)",
  "dy": "Distance in the Y-axis from Origin (m)",
  "k": "Spring Constant (N/m)",
  "dspring": "Displacement of Spring from rest (Δx) (m)",
  "Fspring": "Force exerted by Spring (N)",
  "KW": "Work - Kinetic Energy (J)",
  "UgW": "Work - Gravitational Potential Energy (J)",
  "UspringW": "Work - Elastic Potential Energy (J)",
  "KEi": "Initial Kinetic Energy (J)",
  "KEf": "Final Kinetic Energy (J)",
  "Ugi": "Initial Gravitational Potential Energy (J)",
  "Ugf": "Final Gravitational Potential Energy (J)",
  "Uspringi": "Initial Elastic Potential Energy (J)",
  "Uspringf": "Final Elastic Potential Energy (J)",
  "ei": "Initial Energy (J)",
  "ef": "Final Energy (J)",
  "dyi": "Initial Distance in the Y-axis from Origin (m)",
  "dyf": "Final Distance in the Y-axis from Origin (m)",
  "dspringi": "Initial Displacement of Spring from rest (Δx) (m)",
  "dspringf": "Displacement of Spring from rest (Δx) (m)",
  "W": "Work (J)",
  "P": "Power (W)",
  "hp": "Horsepower (Fd/t)",
  # Rotational Kinematics full names
  "theta_rot": "Angular Displacement (Δθ) (rad)",
  "omega_i": "Initial Angular Velocity (ωi) (rad/s)",
  "omega_f": "Final Angular Velocity (ωf) (rad/s)",
  "omega": "Angular Velocity (ω) (rad/s)",
  "alpha": "Angular Acceleration (α) (rad/s^2)",
  "arc": "Arc Length (s) (m)",
  "r": "Radius (m)",
  # Rotational Dynamics full names
  "tau": "Torque (τ) (Nm)",
  "I": "Moment of Inertia (I) (kgm^2)",
  "alpha_dyn": "Angular Acceleration (α) (rad/s^2)",
  "L": "Angular Momentum (L) (kgm^2/s)",
  "Li": "Initial Angular Momentum (Li) (kgm^2/s)",
  "Lf": "Final Angular Momentum (Lf) (kgm^2/s)",
  "changeOfL": "Change of Angular Momentum (ΔL) (kgm^2/s)",
  "KErot": "Rotational Kinetic Energy (J)",
  "r_dyn": "Radius / Moment Arm (m)",
  "F_tang": "Tangential Force (N)",
  "F_cent": "Centripetal Force (N)",
  "omega_dyn": "Angular Velocity (ω) (rad/s)",
  "mass_dyn": "Mass (kg)",
  "v_tang": "Tangential Velocity (m/s)",
  # Oscillations full names
  "A": "Amplitude (m)",
  "omega_osc": "Angular Frequency (ω) (rad/s)",
  "T_osc": "Period (T) (s)",
  "f_osc": "Frequency (f) (Hz)",
  "x_osc": "Position at time t (m)",
  "v_osc": "Velocity at time t (m/s)",
  "a_osc": "Acceleration at time t (m/s^2)",
  "k_osc": "Spring Constant (N/m)",
  "mass_osc": "Mass (kg)",
  "phi": "Phase Constant (φ) (rad)",
  "E_osc": "Total Mechanical Energy of Oscillator (J)",
  "T_pend": "Period of Pendulum (T) (s)",
  "f_pend": "Frequency of Pendulum (f) (Hz)",
  "L_pend": "Length of Pendulum (m)",
  # Calculus Kinematics full names
  "x0": "Initial Position (x0) (m)",
  "v0": "Initial Velocity (v0) (m/s)",
  "a_const": "Constant Acceleration (a) (m/s^2)",
  "t_calc": "Time (t) (s)",
  "x_t": "Position at time t, x(t) (m)",
  "v_t": "Velocity at time t, v(t) (m/s)",
  "a_t": "Acceleration at time t, a(t) (m/s^2)",
  # Calculus Rotational full names
  "theta0_calc": "Initial Angular Position (θ0) (rad)",
  "omega0_calc": "Initial Angular Velocity (ω0) (rad/s)",
  "alpha_t": "Constant Angular Acceleration (α) (rad/s^2)",
  "theta_t": "Angular Position at time t, θ(t) (rad)",
  "omega_t": "Angular Velocity at time t, ω(t) (rad/s)",
  # Calculus Work-Energy full names
  "W_calc": "Work done by constant force (J)",
  "F_calc": "Constant Force (N)",
  "dx_calc": "Displacement (m)",
  "KE_calc": "Kinetic Energy (J)",
  "PE_calc": "Potential Energy (J)",
  "E_total_calc": "Total Mechanical Energy (J)",
  # Calculus Oscillation full names
  "A_calc": "Amplitude (m)",
  "omega_calc": "Angular Frequency (ω) (rad/s)",
  "phi_calc": "Phase Constant (φ) (rad)",
  "t_osc_calc": "Time (t) (s)",
  "x_calc": "Position x(t) = A*cos(ωt + φ) (m)",
  "v_calc": "Velocity v(t) = -Aω*sin(ωt + φ) (m/s)",
  "a_calc": "Acceleration a(t) = -Aω^2*cos(ωt + φ) (m/s^2)"
}

#These lists are the chapters with each of the concepts that they cover, so that users are able to preview what chapters contain what concepts, so they do not need to flip through all the chapters to find what they need.
kinematics = ["Displacement", "Final Velocity", "Initial Velocity", "Velocity", "Time", "Acceleration"]
forces = ["Force (F=ma)", "Net Force", "Friction", "Weight", "Normal Force (under correct conditions)"]
momentum = ["Linear Momentum", "Impulse"]
collisions = ["Conservation of Momentum (Elastic)", "Conservation of Momentum (Inelastic)"]
energy = ["Kinetic Energy", "Gravitational Potential Energy", "Spring Energy", "Hooke's Law"]
work = ["Work", "Power"]
rotKinematics = ["Angular Displacement", "Angular Velocity", "Angular Acceleration", "Arc Length", "All 5 Rotational Kinematic Equations"]
rotDynamics = ["Torque", "Moment of Inertia", "Angular Momentum", "Rotational Kinetic Energy", "Centripetal Force", "Tangential Force/Velocity"]
oscillations = ["Simple Harmonic Motion (position, velocity, acceleration)", "Period & Frequency", "Spring-Mass System", "Simple Pendulum", "Total Energy of Oscillator"]
calculusPhysics = ["Calculus-Based Kinematics (derivatives/integrals)", "Calculus-Based Rotational Kinematics", "Calculus-Based Work-Energy", "Calculus-Based Oscillations (SHM functions)"]

#A function used to match the user's inputs to the chapter's contents that they want to preview.
def showChapters(chapterNumView):
  #Creates list of all chapter names for index accessing later on.
  allChapterNames = ["Kinematics", "Forces", "Momentum", "Collisions", "Energy", "Work & Power", "Rotational Kinematics", "Rotational Dynamics", "Oscillations", "Calculus-Based Physics"]
  #Uses conditionals to match inputs to the name of the chapter. If they do not input a value from within the range, it prints an error message.
  if chapterNumView in range(1,11):
    chapterDisplay = allChapterNames[chapterNumView-1]
  else:
    print("You inputted an incorrect number value.")
    return

  #Connects chapter number to the correct number, ordinal and references the chapter name and prints this in a statement for the user to view.
  if chapterNumView == 1:
    print(f"\nYou wanted to see the {chapterNumView}st chapter, which is {chapterDisplay}!")
  elif chapterNumView == 2:
    print(f"\nYou wanted to see the {chapterNumView}nd chapter, which is {chapterDisplay}!")
  elif chapterNumView == 3:
    print(f"\nYou wanted to see the {chapterNumView}rd chapter, which is {chapterDisplay}!")
  else:
    print(f"\nYou wanted to see the {chapterNumView}th chapter, which is {chapterDisplay}!")

  #Prints chapter name and the concepts that are displayed within said chapter.
  if chapterNumView == 1:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(kinematics)}.")
  elif chapterNumView == 2:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(forces)}.")
  elif chapterNumView == 3:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(momentum)}.")
  elif chapterNumView == 4:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(collisions)}.")
  elif chapterNumView == 5:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(energy)}.")
  elif chapterNumView == 6:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(work)}.")
  elif chapterNumView == 7:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(rotKinematics)}.")
  elif chapterNumView == 8:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(rotDynamics)}.")
  elif chapterNumView == 9:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(oscillations)}.")
  elif chapterNumView == 10:
    print(f"The concepts covered in {chapterDisplay} are {', '.join(calculusPhysics)}.")

'''
CITATION:
This code was generated using ChatGPT GPT-4-turbo.
Date: 4/26/25
Code Version: Python 3.0
Availability: https://chatgpt.com/
Explanation: ChatGPT aided with the development of this code, by writing how it can continue looping if user does not input yes or no.
'''

#The program asks a lot of Yes or No questions, for abstraction, this function exists to take in inputs (the questions) and reprint it in a new format.
def YesOrNo(question):
  #While true is a safeguard, so if user doesn't input Yes or No, they can do so.
  while True:
    #Asks user for input, and adds (Yes/No) to the question from the inputted parameter to ensure the user knows this is what they need to answer
    answer = input(question + " (Yes/No): ").lower()
    #If answer is Yes or No, code continues-- if Yes, returns value as True.
    if answer in ["yes", "no"]:
      return answer=="yes"
    #If they do not input Yes or No, tells them to enter either Yes or No.
    else:
      print("Enter 'Yes' or 'No'.")


#Since every chapter needs to have a solution printed, this function exists for abstraction and avoids repetitiveness. Prints and formats the solution messages.
def printSolution():
  #If the solution is not equal to None, meaning it got a value, it will print.
  if solution != None:
    #Gets the value inputted in solveFor (user input) and matches it with the longer name found in the dictionary variableFullNames
    print(f"\n{variableFullNames.get(solveFor)} = ") 
    #Prints the solution and formats it to 3 decimals only
    print('{:.3f}'.format(solution))
    #Prints the equation used for calculation and the originalEquation the equation was derived from (if needed)
    print(f"The equation used to calculate this: {equation}")
    print(f"The original equation is: {originalEquation}") 
  else:
  #Else if the solution is equal to None, meaning it wasn't given a value, that means the sufficient values weren't provided and solution could not be calculated.
    print("You have not given sufficient enough values to calculate for the value you were looking for.")

#Function used for abstraction to make code readability easier. Prints Tips and Notes user should consider while calculating.
def tipsAndNotes():

  #Checks if the tipsAndNotes function is being run in the function it is being run in the conditional with, if True, then it will print the tips/notes that must be considered for that said topic.
  
  '''
  CITATION:
  Title: "Get name of current function and caller with Python"
  By: Stefaan Lippens
  Date: 4/27/25
  Code Version: Python 3.0
  Availability: https://www.stefaanlippens.net/python_inspect/
  Explanation: I used this source for "inspect.stack()[1].function", as I did not priorly use the inspect library before and did not know how to use it.
  '''

  if inspect.stack()[1].function == "forcesCalculator":
    print("\nTIP: Remember, Newton's Three Laws are:")
    print("1. Every object at rest will remain at rest unless acted upon by an external force\n2. The acceleration of an object is directly proportional to the net force\n3. If object A exerts a force on object B, object B will exert the same force back on object A in the opposite direction. (FAonB = -FBonA)")

  elif inspect.stack()[1].function == "momentumCalculator":
    print("\nNOTE: J = Change of P (Δp) = Fa*t = mvf - mvi")
    print("If your exact value could not be found, potentially reference this equality sequence as your answer may be there but under another name.")

  elif inspect.stack()[1].function == "collisionsCalculator":
    print("NOTE: Elastic is when both objects do not combine and have seperate velocities after (m1v1i + m2v2i = m1v1f + m2v2f)")
    print("Inelastic is when both objects do combine and have same velocity after (m1v1i + m2v2i = (m1+m2)vf)")

  elif inspect.stack()[1].function == "energyCalculator":
    print("\nNOTE: Energy all depends on the system and how you have defined it, as well as the object(s) you are observing in your system. We are not able to determine specifics exactly, and you must understand your system to be able to use the energy calculator precisely.")

  elif inspect.stack()[1].function == "workCalculator":
    print("\nNOTE: Work all depends on the system and how you have defined it, as well as the object(s)/energy(ies) you are observing in your system. We are not able to determine specifics exactly, and you must understand your system to be able to use the work calculator precisely.")
    print("Additionally, remember that work is exerted from outside the system. Energy can be transferred inside the system, ie; Gravitational Potential -> Kinetic. This isn't considered work, and we do not support calculations for this.")

  elif inspect.stack()[1].function == "rotKinematicsCalculator":
    print("\nNOTE: Rotational Kinematics mirrors Linear Kinematics exactly, but uses angular quantities.")
    print("The analogy is: d -> θ,  v -> ω,  a -> α,  t -> t (same)")
    print("All 5 rotational kinematic equations follow the same structure as their linear counterparts.")
    print("Angles must be in RADIANS for all calculations. If you have degrees, convert: rad = degrees * (π/180)")

  elif inspect.stack()[1].function == "rotDynamicsCalculator":
    print("\nNOTE: Rotational Dynamics mirrors Newton's Second Law: τ = Iα  (analogous to F = ma)")
    print("Torque (τ) is the rotational equivalent of force. Moment of Inertia (I) is the rotational equivalent of mass.")
    print("Angular Momentum L = Iω is conserved when net torque is zero (Conservation of Angular Momentum).")
    print("This chapter handles point-mass moment of inertia (I = mr^2). For extended bodies, I must be given or looked up.")

  elif inspect.stack()[1].function == "oscillationsCalculator":
    print("\nNOTE: Simple Harmonic Motion (SHM) requires a restoring force proportional to displacement: F = -kx")
    print("The general position function is x(t) = A*cos(ωt + φ), where A = amplitude, ω = angular frequency, φ = phase constant.")
    print("For a spring-mass system: ω = sqrt(k/m).  For a simple pendulum (small angles): ω = sqrt(g/L).")
    print("The total energy of the oscillator is constant: E = (1/2)kA^2")

  elif inspect.stack()[1].function == "calculusPhysicsCalculator":
    print("\nNOTE: Calculus-Based Physics uses derivatives and integrals to find exact kinematic quantities from functions.")
    print("Derivative relationships: a(t) = dv/dt = d²x/dt²   |   v(t) = dx/dt")
    print("Integral relationships:   x(t) = ∫v(t)dt + x0       |   v(t) = ∫a(t)dt + v0")
    print("For CONSTANT acceleration, these integrals yield the standard kinematic equations.")
    print("For NON-CONSTANT acceleration, this calculator evaluates the integral symbolically for polynomial a(t).")


#This function is used to gain values of for Kinematics values based on the wording of the problem as described to the user.
def valuesFromWordingKinematics():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global vi, vf, v
  global a 

  #If the object has constant velocity, vi and vf are irrelevant and acceleration is 0. Sets values accordingly and saves it in knowns.
  if YesOrNo("Does the object have a constant velocity?"):
    a = 0
    knowns["a"] = 0
    knowns["vi"] = None
    knowns["vf"] = None
    print("Your acceleration is 0!")

    #If constant velocity is at 0, v=0, sets value accordingly and saves it in knowns.
    if YesOrNo("Is the constant velocity at zero?"):
      v = 0
      knowns["v"] = 0
      print("Your initial and final velocity is 0!")
    return

  #Ensures there are velocities at rest, if not, rest of operations are irrelevant.
  if YesOrNo("Is the initial or final velocity of this object at rest?"):
      #If initial velocity of object is at rest, vi is 0. Sets value accordingly and saves it in knowns.
      if YesOrNo("Is the Initial Velocity of the object at rest?"):
        vi = 0
        knowns["vi"] = vi
        print("Your initial velocity of the object is 0!")
      #If final velocity of object is at rest, vf is 0. Sets value accordingly and saves it in knowns.
      if YesOrNo("Is the Final Velocity of the object at rest?"):
        vf = 0
        knowns["vf"] = vf
        print("Your final velocity of the object is 0!")

#This function is used to gain values of for Forces values based on the wording of the problem as described to the user.
def valuesFromWordingForces():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global mass, Ff, Fa, Fnet, mu, Fn

  #Obtains mass of object from user input to determine weight, can be used later to determine if weight = Fn for a specific scenario. Saves mass and weight to knowns accordingly.
  mass = float(input("What is the mass of the object?: "))
  knowns["mass"] = mass
  weight = mass*gravAcceleration
  knowns["weight"] = weight
  print(f"Your weight is {weight}N")

  #If object has constant velocity, a and all forces (other than weight) are 0. Sets value accordingly and saves it in knowns.
  if YesOrNo("Does your object have a constant velocity?"):
    Ff = 0
    Fa = 0
    Fnet = 0
    a = 0
    knowns["Ff"] = Ff
    knowns["Fa"] = Fa
    knowns["Fnet"] = Fnet
    knowns["a"] = a
  #If object is in free fall, a and all forces (other than weight) are 0. Sets value accordingly and saves it in knowns.
  if YesOrNo("Is your object in free fall?:"):
    Fn = 0
    Ff = 0
    mu = 0
    Fa = 0
    Fnet = weight
    knowns["Fn"] = Fn
    knowns["Ff"] = Ff
    knowns["mu"] = mu
    knowns["Fa"] = Fa
    knowns["Fnet"] = Fnet
    print(f"Your net force is {weight}!")
    return

  #If object is on flat surface and not moving upwards or downwards, weight = Fn. Sets value accordingly and saves to knowns.
  if YesOrNo("Is your object on a flat surface, where it is not moving upwards or downwards (or whichever axis gravity is in)"):
    Fn = weight
    knowns["Fn"] = Fn
    
  #If object is at an angled surface, explains to the user that we cannot support that calculation.
  if YesOrNo("Is your object on an angled surface?"):
    print("Sorry, but we are currently not able to support trigonometric calculations for weight, normal force and friction at this time.")
    
#This function is used to gain values of for Elastic Collision values based on the wording of the problem as described to the user.  
def valuesFromWordingCollisionsElastic():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global v1i, v2i, v1f, v2f
  
  #Checks if there are any velocities at rest
  if YesOrNo("Are any of the initial or final velocities at rest?"):
      #If there is, gathers which are, sets value to 0 and saves value to knowns.
      if YesOrNo("Is the Initial Velocity of the first object at rest?"):
        v1i = 0 
        knowns["v1i"] = v1i
        print("Your initial velocity of the first object is 0!")
      if YesOrNo("Is the Initial Velocity of the second object at rest?"):
        v2i = 0
        knowns["v2i"] = v2i
        print("Your initial velocity of the second object is 0!")
      if YesOrNo("Is the Final Velocity of the first object at rest?"):
        v1f = 0 
        knowns["v1f"] = v1f
        print("Your final velocity of the first object is 0!")
      if YesOrNo("Is the Final Velocity of the second object at rest?"):
        v2f = 0
        knowns["v2f"] = v2f
        print("Your final velocity of the second object is 0!")
      if v1i == 0 and v2i == 0:
        print("Both initial velocities cannot be 0, or else a collision did not occur!")

#This function is used to gain values of for Inelastic Collison values based on the wording of the problem as described to the user.
def valuesFromWordingCollisionsInelastic():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global v1i, v1f, vf

  #Checks if there are any velocities at rest
  if YesOrNo("Are there any of the initial velocities or is the final velocity at rest?"):
    #If there is, gathers which are, sets value to 0 and saves value to knowns.
    if YesOrNo("Is the Initial Velocity of the first object at rest?"):
      v1i = 0 
      knowns["v1i"] = v1i
      print("Your initial velocity of the first object is 0!")
    if YesOrNo("Is the Initial Velocity of the second object at rest?"):
      v2i = 0
      knowns["v2i"] = v2i
      print("Your initial velocity of the second object is 0!")
    if YesOrNo("Is the final velocity of the combined objects at rest?"):
      vf = 0
      knowns["vf"] = vf
      print("Your final velocity is 0!")

#This function is used to gain values of for Energy values based on the wording of the problem/what the user knows.
def valuesFromWordingEnergy():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global KE, Ug, Uspring, dy, v, dspring, Fspring, k

  #Checks if the object interacts with spring energy, if it doesn't, saves all spring-related values to knowns as None
  if YesOrNo("Does the object in your system interact with a spring?"):
    print("Your system has spring energy!")
  else: 
    knowns["Uspring"] = None
    knowns["dspring"] = None
    knowns["Fspring"] = None
    knowns["k"] = None
    print("There is no elastic potential energy or force exerted by the spring in your system!")
    
  #Checks if the Earth is apart of the system, if it isn't, saves Ug and dy to knowns as None and 0.
  if YesOrNo("Is Earth apart of your system?"):
    #Checks if the object is at the y-origin line, if it is, saves Ug and dy to knowns as None and 0.
    if YesOrNo("Is your object on the set y-origin line? (ie; if your y=0, is your object at y=0?)"):
      dy = 0
      knowns["Ug"] = None
      knowns["dy"] = dy
      print("There is no gravitational potential energy in your system!")
  else:
    dy = 0
    knowns["Ug"] = None
    knowns["dy"] = dy
    print("There is no gravitational potential energy in your system!")

  #Checks if the object in the system is moving, if not,saves KE and v to knowns as None and 0.
  if YesOrNo("Is the object in your system moving?"):
    print("There is kinetic energy!")
  else:
    v = 0
    knowns["KE"] = None
    knowns["v"] = v
    print("There is no kinetic energy in your system!")

#This function is used to gain values of for Work values based on the wording of the problem/what the user knows.
def valuesFromWordingWork():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global KW, KEi, KEf, vi, vf, UgW, Ugi, Ugf, dyi, dyf, UspringW, Uspringi, Uspringf, dspringi, dspringf

  #Checks to see if this work problem is related to Kinetic Energy based on user input
  if typeWork == "1":
    #Checks if either velocity is at rest, if yes, sets corresponding values to 0 and saves to knowns,
    if YesOrNo("\nIs the object in your system at rest initially?"):
      KEi = 0
      vi = 0
      knowns["KEi"] = KEi
      knowns["vi"] = vi
      print("You do not have any initial kinetic energy!")
    if YesOrNo("Is the object's final velocity in your system at rest?"):
      KEf = 0
      vf = 0
      knowns["KEf"] = KEf
      knowns["vf"] = vf
      print("You do not have any final kinetic energy!")
    #If Kinetic Initial and Kinetic Final energy is 0, there is no kinetic energy in the system.
    if KEf == 0 and KEi == 0:
      KW = 0
      knowns["KW"] = KW
      print("You do not have any work with Kinetic Energy!")

  #Checks to see if this work problem is related to Gravitational Potential Energy based on user input
  if typeWork == "2":
    #Checks to see if either positions lie at the y-origin line, if yes, sets corresponding values to 0 and saves to knowns.
    if YesOrNo("\nIs your object on the set y-origin line? (ie; if your y=0, is your object at y=0?) initially?"):
      Ugi = 0 
      dyi = 0
      knowns["Ugi"] = Ugi
      knowns["dyi"] = dyi
    if YesOrNo("Is the object's final position on the set y-origin line? (ie; if your y=0, is your object at y=0?) ?"):
      Ugf = 0
      dyf = 0
      knowns["Ugf"] = Ugf
      knowns["dyf"] = dyf
    #If Gravitational Initial and Gravitational Final energy is 0, there is no gravitational potential energy in the system. 
    if Ugf == 0 and Ugi == 0:
      print("You do not have any work with Gravitational Potential Energy!")

  #Checks to see if this work problem is related to Elastic Potential Energy based on user input
  if typeWork == "3":
    #Checks to see if either initial or final have the spring at rest, if yes, sets corresponding values to 0 and saves to knowns.
    if YesOrNo("\nIs your spring initially at rest?"):
      Uspringi = 0 
      dspringi = 0
      knowns["Uspringi"] = Uspringi
      knowns["dspringi"] = dspringi
    if YesOrNo("Is your spring's final position at rest?"):
      Uspringf = 0
      dspringf = 0
      knowns["Uspringf"] = Uspringf
      knowns["dspringf"] = dspringf
    #If Elastic Initial and Elastic Final energy is 0, there is no elastic potential energy in the system. 
    if Uspringi == 0 and dspringi == 0:
      print("You do not have any work with Elastic Potential Energy!")

#This function is used to gain values for Rotational Kinematics based on the wording of the problem.
def valuesFromWordingRotKinematics():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global omega_i, omega_f, omega, alpha, theta_rot

  #If the object has constant angular velocity, alpha is 0 and both omegas are equal. Sets values accordingly and saves to knowns.
  if YesOrNo("Does the object have a constant angular velocity (no angular acceleration)?"):
    alpha = 0
    knowns["alpha"] = 0
    print("Your angular acceleration is 0!")
    if YesOrNo("Is the constant angular velocity at zero?"):
      omega = 0
      omega_i = 0
      omega_f = 0
      knowns["omega"] = 0
      knowns["omega_i"] = 0
      knowns["omega_f"] = 0
      print("Your angular velocity is 0!")
    return

  #Checks if either initial or final angular velocity is at rest.
  if YesOrNo("Is the initial or final angular velocity of this object at rest (at zero)?"):
    if YesOrNo("Is the Initial Angular Velocity (ωi) at rest?"):
      omega_i = 0
      knowns["omega_i"] = omega_i
      print("Your initial angular velocity is 0!")
    if YesOrNo("Is the Final Angular Velocity (ωf) at rest?"):
      omega_f = 0
      knowns["omega_f"] = omega_f
      print("Your final angular velocity is 0!")

#This function is used to gain values for Rotational Dynamics based on the wording of the problem.
def valuesFromWordingRotDynamics():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global omega_dyn, Li, Lf, KErot

  #Checks if object starts or ends at rest rotationally, sets angular momentum and omega accordingly.
  if YesOrNo("Is the object initially at rest (angular velocity = 0) rotationally?"):
    omega_dyn = 0
    Li = 0
    knowns["omega_dyn"] = 0
    knowns["Li"] = 0
    print("Your initial angular velocity and initial angular momentum are 0!")

  if YesOrNo("Is there no net torque acting on this system (conservation of angular momentum applies)?"):
    print("Conservation of Angular Momentum applies: Li = Lf")
    print("NOTE: You will need to provide either Li and Lf, or I and omega for each state.")

#This function is used to gain values for Oscillations based on the wording of the problem.
def valuesFromWordingOscillations():
  #Global as we are editing the values of these global variables to be used later on in calculations in a different function.
  global A, phi, x_osc, v_osc

  #Checks if phase constant is zero (object starts at maximum displacement), a very common initial condition.
  if YesOrNo("Does the oscillation start at maximum displacement (object released from rest at amplitude, so φ = 0)?"):
    phi = 0
    knowns["phi"] = phi
    print("Your phase constant (φ) is 0! x(t) = A*cos(ωt)")

  #Checks if the object starts at equilibrium instead.
  if YesOrNo("Does the oscillation start at equilibrium with maximum velocity (x=0 at t=0, so φ = π/2)?"):
    phi = math.pi / 2
    knowns["phi"] = phi
    print(f"Your phase constant (φ) is π/2 = {phi:.3f} rad! x(t) = A*cos(ωt + π/2) = -A*sin(ωt)")


#Defines a function that efficiently serves as a calculator for all kinematics-related problems.
def kinematicsCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {} 

  print("\nHello! You are in the Kinematics Chapter!")
  print("The values you are able to solve for are: ")
  #Uses for loop to loop through kinematicsVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
  for index in kinematicsVariables:
    print(f"-> {variableFullNames.get(index)}")
  #Prints out the names that users should input to use calculator.
  print(f"The shortened versions are as follows, in the same order: {kinematicsVariables}")

  #Checks for values from certain scenarios and then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
  valuesFromWordingKinematics()
  solveFor = input("Input the value you want to solve for (enter shortened version): ")
  if solveFor in knowns:
    solution = 0
    print(f"{variableFullNames.get(solveFor)} is {solution}!")
    return

  #For every index (kinematicVariable) in the kinematicVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
  for kinematicVariable in kinematicsVariables:
    if kinematicVariable != solveFor and kinematicVariable not in knowns:
      kinematicInput = input(f"\nEnter a value for {variableFullNames.get(kinematicVariable)} or if unknown/not given, leave this value blank: ")
      if kinematicInput != "":
        knowns[kinematicVariable] = float(kinematicInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  vi = knowns.get("vi")
  vf = knowns.get("vf")
  v = knowns.get("v")
  a = knowns.get("a")    
  d = knowns.get("d")
  t = knowns.get("t")

  '''
  CITATION:
  This code was generated using ChatGPT GPT-4-turbo.
  Date: 4/26/25
  Code Version: Python 3.0
  Availability: https://chatgpt.com/
  Explanation: I created the first conditional for the intended variable for each of the equations. I then told ChatGPT to use the same format and solve for the other variables of the equations. 
  '''

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.
  
  #Solving for the first equation v = d/t
  if solveFor == "v" and d!=None and t!=None and t != 0:
    solution = d / t
    equation = "v = d/t"
    originalEquation = "v = d/t"
  elif solveFor == "d" and v != None and t != None:
    solution = v * t
    equation = "d = v*t"
    originalEquation = "v = d / t"
  elif solveFor == "t" and d != None and v != None and v != 0:
    solution = d / v
    equation = "t = d/v"
    originalEquation = "v = d/t"

  #Solving for the second equation a = (vf-vi)/t
  elif solveFor == "a" and vf != None and vi != None and t != None and t != 0:
    solution = (vf - vi) / t
    equation = "a = (vf - vi)/t"
    originalEquation = "a = (vf - vi)/t"
  elif solveFor == "vf" and vi != None and a != None and t != None:
    solution = vi + a * t
    equation = "vf = vi + a*t"
    originalEquation = "a = (vf - vi)/t"
  elif solveFor == "vi" and vf != None and a != None and t != None:
    solution = vf - a * t
    equation = "vi = vf - a*t"
    originalEquation = "a = (vf - vi)/t"
  elif solveFor == "t" and vf != None and vi != None and a != None and a != 0:
    solution = (vf - vi) / a
    equation = "t = (vf - vi)/a"
    originalEquation = "a = (vf - vi)/t"

  #Solving for the third equation: d = vi*t + (0.5)*a*t**2
  elif solveFor == "d" and vi != None and t != None and a != None:
    solution = (vi * t) + (0.5 * a * t**2)
    equation = "(vi * t) + (0.5 * a * t**2)"
    originalEquation = "(vi*t) + (0.5*a*t**2)"
  elif solveFor == "vi" and d != None and t != None and a != None:
    solution = (d - 0.5 * a * t ** 2) / t
    equation = "vi = (d - 0.5*a*t**2) / t"
    originalEquation = "(vi*t) + (0.5*a*t**2)"
  elif solveFor == "a" and d != None and vi != None and t != None:
    solution = (d - vi * t) * 2 / (t ** 2)
    equation = "a = 2 * (d - vi*t) / t**2"
    originalEquation = "(vi*t) + (0.5*a*t**2)"

  # Solving for the fourth equation: vf**2 = (vi**2 + 2*a*d)**0.5
  elif solveFor == "vf" and vi != None and a != None and d != None:
    solution = (vi**2 + 2*a*d)**0.5
    equation = "vf**2 = vi**2 + 2ad"
    originalEquation = "vf**2 = (vi**2 + 2*a*d)**0.5"
  elif solveFor == "vi" and vf != None and a != None and d != None:      
    solution = (vf**2 - 2*a*d)**0.5
    equation = "vi**2 = vf**2 - 2ad"
    originalEquation = "vf**2 = (vi**2 + 2*a*d)**0.5"
  elif solveFor == "a" and vf != None and vi != None and d != None and d != 0:
    solution = (vf**2 - vi**2) / (2*d)
    equation = "a = (vf**2 - vi**2) / 2d"
    originalEquation = "vf**2 = (vi**2 + 2*a*d)**0.5"
  elif solveFor == "d" and vf != None and vi != None and a != None and a != 0:
    solution = (vf**2 - vi**2) / (2*a)
    equation = "d = (vf**2 - vi**2) / 2a"
    originalEquation = "vf**2 = (vi**2 + 2*a*d)**0.5"

  # Solving for the fifth equation: d = 0.5*(vi+vf)*t
  elif solveFor == "d" and vi != None and vf != None and t != None:      
    solution = 0.5*(vi + vf)*t
    equation = "d = 0.5*(vi + vf)*t"
    originalEquation = "d = 0.5*(vi+vf)*t"
  elif solveFor == "vi" and d != None and vf != None and t != None and t != 0:
    solution = (2*d / t) - vf
    equation = "vi = (2d / t) - vf"
    originalEquation = "d = 0.5*(vi+vf)*t"
  elif solveFor == "vf" and d != None and vi != None and t != None and t != 0:
    solution = (2*d / t) - vi
    equation = "vf = (2d / t) - vi"
    originalEquation = "d = 0.5*(vi+vf)*t"
  elif solveFor == "t" and d != None and vi != None and vf != None and (vi + vf) != 0:
    solution = (2*d) / (vi + vf)
    equation = "t = (2d) / (vi + vf)"
    originalEquation = "d = 0.5*(vi+vf)*t"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all forces-related problems.
def forcesCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {} 
  
  print("\nHello! You are in the Forces Chapter!")
  print("The values you are able to solve for are: ")
  #Uses for loop to loop through forcesVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
  for index in forcesVariables:
    print(f"-> {variableFullNames.get(index)}")
  #Prints out the names that users should input to use calculator.
  print(f"The shortened versions are as follows, in the same order: {forcesVariables}")

  #Uses function to call tips/notes for this specific function
  tipsAndNotes()

  #Gets user input for what they want to solve. If user input is not mass, it checks for values from the wording of the problem (checks for not mass because first question asked in scenario-checker is mass. If value has been found from scenario, prints solution and returns. 
  solveFor = input("Input the value you want to solve for (enter shortened version & be precise with capitalization): ")
  if solveFor != "mass":
    valuesFromWordingForces()
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

  #For every index (forcesVariable) in the forcesVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
  for forcesVariable in forcesVariables:
    if forcesVariable != solveFor and forcesVariable not in knowns:
      forcesInput = input(f"\nEnter a value for {variableFullNames.get(forcesVariable)} or if unknown/not given, leave this value blank: ")
      if forcesInput != "":
        knowns[forcesVariable] = float(forcesInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  vi = knowns.get("vi")
  vf = knowns.get("vf")
  a = knowns.get("a")
  t = knowns.get("t")
  Fa = knowns.get("Fa")
  Ff = knowns.get("Ff")
  mu = knowns.get("mu")
  weight = knowns.get("weight")
  Fn = knowns.get("Fn")
  Fnet = knowns.get("Fnet")

  '''
  CITATION:
  This code was generated using ChatGPT GPT-4-turbo.
  Date: 4/26/25
  Code Version: Python 3.0
  Availability: https://chatgpt.com/
  Explanation: I created the first conditional for the intended variable for each of the equations. I then told ChatGPT to use the same format and solve for the other variables of the equations. 
  '''
  
  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.
  
  # Solving for the first equation: Fa = ma
  if solveFor == "Fa" and mass != None and a != None:
    solution = mass * a      
    equation = "F = m*a"
    originalEquation = equation
  elif solveFor == "m" and Fa != None and a != None and a != 0:
    solution = Fa / a
    equation = "m = F/a"
    originalEquation = "F = m*a"
  elif solveFor == "a" and Fa != None and mass != None and mass != 0:
    solution = Fa / mass
    equation = "a = F/m"
    originalEquation = "F = m*a"

  # Solving for the second equation: Fa = m((vf-vi)/t)
  elif solveFor == "Fa" and mass != None and vf != None and vi != None and t != None and t != 0:
    solution = mass * (vf - vi) / t
    equation = "F = m*(vf - vi)/t"
    originalEquation = equation
  elif solveFor == "mass" and Fa != None and vf != None and vi != None and t != None and t != 0:
    solution = Fa / ((vf - vi) / t)
    equation = "m = F/((vf - vi)/t)"
    originalEquation = "F = m*(vf - vi)/t"
  elif solveFor == "vf" and Fa != None and mass != None and vi != None and t != None and mass != 0:
    solution = ((Fa / mass) * t) + vi
    equation = "vf = ((F/m)*t) + vi"
    originalEquation = "F = m*(vf - vi)/t"
  elif solveFor == "vi" and Fa != None and mass != None and vf != None and t != None and mass != 0:
    solution = vf - ((Fa / mass) * t)
    equation = "vi = vf - ((F/m)*t)"
    originalEquation = "F = m*(vf - vi)/t"
  elif solveFor == "t" and Fa != None and mass != None and vf != None and vi != None and (vf - vi) != 0:
    solution = mass * (vf - vi) / Fa
    equation = "t = m*(vf - vi)/F"
    originalEquation = "F = m*(vf - vi)/t"

  # Solving for the third equation: Ff = mu*Fn
  elif solveFor == "Ff" and mu != None and Fn != None:
    solution = mu * Fn
    equation = "Ff = μ*Fn"
    originalEquation = equation
  elif solveFor == "mu" and Ff != None and Fn != None and Fn != 0:
    solution = Ff / Fn
    equation = "μ = Ff/Fn"
    originalEquation = "Ff = μ*Fn"
  elif solveFor == "Fn" and Ff != None and mu != None and mu != 0:
    solution = Ff / mu
    equation = "Fn = Ff/μ"
    originalEquation = "Ff = μ*Fn"

  elif solveFor == "Fnet":
    Fnet = 0
    howManyForces = int(input("\nHow many forces in total are there for the netforce?: "))
    for i in range(howManyForces):
      valueOfForce = float(input("Enter the amount of newtons each force was, one by one: "))
      Fnet+=valueOfForce
    solution = Fnet
    equation = "ΣF"
    originalEquation = "ΣF"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all momentum-related problems.
def momentumCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {} 
  
  print("\nHello! You are in the Momentum Chapter!")
  print("The values you are able to solve for are: ")
  #Uses for loop to loop through momentumVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
  for index in momentumVariables:
    print(f"-> {variableFullNames.get(index)}")
  #Prints out the names that users should input to use calculator.
  print(f"The shortened versions are as follows, in the same order: {momentumVariables}")

  #Uses function to call tips/notes for this specific function
  tipsAndNotes()

  #Gets user input for what they want to solve
  solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

  #For every index (momentumVariable) in the momentumVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
  for momentumVariable in momentumVariables:
    if momentumVariable != solveFor and momentumVariable not in knowns:
      momentumInput = input(f"\nEnter a value for {variableFullNames.get(momentumVariable)} or if unknown/not given, leave this value blank: ")
      if momentumInput != "":
        knowns[momentumVariable] = float(momentumInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  p = knowns.get("p")
  pi = knowns.get("pi")
  pf = knowns.get("pf")
  changeOfp = knowns.get("changeOfp")    
  J = knowns.get("J")
  vi = knowns.get("vi")
  vf = knowns.get("vf")
  v = knowns.get("v")
  t = knowns.get("t")
  Fa = knowns.get("Fa")
  mass = knowns.get("mass")

  '''
  CITATION:
  This code was generated using ChatGPT GPT-4-turbo.
  Date: 4/26/25
  Code Version: Python 3.0
  Availability: https://chatgpt.com/
  Explanation: I created the first conditional for the intended variable for each of the equations. I then told ChatGPT to use the same format and solve for the other variables of the equations. 
  '''

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.
  
  #Solving for the first equation: p = mv
  if solveFor == "p" and mass != None and v != None:
    solution = mass * v
    equation = "p = m * v"
    originalEquation = "p = mv"
  elif solveFor == "v" and p != None and mass != None and mass != 0:
    solution = p / mass
    equation = "v = p / m"
    originalEquation = "p = mv"
  elif solveFor == "mass" and p != None and v != None and v != 0:
    solution = p / v
    equation = "m = p / v"
    originalEquation = "p = mv"

  #Solving for the second equation: J = pf - pi
  elif solveFor == "J" and pf != None and pi != None:
    solution = pf - pi
    equation = "J = pf - pi"
    originalEquation = "J = pf - pi"
  elif solveFor == "pf" and J != None and pi != None:
    solution = J + pi
    equation = "pf = J + pi"
    originalEquation = "J = pf - pi"
  elif solveFor == "pi" and pf != None and J != None:
    solution = pf - J
    equation = "pi = pf - J"
    originalEquation = "J = pf - pi"

  #Solving for the third equation: changeOfp = pf - pi
  elif solveFor == "changeOfp" and pf != None and pi != None:
    solution = pf - pi
    equation = "changeOfp = pf - pi"
    originalEquation = "changeOfp = pf - pi"

  #Solving for the fourth equation: J = Fa * t
  elif solveFor == "J" and Fa != None and t != None:
    solution = Fa * t
    equation = "J = Fa * t"
    originalEquation = "J = Fa * t"
  elif solveFor == "Fa" and J != None and t != None and t != 0:
    solution = J / t
    equation = "Fa = J / t"
    originalEquation = "J = Fa * t"
  elif solveFor == "t" and J != None and Fa != None and Fa != 0:
    solution = J / Fa
    equation = "t = J / Fa"
    originalEquation = "J = Fa * t"

  #Solving for the fifth equation: J = mvf - mvi
  elif solveFor == "J" and vf != None and vi != None and mass != None:
    solution = (mass*vf) - (mass*vi)
    equation = "J = mvf - mvi"
    originalEquation = "J = mvf - mvi"
  elif solveFor == "mass" and J != None and vf != None and vi != None and (vf - vi) != 0:
    solution = J / (vf - vi)
    equation = "mass = J / (vf - vi)"
    originalEquation = "J = mvf - mvi"
  elif solveFor == "vf" and J != None and vi != None and mass != None:
    solution = (J / mass) + vi
    equation = "vf = (J / m) + vi"
    originalEquation = "J = mvf - mvi"
  elif solveFor == "vi" and J != None and vf != None and mass != None:
    solution = vf - (J / mass)
    equation = "vi = vf - (J / m)"
    originalEquation = "J = mvf - mvi"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all collision-related problems.
def collisionsCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {} 
  
  print("\nHello! You are in the Collisions Chapter, an extension of the Momentum Chapter (Conservation of Momentum)!")

  #Uses function to call tips/notes for this specific function
  tipsAndNotes()

  #Checks to see if collision is elastic or not-- this decision changes scenarios as well as solvable values.
  if YesOrNo("Is your collision elastic?"):
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through collisionVariablesElastic list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in collisionVariablesElastic:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {collisionVariablesElastic}")

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingCollisionsElastic()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

    #For every index (collisionVariableE) in the collisionVariablesElastic list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for collisionVariableE in collisionVariablesElastic:
      if collisionVariableE != solveFor and collisionVariableE not in knowns:
        collisionInputE = input(f"\nEnter a value for {variableFullNames.get(collisionVariableE)} or if unknown/not given, leave this value blank: ")
        if collisionInputE != "":
          knowns[collisionVariableE] = float(collisionInputE)
          
  #If inelastic, this segment occurs.
  else:
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through collisionVariablesInelastic list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in collisionVariablesInelastic:
      print(f"-> {variableFullNames.get(index)}")
    print(f"The shortened versions are as follows, in the same order: {collisionVariablesInelastic}")

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingCollisionsInelastic()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

    #For every index (collisionVariableI) in the collisionVariablesInelastic list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for collisionVariableI in collisionVariablesInelastic:
      if collisionVariableI != solveFor and collisionVariableI not in knowns:
        collisionInputI = input(f"\nEnter a value for {variableFullNames.get(collisionVariableI)} or if unknown/not given, leave this value blank: ")
        if collisionInputI != "":
          knowns[collisionVariableI] = float(collisionInputI)
  

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  v1i = knowns.get("v1i")
  v2i = knowns.get("v2i")
  v1f = knowns.get("v1f")
  v2f = knowns.get("v2f") 
  pi1 = knowns.get("pi1")
  pi2 = knowns.get("pi2")
  pf1 = knowns.get("pf1")
  pf2 = knowns.get("pf2")
  m1 = knowns.get("m1")
  m2 = knowns.get("m2")
  vf = knowns.get("vf")
  pfc = knowns.get("pfc")

  '''
  CITATION:
  This code was generated using ChatGPT GPT-4-turbo.
  Date: 4/27/25
  Code Version: Python 3.0
  Availability: https://chatgpt.com/
  Explanation: I created the first conditional for the intended variable for each of the equations. I then told ChatGPT to use the same format and solve for the other variables of the equations.
  '''

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.
  
  #Solving for momentum values: 
  if solveFor == "pi1" and pi2 != None and pf1 != None and pf2 != None:
    solution = (pf1 + pf2) - pi2
    equation = "(pf1 + pf2) - pi2"
    originalEquation = "pi1 + pi2 = pf1 + pf2"

  elif solveFor == "pi1" and m1 != None and m2 != None and v2i != None and v1f != None and v2f != None:
    solution = (m1*v1f + m2*v2f) - m2*v2i
    equation = "(m1*v1f + m2*v2f) - m2*v2i"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  if solveFor == "pi2" and pi1 != None and pf1 != None and pf2 != None:
    solution = (pf1 + pf2) - pi1
    equation = "(pf1 + pf2) - pi1"
    originalEquation = "pi1 + pi2 = pf1 + pf2"

  elif solveFor == "pi2" and m1 != None and m2 != None and v1i != None and v1f != None and v2f != None:
    solution = (m1*v1f + m2*v2f) - m1*v1i
    equation = "(m1*v1f + m2*v2f) - m1*v1i"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  if solveFor == "pf1" and pi2 != None and pi1 != None and pf2 != None: 
    solution = (pi1 + pi2) - pf2
    equation = "(pi1 + pi2) - pf2"
    originalEquation = "pi1 + pi2 = pf1 + pf2"

  elif solveFor == "pf1" and m1 != None and m2 != None and v2i != None and v1i != None and v2f != None: 
    solution = (m1*v1i + m2*v2i) - m2*v2f
    equation = "(m1*v1i + m2*v2i) - m2*v2f"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"
    
  if solveFor == "pf2" and pi2 != None and pi1 != None and pf1 != None: 
    solution = (pi1 + pi2) - pf1
    equation = "(pi1 + pi2) - pf1"
    originalEquation = "pi1 + pi2 = pf1 + pf2"

  elif solveFor == "pf2" and m1 != None and m2 != None and v1i != None and v1f != None and v2i != None:
    solution = (m1*v1i + m2*v2i) - m1*v1f
    equation = "(m1*v1i + m2*v2i) - m1*v1f"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  if solveFor == "pfc" and pi1 != None and pi2 != None:
    solution = pi1 + pi2
    equation = "pi1 + pi2"
    originalEquation = "pi1 + pi2 = pfc"

  elif solveFor == "pfc" and m1 != None and m2 != None and vf != None:
    solution = (m1+m2)*vf
    equation = "(m1+m2)*vf"
    originalEquation = "(m1+m2)*vf"
    
  elif solveFor == "pfc" and m1 != None and m2 != None and v1i != None and v2i != None:
    solution = (m1*v1i) + (m2*v2i)
    equation = "(m1*v1i) + (m2*v2i)"
    originalEquation = "(m1*v1i) + (m2*v2i) = (m1+m2)*vf"
    
  #Solving for the first equation: m1v1i + m2v2i = m1v1f + m2v2f
  if solveFor == "v1f" and m1 != None and m2 != None and v1i != None and v2i != None and v2f != None:
    solution = (m1*v1i + m2*v2i - m2*v2f) / m1
    equation = "v1f = (m1 * v1i + m2 * v2i - m2 * v2f) / m1"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  elif solveFor == "v2f" and m1 != None and m2 != None and v1i != None and v2i != None and v1f != None:
    solution = (m1*v1i + m2*v2i - m1*v1f) / m2
    equation = "v2f = (m1 * v1i + m2 * v2i - m1 * v1f) / m2"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  elif solveFor == "v1i" and m1 != None and m2 != None and v2i != None and v1f != None and v2f != None:
    solution = (m1*v1f + m2*v2f - m2*v2i) / m1
    equation = "v1i = (m1 * v1f + m2 * v2f - m2 * v2i) / m1"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  elif solveFor == "v2i" and m1 != None and m2 != None and v1i != None and v1f != None and v2f != None:
    solution = (m1*v1i + m2*v2f - m1*v1f) / m2
    equation = "v2i = (m1 * v1i + m2 * v2f - m1 * v1f) / m2"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  elif solveFor == "m1" and m2 != None and v1i != None and v1f != None and v2i != None and v2f != None:
    solution = (m2 * (v2f - v2i)) / (v1i - v1f)
    equation = "m1 = (m2 * (v2f - v2i)) / (v1i - v1f)"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  elif solveFor == "m2" and m1 != None and v1i != None and v1f != None and v2i != None and v2f != None:
    solution = (m1 * (v1f - v1i)) / (v2i - v2f)
    equation = "m2 = (m1 * (v1f - v1i)) / (v2i - v2f)"
    originalEquation = "m1v1i + m2v2i = m1v1f + m2v2f"

  #Solving for the second equation: m1v1i + m2v2i = (m1 + m2) * vf
  elif solveFor == "vf" and m1 != None and m2 != None and v1i != None and v2i != None:
    solution = (m1 * v1i + m2 * v2i) / (m1+m2)
    equation = "vf = (m1 * v1i + m2 * v2i) / (m1 + m2)"
    originalEquation = "m1v1i + m2v2i = (m1 + m2) * vf"

  elif solveFor == "v1i" and m1 != None and m2 != None and v2i != None and vf != None:
    solution = ((m1+m2) * vf - m2 * v2i) / m1
    equation = "v1i = ((m1 + m2) * vf - m2 * v2i) / m1"
    originalEquation = "m1v1i + m2v2i = (m1 + m2) * vf"

  elif solveFor == "v2i" and m1 != None and m2 != None and v1i != None and vf != None:
    solution = ((m1+m2) * vf - m1 * v1i) / m2
    equation = "v2i = ((m1 + m2) * vf - m1 * v1i) / m2"
    originalEquation = "m1v1i + m2v2i = (m1 + m2) * vf"

  elif solveFor == "m1" and m2 != None and v1i != None and v2i != None and vf != None:
    solution = ((vf - v2i) * m2) / (v1i - vf)
    equation = "m1 = ((vf - v2i) * m2) / (v1i - vf)"
    originalEquation = "m1v1i + m2v2i = (m1 + m2) * vf"

  elif solveFor == "m2" and m1 != None and v1i != None and v2i != None and vf != None:
    solution = ((vf - v1i) * m1) / (v2i - vf)
    equation = "m2 = ((vf - v1i) * m1) / (v2i - vf)"
    originalEquation = "m1v1i + m2v2i = (m1 + m2) * vf"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all energy-related problems.
def energyCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global energyVariables

  #Resets all values in knowns to restart calculations.
  knowns = {} 
  
  print("\nHello! You are in the Energy Chapter!")
  print("The values you are able to solve for are: ")
  #Uses for loop to loop through energyVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
  for index in energyVariables:
    print(f"-> {variableFullNames.get(index)}")
  #Prints out the names that users should input to use calculator.
  print(f"The shortened versions are as follows, in the same order: {energyVariables}")

  #Uses function to call tips/notes for this specific function
  tipsAndNotes()

  #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
  valuesFromWordingEnergy()
  solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
  if solveFor in knowns:
    print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
    return

    
  #For every index (energyVariable) in the energyVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
  for energyVariable in energyVariables:
    if energyVariable != solveFor and energyVariable not in knowns:
      energyInput = input(f"\nEnter a value for {variableFullNames.get(energyVariable)} or if unknown/not given, leave this value blank: ")
      if energyInput != "":
        knowns[energyVariable] = float(energyInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  energyVariables = ["KE", "Ug", "Uspring", "dy", "mass", "v", "k", "dspring", "Fspring"]
  KE = knowns.get("KE")
  Ug = knowns.get("Ug")
  Uspring = knowns.get("Uspring")
  dy = knowns.get("dy") 
  mass = knowns.get("mass")
  v = knowns.get("v")
  k = knowns.get("k")
  dspring = knowns.get("dspring")
  Fspring = knowns.get("Fspring")

  '''
  CITATION:
  This code was generated using ChatGPT GPT-4-turbo.
  Date: 4/27/25
  Code Version: Python 3.0
  Availability: https://chatgpt.com/
  Explanation: I created the first conditional for the intended variable for each of the equations. I then told ChatGPT to use the same format and solve for the other variables of the equations. 
  '''
  
  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.
  
  # Solving for the first equation: KE = 0.5*mass*v**2
  if solveFor == "KE" and mass != None and v != None:
    solution = 0.5*mass*v**2
    equation = "KE = 0.5*mass*v**2"
    originalEquation = "KE = 0.5*mass*v**2"
  elif solveFor == "mass" and KE != None and v != None and v != 0:
    solution = (2*KE) / (v**2)
    equation = "mass = (2*KE)/v**2"
    originalEquation = "KE = 0.5*mass*v**2"
  elif solveFor == "v" and KE != None and mass != None and mass != 0:
    solution = (2*KE / mass)**0.5
    equation = "v = sqrt(2*KE/mass)"
    originalEquation = "KE = 0.5*mass*v**2"

  # Solving for the second equation: Ug = mass*g*dy
  elif solveFor == "Ug" and mass != None and dy != None:
    solution = mass * gravAcceleration * dy
    equation = "Ug = mass*g*dy"
    originalEquation = "Ug = mass*g*dy"
  elif solveFor == "mass" and Ug != None and dy != None and dy != 0:
    solution = Ug / (gravAcceleration * dy)
    equation = "mass = Ug/(g*dy)"
    originalEquation = "Ug = mass*g*dy"
  elif solveFor == "dy" and Ug != None and mass != None and mass != 0:
    solution = Ug / (mass * gravAcceleration)
    equation = "dy = Ug/(mass*g)"
    originalEquation = "Ug = mass*g*dy"

  # Solving for the third equation: Uspring = 0.5*k*dspring**2
  elif solveFor == "Uspring" and k != None and dspring != None:
    solution = 0.5*k*dspring**2
    equation = "Uspring = 0.5*k*dspring**2"
    originalEquation = "Uspring = 0.5*k*dspring**2"
  elif solveFor == "k" and Uspring != None and dspring != None and dspring != 0:
    solution = (2*Uspring) / (dspring**2)
    equation = "k = (2*Uspring)/dspring**2"
    originalEquation = "Uspring = 0.5*k*dspring**2"
  elif solveFor == "dspring" and Uspring != None and k != None and k != 0:
    solution = (2*Uspring / k)**0.5
    equation = "dspring = sqrt(2*Uspring/k)"
    originalEquation = "Uspring = 0.5*k*dspring**2"

  # Solving for the fourth equation: Fspring = -k*dspring
  elif solveFor == "Fspring" and k != None and dspring != None:
    solution = -k * dspring
    equation = "Fspring = -k*dspring"
    originalEquation = "Fspring = -k*dspring"
  elif solveFor == "k" and Fspring != None and dspring != None and dspring != 0:
    solution = -Fspring / dspring
    equation = "k = -Fspring/dspring"
    originalEquation = "Fspring = -k*dspring"
  elif solveFor == "dspring" and Fspring != None and k != None and k != 0:
    solution = -Fspring / k
    equation = "dspring = -Fspring/k"
    originalEquation = "Fspring = -k*dspring"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all work-related problems.
def workCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor, typeWork
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {} 
  
  print("\nHello! You are in the Work & Power Chapter, an extension of the Energy Chapter!")
  #Asks user to input what type of work it is-- this determines the scenarios, and variables that are possible to solve
  typeWork = input("Is your work with (1) Kinetic, (2) Gravitational Potential, (3) Elastic Potential, or (4) general (this option includes Power/hp)?: ")

  #Checks to determine if work is Kinetic
  if typeWork == "1":          
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through kineticWorkVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in kineticWorkVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {kineticWorkVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingWork()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

    #For every index (kineticWorkVariable) in the kineticWorkVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for kineticWorkVariable in kineticWorkVariables:
      if kineticWorkVariable != solveFor and kineticWorkVariable not in knowns:
        kineticWorkInput = input(f"\nEnter a value for {variableFullNames.get(kineticWorkVariable)} or if unknown/not given, leave this value blank: ")
        if kineticWorkInput != "":
          knowns[kineticWorkVariable] = float(kineticWorkInput)

    
  #Checks to determine if work is Gravitational Potential
  elif typeWork == "2":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through gravPotentialWorkVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in gravPotentialWorkVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {gravPotentialWorkVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingWork()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
        print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
        return

    #For every index (gravPotentialWorkVariable) in the gravPotentialWorkVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for gravPotentialWorkVariable in gravPotentialWorkVariables:
      if gravPotentialWorkVariable != solveFor and gravPotentialWorkVariable not in knowns:
        gravPotentialWorkInput = input(f"\nEnter a value for {variableFullNames.get(gravPotentialWorkVariable)} or if unknown/not given, leave this value blank: ")
        if gravPotentialWorkInput != "":
          knowns[gravPotentialWorkVariable] = float(gravPotentialWorkInput)

  #Checks to determine if work is Elastic Potential
  elif typeWork == "3":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through elastPotentialWorkVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in elastPotentialWorkVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {elastPotentialWorkVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingWork()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

    #For every index (elastPotentialWorkVariable) in the elastPotentialWorkVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for elastPotentialWorkVariable in elastPotentialWorkVariables:
      if elastPotentialWorkVariable != solveFor and elastPotentialWorkVariable not in knowns:
        elastPotentialWorkInput = input(f"\nEnter a value for {variableFullNames.get(elastPotentialWorkVariable)} or if unknown/not given, leave this value blank: ")
        if elastPotentialWorkInput != "":
          knowns[elastPotentialWorkVariable] = float(elastPotentialWorkInput)

  #Checks to determine if work is general
  elif typeWork == "4":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through workVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in workVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {workVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks if work is being done at an angle
    if YesOrNo("Is there any force being applied in the direction of displacement at an angle?"):
      #If yes, gets angle degree and converts it to radians.
      theta = int(input("What is the angle?:  "))
      theta = (theta * (math.pi))/180
      costheta = math.cos(theta)
      
    #Asks user for input for what they want to solve for
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

    #For every index (workVariable) in the workVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for workVariable in workVariables:
      if workVariable != solveFor and workVariable not in knowns:
        workInput = input(f"\nEnter a value for {variableFullNames.get(workVariable)} or if unknown/not given, leave this value blank: ")
        if workInput != "":
          knowns[workVariable] = float(workInput)


  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  W = knowns.get("W")
  ei = knowns.get("ei")
  ef = knowns.get("ef")
  Fa = knowns.get("Fa") 
  d = knowns.get("d")
  P = knowns.get("P")
  hp = knowns.get("hp")
  KW = knowns.get("KW")
  KEi = knowns.get("KEi")
  KEf = knowns.get("KEf")
  vi = knowns.get("vi")
  vf = knowns.get("vf")
  mass = knowns.get("mass")
  UgW = knowns.get("UgW")
  Ugi = knowns.get("Ugi")
  Ugf = knowns.get("Ugf") 
  dyi = knowns.get("dyi")
  dyf = knowns.get("dyf")
  UspringW = knowns.get("UspringW")
  Uspringi = knowns.get("Uspringi")
  Uspringf = knowns.get("Uspringf")
  dspringi = knowns.get("dspringi")
  dspringf = knowns.get("dspringf")
  k = knowns.get("k")
  t = knowns.get("t")

  '''
  CITATION:
  This code was generated using ChatGPT GPT-4-turbo.
  Date: 4/27/25
  Code Version: Python 3.0
  Availability: https://chatgpt.com/
  Explanation: I created the first conditional for the intended variable for each of the equations. I then told ChatGPT to use the same format and solve for the other variables of the equations. 
  '''

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.
  
  #EQUATIONS FOR KINETIC ENERGY - WORK
  # Solving for the first energy equation: KW = KEf - KEi
  if solveFor == "KW" and KEf != None and KEi != None:
    solution = KEf - KEi
    equation = "KW = KEf - KEi"
    originalEquation = "KW = KEf - KEi"
  elif solveFor == "KEf" and KW != None and KEi != None:
    solution = KW + KEi
    equation = "KEf = KW + KEi"
    originalEquation = "KW = KEf - KEi"
  elif solveFor == "KEi" and KEf != None and KW != None:
    solution = KEf - KW
    equation = "KEi = KEf - KW"
    originalEquation = "KW = KEf - KEi"

  # Solving for the second energy equation: KW = (1/2)mass*vf^2 - (1/2)mass*vi^2
  elif solveFor == "KW" and vf != None and vi != None and mass != None:
    solution = 0.5 * mass * vf**2 - 0.5 * mass * vi**2
    equation = "KW = 0.5 * mass * vf^2 - 0.5 * mass * vi^2"
    originalEquation = "KW = (1/2)mass*vf^2 - (1/2)mass*vi^2"
  elif solveFor == "vf" and KW != None and vi != None and mass != None:
    temp = KW + 0.5 * mass * vi**2
    if temp >= 0:
      solution = (2 * temp / mass) ** 0.5
      equation = "vf = sqrt((2 * (KW + 0.5 * mass * vi^2)) / mass)"
      originalEquation = "KW = (1/2)mass*vf^2 - (1/2)mass*vi^2"
  elif solveFor == "vi" and KW != None and vf != None and mass != None:
    temp = 0.5 * mass * vf**2 - KW
    if temp >= 0:
      solution = (2 * temp / mass) ** 0.5
      equation = "vi = sqrt((2 * (0.5 * mass * vf^2 - KW)) / mass)"
      originalEquation = "KW = (1/2)mass*vf^2 - (1/2)mass*vi^2"
  elif solveFor == "mass" and KW != None and vf != None and vi != None and vf**2 != vi**2:
    solution = (2 * KW) / (vf**2 - vi**2)
    equation = "mass = (2 * KW) / (vf^2 - vi^2)"
    originalEquation = "KW = (1/2)mass*vf^2 - (1/2)mass*vi^2"

  #EQUATIONS FOR GRAVITATIONAL POTENTIAL ENERGY - WORK
  # Solving for the first gravitational energy equation: UgW = Ugf - Ugi
  if solveFor == "UgW" and Ugf != None and Ugi != None:
    solution = Ugf - Ugi
    equation = "UgW = Ugf - Ugi"
    originalEquation = "UgW = Ugf - Ugi"
  elif solveFor == "Ugf" and UgW != None and Ugi != None:
    solution = UgW + Ugi
    equation = "Ugf = UgW + Ugi"
    originalEquation = "UgW = Ugf - Ugi"
  elif solveFor == "Ugi" and Ugf != None and UgW != None:
    solution = Ugf - UgW
    equation = "Ugi = Ugf - UgW"
    originalEquation = "UgW = Ugf - Ugi"

  # Solving for the second gravitational energy equation: UgW = mass * g * dyf - mass * g * dyi
  elif solveFor == "UgW" and mass != None and dyf != None and dyi != None:
    solution = mass * gravAcceleration * dyf - mass * gravAcceleration * dyi
    equation = "UgW = mass*g*dyf - mass*g*dyi"
    originalEquation = "UgW = mass*g*dyf - mass*g*dyi"
  elif solveFor == "mass" and UgW != None and dyf != None and dyi != None and (dyf - dyi) != 0:
    solution = UgW / (gravAcceleration * (dyf - dyi))
    equation = "mass = UgW/(g*(dyf - dyi))"
    originalEquation = "UgW = mass*g*dyf - mass*g*dyi"
  elif solveFor == "dyf" and UgW != None and mass != None and dyi != None:
    solution = (UgW + mass * gravAcceleration * dyi) / (mass * gravAcceleration)
    equation = "dyf = (UgW + mass*g*dyi)/(mass*g)"
    originalEquation = "UgW = mass*g*dyf - mass*g*dyi"
  elif solveFor == "dyi" and UgW != None and mass != None and dyf != None:
    solution = (mass * gravAcceleration * dyf - UgW) / (mass * gravAcceleration)
    equation = "dyi = (mass*g*dyf - UgW)/(mass*g)"
    originalEquation = "UgW = mass*g*dyf - mass*g*dyi"

  #EQUATIONS FOR ELASTIC POTENTIAL ENERGY - WORK
  # Solving for the first spring energy equation: UspringW = Uspringf - Uspringi
  if solveFor == "UspringW" and Uspringf != None and Uspringi != None:
    solution = Uspringf - Uspringi
    equation = "UspringW = Uspringf - Uspringi"
    originalEquation = "UspringW = Uspringf - Uspringi"
  elif solveFor == "Uspringf" and UspringW != None and Uspringi != None:
    solution = UspringW + Uspringi
    equation = "Uspringf = UspringW + Uspringi"
    originalEquation = "UspringW = Uspringf - Uspringi"
  elif solveFor == "Uspringi" and Uspringf != None and UspringW != None:
    solution = Uspringf - UspringW
    equation = "Uspringi = Uspringf - UspringW"
    originalEquation = "UspringW = Uspringf - Uspringi"

  # Solving for the second spring energy equation: UspringW = (1/2)k*dspringf^2 - (1/2)k*dspringi^2
  elif solveFor == "UspringW" and k != None and dspringf != None and dspringi != None:
    solution = 0.5 * k * dspringf**2 - 0.5 * k * dspringi**2
    equation = "UspringW = 0.5 * k * dspringf^2 - 0.5 * k * dspringi^2"
    originalEquation = "UspringW = (1/2)k*dspringf^2 - (1/2)k*dspringi^2"
  elif solveFor == "k" and UspringW != None and dspringf != None and dspringi != None and (dspringf**2 - dspringi**2) != 0:
    solution = (2 * UspringW) / (dspringf**2 - dspringi**2)
    equation = "k = (2 * UspringW) / (dspringf^2 - dspringi^2)"
    originalEquation = "UspringW = (1/2)k*dspringf^2 - (1/2)k*dspringi^2"
  elif solveFor == "dspringf" and UspringW != None and k != None and dspringi != None:
    value = (2 * UspringW + k * dspringi**2) / k
    solution = value**0.5 if value >= 0 else None
    equation = "dspringf = sqrt((2 * UspringW + k * dspringi^2) / k)"
    originalEquation = "UspringW = (1/2)k*dspringf^2 - (1/2)k*dspringi^2"
  elif solveFor == "dspringi" and UspringW != None and k != None and dspringf != None:
    value = (k * dspringf**2 - 2 * UspringW) / k
    solution = value**0.5 if value >= 0 else None
    equation = "dspringi = sqrt((k * dspringf^2 - 2 * UspringW) / k)"
    originalEquation = "UspringW = (1/2)k*dspringf^2 - (1/2)k*dspringi^2"

  #EQUATIONS FOR REGULAR WORK
  # Solving for the first work equation: W = (Fa)*(d)*cos(theta)
  if solveFor == "W" and Fa != None and d != None and costheta != None:
    solution = Fa * d * costheta
    equation = "W = Fa*d*cos(theta)"
    originalEquation = "W = Fa*d*cos(theta)"
  elif solveFor == "Fa" and W != None and d != None and costheta != None and (d * costheta) != 0:
    solution = W / (d * costheta)
    equation = "Fa = W/(d*cos(theta))"
    originalEquation = "W = Fa*d*cos(theta)"
  elif solveFor == "d" and W != None and Fa != None and costheta != None and (Fa * costheta) != 0:
    solution = W / (Fa * costheta)
    equation = "d = W/(Fa*cos(theta))"
    originalEquation = "W = Fa*d*cos(theta)"

  # Solving for energy work relation: W = ef - ei
  elif solveFor == "W" and ef != None and ei != None:
    solution = ef - ei
    equation = "W = ef - ei"
    originalEquation = "W = ef - ei"
  elif solveFor == "ef" and W != None and ei != None:
    solution = W + ei
    equation = "ef = W + ei"
    originalEquation = "W = ef - ei"
  elif solveFor == "ei" and ef != None and W != None:
    solution = ef - W
    equation = "ei = ef - W"
    originalEquation = "W = ef - ei"

  # Solving for power: P = (ef - ei) / t
  elif solveFor == "P" and ef != None and ei != None and t != None and t != 0:
    solution = (ef - ei) / t
    equation = "P = (ef - ei)/t"
    originalEquation = "P = (ef - ei)/t"
  elif solveFor == "ef" and P != None and ei != None and t != None:
    solution = P * t + ei
    equation = "ef = P*t + ei"
    originalEquation = "P = (ef - ei)/t"
  elif solveFor == "ei" and ef != None and P != None and t != None:
    solution = ef - P * t
    equation = "ei = ef - P*t"
    originalEquation = "P = (ef - ei)/t"
  elif solveFor == "t" and ef != None and ei != None and P != None and P != 0:
    solution = (ef - ei) / P
    equation = "t = (ef - ei)/P"
    originalEquation = "P = (ef - ei)/t"

  # Solving for power: P = W / t
  elif solveFor == "P" and W != None and t != None and t != 0:
    solution = W / t
    equation = "P = W / t"
    originalEquation = "P = W / t"
  elif solveFor == "W" and P != None and t != None:
    solution = P * t
    equation = "W = P * t"
    originalEquation = "P = W / t"
  elif solveFor == "t" and W != None and P != None and P != 0:
    solution = W / P
    equation = "t = W / P"
    originalEquation = "P = W / t"

  # Solving for horsepower: hp = P / 746
  elif solveFor == "hp" and P != None:
    solution = P / 746
    equation = "hp = P / 746"
    originalEquation = "hp = P / 746"
  elif solveFor == "P" and hp != None:
    solution = hp * 746
    equation = "P = hp * 746"
    originalEquation = "hp = P / 746"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all rotational kinematics-related problems.
def rotKinematicsCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {}

  print("\nHello! You are in the Rotational Kinematics Chapter!")
  print("The values you are able to solve for are: ")
  #Uses for loop to loop through rotKinematicsVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
  for index in rotKinematicsVariables:
    print(f"-> {variableFullNames.get(index)}")
  #Prints out the names that users should input to use calculator.
  print(f"The shortened versions are as follows, in the same order: {rotKinematicsVariables}")

  #Uses function to call tips/notes for this specific function
  tipsAndNotes()

  #Checks for values from certain scenarios, then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
  valuesFromWordingRotKinematics()
  solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
  if solveFor in knowns:
    solution = knowns[solveFor] if knowns[solveFor] != None else 0
    print(f"{variableFullNames.get(solveFor)} is {solution}!")
    return

  #For every index (rotKinematicsVariable) in the rotKinematicsVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
  for rotKinematicsVariable in rotKinematicsVariables:
    if rotKinematicsVariable != solveFor and rotKinematicsVariable not in knowns:
      rotKinematicsInput = input(f"\nEnter a value for {variableFullNames.get(rotKinematicsVariable)} or if unknown/not given, leave this value blank: ")
      if rotKinematicsInput != "":
        knowns[rotKinematicsVariable] = float(rotKinematicsInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  theta_rot = knowns.get("theta_rot")
  omega_i = knowns.get("omega_i")
  omega_f = knowns.get("omega_f")
  omega = knowns.get("omega")
  alpha = knowns.get("alpha")
  arc = knowns.get("arc")
  r = knowns.get("r")
  t = knowns.get("t")

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

  #Solving for the arc length equation: arc = r * theta_rot
  if solveFor == "arc" and r != None and theta_rot != None:
    solution = r * theta_rot
    equation = "arc = r * theta"
    originalEquation = "arc = r * theta"
  elif solveFor == "r" and arc != None and theta_rot != None and theta_rot != 0:
    solution = arc / theta_rot
    equation = "r = arc / theta"
    originalEquation = "arc = r * theta"
  elif solveFor == "theta_rot" and arc != None and r != None and r != 0:
    solution = arc / r
    equation = "theta = arc / r"
    originalEquation = "arc = r * theta"

  #Solving for the first rotational kinematic equation: omega = theta_rot / t
  elif solveFor == "omega" and theta_rot != None and t != None and t != 0:
    solution = theta_rot / t
    equation = "omega = theta / t"
    originalEquation = "omega = theta / t"
  elif solveFor == "theta_rot" and omega != None and t != None:
    solution = omega * t
    equation = "theta = omega * t"
    originalEquation = "omega = theta / t"
  elif solveFor == "t" and theta_rot != None and omega != None and omega != 0:
    solution = theta_rot / omega
    equation = "t = theta / omega"
    originalEquation = "omega = theta / t"

  #Solving for the second rotational kinematic equation: alpha = (omega_f - omega_i) / t
  elif solveFor == "alpha" and omega_f != None and omega_i != None and t != None and t != 0:
    solution = (omega_f - omega_i) / t
    equation = "alpha = (omega_f - omega_i) / t"
    originalEquation = "alpha = (omega_f - omega_i) / t"
  elif solveFor == "omega_f" and omega_i != None and alpha != None and t != None:
    solution = omega_i + alpha * t
    equation = "omega_f = omega_i + alpha * t"
    originalEquation = "alpha = (omega_f - omega_i) / t"
  elif solveFor == "omega_i" and omega_f != None and alpha != None and t != None:
    solution = omega_f - alpha * t
    equation = "omega_i = omega_f - alpha * t"
    originalEquation = "alpha = (omega_f - omega_i) / t"
  elif solveFor == "t" and omega_f != None and omega_i != None and alpha != None and alpha != 0:
    solution = (omega_f - omega_i) / alpha
    equation = "t = (omega_f - omega_i) / alpha"
    originalEquation = "alpha = (omega_f - omega_i) / t"

  #Solving for the third rotational kinematic equation: theta_rot = omega_i*t + 0.5*alpha*t**2
  elif solveFor == "theta_rot" and omega_i != None and t != None and alpha != None:
    solution = omega_i * t + 0.5 * alpha * t**2
    equation = "theta = omega_i * t + 0.5 * alpha * t^2"
    originalEquation = "theta = omega_i*t + 0.5*alpha*t^2"
  elif solveFor == "omega_i" and theta_rot != None and t != None and alpha != None and t != 0:
    solution = (theta_rot - 0.5 * alpha * t**2) / t
    equation = "omega_i = (theta - 0.5 * alpha * t^2) / t"
    originalEquation = "theta = omega_i*t + 0.5*alpha*t^2"
  elif solveFor == "alpha" and theta_rot != None and omega_i != None and t != None and t != 0:
    solution = (theta_rot - omega_i * t) * 2 / (t**2)
    equation = "alpha = 2 * (theta - omega_i * t) / t^2"
    originalEquation = "theta = omega_i*t + 0.5*alpha*t^2"

  #Solving for the fourth rotational kinematic equation: omega_f**2 = omega_i**2 + 2*alpha*theta_rot
  elif solveFor == "omega_f" and omega_i != None and alpha != None and theta_rot != None:
    val = omega_i**2 + 2 * alpha * theta_rot
    solution = val**0.5 if val >= 0 else None
    equation = "omega_f = sqrt(omega_i^2 + 2*alpha*theta)"
    originalEquation = "omega_f^2 = omega_i^2 + 2*alpha*theta"
  elif solveFor == "omega_i" and omega_f != None and alpha != None and theta_rot != None:
    val = omega_f**2 - 2 * alpha * theta_rot
    solution = val**0.5 if val >= 0 else None
    equation = "omega_i = sqrt(omega_f^2 - 2*alpha*theta)"
    originalEquation = "omega_f^2 = omega_i^2 + 2*alpha*theta"
  elif solveFor == "alpha" and omega_f != None and omega_i != None and theta_rot != None and theta_rot != 0:
    solution = (omega_f**2 - omega_i**2) / (2 * theta_rot)
    equation = "alpha = (omega_f^2 - omega_i^2) / (2*theta)"
    originalEquation = "omega_f^2 = omega_i^2 + 2*alpha*theta"
  elif solveFor == "theta_rot" and omega_f != None and omega_i != None and alpha != None and alpha != 0:
    solution = (omega_f**2 - omega_i**2) / (2 * alpha)
    equation = "theta = (omega_f^2 - omega_i^2) / (2*alpha)"
    originalEquation = "omega_f^2 = omega_i^2 + 2*alpha*theta"

  #Solving for the fifth rotational kinematic equation: theta_rot = 0.5*(omega_i + omega_f)*t
  elif solveFor == "theta_rot" and omega_i != None and omega_f != None and t != None:
    solution = 0.5 * (omega_i + omega_f) * t
    equation = "theta = 0.5 * (omega_i + omega_f) * t"
    originalEquation = "theta = 0.5*(omega_i + omega_f)*t"
  elif solveFor == "omega_i" and theta_rot != None and omega_f != None and t != None and t != 0:
    solution = (2 * theta_rot / t) - omega_f
    equation = "omega_i = (2*theta / t) - omega_f"
    originalEquation = "theta = 0.5*(omega_i + omega_f)*t"
  elif solveFor == "omega_f" and theta_rot != None and omega_i != None and t != None and t != 0:
    solution = (2 * theta_rot / t) - omega_i
    equation = "omega_f = (2*theta / t) - omega_i"
    originalEquation = "theta = 0.5*(omega_i + omega_f)*t"
  elif solveFor == "t" and theta_rot != None and omega_i != None and omega_f != None and (omega_i + omega_f) != 0:
    solution = (2 * theta_rot) / (omega_i + omega_f)
    equation = "t = (2*theta) / (omega_i + omega_f)"
    originalEquation = "theta = 0.5*(omega_i + omega_f)*t"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all rotational dynamics-related problems.
def rotDynamicsCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {}

  print("\nHello! You are in the Rotational Dynamics Chapter!")
  print("The values you are able to solve for are: ")
  #Uses for loop to loop through rotDynamicsVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
  for index in rotDynamicsVariables:
    print(f"-> {variableFullNames.get(index)}")
  #Prints out the names that users should input to use calculator.
  print(f"The shortened versions are as follows, in the same order: {rotDynamicsVariables}")

  #Uses function to call tips/notes for this specific function
  tipsAndNotes()

  #Checks for values from certain scenarios, then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
  valuesFromWordingRotDynamics()
  solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
  if solveFor in knowns:
    print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
    return

  #For every index (rotDynamicsVariable) in the rotDynamicsVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
  for rotDynamicsVariable in rotDynamicsVariables:
    if rotDynamicsVariable != solveFor and rotDynamicsVariable not in knowns:
      rotDynamicsInput = input(f"\nEnter a value for {variableFullNames.get(rotDynamicsVariable)} or if unknown/not given, leave this value blank: ")
      if rotDynamicsInput != "":
        knowns[rotDynamicsVariable] = float(rotDynamicsInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  tau = knowns.get("tau")
  I = knowns.get("I")
  alpha_dyn = knowns.get("alpha_dyn")
  L = knowns.get("L")
  Li = knowns.get("Li")
  Lf = knowns.get("Lf")
  changeOfL = knowns.get("changeOfL")
  KErot = knowns.get("KErot")
  r_dyn = knowns.get("r_dyn")
  F_tang = knowns.get("F_tang")
  F_cent = knowns.get("F_cent")
  omega_dyn = knowns.get("omega_dyn")
  mass_dyn = knowns.get("mass_dyn")
  v_tang = knowns.get("v_tang")

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

  #Solving for the first equation: tau = I * alpha_dyn (Newton's 2nd Law for rotation)
  if solveFor == "tau" and I != None and alpha_dyn != None:
    solution = I * alpha_dyn
    equation = "tau = I * alpha"
    originalEquation = "tau = I * alpha"
  elif solveFor == "I" and tau != None and alpha_dyn != None and alpha_dyn != 0:
    solution = tau / alpha_dyn
    equation = "I = tau / alpha"
    originalEquation = "tau = I * alpha"
  elif solveFor == "alpha_dyn" and tau != None and I != None and I != 0:
    solution = tau / I
    equation = "alpha = tau / I"
    originalEquation = "tau = I * alpha"

  #Solving for the second equation: tau = r_dyn * F_tang (Torque from tangential force)
  elif solveFor == "tau" and r_dyn != None and F_tang != None:
    solution = r_dyn * F_tang
    equation = "tau = r * F_tang"
    originalEquation = "tau = r * F"
  elif solveFor == "r_dyn" and tau != None and F_tang != None and F_tang != 0:
    solution = tau / F_tang
    equation = "r = tau / F_tang"
    originalEquation = "tau = r * F"
  elif solveFor == "F_tang" and tau != None and r_dyn != None and r_dyn != 0:
    solution = tau / r_dyn
    equation = "F_tang = tau / r"
    originalEquation = "tau = r * F"

  #Solving for the third equation: L = I * omega_dyn (Angular Momentum)
  elif solveFor == "L" and I != None and omega_dyn != None:
    solution = I * omega_dyn
    equation = "L = I * omega"
    originalEquation = "L = I * omega"
  elif solveFor == "I" and L != None and omega_dyn != None and omega_dyn != 0:
    solution = L / omega_dyn
    equation = "I = L / omega"
    originalEquation = "L = I * omega"
  elif solveFor == "omega_dyn" and L != None and I != None and I != 0:
    solution = L / I
    equation = "omega = L / I"
    originalEquation = "L = I * omega"

  #Solving for the fourth equation: changeOfL = Lf - Li (Change in Angular Momentum)
  elif solveFor == "changeOfL" and Lf != None and Li != None:
    solution = Lf - Li
    equation = "changeOfL = Lf - Li"
    originalEquation = "changeOfL = Lf - Li"
  elif solveFor == "Lf" and changeOfL != None and Li != None:
    solution = changeOfL + Li
    equation = "Lf = changeOfL + Li"
    originalEquation = "changeOfL = Lf - Li"
  elif solveFor == "Li" and Lf != None and changeOfL != None:
    solution = Lf - changeOfL
    equation = "Li = Lf - changeOfL"
    originalEquation = "changeOfL = Lf - Li"

  #Solving for the fifth equation: KErot = 0.5 * I * omega_dyn**2 (Rotational Kinetic Energy)
  elif solveFor == "KErot" and I != None and omega_dyn != None:
    solution = 0.5 * I * omega_dyn**2
    equation = "KErot = 0.5 * I * omega^2"
    originalEquation = "KErot = 0.5 * I * omega^2"
  elif solveFor == "I" and KErot != None and omega_dyn != None and omega_dyn != 0:
    solution = (2 * KErot) / (omega_dyn**2)
    equation = "I = (2 * KErot) / omega^2"
    originalEquation = "KErot = 0.5 * I * omega^2"
  elif solveFor == "omega_dyn" and KErot != None and I != None and I != 0:
    solution = (2 * KErot / I)**0.5
    equation = "omega = sqrt(2 * KErot / I)"
    originalEquation = "KErot = 0.5 * I * omega^2"

  #Solving for the sixth equation: I = mass_dyn * r_dyn**2 (Moment of Inertia for point mass)
  elif solveFor == "I" and mass_dyn != None and r_dyn != None:
    solution = mass_dyn * r_dyn**2
    equation = "I = mass * r^2"
    originalEquation = "I = m * r^2 (point mass)"
  elif solveFor == "mass_dyn" and I != None and r_dyn != None and r_dyn != 0:
    solution = I / (r_dyn**2)
    equation = "mass = I / r^2"
    originalEquation = "I = m * r^2 (point mass)"
  elif solveFor == "r_dyn" and I != None and mass_dyn != None and mass_dyn != 0:
    solution = (I / mass_dyn)**0.5
    equation = "r = sqrt(I / mass)"
    originalEquation = "I = m * r^2 (point mass)"

  #Solving for the seventh equation: F_cent = mass_dyn * omega_dyn**2 * r_dyn (Centripetal Force)
  elif solveFor == "F_cent" and mass_dyn != None and omega_dyn != None and r_dyn != None:
    solution = mass_dyn * omega_dyn**2 * r_dyn
    equation = "F_cent = mass * omega^2 * r"
    originalEquation = "F_cent = m * omega^2 * r"
  elif solveFor == "mass_dyn" and F_cent != None and omega_dyn != None and r_dyn != None and omega_dyn != 0 and r_dyn != 0:
    solution = F_cent / (omega_dyn**2 * r_dyn)
    equation = "mass = F_cent / (omega^2 * r)"
    originalEquation = "F_cent = m * omega^2 * r"
  elif solveFor == "omega_dyn" and F_cent != None and mass_dyn != None and r_dyn != None and mass_dyn != 0 and r_dyn != 0:
    solution = (F_cent / (mass_dyn * r_dyn))**0.5
    equation = "omega = sqrt(F_cent / (mass * r))"
    originalEquation = "F_cent = m * omega^2 * r"
  elif solveFor == "r_dyn" and F_cent != None and mass_dyn != None and omega_dyn != None and mass_dyn != 0 and omega_dyn != 0:
    solution = F_cent / (mass_dyn * omega_dyn**2)
    equation = "r = F_cent / (mass * omega^2)"
    originalEquation = "F_cent = m * omega^2 * r"

  #Solving for the eighth equation: v_tang = omega_dyn * r_dyn (Tangential Velocity)
  elif solveFor == "v_tang" and omega_dyn != None and r_dyn != None:
    solution = omega_dyn * r_dyn
    equation = "v_tang = omega * r"
    originalEquation = "v_tang = omega * r"
  elif solveFor == "omega_dyn" and v_tang != None and r_dyn != None and r_dyn != 0:
    solution = v_tang / r_dyn
    equation = "omega = v_tang / r"
    originalEquation = "v_tang = omega * r"
  elif solveFor == "r_dyn" and v_tang != None and omega_dyn != None and omega_dyn != 0:
    solution = v_tang / omega_dyn
    equation = "r = v_tang / omega"
    originalEquation = "v_tang = omega * r"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all oscillations-related problems.
def oscillationsCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {}

  print("\nHello! You are in the Oscillations Chapter!")
  #Asks user which type of oscillation problem they have, as this determines which variables are relevant.
  typeOsc = input("Is this a (1) Spring-Mass SHM problem, (2) Simple Pendulum problem, or (3) general SHM (position/velocity/acceleration/energy)?: ")

  #Checks to determine if the problem is a Spring-Mass SHM problem
  if typeOsc == "1":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through simpleHarmonicVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in simpleHarmonicVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {simpleHarmonicVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingOscillations()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

    #For every index (simpleHarmonicVariable) in the simpleHarmonicVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for simpleHarmonicVariable in simpleHarmonicVariables:
      if simpleHarmonicVariable != solveFor and simpleHarmonicVariable not in knowns:
        simpleHarmonicInput = input(f"\nEnter a value for {variableFullNames.get(simpleHarmonicVariable)} or if unknown/not given, leave this value blank: ")
        if simpleHarmonicInput != "":
          knowns[simpleHarmonicVariable] = float(simpleHarmonicInput)

  #Checks to determine if the problem is a Simple Pendulum problem
  elif typeOsc == "2":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through pendulumVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in pendulumVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {pendulumVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

    #For every index (pendulumVariable) in the pendulumVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for pendulumVariable in pendulumVariables:
      if pendulumVariable != solveFor and pendulumVariable not in knowns:
        pendulumInput = input(f"\nEnter a value for {variableFullNames.get(pendulumVariable)} or if unknown/not given, leave this value blank: ")
        if pendulumInput != "":
          knowns[pendulumVariable] = float(pendulumInput)

  #Checks to determine if the problem is a general SHM problem
  elif typeOsc == "3":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through simpleHarmonicVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in simpleHarmonicVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {simpleHarmonicVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks for certain values then gets user input for what they want to solve. Then checks to see if the scenario had the value that the user was intending to find. If it did, it prints out the solution and returns.
    valuesFromWordingOscillations()
    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")
    if solveFor in knowns:
      print(f"{variableFullNames.get(solveFor)} is {knowns[solveFor]}!")
      return

    #For every index (simpleHarmonicVariable) in the simpleHarmonicVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for simpleHarmonicVariable in simpleHarmonicVariables:
      if simpleHarmonicVariable != solveFor and simpleHarmonicVariable not in knowns:
        simpleHarmonicInput = input(f"\nEnter a value for {variableFullNames.get(simpleHarmonicVariable)} or if unknown/not given, leave this value blank: ")
        if simpleHarmonicInput != "":
          knowns[simpleHarmonicVariable] = float(simpleHarmonicInput)

  #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
  A = knowns.get("A")
  omega_osc = knowns.get("omega_osc")
  T_osc = knowns.get("T_osc")
  f_osc = knowns.get("f_osc")
  x_osc = knowns.get("x_osc")
  v_osc = knowns.get("v_osc")
  a_osc = knowns.get("a_osc")
  k_osc = knowns.get("k_osc")
  mass_osc = knowns.get("mass_osc")
  phi = knowns.get("phi")
  E_osc = knowns.get("E_osc")
  T_pend = knowns.get("T_pend")
  f_pend = knowns.get("f_pend")
  L_pend = knowns.get("L_pend")
  t = knowns.get("t")

  #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

  #PENDULUM EQUATIONS
  # Solving for pendulum period: T_pend = 2*pi * sqrt(L_pend / g)
  if solveFor == "T_pend" and L_pend != None:
    solution = 2 * math.pi * (L_pend / gravAcceleration)**0.5
    equation = "T_pend = 2*pi * sqrt(L / g)"
    originalEquation = "T_pend = 2*pi * sqrt(L/g)"
  elif solveFor == "L_pend" and T_pend != None:
    solution = gravAcceleration * (T_pend / (2 * math.pi))**2
    equation = "L_pend = g * (T / (2*pi))^2"
    originalEquation = "T_pend = 2*pi * sqrt(L/g)"

  # Solving for pendulum frequency: f_pend = 1 / T_pend
  elif solveFor == "f_pend" and T_pend != None and T_pend != 0:
    solution = 1 / T_pend
    equation = "f_pend = 1 / T_pend"
    originalEquation = "f_pend = 1 / T_pend"
  elif solveFor == "T_pend" and f_pend != None and f_pend != 0:
    solution = 1 / f_pend
    equation = "T_pend = 1 / f_pend"
    originalEquation = "f_pend = 1 / T_pend"

  # Solving for pendulum frequency from length: f_pend = (1/(2*pi)) * sqrt(g / L_pend)
  elif solveFor == "f_pend" and L_pend != None:
    solution = (1 / (2 * math.pi)) * (gravAcceleration / L_pend)**0.5
    equation = "f_pend = (1/(2*pi)) * sqrt(g / L)"
    originalEquation = "f_pend = (1/(2*pi)) * sqrt(g/L)"

  #SPRING-MASS SHM EQUATIONS
  # Solving for angular frequency of spring-mass: omega_osc = sqrt(k_osc / mass_osc)
  elif solveFor == "omega_osc" and k_osc != None and mass_osc != None and mass_osc != 0:
    solution = (k_osc / mass_osc)**0.5
    equation = "omega = sqrt(k / mass)"
    originalEquation = "omega = sqrt(k/m)"
  elif solveFor == "k_osc" and omega_osc != None and mass_osc != None:
    solution = omega_osc**2 * mass_osc
    equation = "k = omega^2 * mass"
    originalEquation = "omega = sqrt(k/m)"
  elif solveFor == "mass_osc" and omega_osc != None and k_osc != None and omega_osc != 0:
    solution = k_osc / (omega_osc**2)
    equation = "mass = k / omega^2"
    originalEquation = "omega = sqrt(k/m)"

  # Solving for period of spring-mass: T_osc = 2*pi * sqrt(mass_osc / k_osc)
  elif solveFor == "T_osc" and mass_osc != None and k_osc != None and k_osc != 0:
    solution = 2 * math.pi * (mass_osc / k_osc)**0.5
    equation = "T = 2*pi * sqrt(mass / k)"
    originalEquation = "T = 2*pi * sqrt(m/k)"
  elif solveFor == "mass_osc" and T_osc != None and k_osc != None:
    solution = k_osc * (T_osc / (2 * math.pi))**2
    equation = "mass = k * (T / (2*pi))^2"
    originalEquation = "T = 2*pi * sqrt(m/k)"
  elif solveFor == "k_osc" and T_osc != None and mass_osc != None and T_osc != 0:
    solution = mass_osc * (2 * math.pi / T_osc)**2
    equation = "k = mass * (2*pi / T)^2"
    originalEquation = "T = 2*pi * sqrt(m/k)"

  # Solving for frequency from period: f_osc = 1 / T_osc
  elif solveFor == "f_osc" and T_osc != None and T_osc != 0:
    solution = 1 / T_osc
    equation = "f = 1 / T"
    originalEquation = "f = 1/T"
  elif solveFor == "T_osc" and f_osc != None and f_osc != 0:
    solution = 1 / f_osc
    equation = "T = 1 / f"
    originalEquation = "f = 1/T"

  # Solving for frequency from omega: f_osc = omega_osc / (2*pi)
  elif solveFor == "f_osc" and omega_osc != None:
    solution = omega_osc / (2 * math.pi)
    equation = "f = omega / (2*pi)"
    originalEquation = "omega = 2*pi*f"
  elif solveFor == "omega_osc" and f_osc != None:
    solution = 2 * math.pi * f_osc
    equation = "omega = 2*pi*f"
    originalEquation = "omega = 2*pi*f"

  # Solving for period from omega: T_osc = 2*pi / omega_osc
  elif solveFor == "T_osc" and omega_osc != None and omega_osc != 0:
    solution = (2 * math.pi) / omega_osc
    equation = "T = 2*pi / omega"
    originalEquation = "T = 2*pi / omega"
  elif solveFor == "omega_osc" and T_osc != None and T_osc != 0:
    solution = (2 * math.pi) / T_osc
    equation = "omega = 2*pi / T"
    originalEquation = "T = 2*pi / omega"

  #GENERAL SHM POSITION, VELOCITY, ACCELERATION EQUATIONS
  # Solving for position: x_osc = A * cos(omega_osc * t + phi)
  elif solveFor == "x_osc" and A != None and omega_osc != None and t != None and phi != None:
    solution = A * math.cos(omega_osc * t + phi)
    equation = "x = A * cos(omega * t + phi)"
    originalEquation = "x(t) = A * cos(omega*t + phi)"
  elif solveFor == "A" and x_osc != None and omega_osc != None and t != None and phi != None:
    cosVal = math.cos(omega_osc * t + phi)
    if cosVal != 0:
      solution = x_osc / cosVal
      equation = "A = x / cos(omega * t + phi)"
      originalEquation = "x(t) = A * cos(omega*t + phi)"

  # Solving for velocity: v_osc = -A * omega_osc * sin(omega_osc * t + phi)
  elif solveFor == "v_osc" and A != None and omega_osc != None and t != None and phi != None:
    solution = -A * omega_osc * math.sin(omega_osc * t + phi)
    equation = "v = -A * omega * sin(omega * t + phi)"
    originalEquation = "v(t) = -A*omega*sin(omega*t + phi)"
  elif solveFor == "A" and v_osc != None and omega_osc != None and t != None and phi != None and omega_osc != 0:
    sinVal = math.sin(omega_osc * t + phi)
    if sinVal != 0:
      solution = -v_osc / (omega_osc * sinVal)
      equation = "A = -v / (omega * sin(omega*t + phi))"
      originalEquation = "v(t) = -A*omega*sin(omega*t + phi)"

  # Solving for acceleration: a_osc = -A * omega_osc**2 * cos(omega_osc * t + phi)
  elif solveFor == "a_osc" and A != None and omega_osc != None and t != None and phi != None:
    solution = -A * omega_osc**2 * math.cos(omega_osc * t + phi)
    equation = "a = -A * omega^2 * cos(omega * t + phi)"
    originalEquation = "a(t) = -A*omega^2*cos(omega*t + phi)"

  # Solving for max velocity from amplitude and omega: v_osc_max = A * omega_osc
  elif solveFor == "v_osc" and A != None and omega_osc != None and t == None:
    solution = A * omega_osc
    equation = "v_max = A * omega"
    originalEquation = "v_max = A * omega (maximum speed)"
  elif solveFor == "A" and v_osc != None and omega_osc != None and t == None and omega_osc != 0:
    solution = v_osc / omega_osc
    equation = "A = v_max / omega"
    originalEquation = "v_max = A * omega"

  # Solving for total energy of oscillator: E_osc = 0.5 * k_osc * A**2
  elif solveFor == "E_osc" and k_osc != None and A != None:
    solution = 0.5 * k_osc * A**2
    equation = "E = 0.5 * k * A^2"
    originalEquation = "E = (1/2)*k*A^2"
  elif solveFor == "A" and E_osc != None and k_osc != None and k_osc != 0:
    solution = (2 * E_osc / k_osc)**0.5
    equation = "A = sqrt(2 * E / k)"
    originalEquation = "E = (1/2)*k*A^2"
  elif solveFor == "k_osc" and E_osc != None and A != None and A != 0:
    solution = (2 * E_osc) / (A**2)
    equation = "k = (2 * E) / A^2"
    originalEquation = "E = (1/2)*k*A^2"

  # Solving for velocity from position using energy conservation in SHM: v_osc = omega_osc * sqrt(A**2 - x_osc**2)
  elif solveFor == "v_osc" and omega_osc != None and A != None and x_osc != None:
    val = A**2 - x_osc**2
    solution = omega_osc * val**0.5 if val >= 0 else None
    equation = "v = omega * sqrt(A^2 - x^2)"
    originalEquation = "v = omega * sqrt(A^2 - x^2)"
  elif solveFor == "x_osc" and v_osc != None and omega_osc != None and A != None and omega_osc != 0:
    val = A**2 - (v_osc / omega_osc)**2
    solution = val**0.5 if val >= 0 else None
    equation = "x = sqrt(A^2 - (v/omega)^2)"
    originalEquation = "v = omega * sqrt(A^2 - x^2)"

  #Uses function to format solution, equation and originalEquation in a nice and abstract way.
  printSolution()

#Defines a function that efficiently serves as a calculator for all calculus-based physics problems.
def calculusPhysicsCalculator():
  #Defines the global values that the function will be editing. These values will be used in other functions and must update.
  global solution, equation, originalEquation, solveFor
  global knowns

  #Resets all values in knowns to restart calculations.
  knowns = {}

  print("\nHello! You are in the Calculus-Based Physics Chapter!")
  print("This chapter uses derivatives and integrals to find kinematic, rotational, work-energy, and oscillation quantities.")
  #Asks user which type of calculus physics problem they have-- separating by type avoids overloading with unnecessary inputs.
  typeCalc = input("Is this a (1) Calculus Kinematics, (2) Calculus Rotational Kinematics, (3) Calculus Work-Energy, or (4) Calculus Oscillations (SHM functions) problem?: ")

  #Checks to determine if this is a Calculus Kinematics problem
  if typeCalc == "1":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through calculusKinematicsVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in calculusKinematicsVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {calculusKinematicsVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

    #For every index (calculusKinematicsVariable) in the calculusKinematicsVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for calculusKinematicsVariable in calculusKinematicsVariables:
      if calculusKinematicsVariable != solveFor and calculusKinematicsVariable not in knowns:
        calculusKinematicsInput = input(f"\nEnter a value for {variableFullNames.get(calculusKinematicsVariable)} or if unknown/not given, leave this value blank: ")
        if calculusKinematicsInput != "":
          knowns[calculusKinematicsVariable] = float(calculusKinematicsInput)

    #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
    x0 = knowns.get("x0")
    v0 = knowns.get("v0")
    a_const = knowns.get("a_const")
    t_calc = knowns.get("t_calc")
    x_t = knowns.get("x_t")
    v_t = knowns.get("v_t")
    a_t = knowns.get("a_t")

    #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

    #Solving for position via integration of velocity: x(t) = x0 + v0*t + 0.5*a_const*t^2
    #This is the result of integrating a(t) = a_const twice with initial conditions x0 and v0.
    if solveFor == "x_t" and x0 != None and v0 != None and a_const != None and t_calc != None:
      solution = x0 + v0 * t_calc + 0.5 * a_const * t_calc**2
      equation = "x(t) = x0 + v0*t + (1/2)*a*t^2"
      originalEquation = "x(t) = integral of v(t)dt = x0 + v0*t + (1/2)*a*t^2"
    elif solveFor == "x_t" and x0 != None and v0 != None and t_calc != None and a_const == None:
      solution = x0 + v0 * t_calc
      equation = "x(t) = x0 + v0*t (constant velocity, a=0)"
      originalEquation = "x(t) = integral of v(t)dt with a=0"

    #Solving for velocity via integration of acceleration: v(t) = v0 + a_const*t
    #This is the result of integrating a(t) = a_const once with initial condition v0.
    elif solveFor == "v_t" and v0 != None and a_const != None and t_calc != None:
      solution = v0 + a_const * t_calc
      equation = "v(t) = v0 + a*t"
      originalEquation = "v(t) = integral of a(t)dt = v0 + a*t"
    elif solveFor == "v_t" and v0 != None and t_calc != None and a_const == None:
      solution = v0
      equation = "v(t) = v0 (constant, a=0)"
      originalEquation = "v(t) = integral of a(t)dt with a=0"

    #Solving for acceleration as the derivative of velocity: a(t) = a_const (given constant a)
    elif solveFor == "a_t" and a_const != None:
      solution = a_const
      equation = "a(t) = a_const (constant acceleration)"
      originalEquation = "a(t) = dv/dt = constant"

    #Solving for initial velocity from known x(t), x0, a_const, and t_calc using integration result
    elif solveFor == "v0" and x_t != None and x0 != None and a_const != None and t_calc != None and t_calc != 0:
      solution = (x_t - x0 - 0.5 * a_const * t_calc**2) / t_calc
      equation = "v0 = (x(t) - x0 - (1/2)*a*t^2) / t"
      originalEquation = "x(t) = x0 + v0*t + (1/2)*a*t^2"

    #Solving for initial position from known x(t), v0, a_const, and t_calc
    elif solveFor == "x0" and x_t != None and v0 != None and a_const != None and t_calc != None:
      solution = x_t - v0 * t_calc - 0.5 * a_const * t_calc**2
      equation = "x0 = x(t) - v0*t - (1/2)*a*t^2"
      originalEquation = "x(t) = x0 + v0*t + (1/2)*a*t^2"

    #Solving for constant acceleration from known v(t), v0, and t_calc (derivative of velocity)
    elif solveFor == "a_const" and v_t != None and v0 != None and t_calc != None and t_calc != 0:
      solution = (v_t - v0) / t_calc
      equation = "a = dv/dt = (v(t) - v0) / t"
      originalEquation = "v(t) = v0 + a*t  =>  a = dv/dt"

    #Solving for time from known v(t), v0, and a_const (solving integral equation for t)
    elif solveFor == "t_calc" and v_t != None and v0 != None and a_const != None and a_const != 0:
      solution = (v_t - v0) / a_const
      equation = "t = (v(t) - v0) / a"
      originalEquation = "v(t) = v0 + a*t"

    #Uses function to format solution, equation and originalEquation in a nice and abstract way.
    printSolution()

  #Checks to determine if this is a Calculus Rotational Kinematics problem
  elif typeCalc == "2":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through calculusRotationalVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in calculusRotationalVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {calculusRotationalVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

    #For every index (calculusRotationalVariable) in the calculusRotationalVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for calculusRotationalVariable in calculusRotationalVariables:
      if calculusRotationalVariable != solveFor and calculusRotationalVariable not in knowns:
        calculusRotationalInput = input(f"\nEnter a value for {variableFullNames.get(calculusRotationalVariable)} or if unknown/not given, leave this value blank: ")
        if calculusRotationalInput != "":
          knowns[calculusRotationalVariable] = float(calculusRotationalInput)

    #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
    theta0_calc = knowns.get("theta0_calc")
    omega0_calc = knowns.get("omega0_calc")
    alpha_t = knowns.get("alpha_t")
    t_calc = knowns.get("t_calc")
    theta_t = knowns.get("theta_t")
    omega_t = knowns.get("omega_t")

    #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

    #Solving for angular position via integration: theta(t) = theta0 + omega0*t + 0.5*alpha*t^2
    #This is the rotational analog of x(t) = x0 + v0*t + 0.5*a*t^2, integrating omega(t).
    if solveFor == "theta_t" and theta0_calc != None and omega0_calc != None and alpha_t != None and t_calc != None:
      solution = theta0_calc + omega0_calc * t_calc + 0.5 * alpha_t * t_calc**2
      equation = "theta(t) = theta0 + omega0*t + (1/2)*alpha*t^2"
      originalEquation = "theta(t) = integral of omega(t)dt = theta0 + omega0*t + (1/2)*alpha*t^2"
    elif solveFor == "theta_t" and theta0_calc != None and omega0_calc != None and t_calc != None and alpha_t == None:
      solution = theta0_calc + omega0_calc * t_calc
      equation = "theta(t) = theta0 + omega0*t (constant omega, alpha=0)"
      originalEquation = "theta(t) = integral of omega(t)dt with alpha=0"

    #Solving for angular velocity via integration of angular acceleration: omega(t) = omega0 + alpha*t
    #This is the rotational analog of v(t) = v0 + a*t, integrating alpha(t).
    elif solveFor == "omega_t" and omega0_calc != None and alpha_t != None and t_calc != None:
      solution = omega0_calc + alpha_t * t_calc
      equation = "omega(t) = omega0 + alpha*t"
      originalEquation = "omega(t) = integral of alpha(t)dt = omega0 + alpha*t"
    elif solveFor == "omega_t" and omega0_calc != None and t_calc != None and alpha_t == None:
      solution = omega0_calc
      equation = "omega(t) = omega0 (constant, alpha=0)"
      originalEquation = "omega(t) = integral of alpha(t)dt with alpha=0"

    #Solving for angular acceleration as derivative of angular velocity: alpha = (omega(t) - omega0) / t
    elif solveFor == "alpha_t" and omega_t != None and omega0_calc != None and t_calc != None and t_calc != 0:
      solution = (omega_t - omega0_calc) / t_calc
      equation = "alpha = d(omega)/dt = (omega(t) - omega0) / t"
      originalEquation = "omega(t) = omega0 + alpha*t  =>  alpha = d(omega)/dt"

    #Solving for initial angular velocity from known theta(t), theta0, alpha, and t
    elif solveFor == "omega0_calc" and theta_t != None and theta0_calc != None and alpha_t != None and t_calc != None and t_calc != 0:
      solution = (theta_t - theta0_calc - 0.5 * alpha_t * t_calc**2) / t_calc
      equation = "omega0 = (theta(t) - theta0 - (1/2)*alpha*t^2) / t"
      originalEquation = "theta(t) = theta0 + omega0*t + (1/2)*alpha*t^2"

    #Solving for initial angular position from known theta(t), omega0, alpha, and t
    elif solveFor == "theta0_calc" and theta_t != None and omega0_calc != None and alpha_t != None and t_calc != None:
      solution = theta_t - omega0_calc * t_calc - 0.5 * alpha_t * t_calc**2
      equation = "theta0 = theta(t) - omega0*t - (1/2)*alpha*t^2"
      originalEquation = "theta(t) = theta0 + omega0*t + (1/2)*alpha*t^2"

    #Solving for time from known omega(t), omega0, and alpha
    elif solveFor == "t_calc" and omega_t != None and omega0_calc != None and alpha_t != None and alpha_t != 0:
      solution = (omega_t - omega0_calc) / alpha_t
      equation = "t = (omega(t) - omega0) / alpha"
      originalEquation = "omega(t) = omega0 + alpha*t"

    #Uses function to format solution, equation and originalEquation in a nice and abstract way.
    printSolution()

  #Checks to determine if this is a Calculus Work-Energy problem
  elif typeCalc == "3":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through calculusWorkEnergyVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in calculusWorkEnergyVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {calculusWorkEnergyVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    #Checks if work is being done at an angle, converts to radians and computes costheta for use in W = F*dx*cos(theta).
    costheta_calc = None
    if YesOrNo("Is there a force applied at an angle to the displacement?"):
      theta_deg = float(input("What is the angle (in degrees)?: "))
      theta_rad = theta_deg * (math.pi / 180)
      costheta_calc = math.cos(theta_rad)

    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

    #For every index (calculusWorkEnergyVariable) in the calculusWorkEnergyVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for calculusWorkEnergyVariable in calculusWorkEnergyVariables:
      if calculusWorkEnergyVariable != solveFor and calculusWorkEnergyVariable not in knowns:
        calculusWorkEnergyInput = input(f"\nEnter a value for {variableFullNames.get(calculusWorkEnergyVariable)} or if unknown/not given, leave this value blank: ")
        if calculusWorkEnergyInput != "":
          knowns[calculusWorkEnergyVariable] = float(calculusWorkEnergyInput)

    #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
    W_calc = knowns.get("W_calc")
    F_calc = knowns.get("F_calc")
    dx_calc = knowns.get("dx_calc")
    KE_calc = knowns.get("KE_calc")
    PE_calc = knowns.get("PE_calc")
    E_total_calc = knowns.get("E_total_calc")
    mass = knowns.get("mass")
    v = knowns.get("v")
    k = knowns.get("k")
    dspring = knowns.get("dspring")

    #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

    #Solving for work done by constant force: W = integral of F*dx = F*dx*cos(theta)
    #For constant F, the integral reduces to F*displacement*cos(theta).
    if solveFor == "W_calc" and F_calc != None and dx_calc != None and costheta_calc != None:
      solution = F_calc * dx_calc * costheta_calc
      equation = "W = integral(F*dx) = F * dx * cos(theta)"
      originalEquation = "W = integral of F dx (constant F with angle)"
    elif solveFor == "W_calc" and F_calc != None and dx_calc != None and costheta_calc == None:
      solution = F_calc * dx_calc
      equation = "W = F * dx (F parallel to displacement)"
      originalEquation = "W = integral of F dx (constant F, angle = 0)"
    elif solveFor == "F_calc" and W_calc != None and dx_calc != None and costheta_calc != None and (dx_calc * costheta_calc) != 0:
      solution = W_calc / (dx_calc * costheta_calc)
      equation = "F = W / (dx * cos(theta))"
      originalEquation = "W = F * dx * cos(theta)"
    elif solveFor == "F_calc" and W_calc != None and dx_calc != None and costheta_calc == None and dx_calc != 0:
      solution = W_calc / dx_calc
      equation = "F = W / dx"
      originalEquation = "W = F * dx"
    elif solveFor == "dx_calc" and W_calc != None and F_calc != None and costheta_calc != None and (F_calc * costheta_calc) != 0:
      solution = W_calc / (F_calc * costheta_calc)
      equation = "dx = W / (F * cos(theta))"
      originalEquation = "W = F * dx * cos(theta)"
    elif solveFor == "dx_calc" and W_calc != None and F_calc != None and costheta_calc == None and F_calc != 0:
      solution = W_calc / F_calc
      equation = "dx = W / F"
      originalEquation = "W = F * dx"

    #Solving for kinetic energy: KE = 0.5 * mass * v^2
    #This is derived from the work-energy theorem: W = delta_KE, integrating F = ma.
    elif solveFor == "KE_calc" and mass != None and v != None:
      solution = 0.5 * mass * v**2
      equation = "KE = (1/2) * mass * v^2"
      originalEquation = "KE = (1/2)mv^2 (from integrating F=ma)"
    elif solveFor == "mass" and KE_calc != None and v != None and v != 0:
      solution = (2 * KE_calc) / (v**2)
      equation = "mass = (2 * KE) / v^2"
      originalEquation = "KE = (1/2)mv^2"
    elif solveFor == "v" and KE_calc != None and mass != None and mass != 0:
      solution = (2 * KE_calc / mass)**0.5
      equation = "v = sqrt(2 * KE / mass)"
      originalEquation = "KE = (1/2)mv^2"

    #Solving for elastic potential energy: PE = 0.5 * k * x^2
    #This is derived by integrating the spring force F = -kx over displacement: integral(-kx dx) = -(1/2)kx^2, so PE = (1/2)kx^2.
    elif solveFor == "PE_calc" and k != None and dspring != None:
      solution = 0.5 * k * dspring**2
      equation = "PE_spring = (1/2) * k * x^2"
      originalEquation = "PE = integral of kx dx = (1/2)kx^2"
    elif solveFor == "k" and PE_calc != None and dspring != None and dspring != 0:
      solution = (2 * PE_calc) / (dspring**2)
      equation = "k = (2 * PE) / x^2"
      originalEquation = "PE = (1/2)kx^2"
    elif solveFor == "dspring" and PE_calc != None and k != None and k != 0:
      solution = (2 * PE_calc / k)**0.5
      equation = "x = sqrt(2 * PE / k)"
      originalEquation = "PE = (1/2)kx^2"

    #Solving for total mechanical energy: E_total = KE + PE (Conservation of Energy)
    #For a conservative system, the total mechanical energy is constant: E_total = KE + PE = constant.
    elif solveFor == "E_total_calc" and KE_calc != None and PE_calc != None:
      solution = KE_calc + PE_calc
      equation = "E_total = KE + PE"
      originalEquation = "E_total = KE + PE (conservation of energy)"
    elif solveFor == "KE_calc" and E_total_calc != None and PE_calc != None:
      solution = E_total_calc - PE_calc
      equation = "KE = E_total - PE"
      originalEquation = "E_total = KE + PE"
    elif solveFor == "PE_calc" and E_total_calc != None and KE_calc != None:
      solution = E_total_calc - KE_calc
      equation = "PE = E_total - KE"
      originalEquation = "E_total = KE + PE"

    #Uses function to format solution, equation and originalEquation in a nice and abstract way.
    printSolution()

  #Checks to determine if this is a Calculus Oscillations (SHM functions) problem
  elif typeCalc == "4":
    print("The values you are able to solve for are: ")
    #Uses for loop to loop through calculusOscillationVariables list by index, and obtains the corresponding value from the variableFullNames dictionary to get the actual name of the index.
    for index in calculusOscillationVariables:
      print(f"-> {variableFullNames.get(index)}")
    #Prints out the names that users should input to use calculator.
    print(f"The shortened versions are as follows, in the same order: {calculusOscillationVariables}")

    #Uses function to call tips/notes for this specific function
    tipsAndNotes()

    solveFor = input("\nInput the value you want to solve for (enter shortened version & be precise with capitalization): ")

    #For every index (calculusOscillationVariable) in the calculusOscillationVariables list, it checks to see if it is solveFor and if it is in knowns, if it is not for either, it will then ask the user to input a value for the missing value. If the user does not leave the response blank, it will then turn this user-inputted value into a float and add it to the dictionary.
    for calculusOscillationVariable in calculusOscillationVariables:
      if calculusOscillationVariable != solveFor and calculusOscillationVariable not in knowns:
        calculusOscillationInput = input(f"\nEnter a value for {variableFullNames.get(calculusOscillationVariable)} or if unknown/not given, leave this value blank: ")
        if calculusOscillationInput != "":
          knowns[calculusOscillationVariable] = float(calculusOscillationInput)

    #Turns all of the known variables into values that can be used for calculations, and the unknown into "None" variables that can be used to aid with matching for an equation using conditionals
    A_calc = knowns.get("A_calc")
    omega_calc = knowns.get("omega_calc")
    phi_calc = knowns.get("phi_calc")
    t_osc_calc = knowns.get("t_osc_calc")
    x_calc = knowns.get("x_calc")
    v_calc = knowns.get("v_calc")
    a_calc = knowns.get("a_calc")

    #Conditional checks to see what needs to be solved, and then checks to see if it has the appropriate values to solve for a certain way for said inputted value. If not, it goes to the next formula.

    #Solving for SHM position function: x(t) = A * cos(omega * t + phi)
    #This is the general solution to the SHM differential equation d^2x/dt^2 = -(omega^2)*x.
    if solveFor == "x_calc" and A_calc != None and omega_calc != None and t_osc_calc != None and phi_calc != None:
      solution = A_calc * math.cos(omega_calc * t_osc_calc + phi_calc)
      equation = "x(t) = A * cos(omega * t + phi)"
      originalEquation = "x(t) = A*cos(omega*t + phi)  (solution to d^2x/dt^2 = -omega^2 * x)"
    elif solveFor == "x_calc" and A_calc != None and omega_calc != None and t_osc_calc != None and phi_calc == None:
      solution = A_calc * math.cos(omega_calc * t_osc_calc)
      equation = "x(t) = A * cos(omega * t)  (phi = 0)"
      originalEquation = "x(t) = A*cos(omega*t)  (phi=0 initial condition)"

    #Solving for SHM velocity function: v(t) = dx/dt = -A * omega * sin(omega * t + phi)
    #This is the first derivative of x(t) with respect to time.
    elif solveFor == "v_calc" and A_calc != None and omega_calc != None and t_osc_calc != None and phi_calc != None:
      solution = -A_calc * omega_calc * math.sin(omega_calc * t_osc_calc + phi_calc)
      equation = "v(t) = dx/dt = -A * omega * sin(omega * t + phi)"
      originalEquation = "v(t) = d/dt [A*cos(omega*t + phi)] = -A*omega*sin(omega*t + phi)"
    elif solveFor == "v_calc" and A_calc != None and omega_calc != None and t_osc_calc != None and phi_calc == None:
      solution = -A_calc * omega_calc * math.sin(omega_calc * t_osc_calc)
      equation = "v(t) = -A * omega * sin(omega * t)  (phi = 0)"
      originalEquation = "v(t) = d/dt [A*cos(omega*t)] = -A*omega*sin(omega*t)"

    #Solving for SHM acceleration function: a(t) = dv/dt = d^2x/dt^2 = -A * omega^2 * cos(omega * t + phi)
    #This is the second derivative of x(t) with respect to time, confirming a = -(omega^2)*x.
    elif solveFor == "a_calc" and A_calc != None and omega_calc != None and t_osc_calc != None and phi_calc != None:
      solution = -A_calc * omega_calc**2 * math.cos(omega_calc * t_osc_calc + phi_calc)
      equation = "a(t) = d^2x/dt^2 = -A * omega^2 * cos(omega * t + phi)"
      originalEquation = "a(t) = d^2/dt^2 [A*cos(omega*t + phi)] = -A*omega^2*cos(omega*t + phi)"
    elif solveFor == "a_calc" and A_calc != None and omega_calc != None and t_osc_calc != None and phi_calc == None:
      solution = -A_calc * omega_calc**2 * math.cos(omega_calc * t_osc_calc)
      equation = "a(t) = -A * omega^2 * cos(omega * t)  (phi = 0)"
      originalEquation = "a(t) = d^2/dt^2 [A*cos(omega*t)] = -A*omega^2*cos(omega*t)"

    #Solving for amplitude from known x and phi at t=0: x(0) = A*cos(phi) => A = x(0) / cos(phi)
    elif solveFor == "A_calc" and x_calc != None and phi_calc != None:
      cosVal = math.cos(phi_calc)
      if cosVal != 0:
        solution = x_calc / cosVal
        equation = "A = x(0) / cos(phi)  (using initial condition at t=0)"
        originalEquation = "x(0) = A * cos(phi)"

    #Solving for angular frequency from known a(t) and x(t) at same time: a = -omega^2 * x => omega = sqrt(-a/x)
    elif solveFor == "omega_calc" and a_calc != None and x_calc != None and x_calc != 0:
      val = -a_calc / x_calc
      if val >= 0:
        solution = val**0.5
        equation = "omega = sqrt(-a / x)  (from a = -omega^2 * x)"
        originalEquation = "a(t) = -omega^2 * x(t)"

    #Uses function to format solution, equation and originalEquation in a nice and abstract way.
    printSolution()

#Creates function to organize how the chapter functions are called, based on user input from defined parameter (chaptNum)
def showChapter(chaptNum):

  #Creates a function that easy allows for recursive calling of showChapter if needed to for as long as needed due to while loop.
  def whatNext():
    #Accesses and changes global variables, hence defining these variables as global
    global wantToContinue, chapterNum

    #While wantToContinue is true, it will repeat this question until user selects 3 and while loop ends.
    while wantToContinue == True:
      whatNext = input("Do you want to (1) use this chapter again, (2) go to another chapter or (3) leave?: ")
      #If 1, recursive calls showChapter() function with already inputted value. If 2, recursive calls showChapter() function with new value from new user  input.
      if whatNext == "1":
        showChapter(chapterNum)
      elif whatNext == "2":
        chapterNum = int(input("What chapter would you like to see?: "))
        showChapter(chapterNum)
      elif whatNext == "3":
        print("Thank you for using our Physics Calculator! I hope you have enjoyed and got the answer you needed!")
        wantToContinue = False

  #Conditional statements based on what the user input and what the parameter is that will run different functions and different segments of code as it matches the user's input to the correct function.
  if chapterNum == 1:
    kinematicsCalculator()
    whatNext()
  elif chapterNum == 2:
    forcesCalculator()
    whatNext()
  elif chapterNum == 3:
    momentumCalculator()
    whatNext()
  elif chapterNum == 4:
    collisionsCalculator()
    whatNext()
  elif chapterNum == 5:
    energyCalculator()
    whatNext()
  elif chapterNum == 6:
    workCalculator()
    whatNext()
  elif chapterNum == 7:
    rotKinematicsCalculator()
    whatNext()
  elif chapterNum == 8:
    rotDynamicsCalculator()
    whatNext()
  elif chapterNum == 9:
    oscillationsCalculator()
    whatNext()
  elif chapterNum == 10:
    calculusPhysicsCalculator()
    whatNext()

#Prints a welcome message and note when the calculator first starts off to give the user an understanding of what this is.
print("Welcome to our Fundamental Physics 1 Calculator. There are currently 10 chapters available, ranging from Kinematics to Calculus-Based Physics!")
print("NOTE: Physics is very much based on the question and your understanding rather than just mathematical formulas. Please ensure you understand your problem, its values, and what it is asking for. This is simply used to remove some time from the calculations. Trigonometry (angled surfaces in Forces) is not fully available for this calculator. ")

#Prints a message encouraging user to explore the concepts of the chapters so they understand where things are before jumping into the calculator.
print("\nIt is recommended you view all of the chapters so you know which concepts are covered in which chapter, so you know where to go to start off.")
#Asks user if they want to, if they do, it will ask them how many chapters they want to see and loop for that long asking them which chapters they want to see. 
if YesOrNo("Do you want to see the possible chapters?"):
  amountOfTimes = int(input("How many chapters would you like to see (1-10): "))
  for i in range(amountOfTimes):
    inputChapterNum = int(input("\nEnter the number of the chapter you would like to see, so you can see the concepts inside: "))
    showChapters(inputChapterNum)

#After this, if they chose the above option or not, the code initiates as it asks the user to input a chapter number and initially runs the showChapter() function.
chapterNum = int(input("What chapter would you like to go to?: "))
showChapter(chapterNum)
