import textblob as tb


def reformatText(text):
    textList = text.split(' ')
    for i in range(len(textList) - 1):
        if textList[i] + ' ' + textList[i + 1] in formatDict:
            textList.insert(i, formatDict[textList[i] + ' ' + textList[i + 1]])
            textList.pop(i + 1)
            textList.pop(i + 1)
            textList.append('')
    return ' '.join(textList)


def makeFormatDict(rawInput):
    tempDict = {}
    lines = rawInput.split("\n")
    for line in lines:
        dictEntry = line.split(":")
        tempDict[dictEntry[0]] = dictEntry[1]
    return tempDict


if __name__ == '__main__':
    actions = open("actions.txt", "r").read()

    recipients = open("recipients.txt", "r").read()

    castables = open('castables.txt', 'r').read()

    throwables = open('throwables.txt', 'r').read()

    formatRaw = open("format.txt", 'r').read()

    formatDict = makeFormatDict(formatRaw)

    command = "I would like to throw a dagger at the skeleton"  # test command to be replaced by user entry
    command = reformatText(command)
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
        if blob.tags[index][1] == 'VB' and blob.tags[index][0] in actions:
            action = blob.tags[index][0]
            continue
        if action == 'cast' and blob.tags[index][1] == 'NN' and blob.tags[index][0] in castables:
            action_classifier = blob.tags[index][0]
            continue
        if action == 'throw' and blob.tags[index][1] == 'NN' and blob.tags[index][0] in throwables:
            action_classifier = blob.tags[index][0]
            continue

    print(action, action_classifier, recipient, parameter)
