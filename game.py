import world
from player import Player
from colored import fg, bg, attr

# Set text formatting
color = fg(1)
res = attr('reset') + attr('bold')

# Starting Image
start_img = r'''
        _____ ____  _____ _   _  ____ _   _
       |_   _|  _ \| ____| \ | |/ ___| | | |
         | | | |_) |  _| |  \| | |   | |_| |
         | | |  _ <| |___| |\  | |___|  _  |
         |_| |_| \_\_____|_| \_|\____|_| |_|
                       ___
                    .-'   `'.
                   /         \
                   |         ;
                   |         |           ___.--,
          _.._     |0) ~ (0) |    _.---'`__.-( (_.
   __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
  ( ,.--'`   ',__ /./;   ;, '.__.'`    __
  _`) )  .---.__.' / |   |\   \__..--""  """--.,_
 `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
       | |  .' _.-' |  |  \  \  '.               `~---`
        \ \/ .'     \  \   '. '-._)
         \/ /        \  \    `=.__`~-.
         / /\         `) )    / / `"".`\
   , _.-'.'\ \        / /    ( (     / /
    `--~`   ) )    .-'.'      '.'.  | (
           (/`    ( (`          ) )  '-;
            `      '-;         (-'
'''

def play():
    world.load_tiles()
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(start_img)
    print(color + room.intro_text() + res)
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print(color + "Choose an action:\n" + res)
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()
