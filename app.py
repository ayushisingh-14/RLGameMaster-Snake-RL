import streamlit as st
import torch
from env.snake_env import SnakeEnv
from model.dqn_model import DQN

st.title("🐍 RLGameMaster – Snake AI")

env = SnakeEnv()
state_shape = env.observation_space.shape
action_size = env.action_space.n

model = DQN(state_shape, action_size)
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()

if st.button("Play Snake"):
    state, _ = env.reset()
    total_reward = 0

    for _ in range(200):
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            action = torch.argmax(model(state_tensor)).item()

        state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward

        if terminated or truncated:
            break

    st.success(f"Game Over! Total Reward: {total_reward}")
