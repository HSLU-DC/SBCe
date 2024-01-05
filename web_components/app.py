from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_BASE_URL'] = 'localhost'
app.config['FREEZER_DESTINATION'] = 'public'
freezer = Freezer(app)


@app.cli.command()
def freeze():
    freezer.freeze()


@app.cli.command()
def serve():
    freezer.run()


@freezer.register_generator
def page_generator():
    """
    Frozen-Flask doesn't know what to generate when a route contains a
    variable. This function resolves this, refer to Frozen-Flask's
    documentation for more information.
    """
    for template_path in app.jinja_env.list_templates():
        try:
            page = Path(template_path).relative_to("content").stem
            yield 'pages', {'page': page}
        except ValueError:
            pass


@app.route('/')
def root():
    return render_template('root.html', pages=page_generator())


@app.route('/<page>/')
def pages(page):
    return render_template(str(Path('content') / (page + '.html')))
