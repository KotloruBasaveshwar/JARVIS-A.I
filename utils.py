def preprocess_command(command):

    command = command.lower().strip()

    replacements = {

        # Dataset
        "data set": "dataset",

        # Analyze
        "analyse": "analyze",
        "analyses": "analyze",

        # Open
        "launch": "open",
        "start": "open",
        "run": "open",

        # Shutdown
        "shut down": "shutdown",
        "turn off": "shutdown",
        "power off": "shutdown",

        # Restart
        "re boot": "restart",
        "reboot": "restart",

        # Website
        "web site": "website",

        # Students
        "student's": "students",

    }

    for old, new in replacements.items():

        command = command.replace(old, new)

    command = " ".join(command.split())

    return command