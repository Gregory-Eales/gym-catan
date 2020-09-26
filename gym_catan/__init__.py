from gym.envs.registration import register

register(
    id='catan-v0',
    entry_point='gym_catan.envs:CatanEnv',
)
register(
    id='snake-extrahard-v0',
    entry_point='gym_catan.envs:CatanExtraHardEnv',
)