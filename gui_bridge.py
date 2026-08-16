class JarvisGUIBridge:

    def __init__(self, gui):

        self.gui = gui
        self.root = gui.root

    # ==========================================
    # SAFE GUI UPDATE
    # ==========================================

    def run_on_gui(self, function):

        self.root.after(
            0,
            function
        )

    # ==========================================
    # LISTENING
    # ==========================================

    def listening(self):

        self.run_on_gui(
            lambda: self._listening()
        )

    def _listening(self):

        self.gui.set_status(
            "LISTENING",
            "Listening for your command...",
            "Speak now.",
            self.gui.green
        )

        self.gui.mic.config(
            text="●  MICROPHONE ACTIVE",
            fg=self.gui.green
        )

    # ==========================================
    # PROCESSING
    # ==========================================

    def processing(self, command):

        self.run_on_gui(
            lambda: self._processing(command)
        )

    def _processing(self, command):

        self.gui.set_status(
            "PROCESSING",
            command,
            "Understanding your request...",
            self.gui.orange
        )

        self.gui.mic.config(
            text="●  PROCESSING",
            fg=self.gui.orange
        )

    # ==========================================
    # SPEAKING
    # ==========================================

    def speaking(self, response):

        self.run_on_gui(
            lambda: self._speaking(response)
        )

    def _speaking(self, response):

        self.gui.set_status(
            "SPEAKING",
            self.gui.command.cget("text"),
            response,
            self.gui.cyan
        )

        self.gui.mic.config(
            text="●  VOICE OUTPUT ACTIVE",
            fg=self.gui.cyan
        )

    # ==========================================
    # READY
    # ==========================================

    def ready(self):

        self.run_on_gui(
            lambda: self._ready()
        )

    def _ready(self):

        self.gui.set_status(
            "READY",
            "Waiting for voice input...",
            "System ready.",
            self.gui.cyan
        )

        self.gui.mic.config(
            text="●  MICROPHONE READY",
            fg=self.gui.green
        )

    # ==========================================
    # SHUTDOWN
    # ==========================================

    def shutdown(self):

        self.run_on_gui(
            self.root.destroy
        )