INTENTS = {
    "open": [
        "open",
        "launch",
        "start",
        "run"
    ],

    "shutdown": [
        "shutdown",
        "shut down",
        "turn off",
        "power off"
    ],

    "restart": [
        "restart",
        "reboot",
        "re boot"
    ],

    "dataset": [
        "dataset",
        "data set"
    ]
}


def get_intent(command):

    command = command.lower()

    for intent, words in INTENTS.items():

        for word in words:

            if word in command:

                return intent

    return None