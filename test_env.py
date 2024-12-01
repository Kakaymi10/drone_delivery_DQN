import time
from drone_delivery_gym_env import DroneDeliveryEnv
# Initialize the environment
env = DroneDeliveryEnv()

# Reset the environment
observation, _ = env.reset()
done = False
truncated = False
total_reward = 0

print("Starting environment testing...\n")
print("Initial Observation:\n", observation)

# Run the agent for a series of random steps
for step in range(1):
    if done or truncated:
        break

    # Take a random action
    action = env.action_space.sample()
    observation, reward, done, truncated, info = env.step(action)
    total_reward += reward

    # Print the agent's state
    print(f"Step {step + 1}:")
    print(f"Action Taken: {action} (0=Up, 1=Down, 2=Left, 3=Right)")
    print("Observation:\n", observation)
    print(f"Reward: {reward}")
    print(f"Done: {done}, Truncated: {truncated}\n")

    # Render the environment
    env.render()
    time.sleep(50)  # Pause to visually observe movement


env.close()
