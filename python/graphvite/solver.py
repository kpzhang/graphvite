# Copyright 2019 MilaGraph. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Zhaocheng Zhu

"""Solver module of GraphVite"""
from __future__ import absolute_import

import sys

from . import lib, cfg
from .helper import find_all_templates, make_helper_class

module = sys.modules[__name__]

for name in find_all_templates(lib.solver):
    module.__dict__[name] = make_helper_class(lib.solver, name, module,
                                              ["dim", "float_type", "index_type"],
                                              [None, cfg.float_type, cfg.index_type])

__all__ = [
    "GraphSolver", "KnowledgeGraphSolver", "VisualizationSolver"
]