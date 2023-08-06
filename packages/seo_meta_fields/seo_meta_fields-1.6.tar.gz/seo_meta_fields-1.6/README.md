# meta_management


STEP 1:
###################################################################
Install the package:

$ pip install seo_meta_fields
###################################################################

STEP 2:
###################################################################
Add seo_meta_fields to your INSTALLED_APPS setting:

INSTALLED_APPS = [
    ...
    'seo_meta_fields',
]
###################################################################

STEP 3:
###################################################################
Run python manage.py makemigrations to create the seo_meta_fields fields in database.
###################################################################

STEP 4:
###################################################################
Run python manage.py migrate to create the seo_meta_fields models.
###################################################################

STEP 5:
###################################################################
Extend
!!!!
MetaImage

SiteInformation

OpenGraph

GoogleVerification

BingVerification

BasicTags

AdvancedTags
!!!

Modules in Model.py
to use the fields of that classes.

###################################################################

STEP 6:
###################################################################

import Class in admin.py

register module in admin.py

according to needs

admin.site.register('Class Name')

Available Classes for Meta Fields in Django APP in Django Meta Management
###################################################################

extending admin functionality in next version.
