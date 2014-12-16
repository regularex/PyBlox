from paste.script import templates
from paste.deploy.converters import asbool
from paste.script.appinstall import Installer
from paste.script.templates import Template, var


vars = [
    templates.var('version', '0.1'),
    templates.var('description', ''),
    templates.var('long_description', ''),
    templates.var('keywords', 'pyblox'),
    templates.var('author', ''),
    templates.var('author_email', ''),
    templates.var('url', ''),
    templates.var('license_name', ''),
    templates.var('zip_safe', 'True/False: if the package can be distributed as a .zip file',
        default=True),
    ]

class PyBloxTemplate(templates.Template):
    egg_plugins = ['PasteScript', 'PyBlox']
    summary = 'Template system for creating PyBlox web framework applications.'
    required_templates = ['basic_package']
    _template_dir =  'templates'
    use_cheetah = False
    vars=vars
