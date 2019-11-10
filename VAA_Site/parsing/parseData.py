import textblob as tb


def reformat_text(text, format_dict):
    text_list = text.split(' ')
    for i in range(len(text_list) - 1):
        if text_list[i] + ' ' + text_list[i + 1] in format_dict:
            text_list.insert(i, format_dict[text_list[i] + ' ' + text_list[i + 1]])
            text_list.pop(i + 1)
            text_list.pop(i + 1)
            text_list.append('')
    return ' '.join(text_list)


def make_format_dict(raw_input):
    temp_dict = {}
    lines = raw_input.split("\n")
    for line in lines:
        dict_entry = line.split(":")
        temp_dict[dict_entry[0]] = dict_entry[1]
    return temp_dict


def parse_data(text):
    actions = open("VAA_Site/parsing/actions.txt", "r").read()

    recipients = open("VAA_Site/parsing/recipients.txt", "r").read()

    castables = open('VAA_Site/parsing/castables.txt', 'r').read()

    throwables = open('VAA_Site/parsing/throwables.txt', 'r').read()

    directions = open('VAA_Site/parsing/directions.txt', 'r').read()

    ways_to_move = open('VAA_Site/parsing/ways_to_move.txt', 'r').read()

    format_raw = open("VAA_Site/parsing/format.txt", 'r').read()

    format_dict = make_format_dict(format_raw)

    # command = "I would like to cast fire ball at the dragon"  # test command to be replaced by user entry
    command = text
    command = reformat_text(command, format_dict)
    blob = tb.TextBlob(command)
    print(blob.tags)

    recipient = ''
    action = ''
    parameter = ''
    action_classifier = ''

    for index in range(len(blob.tags)):
        if blob.tags[index][1] == 'NN' and blob.tags[index][0] in recipients:
            recipient = blob.tags[index][0]
            continue
        if (blob.tags[index][1] == 'VB' or blob.tags[index][1] == 'NN' or blob.tags[index][1] == 'JJ') and blob.tags[index][0] in actions:
            action = blob.tags[index][0]
            if action in ways_to_move:
                action = 'move'
            continue
        if action == 'cast' and blob.tags[index][1] == 'NN' and blob.tags[index][0] in castables:
            action_classifier = blob.tags[index][0]
            continue
        if action == 'throw' and blob.tags[index][1] == 'NN' and blob.tags[index][0] in throwables:
            action_classifier = blob.tags[index][0]
            continue
        if action == 'listen' and blob.tags[index][1] == 'NN' and blob.tags[index][0] in directions:
            action_classifier = blob.tags[index][0]
            continue
        if action == 'move' and (blob.tags[index][1] == 'NN' or blob.tags[index][1] == 'NNS') and blob.tags[index][0] in directions:
            action_classifier = blob.tags[index][0]
            continue

    return[action, action_classifier, recipient, parameter]
