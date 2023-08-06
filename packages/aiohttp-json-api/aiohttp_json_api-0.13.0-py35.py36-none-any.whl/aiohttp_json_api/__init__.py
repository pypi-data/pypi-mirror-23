# -*- coding: utf-8 -*-
__author__ = """Vladimir Bolshakov"""
__email__ = 'vovanbo@gmail.com'
__version__ = '0.13.0'


def setup_jsonapi(app, schemas, *, base_path='/api', version='1.0.0',
                  meta=None, context_class=None, registry_class=None,
                  custom_handlers=None, log_errors=True):
    import inspect
    from collections import MutableMapping, Sequence

    from . import handlers as default_handlers
    from .const import JSONAPI
    from .context import RequestContext
    from .log import logger
    from .middleware import jsonapi_middleware
    from .registry import Registry
    from .schema import Schema

    if registry_class is not None:
        assert issubclass(registry_class, Registry), \
            'Subclass of Registry is required. Got: {}'.format(registry_class)
    else:
        registry_class = Registry

    if context_class is not None:
        assert issubclass(context_class, RequestContext), \
            'Subclass of RequestContext is required. ' \
            'Got: {}'.format(context_class)
    else:
        context_class = RequestContext

    app_registry = registry_class()

    for schema_cls in schemas:
        assert inspect.isclass(schema_cls), \
            'Class (not instance) of schema is required.'
        assert issubclass(schema_cls, Schema), \
            'Subclass of Schema is required. Got: {}'.format(schema_cls)

        schema = schema_cls(app)
        assert isinstance(schema.type, str), 'Schema type must be a string.'

        app_registry[schema.type] = schema
        if schema.resource_class is None:
            logger.warning(
                'The schema "%s" is not bound to a resource class.',
                schema.type
            )
        else:
            assert inspect.isclass(schema.resource_class), \
                'Class (not instance) of resource is required.'
            app_registry[schema.resource_class] = schema

    app[JSONAPI] = {
        'context_class': context_class,
        'jsonapi': {
            'version': version,
            'meta': meta
        },
        'registry': app_registry,
        'log_errors': log_errors
    }

    collection_resource = app.router.add_resource(
        '{}/{{type}}'.format(base_path),
        name='jsonapi.collection'
    )
    resource_resource = app.router.add_resource(
        '{}/{{type}}/{{id}}'.format(base_path),
        name='jsonapi.resource'
    )
    relationships_resource = app.router.add_resource(
        '{}/{{type}}/{{id}}/relationships/{{relation}}'.format(base_path),
        name='jsonapi.relationships'
    )
    related_resource = app.router.add_resource(
        '{}/{{type}}/{{id}}/{{relation}}'.format(base_path),
        name='jsonapi.related'
    )

    handlers = {
        i[0]: i[1]
        for i in inspect.getmembers(default_handlers,
                                    inspect.iscoroutinefunction)
        if i[0] in default_handlers.__all__
    }
    if custom_handlers is not None:
        if isinstance(custom_handlers, MutableMapping):
            handlers.update(custom_handlers)
        elif isinstance(custom_handlers, Sequence):
            for custom_handler in custom_handlers:
                if inspect.iscoroutinefunction(custom_handler):
                    handlers[custom_handler.__name__] = custom_handler

    collection_resource.add_route('GET', handlers['get_collection'])
    collection_resource.add_route('POST', handlers['post_resource'])
    resource_resource.add_route('GET', handlers['get_resource'])
    resource_resource.add_route('PATCH', handlers['patch_resource'])
    resource_resource.add_route('DELETE', handlers['delete_resource'])
    relationships_resource.add_route('GET', handlers['get_relationship'])
    relationships_resource.add_route('POST', handlers['post_relationship'])
    relationships_resource.add_route('PATCH', handlers['patch_relationship'])
    relationships_resource.add_route('DELETE', handlers['delete_relationship'])
    related_resource.add_route('GET', handlers['get_related'])

    logger.debug('Registered JSON API related resources list:')
    for resource in filter(lambda r: r.name.startswith('jsonapi'),
                           app.router.resources()):
        logger.debug('%s -> %s',
                     [r.method for r in resource], resource.get_info())

    app.middlewares.append(jsonapi_middleware)

    return app
