import os
from watchdog.events import FileSystemEventHandler
from scripts.plot_manager import load_and_run_plot_script, generate_main_html_report

class PlotFileEventHandler(FileSystemEventHandler):
    def __init__(self, df, output_dir):
        self.df = df
        self.output_dir = output_dir

    def _handle_event(self, event, action):
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        print(f"Plot script {action}: {event.src_path}")
        script_name = os.path.basename(event.src_path)
        full_path = os.path.abspath(os.path.join('scripts', 'plots', script_name))
        load_and_run_plot_script(full_path, self.df, self.output_dir)
        generate_main_html_report(self.output_dir)

    def on_created(self, event):
        self._handle_event(event, "created")

    def on_modified(self, event):
        self._handle_event(event, "modified")

    def on_deleted(self, event):
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        print(f"Plot script deleted: {event.src_path}")
        script_name = os.path.splitext(os.path.basename(event.src_path))[0]
        image_path = os.path.join(self.output_dir, 'plots', f'{script_name}.png')
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Removed plot image: {image_path}")
        generate_main_html_report(self.output_dir)
