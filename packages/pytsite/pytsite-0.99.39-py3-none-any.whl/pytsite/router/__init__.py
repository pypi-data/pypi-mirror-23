"""PytSite Router
"""
from ._api import handle, add_path_alias, base_path, base_url, call, current_path, current_url, dispatch, rule_path, \
    rule_url, is_base_url, has_rule, get_no_cache, set_no_cache, remove_path_alias, scheme, server_name, url, \
    session, request, set_request, get_session_store, on_pre_dispatch, on_dispatch, on_response, on_exception, \
    on_xhr_dispatch, on_xhr_pre_dispatch, on_xhr_response

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from os import path, makedirs
    from pytsite import tpl, lang, reg

    # Resources
    tpl.register_package(__name__)
    lang.register_package(__name__)

    # Create directory to store session data
    session_storage_path = reg.get('paths.session')
    if not path.exists(session_storage_path):
        makedirs(session_storage_path, 0o755, True)

    # Lang globals
    lang.register_global('base_url', lambda language, args: base_url(language))

    # Tpl globals
    tpl.register_global('url', url)
    tpl.register_global('rule_url', rule_url)
    tpl.register_global('current_url', current_url)
    tpl.register_global('current_path', current_path)
    tpl.register_global('base_url', base_url)
    tpl.register_global('is_base_url', is_base_url)
    tpl.register_global('session_messages', lambda x: session().get_messages(x) if session() else ())

    # Clear flash messages from all session
    s_store = get_session_store()
    for sid in s_store.list():
        s_store.save_if_modified(s_store.get(sid).flash_clear())


_init()
