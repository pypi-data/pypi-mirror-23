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

import pytest

from ara.tests.unit.common import ansible_run
from ara.tests.unit.common import TestAra


class TestApp(TestAra):
    """ Tests for the ARA web interface """
    def setUp(self):
        super(TestApp, self).setUp()

    def tearDown(self):
        super(TestApp, self).tearDown()

    def test_about_with_data(self):
        ansible_run()
        res = self.client.get('/about/')
        self.assertEqual(res.status_code, 200)

    def test_about_without_data(self):
        res = self.client.get('/about/')
        self.assertEqual(res.status_code, 200)

    def test_reports_without_data_at_root(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 302)

    def test_reports_without_data(self):
        res = self.client.get('/reports/')
        self.assertEqual(res.status_code, 302)

    def test_reports(self):
        ansible_run()
        res = self.client.get('/reports/')
        self.assertEqual(res.status_code, 200)

    def test_reports_with_incomplete(self):
        ansible_run(complete=False)
        res = self.client.get('/reports/')
        self.assertEqual(res.status_code, 200)

    def test_reports_with_override(self):
        ctx = ansible_run()
        self.app.config['ARA_PLAYBOOK_OVERRIDE'] = [ctx['playbook'].id]
        res = self.client.get('/reports/')
        self.assertEqual(res.status_code, 200)

    def test_reports_with_bad_override(self):
        ansible_run()
        self.app.config['ARA_PLAYBOOK_OVERRIDE'] = ['uuuu-iiii-dddd-0000']
        res = self.client.get('/reports/')
        self.assertEqual(res.status_code, 302)

    def test_reports_with_pagination(self):
        ansible_run()
        ansible_run()
        self.app.config['ARA_PLAYBOOK_PER_PAGE'] = 1
        res = self.client.get('/reports/')
        self.assertEqual(res.status_code, 200)

        res = self.client.get('/reports/list/1.html')
        self.assertEqual(res.status_code, 200)

        res = self.client.get('/reports/list/2.html')
        self.assertEqual(res.status_code, 200)

    def test_reports_single(self):
        ctx = ansible_run()
        res = self.client.get('/reports/{0}.html'.format(ctx['playbook'].id))
        self.assertEqual(res.status_code, 200)

    def test_reports_single_bad_playbook(self):
        ansible_run()
        uuid = 'uuuu-iiii-dddd-0000'
        res = self.client.get('/reports/{0}.html'.format(uuid))
        self.assertEqual(res.status_code, 404)

    def test_report_ajax_parameters(self):
        ctx = ansible_run()
        pbid = ctx['playbook'].id
        res = self.client.get('/reports/ajax/parameters/{0}.txt'.format(pbid))
        self.assertEqual(res.status_code, 200)

    def test_report_ajax_no_parameters(self):
        ansible_run()
        res = self.client.get('/reports/ajax/parameters/uuid.txt')
        self.assertEqual(res.status_code, 404)

    def test_report_ajax_plays(self):
        ctx = ansible_run()
        pbid = ctx['playbook'].id
        res = self.client.get('/reports/ajax/plays/{0}.txt'.format(pbid))
        self.assertEqual(res.status_code, 200)

    def test_report_ajax_no_plays(self):
        ansible_run()
        res = self.client.get('/reports/ajax/plays/uuid.txt')
        self.assertEqual(res.status_code, 404)

    def test_report_ajax_records(self):
        ctx = ansible_run(ara_record=True)
        pbid = ctx['playbook'].id
        res = self.client.get('/reports/ajax/records/{0}.txt'.format(pbid))
        self.assertEqual(res.status_code, 200)

    def test_report_ajax_no_records(self):
        ansible_run()
        res = self.client.get('/reports/ajax/records/uuid.txt')
        self.assertEqual(res.status_code, 404)

    def test_report_ajax_results(self):
        ctx = ansible_run()
        pbid = ctx['playbook'].id
        res = self.client.get('/reports/ajax/results/{0}.txt'.format(pbid))
        self.assertEqual(res.status_code, 200)

    def test_report_ajax_no_results(self):
        ansible_run()
        res = self.client.get('/reports/ajax/results/uuid.txt')
        self.assertEqual(res.status_code, 404)

    def test_report_ajax_stats(self):
        ctx = ansible_run()
        pbid = ctx['playbook'].id
        res = self.client.get('/reports/ajax/stats/{0}.txt'.format(pbid))
        self.assertEqual(res.status_code, 200)

    def test_report_ajax_no_stats(self):
        ansible_run()
        res = self.client.get('/reports/ajax/stats/uuid.txt')
        self.assertEqual(res.status_code, 404)

    def test_show_file(self):
        ctx = ansible_run()
        res = self.client.get('/file/{0}/'.format(ctx['pb_file'].id))
        self.assertEqual(res.status_code, 200)

    def test_show_file_index(self):
        ansible_run()
        res = self.client.get('/file/')
        self.assertEqual(res.status_code, 200)

    def test_show_host(self):
        ctx = ansible_run()
        res = self.client.get('/host/{}/'.format(ctx['host'].id))
        self.assertEqual(res.status_code, 200)

    def test_show_host_index(self):
        ansible_run()
        res = self.client.get('/host/')
        self.assertEqual(res.status_code, 200)

    def test_show_host_missing(self):
        ansible_run()
        res = self.client.get('/host/foo/')
        self.assertEqual(res.status_code, 404)

    def test_show_host_exists_facts_missing(self):
        ctx = ansible_run(gather_facts=False)
        res = self.client.get('/host/{}/'.format(ctx['host'].id))
        self.assertEqual(res.status_code, 404)

    def test_show_host_missing_facts_missing(self):
        ansible_run()
        res = self.client.get('/host/foo/')
        self.assertEqual(res.status_code, 404)

    def test_show_result(self):
        ctx = ansible_run()
        res = self.client.get('/result/{}/'.format(ctx['result'].id))
        self.assertEqual(res.status_code, 200)

    def test_show_result_index(self):
        ansible_run()
        res = self.client.get('/result/')
        self.assertEqual(res.status_code, 200)

    def test_show_result_missing(self):
        ansible_run()
        res = self.client.get('/result/foo/')
        self.assertEqual(res.status_code, 404)

    @pytest.mark.incomplete
    def test_show_result_incomplete(self):
        ctx = ansible_run(complete=False)
        res = self.client.get('/result/{}/'.format(ctx['result'].id))
        self.assertEqual(res.status_code, 200)
