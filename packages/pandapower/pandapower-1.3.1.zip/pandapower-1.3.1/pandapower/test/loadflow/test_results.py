# -*- coding: utf-8 -*-

# Copyright (c) 2016-2017 by University of Kassel and Fraunhofer Institute for Wind Energy and
# Energy System Technology (IWES), Kassel. All rights reserved. Use of this source code is governed
# by a BSD-style license that can be found in the LICENSE file.

import pytest
from numpy import in1d

import pandapower as pp
from pandapower.test.consistency_checks import runpp_with_consistency_checks
from pandapower.test.loadflow.result_test_network_generator import add_test_enforce_qlims, \
    add_test_gen


def test_line(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_line"]
    lines = [x for x in net.line.index if net.line.from_bus[x] in buses.index]
    l1 = lines[0]
    l2 = lines[1]
    l3 = lines[2]
    b2 = buses.index[1]

    # result values from powerfactory
    load1 = 14.578
    load2 = 8.385

    ika1 = 0.0466479
    ika2 = 0.0134154

    p_from1 = 1202.21
    p_from2 = 0.132

    q_from1 = 167.390
    q_from2 = -469.371

    p_to1 = -1200.000
    p_to2 = 0.000

    q_to1 = -1100.000
    q_to2 = 0.0000

    v = 1.007395422

    # line 1
    assert abs(net.res_line.loading_percent.at[l1] - load1) < l_tol
    assert abs(net.res_line.i_ka.at[l1] - ika1) < i_tol
    assert abs(net.res_line.p_from_kw.at[l1] - p_from1) < s_tol
    assert abs(net.res_line.q_from_kvar.at[l1] - q_from1) < s_tol
    assert abs(net.res_line.p_to_kw.at[l1] - p_to1) < s_tol
    assert abs(net.res_line.q_to_kvar.at[l1] - q_to1) < s_tol

    # line2 (open switch line)
    assert abs(net.res_line.loading_percent.at[l2] - load2) < l_tol
    assert abs(net.res_line.i_ka.at[l2] - ika2) < i_tol
    assert abs(net.res_line.p_from_kw.at[l2] - p_from2) < s_tol
    assert abs(net.res_line.q_from_kvar.at[l2] - q_from2) < s_tol
    assert abs(net.res_line.p_to_kw.at[l2] - p_to2) < s_tol
    assert abs(net.res_line.q_to_kvar.at[l2] - q_to2) < s_tol

    assert abs(net.res_bus.vm_pu.at[b2] - v) < v_tol

    # line3 (of out of service line)
    assert abs(net.res_line.loading_percent.at[l3] - 0) < l_tol
    assert abs(net.res_line.i_ka.at[l3] - 0) < i_tol
    assert abs(net.res_line.p_from_kw.at[l3] - 0) < s_tol
    assert abs(net.res_line.q_from_kvar.at[l3] - 0) < s_tol
    assert abs(net.res_line.p_to_kw.at[l3] - 0) < s_tol
    assert abs(net.res_line.q_to_kvar.at[l3] - 0) < s_tol


def test_load_sgen(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_load_sgen"]
    loads = [x for x in net.load.index if net.load.bus[x] in buses.index]
    sgens = [x for x in net.sgen.index if net.sgen.bus[x] in buses.index]
    l1 = loads[0]
    sg1 = sgens[0]
    b2 = buses.index[1]
    # result values from powerfactory
    pl1 = 1200.000
    ql1 = 1100.000

    qs1 = -100.000
    ps1 = 500.000

    u = 1.00477465

    assert abs(net.res_load.p_kw.at[l1] - pl1) < s_tol
    assert abs(net.res_load.q_kvar.at[l1] - ql1) < s_tol
    # pf uses generator system
    assert abs(net.res_sgen.p_kw.at[sg1] - (- ps1)) < s_tol
    # pf uses generator system
    assert abs(net.res_sgen.q_kvar.at[sg1] - (-qs1)) < s_tol
    assert abs(net.res_bus.vm_pu.at[b2] - u) < v_tol


def test_load_sgen_split(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    # splitting up the load/sgen should not change the result
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_load_sgen_split"]
    b2 = buses.index[1]

    u = 1.00477465

    assert abs(net.res_bus.vm_pu.at[b2] - u) < v_tol


def test_trafo(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=1e-2, l_tol=1e-3, va_tol=1e-2):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_trafo"]
    trafos = [x for x in net.trafo.index if net.trafo.hv_bus[x] in buses.index]
    t1 = trafos[0]
    t2 = trafos[1]
    t3 = trafos[2]
    b2 = buses.index[1]
    b3 = buses.index[2]
    # powerfactory results to check t-equivalent circuit model
    runpp_with_consistency_checks(net, trafo_model="t", trafo_loading="current", init="dc",
                                  calculate_voltage_angles=True)

    load1 = 28.7842
    load2 = 0.4830

    ph1 = 204.756
    ph2 = 1.7741

    qh1 = 52.848
    qh2 = 0.0038

    pl1 = -200.0000
    pl2 = 0

    ql1 = -50.0000
    ql2 = 0.0

    ih1 = 0.006043
    ih2 = 0.000051

    il1 = 0.303631
    il2 = 0

    v2 = 1.010159155
    v3 = 0.980003098

    va2 = -0.06736233
    va3 = -150.73914408

    assert abs(net.res_trafo.loading_percent.at[t1] - load1) < l_tol
    assert abs(net.res_trafo.p_hv_kw.at[t1] - ph1) < s_tol
    assert abs(net.res_trafo.q_hv_kvar.at[t1] - qh1) < s_tol
    assert abs(net.res_trafo.p_lv_kw.at[t1] - pl1) < s_tol
    assert abs(net.res_trafo.q_lv_kvar.at[t1] - ql1) < s_tol
    assert abs(net.res_trafo.i_hv_ka.at[t1] - ih1) < i_tol
    assert abs(net.res_trafo.i_lv_ka.at[t1] - il1) < i_tol

    assert abs(net.res_trafo.loading_percent.at[t2] - load2) < l_tol
    assert abs(net.res_trafo.p_hv_kw.at[t2] - ph2) < s_tol
    assert abs(net.res_trafo.q_hv_kvar.at[t2] - qh2) < s_tol
    assert abs(net.res_trafo.p_lv_kw.at[t2] - pl2) < s_tol
    assert abs(net.res_trafo.q_lv_kvar.at[t2] - ql2) < s_tol
    assert abs(net.res_trafo.i_hv_ka.at[t2] - ih2) < i_tol
    assert abs(net.res_trafo.i_lv_ka.at[t2] - il2) < i_tol

    assert abs(net.res_trafo.loading_percent.at[t3] - 0) < l_tol
    assert abs(net.res_trafo.p_hv_kw.at[t3] - 0) < s_tol
    assert abs(net.res_trafo.q_hv_kvar.at[t3] - 0) < s_tol
    assert abs(net.res_trafo.p_lv_kw.at[t3] - 0) < s_tol
    assert abs(net.res_trafo.q_lv_kvar.at[t3] - 0) < s_tol
    assert abs(net.res_trafo.i_hv_ka.at[t3] - 0) < i_tol
    assert abs(net.res_trafo.i_lv_ka.at[t3] - 0) < i_tol

    assert abs(net.res_bus.vm_pu.at[b2] - v2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - v3) < v_tol

    assert abs(net.res_bus.va_degree.at[b2] - va2) < va_tol
    assert abs(net.res_bus.va_degree.at[b3] - va3) < va_tol

    # sincal results to check pi-equivalent circuit model
    net.trafo.parallel.loc[trafos] = 1  # sincal is tested without parallel transformers
    runpp_with_consistency_checks(net, trafo_model="pi", trafo_loading="current")

    load1 = 57.637
    load2 = 0.483
    v2 = 1.01014991616
    v3 = 0.97077261471

    assert abs(net.res_trafo.loading_percent.at[t1] - load1) < l_tol
    assert abs(net.res_trafo.loading_percent.at[t2] - load2) < l_tol

    assert abs(net.res_bus.vm_pu.at[b2] - v2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - v3) < v_tol

    runpp_with_consistency_checks(net, trafo_model="pi", trafo_loading="power")

    load1 = 52.929
    load2 = 0.444

    assert abs(net.res_trafo.loading_percent.at[t1] - load1) < l_tol
    assert abs(net.res_trafo.loading_percent.at[t2] - load2) < l_tol


def test_ext_grid(result_test_network, v_tol=1e-6, va_tol=1e-2, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    runpp_with_consistency_checks(net, calculate_voltage_angles=True)
    buses = net.bus[net.bus.zone == "test_ext_grid"]
    b2 = buses.index[1]
    ext_grids = [
        x for x in net.ext_grid.index if net.ext_grid.bus[x] in buses.index]
    eg1 = ext_grids[0]
    eg2 = ext_grids[1]
    # results from powerfactory
    p1 = --5653.1650
    q1 = -2107.4499

    v2 = 1.015506741
    va2 = 1.47521433

    p2 = 5837.7758
    q2 = -2778.6795

    assert abs(net.res_ext_grid.p_kw.at[eg1] - (-p1))
    assert abs(net.res_ext_grid.q_kvar.at[eg1] - (-q1))

    assert abs(net.res_ext_grid.p_kw.at[eg2] - (-p2))
    assert abs(net.res_ext_grid.q_kvar.at[eg2] - (-q2))

    assert abs(net.res_bus.vm_pu.at[b2] - v2) < v_tol
    assert abs(net.res_bus.va_degree.at[b2] - va2) < va_tol


def test_ward(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_ward"]
    wards = [x for x in net.ward.index if net.ward.bus[x] in buses.index]
    b2 = buses.index[1]
    w1 = wards[0]
    # powerfactory results
    pw = -1704.6146
    qw = -1304.2294
    u = 1.00192121

    assert abs(net.res_bus.vm_pu.loc[b2] - u) < v_tol
    assert abs(net.res_ward.p_kw.loc[w1] - (-pw)) < s_tol
    assert abs(net.res_ward.q_kvar.loc[w1] - (-qw)) < s_tol


def test_ward_split(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_ward_split"]
    wards = [x for x in net.ward.index if net.ward.bus[x] in buses.index]
    b2 = buses.index[1]
    w1 = wards[0]
    w2 = wards[1]
    # powerfactory results
    pw = -1704.6146
    qw = -1304.2294
    u = 1.00192121

    assert abs(net.res_bus.vm_pu.at[b2] - u)
    assert abs(net.res_ward.p_kw.loc[[w1, w2]].sum() - (-pw))
    assert abs(net.res_ward.q_kvar.loc[[w1, w2]].sum() - (-qw))
    #


def test_xward(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_xward"]
    xwards = [x for x in net.xward.index if net.xward.bus[x] in buses.index]
    b2 = buses.index[1]
    xw1 = xwards[0]
    xw2 = xwards[1]  # Out of servic xward
    #    powerfactory result for 1 xward
    u = 1.00308684
    pxw = -1721.0380
    qxw = -975.9919
    #
    assert abs(net.res_bus.vm_pu.at[b2] - u) < v_tol
    assert abs(net.res_xward.p_kw.at[xw1] - (-pxw)) < s_tol
    assert abs(net.res_xward.q_kvar.at[xw1] - (-qxw)) < s_tol

    assert abs(net.res_bus.vm_pu.at[b2] - u) < 1e-2
    assert abs(net.res_xward.p_kw.loc[[xw1, xw2]].sum() - (-pxw)) < s_tol
    assert abs(net.res_xward.q_kvar.loc[[xw1, xw2]].sum() - (-qxw)) < s_tol


def test_xward_combination(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_xward_combination"]
    xwards = [x for x in net.xward.index if net.xward.bus[x] in buses.index]
    b2 = buses.index[1]
    xw1 = xwards[0]
    xw3 = xwards[2]

    # powerfactory result for 2 active xwards
    u = 0.99568034
    pxw1 = -1707.1216
    pxw3 = -1707.1216

    qxw1 = -918.7316
    qxw3 = -918.7316

    assert abs(net.res_bus.vm_pu.at[b2] - u) < 1e-2
    assert abs(net.res_xward.p_kw.at[xw1] - (-pxw1)) < s_tol
    assert abs(net.res_xward.q_kvar.at[xw1] - (-qxw1)) < s_tol

    assert abs(net.res_xward.p_kw.at[xw3] - (-pxw3)) < s_tol
    assert abs(net.res_xward.q_kvar.at[xw3] - (-qxw3)) < s_tol


def test_gen(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_gen"]
    gens = [x for x in net.gen.index if net.gen.bus[x] in buses.index]
    b2 = buses.index[1]
    b3 = buses.index[2]
    g1 = gens[0]
    # powerfactory results
    q = -260.660
    u2 = 1.00584636
    u_set = 1.0

    assert abs(net.res_bus.vm_pu.at[b2] - u2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - u_set) < v_tol
    assert abs(net.res_gen.q_kvar.at[g1] - (-q)) < s_tol


def test_enforce_qlims(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_enforce_qlims"]
    gens = [x for x in net.gen.index if net.gen.bus[x] in buses.index]
    b2 = buses.index[1]
    b3 = buses.index[2]
    g1 = gens[0]

    # enforce reactive power limits
    runpp_with_consistency_checks(net, enforce_q_lims=True)

    # powerfactory results
    u2 = 1.00607194
    u3 = 1.00045091

    assert abs(net.res_bus.vm_pu.at[b2] - u2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - u3) < v_tol
    assert abs(net.res_gen.q_kvar.at[g1] - net.gen.max_q_kvar.at[g1]) < s_tol


def test_trafo3w(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=2e-2, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_trafo3w"]
    trafos = [x for x in net.trafo3w.index if net.trafo3w.hv_bus[
        x] in buses.index]
    runpp_with_consistency_checks(net, trafo_model="pi")
    b2 = buses.index[1]
    b3 = buses.index[2]
    b4 = buses.index[3]
    t3 = trafos[0]

    uhv = 1.010117166
    umv = 0.955501331
    ulv = 0.940630980

    load = 37.21
    qhv = 1.64375
    qmv = 0
    qlv = 0

    ihv = 0.00858590198
    imv = 0.20141269123
    ilv = 0.15344761586

    phv = 300.43
    pmv = -200.00
    plv = -100.00

    assert abs((net.res_bus.vm_pu.at[b2] - uhv)) < v_tol
    assert abs((net.res_bus.vm_pu.at[b3] - umv)) < v_tol
    assert abs((net.res_bus.vm_pu.at[b4] - ulv)) < v_tol

    assert abs((net.res_trafo3w.loading_percent.at[t3] - load)) < l_tol

    assert abs((net.res_trafo3w.p_hv_kw.at[t3] - phv)) < s_tol
    assert abs((net.res_trafo3w.p_mv_kw.at[t3] - pmv)) < s_tol
    assert abs((net.res_trafo3w.p_lv_kw.at[t3] - plv)) < s_tol

    assert abs((net.res_trafo3w.q_hv_kvar.at[t3] - qhv)) < s_tol
    assert abs((net.res_trafo3w.q_mv_kvar.at[t3] - qmv)) < s_tol
    assert abs((net.res_trafo3w.q_lv_kvar.at[t3] - qlv)) < s_tol

    assert abs((net.res_trafo3w.i_hv_ka.at[t3] - ihv)) < i_tol
    assert abs((net.res_trafo3w.i_mv_ka.at[t3] - imv)) < i_tol
    assert abs((net.res_trafo3w.i_lv_ka.at[t3] - ilv)) < i_tol


def test_impedance(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_impedance"]
    impedances = [
        x for x in net.impedance.index if net.impedance.from_bus[x] in buses.index]
    runpp_with_consistency_checks(net)
    buses = net.bus[net.bus.zone == "test_impedance"]
    impedances = [x for x in net.impedance.index if net.impedance.from_bus[x] in buses.index]
    runpp_with_consistency_checks(net, trafo_model="t", numba=True)
    b2 = buses.index[1]
    b3 = buses.index[2]
    imp1 = impedances[0]

    # powerfactory results
    ifrom = 0.0444417
    ito = 0.0029704

    pfrom = 1123.7008
    qfrom = 1061.8504

    pto = -1000.0000
    qto = -500.0000

    u2 = 1.004242894
    u3 = 0.987779091

    assert abs(net.res_impedance.p_from_kw.at[imp1] - pfrom) < s_tol
    assert abs(net.res_impedance.p_to_kw.at[imp1] - pto) < s_tol
    assert abs(net.res_impedance.q_from_kvar.at[imp1] - qfrom) < s_tol
    assert abs(net.res_impedance.q_to_kvar.at[imp1] - qto) < s_tol
    assert abs(net.res_impedance.i_from_ka.at[imp1] - ifrom) < i_tol
    assert abs(net.res_impedance.i_to_ka.at[imp1] - ito) < i_tol

    assert abs(net.res_bus.vm_pu.at[b2] - u2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - u3) < v_tol


def test_bus_bus_switch(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_bus_bus_switch"]
    b2 = buses.index[1]
    b3 = buses.index[2]

    # powerfactory voltage
    v2 = 0.982264132
    assert abs(net.res_bus.vm_pu.at[b2] - v2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - v2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b2] == net.res_bus.vm_pu.at[b2])


def test_enforce_q_lims(v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    """ Test for enforce_q_lims loadflow option
    """
    net = pp.create_empty_network()
    net = add_test_gen(net)
    pp.runpp(net)
    buses = net.bus[net.bus.zone == "test_gen"]
    gens = [x for x in net.gen.index if net.gen.bus[x] in buses.index]
    #    b1=buses.index[0]
    b2 = buses.index[1]
    b3 = buses.index[2]
    g1 = gens[0]
    q = -260.660
    u2 = 1.00584636
    u_set = 1.0
    assert abs(net.res_bus.vm_pu.at[b2] - u2) < v_tol
    assert abs(net.res_bus.vm_pu.at[b3] - u_set) < v_tol
    assert abs(net.res_gen.q_kvar.at[g1] - (-q)) < s_tol

    # test_enforce_qlims
    net = add_test_enforce_qlims(net)

    pp.runpp(net, enforce_q_lims=True)
    buses = net.bus[net.bus.zone == "test_enforce_qlims"]
    gens = [x for x in net.gen.index if net.gen.bus[x] in buses.index]
    b2 = buses.index[1]
    b3 = buses.index[2]
    g1 = gens[0]
    u2 = 1.00607194
    u3 = 1.00045091
    assert abs(net.res_bus.vm_pu.at[b2] - u2) < 1e-2
    assert abs(net.res_bus.vm_pu.at[b3] - u3) < 1e-2
    assert abs(net.res_gen.q_kvar.at[g1] - net.gen.max_q_kvar.at[g1]) < 1e-2


def test_shunt(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_shunt"]
    b2 = buses.index[1]
    shunts = [x for x in net.shunt.index if net.shunt.bus[x] in buses.index]
    s1 = shunts[0]

    u = 1.0177330269
    p = 205.44
    q = -2054.44

    assert abs(net.res_bus.vm_pu.loc[b2] - u) < v_tol
    assert abs(net.res_shunt.p_kw.loc[s1] - p) < s_tol
    assert abs(net.res_shunt.q_kvar.loc[s1] - q) < s_tol


def test_shunt_split(result_test_network, v_tol=1e-6, i_tol=1e-6, s_tol=5e-3, l_tol=1e-3):
    net = result_test_network
    buses = net.bus[net.bus.zone == "test_shunt_split"]
    b2 = buses.index[1]
    shunts = [x for x in net.shunt.index if net.shunt.bus[x] in buses.index]
    s1 = shunts[0]

    u = 1.015007138
    p = 123.628741
    q = -1236.287413

    assert abs(net.res_bus.vm_pu.loc[b2] - u) < v_tol
    assert abs(net.res_shunt.p_kw.loc[s1] - p / 2) < s_tol
    assert abs(net.res_shunt.q_kvar.loc[s1] - q / 2) < s_tol


def test_open(result_test_network):
    net = result_test_network
    buses = net.bus[net.bus.zone == "two_open_switches_on_deactive_line"]
    lines = net['line'][in1d(net['line'].from_bus, buses.index) | in1d(net['line'].to_bus, buses.index)]

    assert net['res_line'].ix[lines.index].i_ka.iloc[1] == 0.


if __name__ == "__main__":
    pytest.main(["test_results.py"])
