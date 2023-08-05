# Copyright 2013 Rackspace Hosting
# All Rights Reserved.
#
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

from novaclient import base


class InstanceAction(base.Resource):
    pass


class InstanceActionManager(base.ManagerWithFind):
    resource_class = InstanceAction

    def get(self, server, request_id):
        """
        Get details of an action performed on an instance.

        :param request_id: The request_id of the action to get.
        """
        return self._get("/servers/%s/os-instance-actions/%s" %
                         (base.getid(server), request_id), 'instanceAction')

    def list(self, server):
        """
        Get a list of actions performed on a server.
        """
        return self._list('/servers/%s/os-instance-actions' %
                          base.getid(server), 'instanceActions')
