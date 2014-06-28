# -*- coding: utf-8 -*-

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


import webapp2

try:
    import conf
    loader = conf.JINJA_ENVIRONMENT
except ImportError:
    # Stub configuration
    from jinja2 import Environment, PackageLoader
    loader = Environment(loader=PackageLoader('core', 'tests'))


def get_template(loader, template_name):
    """
    Gets template to be rendered.
    :param loader: loader is jinja environment instance
    :param template_name: name of template
    :returns: template to render
    """
    return loader.get_template(template_name)


class BaseHandler(webapp2.RequestHandler):
    """
    Base request handler for application
    """
    template_name = None

    def get_context(self, *args, **kwargs):
        """
        Returns context as dictionary
        """
        ctx = {}
        for k, v in kwargs.iteritems():
            ctx[k] = v
        if args:
            for idx, arg in enumerate(args):
                ctx['arg_%d' % idx] = arg
        return ctx

    def render_response(self, *args, **kwargs):
        """
        Renders context into template
        """
        if self.template_name is not None:
            template = get_template(loader, self.template_name)
            self.response.write(template.render(**self.get_context(*args, **kwargs)))
        else:
            raise ValueError('No template provided.')

    def get(self, *args, **kwargs):
        return self.render_response(*args, **kwargs)
