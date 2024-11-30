# README: Drone Delivery Simulation

## **Mission Statement**
Our mission is to build healthtech infrastructure that leverages artificial intelligence and robotics to solve real-world challenges in **education**, **healthcare**, and **infrastructure**. By simulating critical scenarios, we aim to develop AI-driven solutions that enhance efficiency, accessibility, and impact in these sectors.

This drone delivery simulation is a step toward achieving these goals by exploring the role of autonomous systems in infrastructure and healthcare delivery.

---

## **About the Drone Delivery Simulation**
This project simulates a **drone navigating a 5x5 grid**, delivering packages to designated locations while avoiding restricted areas (obstacles). It demonstrates the use of **reinforcement learning (RL)** for navigation and decision-making in a constrained environment.

### **Environment Description**
The environment is built with the following features:

- **Grid Dimensions**: 5x5 grid representing the operational area.
- **Agent**: The drone starts at the top-left corner of the grid (`[0, 0]`).
- **Goals**: Represented by green cells on the grid, the drone must visit each goal location (`[4, 4], [2, 2], [1, 3]`).
- **Obstacles**: Represented by red cells, these are no-fly zones (`[1, 1], [3, 3], [2, 4]`).
- **Rewards**:  
  - +10 for visiting a goal.  
  - -10 for entering a restricted area (immediate termination).  
  - +50 bonus for successfully delivering all packages.  
- **Termination**:  
  - All goals are visited, or the drone enters a restricted area.  
  - Step limit exceeded (default: 50 steps).  

The simulation is visualized using **Pygame**, where:
- The drone is represented as a **blue circle**.
- Goals are **green squares**.
- Obstacles are **red squares**.

---

## **Setup and Execution**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd <repository_folder>
```

### **2. Install Dependencies**
Make sure you have Python 3.8 or above. Install the required packages using:
```bash
pip install -r requirements.txt
```

### **3. Running the Environment**
There are multiple ways to interact with the environment:

#### **Run a Pre-Trained Agent (Play)**
To test a trained agent navigating the grid:
```bash
python play.py
```

#### **Train a New Model**
To train a new RL agent:
```bash
python train.py
```

#### **Test Random Actions (Baseline)**
To see how the environment works with a random policy:
```bash
python test_env.py
```

---

## **Code Explanation**
### **Environment (`FitnessGymEnv`)**
1. **Grid Initialization**:  
   - A 5x5 grid with distinct cells for goals, obstacles, and the agent.  
   - Rewards and penalties incentivize proper navigation.

2. **Reset Function**:  
   Resets the grid, places the drone at `[0, 0]`, and reinitializes goal positions.

3. **Step Function**:  
   - Executes actions (`Up`, `Down`, `Left`, `Right`), updating the drone’s position.  
   - Handles collision detection with obstacles.  
   - Awards or penalizes the agent based on its state.

4. **Rendering**:  
   - Uses **Pygame** to visually render the environment.  
   - Colors represent the agent (blue), goals (green), and obstacles (red).  

5. **Termination**:  
   - Ends the simulation when all goals are collected, the drone enters restricted areas, or the step limit is exceeded.

-

---

## **License**
This project is open-source and licensed under the MIT License. Feel free to modify and distribute it as needed.
