# README: Drone Delivery Simulation

## **Mission Statement**
My mission is to build healthtech infrastructure that leverages artificial intelligence to solve real-world challenges in **healthcare**.  I aim to develop AI-driven solutions that enhance efficiency, accessibility, and impact in these sectors:  **education**, **healthcare**, and **infrastructure**. This project simulates a drone delivery system to improve efficiency in resource distribution, such as delivering critical medical supplies to remote areas.

---
[Link to simulation](https://drive.google.com/file/d/1fHqbK1sTjCrZQ8zQIzq1_c1bCJNZQJuC/view?usp=sharing): It shows how the model behaves in different environments, the model loops infinitely in an environment without a termination condition, otherwise the model successfully complete the task by avoiding all the obstacles.

[Link to demo](https://drive.google.com/file/d/1az8yazw2gvgYKk_dv2q3xZKjxcGjjNFG/view?usp=sharing)

## **Environment Overview**

This project uses a custom-built reinforcement learning environment based on the Gymnasium framework to simulate a drone navigating a grid. The environment is designed to replicate real-world scenarios, such as avoiding obstacles and efficiently reaching multiple delivery goals.

### **Environment Details**
- **Grid Size:** 5x5
- **Agent (Drone) in blue:** Starts at the top-left corner of the grid.
- **Goals (Delivery Points) in green:** Represented as specific locations in the grid where the drone must deliver packages.
- **Obstacles in red:** Represent barriers that the drone must avoid to complete its mission.

![image](https://github.com/user-attachments/assets/5b1ec072-6ba0-4957-816e-246925845a3d)


- **Actions:**
  - `0`: Move up
  - `1`: Move down
  - `2`: Move left
  - `3`: Move right
- **Rewards:**
  - +10 for reaching a delivery point.
  - +50 bonus for completing all deliveries.
  - -1 penalty for each step taken.
  - -10 penalty for hitting an obstacle or exceeding step limits.
- **Termination Conditions:**
  - All delivery points are completed.
  - The drone exceeds the maximum step limit (50 steps).
  - The drone collides with an obstacle.

---

## **Model Training**

The model is trained using **Stable-Baselines3**'s **Deep Q-Network (DQN)** algorithm. Below are the training details:
![image](https://github.com/user-attachments/assets/9fb3dbfd-1901-406b-abb2-fe47c283f065)



### **Training Parameters**
- **Episodes:** 9,932
- **Total Timesteps:** 99,965
- **Learning Rate:** 0.001
- **loss:** 0.00643
- **Exploration Rate:** Initially high and gradually reduced to 0.05 to balance exploration and exploitation.
- **Updates:** 24,741
- **Average Reward:** ~68
- **Average Episode Length:** 10 steps

### **Training Process**
1. **Initialization:** The DQN model is set up with a neural network to predict Q-values for each action.
2. **Exploration:** The agent initially explores the environment randomly to gather diverse data.
3. **Learning:** As training progresses, the agent updates its policy based on rewards received, aiming to maximize efficiency.
4. **Optimization:** The model fine-tunes its behavior through 24,745 updates to minimize loss.
5. **Result:** The trained model achieves an average reward of ~63.9, indicating efficient performance in navigating the grid.

---

## **How to Set Up and Run**

### **1. Clone the Repository**
```bash
git clone https://github.com/Kakaymi10/drone_delivery_DQN.git
cd drone_delivery_DQN
```

### **2. Install Dependencies**
Ensure you have Python 3.8+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### **3. Test the Environment**
You can test the environment with random actions before using the trained model:
```bash
python test_env.py
```

### **4. Train the Model**
To retrain the model, run:
```bash
python train.py
```
The training process will save the model as `drone_delivery_agent_model.zip`.

### **5. Use the Trained Model**
To play with the trained model, run:
```bash
python play.py
```

---

## **Files in the Repository**
- **`drone_delivery_gym_env_opt.py`**: Custom Gym environment implementation with termination conditions.
- - **`drone_delivery_gym_env.py`**: Custom Gym environment implementation without termination conditions.
- **`train.py`**: Code for training the model using Stable-Baselines3.
- **`play.py`**: Script to test the trained model.
- **`test_env.py`**: Script to run a random agent in the environment.
- **`requirements.txt`**: List of required Python packages.

---

## **Conclusion**
This project demonstrates the potential of reinforcement learning in solving real-world challenges. By simulating a drone delivery system, we can explore ways to enhance healthcare delivery, especially in remote areas.
