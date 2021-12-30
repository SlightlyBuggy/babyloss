#!/bin/bash

pushd /opt/bitnami/projects/babyloss/babyloss

git pull https://github.com/SlightlyBuggy/babyloss.git dev
python manage.py collectstatic --noinput
/opt/bitnami/ctlscript.sh restart apache

popd