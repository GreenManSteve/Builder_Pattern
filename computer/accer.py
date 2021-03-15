from builder import AbsBuilder


class Accer(AbsBuilder):
    def build_pc(self):
        self._computer.cpu = "152 mghz"
        self._computer.drive = "CD Rom"
        self._computer.screen = "15 inch"
        self._computer.wifi = "Enabled"