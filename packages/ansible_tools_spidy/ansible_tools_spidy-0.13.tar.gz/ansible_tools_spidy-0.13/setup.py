from distutils.core import setup
setup(
  name = 'ansible_tools_spidy',
  packages = ['FILE_spidy','Utilities_spidy','constrains_spidy'], # this must be the same as the name above
  version = '0.13',
  description = 'ansible_tools_spidy allows you to store and retreive playbooks in mongodb using passwordless auth, Security Wrappers in the next Release command :- /usr/local/bin/ansible_playbook & yaml_to_mongo',
  author = 'Anish V Tharagar',
  author_email = 'anish.tharagar@gmail.com',
  url = 'https://github.com/anishtharagar/code_repo_public.git', # use the URL to the github repo
  download_url = 'https://github.com/anishtharagar/code_repo_public/packaging/', # I'll explain this in a second
  keywords = ['ansible', 'playbooks', 'automation'], # arbitrary keywords
  install_requires = [ 'pyaml','pymongo','libmagic', 'termcolor' ],
  classifiers = [],
  data_files=[('/usr/local/bin',['Tools_spidy/ansible_playbook','Tools_spidy/yaml_to_mongo']),
	      ('/usr/share',['files_repo/mongo_connect.json'])],
  license = 'MIT',
)
