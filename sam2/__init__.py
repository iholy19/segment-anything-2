# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from hydra import initialize_config_module
from hydra.core.global_hydra import GlobalHydra
import os

print("FROM app:", os.getcwd())

if GlobalHydra.instance().is_initialized()==False:
  GlobalHydra.instance().clear()
  initialize_config_module("../sam2_configs", version_base="1.2")
