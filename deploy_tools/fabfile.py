import os

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run, put
import random

REPO_URL = 'https://github.com/djunh1/hhockey.git'
LOCAL_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env.host = ['ec2-35-166-188-189.us-west-2.compute.amazonaws.com']
env.user = 'ec2-user'
env.key_filename = '/Users/djunh/.ssh/hopewell-hockey-kp.pem'

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _copy_secrets_file(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(site_folder, source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('static', 'virtualenv', 'source', 'media'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/hhockey/settings/base.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/hhockey/settings/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(site_folder, source_folder):
    virtualenv_folder = site_folder + '/virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('python3 -m venv --without-pip %s' % (virtualenv_folder,))
        run('cd %s && curl https://bootstrap.pypa.io/get-pip.py | python' %(virtualenv_folder +'/bin'))
    run('%s/bin/pip install -r %s/requirements.txt' % (
            virtualenv_folder, source_folder
    ))


def _copy_secrets_file(source_folder):
    output = run('cd %s && test -f secrets.json && echo "TRUE"  || echo "FALSE"' % (source_folder))
    status_stdout = output.stdout.split("\r\n")
    if 'FALSE' in status_stdout:
        print("CREATING Secrets File")
        put(LOCAL_DIR+'/secrets.json', source_folder)
    elif 'TRUE' in status_stdout:
        print('UPDATING Secrets file.  Check everything is correct')
        put(LOCAL_DIR+'/secrets.json', source_folder)


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python manage.py collectstatic --noinput' % (
        source_folder,
    ))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python manage.py migrate --noinput' % (
        source_folder,
    ))