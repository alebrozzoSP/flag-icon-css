# -*- coding: utf-8 -*-

import os
import operator

try:
  # This part is surrounded in try/except because the config.py file is
  # also used in the run.py script which is used to compile/minify the client
  # side files (*.less, *.coffee, *.js) and is not aware of the GAE
  from datetime import datetime
  import model
  CONFIG_DB = model.Config.get_master_db()
  SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
  LOCALE_DEFAULT = CONFIG_DB.locale
  CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
  CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
  CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
  CURRENT_VERSION_DATE = datetime.fromtimestamp(CURRENT_VERSION_TIMESTAMP)
except:
  pass

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEVELOPMENT = not PRODUCTION
DEBUG = DEVELOPMENT

DEFAULT_DB_LIMIT = 64

###############################################################################
# i18n Stuff
###############################################################################

# Languages: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# Countries: http://en.wikipedia.org/wiki/ISO_3166-1
# To Add/Modify languages use one of the filenames in: libx/babel/localedata/
# Examples with country included: en_GB, ru_RU, de_CH
LOCALE = {
  'en': u'English',
  'el': u'Ελληνικά',
  'pl': u'Polski',
  'ru': u'Русский',
}

LOCALE_SORTED = sorted(LOCALE.iteritems(), key=operator.itemgetter(1))
LANGUAGES = [l.lower().replace('_', '-') for l in LOCALE.keys()]

###############################################################################
# Client modules, also used by the run.py script.
###############################################################################
STYLES = [
    'src/style/style.less',
  ]

SCRIPTS_MODULES = [
    'libs',
    'scripts',
  ]

SCRIPTS = {
    'libs': [
        'src/lib/jquery.js',
        'src/lib/moment.js',
        'src/lib/nprogress/nprogress.js',
        'src/lib/bootstrap/js/alert.js',
        'src/lib/bootstrap/js/button.js',
        'src/lib/bootstrap/js/collapse.js',
        'src/lib/bootstrap/js/dropdown.js',
        'src/lib/bootstrap/js/tooltip.js',
      ] + ['src/lib/lang/%s.js' % l for l in LANGUAGES if l != 'en'],
    'scripts': [
        'src/script/common/service.coffee',
        'src/script/common/util.coffee',
        'src/script/site/app.coffee',
        'src/script/site/admin.coffee',
        'src/script/site/profile.coffee',
        'src/script/site/user.coffee',
      ],
  }
