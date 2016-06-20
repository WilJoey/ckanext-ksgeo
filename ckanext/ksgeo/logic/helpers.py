import ckan.model as model
import ckan.lib.helpers as h
import ckan.logic as logic
from ckan.plugins import toolkit as tk

def get_site_statistics_geo():
    '''
    Custom stats helper, so we can get the correct number of packages, and a
    count of showcases.
    '''

    stats = {}

    stats['dataset_count'] = tk.get_action('package_search')(
        {}, {"rows": 1, 'fq': '!dataset_type:showcase'})['count']

    stats['showcase_count'] = tk.get_action('package_search')(
        {}, {"rows": 1, 'fq': 'dataset_type:showcase'})['count']

    stats['group_count'] = len(logic.get_action('group_list')({}, {}))

    stats['organization_count'] = len(
        logic.get_action('organization_list')({}, {}))
    
    stats['resource_count'] = get_resource_count()

    return stats

def get_resource_count():
    
    q = model.Session.query(model.Resource) \
        .join(model.Package) \
        .filter(model.Package.state == 'active') \
        .filter(model.Package.private == False) \
        .filter(model.Resource.state == 'active')

    return q.count()

