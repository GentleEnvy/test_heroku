from src.app import app, run_configuration
from src.urls import init_urls

init_urls(app)
app.run(**run_configuration)
