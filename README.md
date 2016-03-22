# New Relic APM Agent Installer
**Description:**
    
Ansible scripts for installing php or python [New Relic](http://www.newrelic.com) agents, as well as very simple LAMP php or wsgi python applications on CentOS 6.5. The agents report application statistics to New Relic and the web apps are present so to test that the Agent installation will work as expected.

  - **Technology stack**: CentOS 6.5, Apache, Mod_wsgi, MySQL, Python2.7, PHP, Ansible, Vagrant.
  - **Status**:  Alpha

## Installation
The project is configured to require an encrypted license.yml file -- containing the New Relic license key -- that gets opened with a password. To create the encrypted license.yml file follow [these instructions](http://docs.ansible.com/ansible/playbooks_vault.html#creating-encrypted-files), entering the password above when prompted, and creating a file containing the following.

```
---
newrelic_license_key: <insertyournewreliclicensekey>
```

Follow directions [here](https://docs.newrelic.com/docs/accounts-partnerships/accounts/account-setup/license-key) to find the license key.

**Local Installation:** For local testing, after `vagrant up` the resulting virtual box serves a local python application at http://127.0.0.1:8080/myapp and a PHP application at http://127.0.0.1:8080/info.php. Create and store the vault password locally in `password.txt`. 
    
**Remote Installation:**
Create an `inventory_file`:
```
[nr-python]
<INSERT-UNIQUE-ALIAS> ansible_ssh_host=<INSERT-HOST> ansible_ssh_user=<INSERT-USER> wsgi_scriptfile=<INSERT-PATH> application_name="<INSERT-NAME>"

[nr-php]
<INSERT-UNIQUE-ALIAS> ansible_ssh_host=<INSERT-HOST> ansible_ssh_user=<INSERT-USER> application_name="<INSERT-NAME>"
```

If using Jenkins, you can securely store the ansible vault password in an environment variable and then run. 
```
ansible-playbook provisioners/provision.yml -i inventory_file --vault-password-file=get_vault_password.py -e @license.yml
```

where `get_vault_password.py` provides the environment variable storing your ansible vault password:
```
import os
print os.environ['NEW_RELIC_VAULT_PASSWORD']
```
    

## Known issues

**To use New Relic with an app installed in a virtualenv, you will need to `pip install newrelic` before using this installer**


## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

