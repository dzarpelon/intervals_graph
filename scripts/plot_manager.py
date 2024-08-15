import os
import importlib.util
from scripts.generate_report import generate_main_html


def load_and_run_plot_script(script_path, df, output_dir):
    try:
        abs_script_path = os.path.abspath(script_path)
        spec = importlib.util.spec_from_file_location("module.name", abs_script_path)
        plot_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plot_module)

        if hasattr(plot_module, 'generate_plot'):
            plot_module.generate_plot(df, output_dir)
        else:
            print(f"Error: 'generate_plot' function not found in {abs_script_path}")
    except Exception as e:
        print(f"Failed to load and run {abs_script_path}: {e}")

def generate_all_plots(df, output_dir):
    plot_scripts_dir = os.path.join('scripts', 'plots')
    for script_file in os.listdir(plot_scripts_dir):
        if script_file.endswith('.py'):
            script_path = os.path.join(plot_scripts_dir, script_file)
            load_and_run_plot_script(script_path, df, output_dir)

def generate_main_html_report(output_dir):
    plots_dir = os.path.join(output_dir, 'plots')
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    
    plot_files = [os.path.join(plots_dir, fname) for fname in os.listdir(plots_dir) if fname.endswith('.png')]
    generate_main_html(output_dir, plot_files)
