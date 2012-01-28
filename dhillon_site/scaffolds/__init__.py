from pyramid.scaffolds import PyramidTemplate

class DhillonTemplate(PyramidTemplate):
    egg_plugins = ['dhillon_site']
    summary = "Jesse Dhillon preferred Pyramid template"
    _template_dir = 'template'
    use_cheetah = True
