from pypokerengine.api.game import setup_config, start_poker
from agent22player import Group22Player

#TODO:config the config as our wish
config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=10)



config.register_player(name="FT1", algorithm=Group22Player())
config.register_player(name="FT2", algorithm=Group22Player())


game_result = start_poker(config, verbose=0)