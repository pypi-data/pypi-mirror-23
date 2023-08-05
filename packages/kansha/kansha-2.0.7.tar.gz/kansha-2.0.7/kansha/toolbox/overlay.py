# -*- coding:utf-8 -*-
#--
# Copyright (c) 2012-2014 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
#--

from nagare import presentation, ajax
from nagare.i18n import _


class Overlay(object):

    """Overlay component
    """

    def __init__(self, text_factory, content_factory, title=None, dynamic=True, cls=None, centered=False):
        """Initialization

        In:
            - ``text_factory`` -- a callable generating the overlay title
            - ``content_factory`` -- a callable generating the overlay content
            - ``title`` -- if given, the text will be used in the overlay title when showed
            - ``dynamic`` -- if True, the content of the overlay will be filled using AJAX.
            - ``cls`` -- an additional class name
        """
        self.text = text_factory
        self.content = content_factory
        self.title = title
        self.dynamic = dynamic
        self.cls = cls
        self.centered = centered

    def render_a(self, h, link_id):
        h << h.a(self.text(h), href='#', id_=link_id, title=self.title or '')


@presentation.render_for(Overlay)
def render(self, h, comp, *args):
    """Render the overlay"""
    link_id = h.generate_id()
    overlay_id = h.generate_id()
    body_id = h.generate_id('BODY_')

    self.render_a(h, link_id)

    # TODO: find a cleaner solution
    if self.dynamic:
        # Load overlay body dynamically
        load = ajax.js(
            "YAHOO.util.Dom.get(%(body_id)s).innerHTML = '';"
            "%(load_body)s" %
            {
                'body_id': ajax.py2js(body_id),
                'load_body': h.a.action(
                    ajax.Update(render=self.content, component_to_update=body_id)
                ).get('onclick').replace('return', '')
            }
        )
    else:
        # The overlay body is already present in the DOM tree
        load = ajax.js('')

    js = ajax.js(
        "%(load)s;"
        "YAHOO.kansha.app.showOverlay(%(overlay_id)s, %(link_id)s, %(centered)s)" %
        {
            'load': ajax.py2js(load),
            'link_id': ajax.py2js(link_id),
            'overlay_id': ajax.py2js(overlay_id),
            'centered': ajax.py2js(self.centered, h)
        }
    )

    h.head.javascript(
        h.generate_id(),
        "YAHOO.util.Event.addListener(%(link_id)s, 'click', "
        "function(){%(js)s;}"
        ")" % {'link_id': ajax.py2js(link_id), "js": ajax.py2js(js)}
    )

    cls = [u'overlay']
    if self.cls:
        cls.append(self.cls)
    with h.div(class_=u' '.join(cls), id=overlay_id, onclick="YAHOO.kansha.app.stopEvent()"):
        if not self.centered:
            h << h.span(class_='overlay_arrow')
        with h.div(class_='overlay-header'):
            with h.div(class_='overlay-title'):
                h << h.div(self.title or self.text(h))
        h << h.div(' ' if self.dynamic else self.content(h), class_='overlay-body', id=body_id)

    return h.root
