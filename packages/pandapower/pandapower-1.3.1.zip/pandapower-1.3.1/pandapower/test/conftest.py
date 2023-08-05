# -*- coding: utf-8 -*-

# Copyright (c) 2016-2017 by University of Kassel and Fraunhofer Institute for Wind Energy and
# Energy System Technology (IWES), Kassel. All rights reserved. Use of this source code is governed
# by a BSD-style license that can be found in the LICENSE file.

import numpy as np
import pytest

import pandapower as pp
from pandapower.test.loadflow.result_test_network_generator import result_test_network_generator


@pytest.fixture(scope="session")
def simple_network():
    net = pp.create_empty_network()
    b1 = pp.create_bus(net, name="bus1", vn_kv=10.)
    pp.create_ext_grid(net, b1)
    b2 = pp.create_bus(net, name="bus2", geodata=(1, 2))
    b3 = pp.create_bus(net, name="bus3", geodata=(1, 3))
    b4 = pp.create_bus(net, name="bus4", vn_kv=10.)
    pp.create_transformer(net, b4, b2,
                          std_type="0.25 MVA 10/0.4 kV",
                          name=None, in_service=True, index=None)
    pp.create_line(net, b2, b3, 1, name="line1",
                   std_type="NAYY 4x150 SE",
                   geodata=np.array([[1, 2], [3, 4]]))
    pp.create_line(net, b1, b4, 1, name="line2",
                   std_type="NAYY 4x150 SE")
    pp.create_load(net, b2, p_kw=10, q_kvar=0, name="load1")
    pp.create_load(net, b3, p_kw=40, q_kvar=2, name="load2")
    pp.create_gen(net, 3, p_kw=-200., vm_pu=1.0)
    pp.create_sgen(net, 2, p_kw=-50, sn_kva=100)
    return net



@pytest.fixture(scope="session")
def result_test_network():
    for net in result_test_network_generator():
        pass
    pp.runpp(net, trafo_model="t", trafo_loading="current")
    return net

if __name__ == '__main__':
    net = result_test_network()
    # pp.rundcpp(net)