#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six

from novaclient.tests.functional import base


class TestHypervisors(base.ClientTestBase):

    COMPUTE_API_VERSION = "2.1"

    def _test_list(self, cpu_info_type):
        hypervisors = self.client.hypervisors.list()
        if not len(hypervisors):
            self.fail("No hypervisors detected.")
        for hypervisor in hypervisors:
            self.assertIsInstance(hypervisor.cpu_info, cpu_info_type)

    def test_list(self):
        self._test_list(six.text_type)
