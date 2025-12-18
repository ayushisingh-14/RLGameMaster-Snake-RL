import streamlit as st
import time
import random

st.set_page_config(page_title="RLGameMaster Snake", layout="centered")
st.title("🐍 RLGameMaster – Snake AI Demo")

GRID_SIZE = 10

def init_game():
    return {
        "snake": [(5, 5)],
        "food": (random.randint(0, 9), random.randint(0, 9)),
        "direction": (0, 1),
        "score": 0,
        "game_over": False
    }

def move_snake(state):
    head_x, head_y = state["snake"][0]
    dx, dy = state["direction"]
    new_head = (head_x + dx, head_y + dy)

    if (
        new_head[0] < 0 or new_head[0] >= GRID_SIZE or
        new_head[1] < 0 or new_head[1] >= GRID_SIZE or
        new_head in state["snake"]
    ):
        state["game_over"] = True
        return

    state["snake"].insert(0, new_head)

    if new_head == state["food"]:
        state["score"] += 1
        state["food"] = (random.randint(0, 9), random.randint(0, 9))
    else:
        state["snake"].pop()

def render_grid(state):
    grid = [["⬜" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x, y in state["snake"]:
        grid[x][y] = "🟩"
    fx, fy = state["food"]
    grid[fx][fy] = "🍎"
    return grid

if "state" not in st.session_state:
    st.session_state.state = init_game()

col1, col2, col3, col4 = st.columns(4)

if col1.button("⬆️"):
    st.session_state.state["direction"] = (-1, 0)
if col2.button("⬅️"):
    st.session_state.state["direction"] = (0, -1)
if col3.button("➡️"):
    st.session_state.state["direction"] = (0, 1)
if col4.button("⬇️"):
    st.session_state.state["direction"] = (1, 0)

if st.button("▶️ Step"):
    move_snake(st.session_state.state)

grid = render_grid(st.session_state.state)
for row in grid:
    st.write(" ".join(row))

if st.session_state.state["game_over"]:
    st.error(f"Game Over! Score: {st.session_state.state['score']}")

  
