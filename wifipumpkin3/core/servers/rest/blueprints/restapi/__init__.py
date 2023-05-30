from flask import Blueprint
from flask_restful import Resource, Api
import wifipumpkin3.core.servers.rest.blueprints.restapi.accesspoint as res_ap
import wifipumpkin3.core.servers.rest.blueprints.restapi.authenticate as res_auth
import wifipumpkin3.core.servers.rest.blueprints.restapi.logger as res_logger
import wifipumpkin3.core.servers.rest.blueprints.restapi.plugins as res_plugins
import wifipumpkin3.core.servers.rest.blueprints.restapi.proxies as res_proxies
import wifipumpkin3.core.servers.rest.blueprints.restapi.commands as res_command
import wifipumpkin3.core.servers.rest.blueprints.restapi.sbk as res_sbk
import wifipumpkin3.core.servers.rest.blueprints.gui.gui as gui


bp = Blueprint("wp3 Rest API", __name__, url_prefix="/api/v1")
api = Api(bp)

gui = gui.bp_gui

def init_app(app):


    api.add_resource(res_auth.LoginResource, "/authenticate/")
    api.add_resource(res_logger.getFileLogResource, "/logger/<string:filename>")
    api.add_resource(res_logger.getAllFileLogResource, "/loggers")

    api.add_resource(
        res_sbk.SbkPluginsResource,
        "/config/sbk",
    )

    api.add_resource(
        res_ap.SettingsAccesspointResource,
        "/config/accesspoint",
        "/config/accesspoint/<string:attribute>",
    )   

    api.add_resource(
        res_ap.SettingsDHCPResource, "/config/dhcp", "/config/dhcp/<string:attribute>"
    )

    api.add_resource(
        res_ap.SettingsAPmodeResource, "/apmode", "/apmode/<string:attribute>"
    )

    api.add_resource(
        res_plugins.SettingsPluginResource, "/plugins", "/plugins/<string:attribute>"
    )
    api.add_resource(res_plugins.MitmPluginsResource, "/plugins/info")

    api.add_resource(
        res_plugins.PluginsInfoResource,
        "/plugins",
        "/plugins/<string:plugin_name>/info",
    )

    api.add_resource(
        res_proxies.SettingsProxyResource, "/proxies", "/proxies/<string:attribute>"
    )

    api.add_resource(
        res_proxies.ProxiesInfoResource, "/proxies", "/proxies/<string:proxy_name>/info"
    )
    api.add_resource(res_proxies.ProxiesAllInfoResource, "/proxies", "/proxies/info")

    api.add_resource(res_plugins.SettingsPluginsResource, "/<string:plugin_id>/plugins")

    api.add_resource(res_command.CommandsResource, "/commands/<string:command>")
    api.add_resource(res_command.CommandsPostResource, "/commands")

    
    app.register_blueprint(bp)
    app.register_blueprint(gui)

    