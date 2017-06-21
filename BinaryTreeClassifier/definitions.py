__author__ = 'root'
import sys

CONST_LOG_LEVEL_ALL = 0
CONST_LOG_LEVEL_NO_DEBUG = 1
CONST_LOG_LEVEL_NO_INFO = 2
CONST_LOG_LEVEL_NONE = 3

log_level = CONST_LOG_LEVEL_ALL


def set_version_id():
    """
    Sets the version id according to python version on
    the system
    :param None:
    :return version_id:
    """

    if sys.version_info[:1] == (2, ):
        version_id = 2
        print "version_id", version_id
    else:
        version_id = 3
        print("version_id", version_id)
    return version_id