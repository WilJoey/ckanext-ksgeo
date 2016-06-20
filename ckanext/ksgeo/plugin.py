# encoding: utf-8

import ckan.plugins as plugins
import ckan.lib.plugins as lib_plugins
import ckan.lib.helpers as h
import ckan.plugins.toolkit as toolkit
import ckanext.ksgeo.logic.helpers as ksgeo_helpers

class KsgeoPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    #plugins.implements(plugins.IConfigurable)
    #plugins.implements(plugins.IConfigurer)
    #plugins.implements(plugins.IDatasetForm)
    #plugins.implements(plugins.IFacets, inherit=True)
    #plugins.implements(plugins.IRoutes, inherit=True)
    #plugins.implements(plugins.IAuthFunctions)
    #plugins.implements(plugins.IActions)
    #plugins.implements(plugins.IPackageController, inherit=True)
    #plugins.implements(plugins.ITemplateHelpers)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ksgeo')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'get_site_statistics_geo': ksgeo_helpers.get_site_statistics_geo
        }
