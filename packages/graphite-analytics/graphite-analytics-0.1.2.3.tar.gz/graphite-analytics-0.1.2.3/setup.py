from distutils.core import setup
setup(
  name = 'graphite-analytics',
  packages = ['graphite'],
  version = '0.1.2.3',
  description = 'Create a print-out template for your google analytics data',
  author = 'Arian Moslem',
  author_email = 'amoslem678@gmail.com',
  url = 'https://github.com/ARM-open/Graphite',
  download_url = 'https://github.com/ARM-open/Graphite/archive/0.1.1.tar.gz',
  keywords = ['Google analytics', 'analytics', 'templates'], 
  classifiers = [],
  install_requires=['Click', 'google-api-python-client', 'jinja2'],
  entry_points={'console_scripts': [
    'graphite-analytics = graphite.graphite:main'
  ]},
  include_package_data=True
)