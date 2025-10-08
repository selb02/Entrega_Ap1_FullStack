from flask import Flask, jsonify
from flask_cors import CORS
from extensions import db, ma

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema_transportadora.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        # import models so SQLAlchemy knows them
        from models import morador, apartamento, funcionario, conta, admin
        db.create_all()

    # register blueprints
    from routes import register_blueprints
    register_blueprints(app)

    # swagger setup
    try:
        from flask_swagger_ui import get_swaggerui_blueprint
    except Exception:
        get_swaggerui_blueprint = None

    def build_openapi_spec(app):
        paths = {}
        for rule in app.url_map.iter_rules():
            if rule.endpoint == 'static' or rule.rule.startswith('/static'):
                continue
            view = app.view_functions.get(rule.endpoint)
            if view is None:
                continue
            doc = (view.__doc__ or '').strip()
            first_part = rule.rule.strip('/').split('/')
            tag = first_part[0].capitalize() if first_part and first_part[0] else 'Default'
            methods = {}
            for m in rule.methods - {'HEAD', 'OPTIONS'}:
                methods[m.lower()] = {
                    'summary': doc.splitlines()[0] if doc else '',
                    'description': doc,
                    'tags': [tag],
                    'responses': {'200': {'description': 'Success'}}
                }
            paths[rule.rule] = methods
        spec = {
            'openapi': '3.0.0',
            'info': {'title': 'Sistema Transportadora API', 'version': '1.0'},
            'paths': paths
        }
        return spec

    @app.route('/swagger.json')
    def swagger_json():
        return jsonify(build_openapi_spec(app))

    if get_swaggerui_blueprint is not None:
        SWAGGER_URL = '/docs'
        API_URL = '/swagger.json'
        swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'Sistema Transportadora API'})
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/')
    def index():
        """API inicial. Retorna status do serviço."""
        return jsonify({'message': 'Sistema Transportadora API - rodando'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
