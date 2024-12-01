import gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env
from drone_delivery_gym_env_opt import DroneDeliveryEnv
# Create the environment
env = DroneDeliveryEnv()

# Optional: Check if the environment follows Gym's API
check_env(env)

# Define the DQN model
model = DQN(
    "MlpPolicy",  # Multi-Layer Perceptron Policy
    env,  # Custom environment
    learning_rate=1e-3, 
    buffer_size=10000, 
    learning_starts=1000,  # Number of steps before training starts
    batch_size=64,
    gamma=0.99,  # Discount factor
    target_update_interval=100,  # Update frequency of the target network
    verbose=1,  
)

# Train the model
print("Training the model...")
model.learn(total_timesteps=100000)  
print("Training complete!")

# Save the model
model.save("drone_delivery_agent_model")
print("Model saved as 'drone_delivery_agent_model_2.zip'")
env.close()
