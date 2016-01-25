# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014, 2015 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from invenio.ext.template import render_template_to_string


def circulation_information(record, current_user):
    from invenio.modules.circulation.views.utils import send_signal
    from invenio.modules.circulation.signals import record_actions

    record_id = record['recid']
    user_id = current_user.get_id()
    data = {'record_id': record_id, 'user_id': user_id}

    ra = " | ".join(send_signal(record_actions, None, data))

    return render_template_to_string('search/record_actions.html',
                                     record_actions=ra)


def setup_app(app):
    app.jinja_env.filters['circulation_information'] = circulation_information
