#   Copyright 2017 Red Hat, Inc. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import cgi

from flask import Blueprint
from flask import Response
from flask import url_for

debug = Blueprint('debug', __name__)


@debug.record
def record_app(state):
    global app
    app = state.app


@debug.route('/config')
def config_dump():
    return '\n'.join(['<table>'] +
                     ['<tr><td>%s</td><td>%s</td></tr>' % (k, v)
                      for k, v in sorted(app.config.items())] +
                     ['</table>'])


@debug.route('/app')
def app_dump():
    lines = ['<table>']

    for attr in sorted(dir(app)):
        attrval = getattr(app, attr)
        lines.append('<tr>')
        lines.append('<td><a href="{url}">{attr}</a></td>'.format(
            url=url_for('debug.app_dump_attr', attr=attr),
            attr=attr))
        lines.append('<td>{_type}</td>'.format(
            _type=cgi.escape(str(type(attrval)))))
        lines.append('<td>{callable}</td>'.format(
            callable=callable(attrval)))
        lines.append('</tr>')

    lines.append('</table>')
    return '\n'.join(lines)


@debug.route('/app/<attr>')
def app_dump_attr(attr):
    return Response(repr(getattr(app, attr, None)),
                    mimetype='text/plain')


@debug.route('/map')
def map_dump():
    lines = ['<table>']

    for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
        lines.append('<tr>')
        lines.append(''.join('<td>%s</td>' % cgi.escape(col) for col in [
            rule.rule,
            ' '.join(rule.methods),
            rule.endpoint]))
        lines.append('</tr>')
    lines.append('</table>')
    return '\n'.join(lines)
