states = {
    'a':
        {'look': ['bookcase', 'floor', ''],
         'push': ['switch', 'book', 'bookcase'],
         'walk': ['tunnel']
         },
    'b':
        {'listen': [''],
         'move': ['']
         }
}

look = {
    'a':
        {'around': "its about as average as a bar can get, people milling about, lurkers around the outskirts of the room, shady figures in the shadows",
         'floor': "you see scratches on the floor near the bookcase, maybe signs that it has moved recently"}
}

def action_legal(state, action, target):
    return target in states.get(state).get(action)


def perform_action(state, action, action_modifier, target, parameter):
    if action_legal(state, action, target):
        if action == 'cast':
            cast_text(action_modifier, target)


def cast_text(action_modifier, target):
    return 'You cast', action_modifier, 'at', target, '!'

def look_text(state, target):
    return 'You look at the', target, 'and see', look.get(state).get(target)