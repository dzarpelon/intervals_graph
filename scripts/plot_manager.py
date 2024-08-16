import os
import importlib.util

# Use the correct directories
PLOT_SCRIPTS_DIR = os.path.join(os.getcwd(), 'scripts', 'plots')
OUTPUT_PLOTS_DIR = os.path.join(os.getcwd(), 'output', 'plots')

def load_and_run_plot_script(script_path, df, output_dir):
    try:
        spec = importlib.util.spec_from_file_location("module.name", script_path)
        plot_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plot_module)

        if hasattr(plot_module, 'generate_plot'):
            plot_module.generate_plot(df, output_dir)
        else:
            print(f"Error: 'generate_plot' function not found in {script_path}")
    except Exception as e:
        print(f"Failed to load and run {script_path}: {e}")

def generate_main_html_report(output_dir):
    plots_dir = os.path.join(output_dir)
    
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    
    plot_files = [os.path.join(plots_dir, fname) for fname in os.listdir(plots_dir) if fname.endswith('.png')]
    generate_main_html(output_dir, plot_files)

def generate_main_html(output_dir, plot_files):
    html_content = "<html><head><title>All Plots</title></head><body><h1>All Plots</h1>"

    for plot in plot_files:
        plot_relative_path = os.path.relpath(plot, start=output_dir)
        html_content += f'<h2>{os.path.basename(plot)}</h2>'
        html_content += f'<img src="{plot_relative_path}" alt="{os.path.basename(plot)}"><br><br>'

    html_content += "</body></html>"

    html_path = os.path.join(output_dir, 'index.html')
    with open(html_path, 'w') as file:
        file.write(html_content)
    
    return html_path

def generate_all_plots(df, output_dir):
    """Generate all plots by running each script in the plots directory."""
    for script_file in os.listdir(PLOT_SCRIPTS_DIR):
        if script_file.endswith('.py'):
            script_path = os.path.join(PLOT_SCRIPTS_DIR, script_file)
            load_and_run_plot_script(script_path, df, output_dir)
