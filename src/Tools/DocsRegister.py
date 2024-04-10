def docs_register(app, docs, blueprint_name):
    app.register_blueprint(blueprint_name, url_prefix="/api")
    for rule in app.url_map.iter_rules():
        if rule.endpoint.startswith(blueprint_name.name):
            endpoint = app.view_functions[rule.endpoint]
            docs.register(endpoint, blueprint=blueprint_name.name)
