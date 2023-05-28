from wifipumpkin3.core.utility.collection import SettingsINI
import wifipumpkin3.core.utility.constants as C
from wifipumpkin3 import PumpkinShell
from flask_restful import Resource
from flask import jsonify, request
from wifipumpkin3.core.servers.rest.ext.auth import token_required
from wifipumpkin3.core.servers.rest.ext.exceptions import exception
from wifipumpkin3.extensions.dump import Dump


class SbkPluginsResource(Resource):
    config = SettingsINI.getInstance()
    key_name = "sbk_plugin"

    #@token_required
    def get(self):
        self.root = PumpkinShell.getInstance()
        ducp = self.root.getDefault.getController("dhcp_controller").Active
        data_dict: dict = ducp.getStaClients
        if not data_dict:
            return jsonify({"error": "No clients connected on AP!"})
        clients  = []
        for data in data_dict:
            clients.append(data_dict[data])
            print(data_dict[data])
        return jsonify({"clients": clients})
    