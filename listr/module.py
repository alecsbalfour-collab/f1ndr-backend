from core.controller_core import ControllerCore
from core.service_core import ServiceCore
from core.validation_core import ValidationCore

from config.post_config import post_config
from config.validate_config import validate_config

from db.post_repo_db import post_repo_db
from db.validate_repo_db import validate_repo_db

from utils.dict_utils import dict_utils
from utils.post_utils import post_utils
from utils.validation_utils import validation_utils


def build_listr_module():
    validator = ValidationCore(validate_config.rules())
    service = ServiceCore(post_repo_db)
    controller = ControllerCore(service, validator)

    return {
        "controller": controller,
        "service": service,
        "validator": validator,
        "post_config": post_config,
        "validate_config": validate_config,
        "post_repo": post_repo_db,
        "validate_repo": validate_repo_db,
        "dict_utils": dict_utils,
        "post_utils": post_utils,
        "validation_utils": validation_utils,
    }


listr = build_listr_module()
