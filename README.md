# gym-catan
catan gym for training reinforcement learning algorithms


### Notable features

- tunable reward incentives
- fully functional gui for game viewing and playing
- 3 different observation types (feature plane, feature plane + feature vector, feature vector)

## Installation

Install from pip package, if you only want to use the gym environment, but don't want the example usage scripts:

```python
pip install gym-catan
```

Install from the repo, if you want basic usage demos, training scripts, pre-trained models:

```python
git clone https://github.com/Gregory-Eales/gym-catan.git
cd gym-catan
pip install -e .
```

## Environment

There are two types of environments: state-space observation or pixel observations:

|Environment|Observation Space|Action Space
|---|---|---|
|catan-v0|Box(23, 19, 5)+Vector(49)|Vector(200+)
|catan-extrahard-v0|Box(23, 19, 5)+Vector(49)|Vector(200+)


### Using Environment

basic usage

```python
import gym

env = gym.make("catan-v0")

obs = env.reset()
done = False
total_reward = 0

while not done:
  action = agent.act(obs)
  obs, reward, done, info = env.step(action)
  total_reward += reward
  env.render()

print("score: {}".format(total_reward))
```



## RL Algorithm Comparison


### catan-v0


### catan-v0 (Sample Efficiency)


### catan-v0 (Against Other Agents)


## Publications

## Sources

https://www.redblobgames.com/grids/hexagons/implementation.html


## Citation

Please use this BibTeX to cite this repository in your publications:

```

```
