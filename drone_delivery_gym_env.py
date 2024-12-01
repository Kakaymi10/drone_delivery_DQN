import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame


class DroneDeliveryEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super(DroneDeliveryEnv, self).__init__()
        # Define grid dimensions
        self.grid_size = 5
        self.observation_space = spaces.Box(
            low=-1, high=2, shape=(self.grid_size, self.grid_size), dtype=np.int32
        )
        self.action_space = spaces.Discrete(4)  # Actions: 0=Up, 1=Down, 2=Left, 3=Right

        # Environment variables
        self.agent_pos = [0, 0]  # Starting position
        self.goal_positions = [[4, 4], [2, 2], [1, 3]]  # Exercise stations
        self.obstacle_positions = [[1, 1], [3, 3], [2, 4]]  # Obstacles

        # Visualization
        self.cell_size = 100
        self.window_size = self.grid_size * self.cell_size
        self.window = None
        self.clock = None

    def reset(self, seed=None, options=None):
        # Reset agent position
        super().reset(seed=seed)
        self.agent_pos = [0, 0]
        self.steps = 0
        self.visited_goals = set()
        return self._get_obs(), {}

    def _get_obs(self):
        grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        grid[self.agent_pos[0], self.agent_pos[1]] = 1  # Agent
        for goal in self.goal_positions:
            grid[goal[0], goal[1]] = 2  # Goals
        for obs in self.obstacle_positions:
            grid[obs[0], obs[1]] = -1  # Obstacles
        return grid

    def step(self, action):
        # Update agent position based on action
        new_pos = self.agent_pos.copy()
        if action == 0:  # Move up
            new_pos[0] -= 1
        elif action == 1:  # Move down
            new_pos[0] += 1
        elif action == 2:  # Move left
            new_pos[1] -= 1
        elif action == 3:  # Move right
            new_pos[1] += 1

        # Check boundaries and obstacles
        if (
            0 <= new_pos[0] < self.grid_size
            and 0 <= new_pos[1] < self.grid_size
            and new_pos not in self.obstacle_positions
        ):
            self.agent_pos = new_pos

        # Rewards and termination
        reward = -1  # Default step reward
        if self.agent_pos in self.goal_positions:
            self.visited_goals.add(tuple(self.agent_pos))
            reward = 10

        done = False
        truncated = False
        if len(self.visited_goals) == len(self.goal_positions):  # Win condition
            done = True
            reward += 50

        self.steps += 1
        if self.steps >= 50:  # Step limit
            done = True
            reward -= 10

        return self._get_obs(), reward, done, truncated, {}

    def render(self, mode="human"):
        if self.window is None:
            pygame.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
            pygame.display.set_caption("Drone delivery Gym Environment")
            self.clock = pygame.time.Clock()

        self.window.fill((255, 255, 255))  # White background

        # Draw grid
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.window, (200, 200, 200), rect, 1)

                if [x, y] == self.agent_pos:
                    pygame.draw.circle(
                        self.window,
                        (0, 0, 255),
                        rect.center,
                        self.cell_size // 3,
                    )  # Agent
                elif [x, y] in self.goal_positions:
                    pygame.draw.rect(self.window, (0, 255, 0), rect)  # Goals
                elif [x, y] in self.obstacle_positions:
                    pygame.draw.rect(self.window, (255, 0, 0), rect)  # Obstacles

        pygame.display.flip()
        self.clock.tick(30)

    def close(self):
        if self.window:
            pygame.quit()
            self.window = None
