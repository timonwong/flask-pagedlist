# -*- coding: utf-8 -*-
import os

import jinja2
from flask import Blueprint
from flask import current_app
from flask import url_for

from pagedlist.web import builder as pl_builder
from pagedlist.web import options as pl_options


class Builder(object):
    @classmethod
    def paged_list_pager(cls, paged_list, page_url_generator, options=None):
        return jinja2.Markup(pl_builder.Builder.paged_list_pager(
            paged_list, page_url_generator, options))

    @classmethod
    def paged_list_goto_page_form(cls, paged_list, form_action, options=None):
        return jinja2.Markup(pl_builder.Builder.paged_list_goto_page_form(
            paged_list, form_action, options))

    @classmethod
    def page_url_generator(cls, endpoint):
        return lambda page: url_for(endpoint, page=page)


def pagedlist_static_for(filename, use_minified=None):
    """Resource finding function, also available in templates.

    :param filename: File to find a URL for.
    :param use_minified': If set to ``True``/``False``, use/don't use
                          minified. If ``None``, use the default setting
                          from ``PAGEDLIST_USE_MINIFIED``.
    :return: A URL.
    """
    config = current_app.config

    if use_minified is None:
        use_minified = config['PAGEDLIST_USE_MINIFIED']
    if use_minified:
        filename = '.min'.join(os.path.splitext(filename))
    return url_for('pagedlist.static', filename=filename)


class PagedList(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Set default configs
        app.config.setdefault('PAGEDLIST_USE_MINIFIED', True)
        app.config.setdefault('PAGEDLIST_PREFIX', 'pl_')

        # For static files
        blueprint = Blueprint(
            'pagedlist',
            __name__,
            static_folder='static',
            static_url_path=app.static_url_path + '/pagedlist')
        app.register_blueprint(blueprint)

        app.jinja_env.globals['pagedlist_static_for'] = pagedlist_static_for

        # Helpers for jinja2
        prefix = app.config['PAGEDLIST_PREFIX']
        app.jinja_env.globals['%sbuilder' % prefix] = Builder()
        app.jinja_env.globals['%soptions' % prefix] = pl_options
