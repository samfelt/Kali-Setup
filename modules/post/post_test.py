#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_success("This is a post module template", 2)
