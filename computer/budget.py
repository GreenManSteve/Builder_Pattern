from builder import AbsBuilder


class Budget(AbsBuilder):
    def build_pc(self):
        self._computer.cpu = "10 mghz"
        self._computer.drive = "Tape drive"
        self._computer.screen = "5 inch"
        self._computer.wifi = "None"