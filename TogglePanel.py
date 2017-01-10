
import sublime_plugin


class TogglePanelCommand(sublime_plugin.WindowCommand):
    def run(self, panel='output.exec'):
        ap = self.window.active_panel()
        if ap == panel:
            self.window.run_command("hide_panel", {"panel": panel})
        else:
            self.window.run_command("show_panel", {"panel": panel})

