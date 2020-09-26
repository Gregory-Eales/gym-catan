from gym.envs.registration import register

register(
    id='catan-v0',
    entry_point='gym_catan.envs:CatanEnv',
)
register(
    id='catan-extrahard-v0',
    entry_point='gym_catan.envs:CatanExtraHardEnv',
)