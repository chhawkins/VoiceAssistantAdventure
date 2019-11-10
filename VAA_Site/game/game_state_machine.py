states = {
    'a':
        {'look': ['bookcase', 'floor', ''],
         'activate': ['switch', 'book', 'bookcase'],
         'move': ['tunnel', 'forward']
         },
    'b':
        {'listen': ['left', 'right'],
         'move': ['left', 'right'],
         'look': ['around', '']}
}

look = {
    'a':
        {
            '': "its about as average as a bar can get, people milling about, lurkers around the outskirts of the room, shady figures in the shadows",
            'floor': "you see scratches on the floor near the bookcase, maybe signs that it has moved recently",
            'bookcase': "the bookcase is fairly new and sturdy, but it looks highly worn in a spot near the book 'Python: For Dummies'"},
    'b':
        {
            '': "you are in a room that branches to 2 areas, with a path going left and a path going right"
        }}

move = {
    'a':
        {
            'forward': 'b',
            'tunnel': 'b',
            'in': 'b'
        },
    'b':
        {
            'left': 'c',
            'right': 'd'
        }
}

path_open = {
    'a': {
        'b': False
    },
    'b': {
        'c': False,
        'd': False
    }
}


def action_legal(state, action, target):
    return target in states.get(state).get(action)


def perform_action(action, action_modifier, target, parameter):
    file = open('VAA_Site/game/state.txt', 'r')
    state = file.read()
    file.close()
    if action_legal(state, action, target):
        if action == 'cast':
            return cast_text(action_modifier, target)
        if action == 'look':
            return look_text(state, target)
        if action == 'move':
            if path_open.get(move.get(state).get(action_modifier)):
                state = move.get(state).get(action_modifier)
                file = open('VAA_Site/game/state.txt', 'w')
                file.write(state)
                file.close()


def cast_text(action_modifier, target):
    return 'You cast', action_modifier, 'at', target, '!'


def look_text(state, target):
    if target != '' and target != 'around':
        return 'You look at the', target, 'and see', look.get(state).get(target)
    else:
        return 'You look around and see', look.get(state).get('')
