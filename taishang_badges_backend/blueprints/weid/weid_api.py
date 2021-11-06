# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    abort,
    jsonify,
    g
)

from taishang_badges_backend.extensions import db, csrf_protect
from taishang_badges_backend.settings import WEIDSERVICE_URL
from pyweidentity.weidentityService import weidentityService

weid_bp = Blueprint("weid", __name__)

class ValidationError(Exception):
    pass

@csrf_protect.exempt
@weid_bp.route("/createWeid", methods=["GET"])
def create_weid():
    weid = weidentityService(WEIDSERVICE_URL)
    weid_result = weid.create_weidentity_did()
    item = weid_result["respBody"].split(":")
    item[2] = "3"
    weid_return = ":".join(item)
    return jsonify({"weid": weid_return})
