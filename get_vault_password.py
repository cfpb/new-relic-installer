#!/usr/bin/env python
# this file must be executable (chmod +x get_vault_password.py)
# the password should be in jenkins -> configure system -> global passwords
import os
print os.environ['NEW_RELIC_VAULT_PASSWORD']
