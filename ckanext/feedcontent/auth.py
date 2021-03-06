from pylons.i18n import _
from ckan.authz import is_sysadmin
#from ckan.logic import check_access_old
#from ckan.logic.auth import get_group_object, get_package_object
#from ckan.logic.auth.publisher import _groups_intersect
from ckan.plugins import implements, SingletonPlugin, IAuthFunctions


def feed_create(context, data_dict):
    """
    Feed create permissions.  Only sysadmins are allowed to create new feeds
    """
    model = context['model']
    user = context.get('user','')

    if not is_sysadmin(unicode(user)):
        return {'success': False,
                'msg': _('You are not allowed to create a new feed')}

    return { 'success': True }


def feed_get(context, data_dict):
    """
    Feed get permissions.  Only sysadmins are allowed to view feeds
    """
    user = context.get('user','')
    if not is_sysadmin(unicode(user)):
        return {'success': False,
                'msg': _('You are not allowed to view this feed')}
    return { 'success': True }


def feed_list(context, data_dict):
    """
    Feed list permissions. Only sysadmins can list feed
    """
    model = context['model']
    user = context.get('user','')

    if not is_sysadmin(unicode(user)):
        return {'success': False,
                'msg': _('You are not allowed to list feeds')}

    return { 'success': True }


def feed_update(context, data_dict):
    """
    Feed update permissions.  Only sysadmins are allowed to update feeds
    """
    model = context['model']
    user = context.get('user','')

    if not is_sysadmin(unicode(user)):
        return {'success': False,
                'msg': _('You are not allowed to update a feed')}

    return { 'success': True }

def feed_delete(context, data_dict):
    """
    Feed delete permissions.  Only sysadmins are allowed to delete feeds
    """
    model = context['model']
    user = context.get('user','')

    if not is_sysadmin(unicode(user)):
        return {'success': False,
                'msg': _('You are not allowed to delete this feed')}

    return { 'success': True }
