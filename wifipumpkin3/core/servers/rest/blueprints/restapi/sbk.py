from wifipumpkin3.core.utility.collection import SettingsINI
import wifipumpkin3.core.utility.constants as C
from wifipumpkin3 import PumpkinShell
from flask_restful import Resource
from flask import jsonify, request
from wifipumpkin3.core.servers.rest.ext.auth import token_required
from wifipumpkin3.core.servers.rest.ext.exceptions import exception

# This file is part of the wifipumpkin3 Open Source Project.
# wifipumpkin3 is licensed under the Apache 2.0.

# Copyright 2020 P0cL4bs Team - Marcos Bomfim (mh4x0f)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class SbkPluginsResource(Resource):
    config = SettingsINI.getInstance()
    key_name = "sbk_plugin"

    @token_required
    def get(self):
        self.root = PumpkinShell.getInstance()
        proxy_plugins = self.root.proxy_controller.getInfo(excluded=("Config"))
        list_plugins = ['Fahad','Coder']
        return jsonify({"sbk": list_plugins})