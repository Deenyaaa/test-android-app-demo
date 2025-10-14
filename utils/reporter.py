import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def render_report(reports):
    template_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=False)

    template = env.get_template("report_template.txt")
    return template.render(reports=reports)

def save_report_to_file(reports):
    text = render_report(reports)

    # Папка для отчётов
    reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Имя файла с датой
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(reports_dir, f"report_{date_str}.txt")

    # Записать отчет в файл
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    return file_path
