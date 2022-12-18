from config import App
from controllers.public import routes
from controllers.private import consultas
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("templates"))
env.globals["enumerate"] = enumerate

app = App().get_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
