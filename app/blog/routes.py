from flask import Blueprint, abort, render_template

blog_bp = Blueprint('blog', __name__)

ENTRADAS = {
    1: "Mi primera entrada",
    2: "Aprendiendo Flask con blueprints",
    3: "Plantillas con Jinja2",
}


@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = ENTRADAS.get(id)
    if titulo is None:
        abort(404)
    return render_template('blog/entrada.html', titulo=titulo)