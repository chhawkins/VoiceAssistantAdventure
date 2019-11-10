states = {
    'a':
        {'look': ['bookcase', 'floor', ''],
         'activate': ['switch', 'book', 'bookcase'],
         'walk': ['tunnel']
         },
    'b':
        {'listen': ['left', 'right'],
         'move': ['left', 'right']
         }
}

look = {
    'a':
        {
            'around': "its about as average as a bar can get, people milling about, lurkers around the outskirts of the room, shady figures in the shadows",
            'floor': "you see scratches on the floor near the bookcase, maybe signs that it has moved recently",
            'bookcase': "the bookcase is fairly new and sturdy, but it looks highly worn in a spot near the book 'Python: For Dummies'"}
}


def action_legal(state, action, target):
    return target in states.get(state).get(action)


def perform_action(state, action, action_modifier, target, parameter):
    if action_legal(state, action, target):
        if action == 'cast':
            cast_text(action_modifier, target)
        if action == 'look':
            look_text(state, target)


def cast_text(action_modifier, target):
    return 'You cast', action_modifier, 'at', target, '!'


def look_text(state, target):
    if target != '':
        return 'You look at the', target, 'and see', look.get(state).get(target)
    else:
        return 'You look around and see', look.get(state).get(target)
