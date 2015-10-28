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

import datetime

from invenio.ext.template import render_template_to_string
from invenio.modules.circulation.models import CirculationItem


def has_items(record_id):
    return CirculationItem.search('record_id:{0}'.format(record_id))


def encode_circulation_state(users, items, records, start_date, end_date):
    # :1::2015-09-22:2015-10-20:
    return '{items}:{users}:{records}:{start}:{end}:'.format(
            items=','.join(str(x) for x in items),
            users=','.join(str(x) for x in users),
            records=','.join(str(x) for x in records),
            start=start_date, end=end_date)


def circulation_information(record, current_user):
    record_id = record['recid']
    user_id = current_user.get_id()
    if has_items(record_id):
        start = datetime.date.today()
        end = start + datetime.timedelta(weeks=4)
        link = encode_circulation_state([user_id], [], [record_id], start, end)
        return render_template_to_string('search/search_res_addition.html',
                                         state=link, record_id=record_id)
    return ''


def setup_app(app):
    app.jinja_env.filters['circulation_information'] = circulation_information

