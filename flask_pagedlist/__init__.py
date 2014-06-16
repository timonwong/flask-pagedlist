# -*- coding: utf-8 -*-

import jinja2
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


class PagedList(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('PAGEDLIST_PREFIX', 'pl_')

        prefix = app.config['PAGEDLIST_PREFIX']
        app.jinja_env.globals['%sbuilder' % prefix] = Builder()
        app.jinja_env.globals['%soptions' % prefix] = pl_options
