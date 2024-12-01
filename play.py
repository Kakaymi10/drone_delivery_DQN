import time
from stable_baselines3 import DQN
from drone_delivery_gym_env_opt import DroneDeliveryEnv 

# Load the trained model
model = DQN.load("drone_delivery_agent_model")  

# Initialize the environment
env = DroneDeliveryEnv()

# Reset the environment
observation, _ = env.reset()
done = False
total_reward = 0

print("Starting environment testing...\n")
print("Initial Observation:\n", observation)

# Run the agent for a series of steps using the trained model
for step in range(50):  # Run for a maximum of 55 steps
    if done:
        print("Stopping the simulation as the episode is done.")
        break

    # Get action from the trained model
    action, _states = model.predict(observation, deterministic=True)  # Get predicted action

    # Take the action in the environment
    observation, reward, done, truncated, info = env.step(action)
    total_reward += reward

    # Render the environment
    env.render()


    #wait for 1 second
    time.sleep(1)
    # Stop if the game is done
    if done:
        print("Episode ended!")
        env.close("Congrats you delivered all!")  # Display the completion message
        break

# Final output
print("Testing complete!")
print(f"Total Reward: {total_reward}")
env.close("Drone Crashed")  # Display message if drone crashed
