# SPDX-FileCopyrightText: 2022 Krzysztof Królczyk
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import pytest
import script_3


# parallel nested module tests should be runnable from any dir in package
MODULE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
TEST_PATH = os.path.join(MODULE_DIR, "tests", "tests_data")


