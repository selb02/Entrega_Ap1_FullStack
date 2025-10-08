def register_blueprints(app):
    from .morador_route import bp as morador_bp
    from .apartamento_route import bp as apartamento_bp
    from .funcionario_route import bp as funcionario_bp
    from .conta_route import bp as conta_bp
    from .admin_route import bp as admin_bp

    app.register_blueprint(morador_bp, url_prefix='/moradores')
    app.register_blueprint(apartamento_bp, url_prefix='/apartamentos')
    app.register_blueprint(funcionario_bp, url_prefix='/funcionarios')
    app.register_blueprint(conta_bp, url_prefix='/contas')
    app.register_blueprint(admin_bp, url_prefix='/admin')
