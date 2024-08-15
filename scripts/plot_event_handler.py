import os
from watchdog.events import FileSystemEventHandler
from scripts.plot_manager import generate_main_html_report

class PlotFileEventHandler(FileSystemEventHandler):
    """Handle creation, modification, and deletion of plot files."""
    def __init__(self, df, output_dir):
        self.df = df
        self.output_dir = output_dir

    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        print(f"New plot script detected: {event.src_path}")
        script_name = os.path.basename(event.src_path)
        full_path = os.path.abspath(os.path.join('scripts', 'plots', script_name))
        print(f"Full path used: {full_path}")
        load_and_run_plot_script(full_path, self.df, self.output_dir)
        generate_main_html_report(self.output_dir)

    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        print(f"Plot script modified: {event.src_path}")
        script_name = os.path.basename(event.src_path)
        full_path = os.path.abspath(os.path.join('scripts', 'plots', script_name))
        print(f"Full path used: {full_path}")
        load_and_run_plot_script(full_path, self.df, self.output_dir)
        generate_main_html_report(self.output_dir)

    def on_deleted(self, event):
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        print(f"Plot script deleted: {event.src_path}")
        script_name = os.path.splitext(os.path.basename(event.src_path))[0]
        image_path = os.path.join(self.output_dir, 'plots', f'{script_name}.png')
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Removed plot image: {image_path}")
        else:
            print(f"No corresponding plot image found for {script_name}")

        # Regenerate the HTML report after deletion
        generate_main_html_report(self.output_dir)
