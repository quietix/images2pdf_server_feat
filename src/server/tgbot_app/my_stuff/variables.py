import dotenv


downloads_path = dotenv.dotenv_values('.env')['DOWNLOADS_PATH']

img_2_pdf_stop_commands = [
    "/create_pdf",
    "Завершити сеанс",
    "Відмінити створення pdf ❌",
]

merge_pdf_stop_commands = [
    "/merge_pdf",
    "Завершити сеанс",
    "Відмінити об'єднання pdf ❌",
]

ready_commands = [
    "/ready_creation",
    "/ready_merge"
]