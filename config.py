#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3f3f1c1e-5729-4f36-8a13-dd1cb09ded68")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "D93DQBoQxRxWYa7rkxByOmYLoGwMza41WEl5VYFHwoIOUaUAd6VlJQQJ99BAAC3pKaRAArohAAABAZBS1Wxl")
