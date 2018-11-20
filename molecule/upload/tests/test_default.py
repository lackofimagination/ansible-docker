import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_user(host):
    u = host.user('docker')

    assert u.name == 'docker'
    assert 'docker' in u.groups


def test_containerd_systemd_file(host):
    f = host.file('/etc/systemd/system/containerd.service.d/override.conf')

    assert f.exists


def test_docker_systemd_options_file(host):
    f = host.file('/etc/systemd/system/docker.service.d/options.conf')

    assert f.exists


def test_docker_systemd_environment_file(host):
    f = host.file('/etc/systemd/system/docker.service.d/environment.conf')

    assert f.exists


def test_docker_daemon_file(host):
    f = host.file('/etc/docker/daemon.json')

    assert f.exists


def test_docker_service(host):
    s = host.service('docker')

    assert s.is_enabled
    assert s.is_running


def test_docker_compose_file(host):
    f = host.file('/usr/local/bin/docker-compose')

    assert f.exists
