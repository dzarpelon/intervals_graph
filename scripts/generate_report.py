import os

def generate_main_html(output_dir, plot_files):
    """
    Generates the main HTML report that includes all plots.
    """
    html_content = "<html><head><title>All Plots</title></head><body><h1>All Plots</h1>"

    for plot in plot_files:
        plot_relative_path = os.path.relpath(plot, start=output_dir)
        html_content += f'<h2>{os.path.basename(plot)}</h2>'
        html_content += f'<img src="{plot_relative_path}" alt="{os.path.basename(plot)}"><br><br>'

    html_content += "</body></html>"

    # Save the HTML report in the output directory
    html_path = os.path.join(output_dir, 'index.html')
    with open(html_path, 'w') as file:
        file.write(html_content)
    
    return html_path

def generate_html_report(image_path, output_dir):
    """
    Generates an individual HTML report for a specific plot.
    """
    if image_path is None:
        print("No image to generate HTML report.")
        return None

    reports_dir = os.path.join(output_dir, 'reports')

    # Ensure the reports directory exists
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    image_relative_path = os.path.relpath(image_path, start=reports_dir)

    html_content = f"""
    <html>
    <head><title>Pace and Heart Rate Graph</title></head>
    <body>
    <h1>Pace and Heart Rate vs. Time</h1>
    <img src="{image_relative_path}" alt="Pace and Heart Rate Graph">
    </body>
    </html>
    """

    html_path = os.path.join(reports_dir, 'index.html')
    with open(html_path, 'w') as file:
        file.write(html_content)
    
    return html_path
