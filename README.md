# gym-catan
catan gym for training reinforcement learning algorithms


### Notable features

- 

## Installation

Install from pip package, if you only want to use the gym environment, but don't want the example usage scripts:

```
pip install gym-catan
```

Install from the repo, if you want basic usage demos, training scripts, pre-trained models:

```
git clone https://github.com/Gregory-Eales/gym-catan.git
cd gym-catan
pip install -e .
```

## Basic Usage

After installing from the repo, you can play the game against the baseline agent by running:

```
python test.py
```


## Environment

There are two types of environments: state-space observation or pixel observations:

|Environment|Observation Space|Action Space
|---|---|---|
|catan-v0|Box(11, 11, 64)|MultiBinary(1000)
|catan-extrahard-v0|Box(11, 11, 64)|MultiBinary(1000)


### Using Multi-Agent Environment

It is straight forward to modify the gym loop to enable multi-agent or self-play. Here is a basic gym loop:

```python
import gym

env = gym.make("catan-v0")

obs = env.reset()
done = False
total_reward = 0

while not done:
  action = my_policy(obs)
  obs, reward, done, info = env.step(action)
  total_reward += reward
  env.render()

print("score:", total_reward)
```

The `info` object contains extra information including the observation for the opponent:

```
info = {
  'ale.lives': agent's lives left,
  'ale.otherLives': opponent's lives left,
  'otherObs': opponent's observations,
  'state': agent's state (same as obs in state mode),
  'otherState': opponent's state (same as otherObs in state mode),
}
```

This modification allows you to evaluate `policy1` against `policy2`

```python
obs1 = env.reset()
obs2 = obs1 # both sides always see the same initial observation.

done = False
total_reward = 0

while not done:

  action1 = policy1(obs1)
  action2 = policy2(obs2)

  obs1, reward, done, info = env.step(action1, action2) # extra argument
  obs2 = info['otherObs']

  total_reward += reward
  env.render()

print("policy1's score:", total_reward)
print("policy2's score:", -total_reward)
```



## Evaluating against other agents


### catan-v0


### catan-v0 (Sample Efficiency)


### catan-v0 (Against Other Agents)


## Publications

## Sources

https://www.redblobgames.com/grids/hexagons/implementation.html



## Citation

<!--<p align="left">
  <img width="100%" src="https://media.giphy.com/media/WsMaF3xeATeiCv7dBq/giphy.gif"></img></img>
</p>-->

Please use this BibTeX to cite this repository in your publications:

```

```