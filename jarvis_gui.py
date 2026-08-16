import tkinter as tk
import psutil
import math
import time
from datetime import datetime


class JarvisGUI:

    def __init__(self, root):

        self.root = root

        # ==================================================
        # WINDOW
        # ==================================================

        self.root.title("J.A.R.V.I.S — Personal AI Assistant")
        self.root.geometry("1400x800")
        self.root.minsize(1100, 650)
        self.root.configure(bg="#030810")

        # ==================================================
        # COLORS
        # ==================================================

        self.bg = "#030810"
        self.panel = "#071421"
        self.panel2 = "#091a29"

        self.cyan = "#00e5ff"
        self.blue = "#168cff"
        self.green = "#00ff9d"
        self.orange = "#ffb000"
        self.red = "#ff3b5f"
        self.dark_line = "#0d2a3b"
        self.glow = "#123f55"
        self.white = "#e8fbff"
        self.dim = "#668b9d"

        # ==================================================
        # ANIMATION
        # ==================================================

        self.angle = 0
        self.scan_angle = 0
        self.pulse = 0

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            root,
            bg=self.bg,
            height=75
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(15, 0)
        )

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="J.A.R.V.I.S",
            font=("Arial", 24, "bold"),
            fg=self.cyan,
            bg=self.bg
        )

        title.pack(
            side="left",
            padx=10
        )

        subtitle = tk.Label(
            header,
            text="PERSONAL AI ASSISTANT  •  v2",
            font=("Segoe UI", 9, "bold"),
            fg=self.dim,
            bg=self.bg
        )

        subtitle.pack(
            side="left",
            padx=10,
            pady=(12, 0)
        )

        self.time_label = tk.Label(
            header,
            text="",
            font=("Segoe UI", 11, "bold"),
            fg=self.white,
            bg=self.bg
        )

        self.time_label.pack(
            side="right",
            padx=15
        )

        status = tk.Label(
            header,
            text="● SYSTEM ONLINE",
            font=("Segoe UI", 10, "bold"),
            fg=self.green,
            bg=self.bg
        )

        status.pack(
            side="right",
            padx=25
        )

        # ==================================================
        # MAIN
        # ==================================================

        main = tk.Frame(
            root,
            bg=self.bg
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        # ==================================================
        # LEFT PANEL
        # ==================================================

        self.left_panel = tk.Frame(
            main,
            bg=self.panel,
            width=255
        )

        self.left_panel.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        self.left_panel.pack_propagate(False)

        self.panel_title(
            self.left_panel,
            "SYSTEM TELEMETRY"
        )

        self.cpu = self.status_row(
            self.left_panel,
            "CPU"
        )

        self.memory = self.status_row(
            self.left_panel,
            "MEMORY"
        )

        self.disk = self.status_row(
            self.left_panel,
            "STORAGE"
        )

        self.network = self.status_row(
            self.left_panel,
            "NETWORK"
        )

        self.panel_title(
            self.left_panel,
            "CORE STATUS"
        )

        self.core_status = tk.Label(
            self.left_panel,
            text="● ONLINE",
            font=("Segoe UI", 11, "bold"),
            fg=self.green,
            bg=self.panel
        )

        self.core_status.pack(
            anchor="w",
            padx=20,
            pady=10
        )
        self.core_info = tk.Label(
            self.left_panel,
            text=(
                "NEURAL ENGINE     ACTIVE\n"
                "VOICE ENGINE      READY\n"
                "COMMAND ENGINE    ONLINE\n"
                "AI MODULE         STANDBY"
            ),
            font=("Consolas", 8),
            fg=self.dim,
            bg=self.panel,
            justify="left"
        )

        self.core_info.pack(
            anchor="w",
            padx=20,
            pady=15
        )
        # ==================================================
        # CENTER
        # ==================================================

        center = tk.Frame(
            main,
            bg=self.bg
        )

        center.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.canvas = tk.Canvas(
            center,
            bg=self.bg,
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.center_status = tk.Label(
            center,
            text="JARVIS CORE • READY",
            font=("Segoe UI", 9, "bold"),
            fg=self.dim,
            bg=self.bg
        )

        self.center_status.place(
            relx=0.5,
            rely=0.92,
            anchor="center"
        )

        # ==================================================
        # RIGHT PANEL
        # ==================================================

        self.right_panel = tk.Frame(
            main,
            bg=self.panel,
            width=285
        )

        self.right_panel.pack(
            side="right",
            fill="y",
            padx=(15, 0)
        )

        self.right_panel.pack_propagate(False)

        self.panel_title(
            self.right_panel,
            "AI ACTIVITY"
        )

        self.activity = tk.Label(
            self.right_panel,
            text="READY",
            font=("Segoe UI", 20, "bold"),
            fg=self.cyan,
            bg=self.panel
        )

        self.activity.pack(
            pady=(25, 10)
        )

        self.activity_line = tk.Frame(
            self.right_panel,
            bg=self.cyan,
            height=2
        )

        self.activity_line.pack(
            fill="x",
            padx=30,
            pady=5
        )

        self.command_title = tk.Label(
            self.right_panel,
            text="CURRENT COMMAND",
            font=("Segoe UI", 8, "bold"),
            fg=self.dim,
            bg=self.panel
        )

        self.command_title.pack(
            anchor="w",
            padx=25,
            pady=(30, 5)
        )

        self.command = tk.Label(
            self.right_panel,
            text="Waiting for voice input...",
            font=("Segoe UI", 10, "bold"),
            fg=self.white,
            bg=self.panel2,
            wraplength=220,
            justify="left",
            padx=15,
            pady=15
        )

        self.command.pack(
            fill="x",
            padx=20
        )

        self.response_title = tk.Label(
            self.right_panel,
            text="JARVIS RESPONSE",
            font=("Segoe UI", 8, "bold"),
            fg=self.dim,
            bg=self.panel
        )

        self.response_title.pack(
            anchor="w",
            padx=25,
            pady=(35, 5)
        )

        self.response = tk.Label(
            self.right_panel,
            text="System ready.",
            font=("Segoe UI", 10),
            fg=self.cyan,
            bg=self.panel2,
            wraplength=220,
            justify="left",
            padx=15,
            pady=15
        )

        self.response.pack(
            fill="x",
            padx=20
        )

        # ==================================================
        # DEMO BUTTONS
        # ==================================================

        self.panel_title(
            self.right_panel,
            "SIMULATION"
        )

        button_frame = tk.Frame(
            self.right_panel,
            bg=self.panel
        )

        button_frame.pack(
            fill="x",
            padx=20
        )

        self.create_demo_button(
            button_frame,
            "LISTEN",
            self.demo_listening
        )

        self.create_demo_button(
            button_frame,
            "PROCESS",
            self.demo_processing
        )

        self.create_demo_button(
            button_frame,
            "SPEAK",
            self.demo_speaking
        )

        # ==================================================
        # BOTTOM BAR
        # ==================================================

        bottom = tk.Frame(
            root,
            bg=self.panel,
            height=85
        )

        bottom.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        bottom.pack_propagate(False)

        self.mic = tk.Label(
            bottom,
            text="●  MICROPHONE READY",
            font=("Segoe UI", 10, "bold"),
            fg=self.green,
            bg=self.panel
        )

        self.mic.pack(
            side="left",
            padx=25
        )

        self.voice_state = tk.Label(
            bottom,
            text="READY",
            font=("Segoe UI", 14, "bold"),
            fg=self.cyan,
            bg=self.panel
        )

        self.voice_state.pack(
            side="left",
            padx=45
        )

        self.wave_canvas = tk.Canvas(
            bottom,
            width=260,
            height=45,
            bg=self.panel,
            highlightthickness=0
        )

        self.wave_canvas.pack(
            side="left"
        )

        footer = tk.Label(
            bottom,
            text="VOICE ASSISTANT  •  AI CORE ACTIVE",
            font=("Segoe UI", 8, "bold"),
            fg=self.dim,
            bg=self.panel
        )

        footer.pack(
            side="right",
            padx=25
        )

        # ==================================================
        # START
        # ==================================================

        self.update_system()
        self.update_clock()
        self.animate_core()
        self.animate_wave()

    # ======================================================
    # PANEL TITLE
    # ======================================================

    def panel_title(self, parent, text):

        label = tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 9, "bold"),
            fg=self.dim,
            bg=self.panel
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

    # ======================================================
    # STATUS ROW
    # ======================================================

    def status_row(self, parent, name):

        frame = tk.Frame(
            parent,
            bg=self.panel
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=8
        )

        label = tk.Label(
            frame,
            text=name,
            font=("Segoe UI", 9),
            fg=self.dim,
            bg=self.panel
        )

        label.pack(
            side="left"
        )

        value = tk.Label(
            frame,
            text="--",
            font=("Segoe UI", 10, "bold"),
            fg=self.white,
            bg=self.panel
        )

        value.pack(
            side="right"
        )

        return value

    # ======================================================
    # DEMO BUTTON
    # ======================================================

    def create_demo_button(self, parent, text, command):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 8, "bold"),
            fg=self.cyan,
            bg=self.panel2,
            activeforeground=self.white,
            activebackground=self.panel2,
            relief="flat",
            bd=0,
            padx=8,
            pady=5,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            pady=3
        )

    # ======================================================
    # SYSTEM
    # ======================================================

    def update_system(self):

        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        self.cpu.config(
            text=f"{cpu:.0f}%"
        )

        self.memory.config(
            text=f"{memory:.0f}%"
        )

        self.disk.config(
            text=f"{disk:.0f}%"
        )

        self.network.config(
            text="ONLINE"
        )

        self.root.after(
            1000,
            self.update_system
        )

    # ======================================================
    # CLOCK
    # ======================================================

    def update_clock(self):

        now = datetime.now()

        self.time_label.config(
            text=now.strftime(
                "%d %b %Y   %H:%M:%S"
            )
        )

        self.root.after(
            1000,
            self.update_clock
        )

    # ======================================================
    # STATUS ENGINE
    # ======================================================

    def set_status(
        self,
        status,
        command,
        response,
        color
    ):

        self.activity.config(
            text=status,
            fg=color
        )

        self.voice_state.config(
            text=status,
            fg=color
        )

        self.center_status.config(
            text=f"JARVIS CORE • {status}"
        )

        self.command.config(
            text=command
        )

        self.response.config(
            text=response
        )

        self.activity_line.config(
            bg=color
        )

    # ======================================================
    # LISTENING
    # ======================================================

    def demo_listening(self):

        self.set_status(
            "LISTENING",
            'Listening for your command...',
            'Say something to JARVIS.',
            self.green
        )

        self.mic.config(
            text="●  MICROPHONE ACTIVE",
            fg=self.green
        )

    # ======================================================
    # PROCESSING
    # ======================================================

    def demo_processing(self):

        self.set_status(
            "PROCESSING",
            '"Open YouTube"',
            "Understanding your request...",
            self.orange
        )

        self.mic.config(
            text="●  PROCESSING",
            fg=self.orange
        )

    # ======================================================
    # SPEAKING
    # ======================================================

    def demo_speaking(self):

        self.set_status(
            "SPEAKING",
            '"Open YouTube"',
            "Opening YouTube for you.",
            self.cyan
        )

        self.mic.config(
            text="●  VOICE OUTPUT ACTIVE",
            fg=self.cyan
        )

        self.root.after(
            2500,
            self.reset_ready
        )

    # ======================================================
    # READY
    # ======================================================

    def reset_ready(self):

        self.set_status(
            "READY",
            "Waiting for voice input...",
            "System ready.",
            self.cyan
        )

        self.mic.config(
            text="●  MICROPHONE READY",
            fg=self.green
        )

    # ======================================================
    # AI CORE
    # ======================================================

    def animate_core(self):

        self.canvas.delete("core")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width < 100 or height < 100:

            self.root.after(
                50,
                self.animate_core
            )

            return

        cx = width // 2
        cy = height // 2

        pulse = (
            math.sin(time.time() * 3)
            * 7
        )

        # Outer rings

        for i in range(5):

            radius = (
                155
                + i * 25
                + pulse
            )

            self.canvas.create_oval(
                cx - radius,
                cy - radius,
                cx + radius,
                cy + radius,
                outline=self.cyan,
                width=1,
                tags="core"
            )

        # Orbiting particles

        for i in range(16):

            angle = (
                self.angle
                + i * 22.5
            )

            rad = math.radians(angle)

            radius = 205 + pulse

            x = cx + math.cos(rad) * radius
            y = cy + math.sin(rad) * radius

            size = 3 if i % 2 else 5

            self.canvas.create_oval(
                x - size,
                y - size,
                x + size,
                y + size,
                fill=self.cyan,
                outline="",
                tags="core"
            )

        # Scanner

        scan_rad = math.radians(
            self.scan_angle
        )

        scan_radius = 225

        sx = cx + math.cos(scan_rad) * scan_radius
        sy = cy + math.sin(scan_rad) * scan_radius

        self.canvas.create_line(
            cx,
            cy,
            sx,
            sy,
            fill=self.blue,
            width=1,
            tags="core"
        )

        # Core layers

        for i in range(5):

            radius = (
                105
                - i * 15
                + pulse / 3
            )

            self.canvas.create_oval(
                cx - radius,
                cy - radius,
                cx + radius,
                cy + radius,
                outline=(
                    self.blue
                    if i % 2
                    else self.cyan
                ),
                width=2,
                tags="core"
            )

        # Center

        self.canvas.create_oval(
            cx - 62,
            cy - 62,
            cx + 62,
            cy + 62,
            fill=self.panel2,
            outline=self.cyan,
            width=3,
            tags="core"
        )

        self.canvas.create_text(
            cx,
            cy - 8,
            text="JARVIS",
            fill=self.cyan,
            font=("Segoe UI", 21, "bold"),
            tags="core"
        )

        self.canvas.create_text(
            cx,
            cy + 18,
            text="AI CORE",
            fill=self.dim,
            font=("Segoe UI", 8, "bold"),
            tags="core"
        )

        self.angle = (
            self.angle + 1.5
        ) % 360

        self.scan_angle = (
            self.scan_angle + 2
        ) % 360

        self.root.after(
            30,
            self.animate_core
        )

    # ======================================================
    # WAVEFORM
    # ======================================================

    def animate_wave(self):

        self.wave_canvas.delete("wave")

        width = 260
        height = 45

        points = []

        for x in range(
            0,
            width,
            5
        ):

            wave = math.sin(
                (x * 0.15)
                + time.time() * 4
            )

            amplitude = 7 + (
                math.sin(time.time() * 2)
                + 1
            ) * 3

            y = (
                height / 2
                + wave * amplitude
            )

            points.extend(
                [x, y]
            )

        self.wave_canvas.create_line(
            *points,
            fill=self.cyan,
            width=2,
            smooth=True,
            tags="wave"
        )

        self.root.after(
            50,
            self.animate_wave
        )


# ==========================================================
# START
# ==========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = JarvisGUI(root)

    root.mainloop()