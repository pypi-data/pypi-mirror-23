# -*- coding: utf-8 -*-
"""
Electrical loads
"""
from __future__ import division
import numpy as np
from cea.utilities import physics

__author__ = "Jimeno A. Fonseca"
__copyright__ = "Copyright 2016, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Jimeno A. Fonseca"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"


def calc_Eint(tsd, bpr, list_uses, schedules):
    """
    Calculate final internal electrical loads (without auxiliary loads)

    :param tsd: Timestep data
    :type tsd: Dict[str, numpy.ndarray]

    :param bpr: building properties
    :type bpr: cea.demand.thermal_loads.BuildingPropertiesRow

    :param list_uses: The list of uses used in the project
    :type list_uses: list

    :param schedules: The list of schedules defined for the project - in the same order as `list_uses`
    :type schedules: List[numpy.ndarray]

    :param building_uses: for each use in `list_uses`, the percentage of that use for this building.
        Sum of values is 1.0
    :type building_uses: Dict[str, numpy.ndarray]

    :returns: `tsd` with new keys: `['Eaf', 'Elf', 'Ealf', 'Edataf', 'Eref', 'Eprof']`
    :rtype: Dict[str, numpy.ndarray]
    """

    # calculate schedules
    schedule_applicances_lighting = average_appliances_lighting_schedule(list_uses, schedules, bpr.occupancy)

    # calculate final electrical consumption due to appliances and lights
    tsd['Eaf'] = schedule_applicances_lighting * bpr.internal_loads['Ea_Wm2'] * bpr.rc_model['Aef']
    tsd['Elf'] = schedule_applicances_lighting * bpr.internal_loads['El_Wm2'] * bpr.rc_model['Aef']
    tsd['Ealf'] = tsd['Elf'] + tsd['Eaf']

    # calculate other loads
    if 'COOLROOM' in bpr.occupancy:
        schedule_Eref = average_appliances_lighting_schedule(['COOLROOM'], schedules, bpr.occupancy)
        tsd['Eref'] = calc_Eref(schedule_Eref, bpr.internal_loads['Ere_Wm2'], bpr.rc_model['Aef'])  # in W
    else:
        tsd['Eref'] = np.zeros(8760)

    if 'SERVERROOM' in bpr.occupancy:
        schedule_Edata = average_appliances_lighting_schedule(['SERVERROOM'], schedules, bpr.occupancy)
        tsd['Edataf'] = calc_Edataf(schedule_Edata, bpr.internal_loads['Ed_Wm2'], bpr.rc_model['Aef'])  # in W
    else:
        tsd['Edataf'] = np.zeros(8760)

    if 'INDUSTRY' in bpr.occupancy:
        schedule_pro = calc_Eprof_schedule(list_uses, schedules, bpr.occupancy)
        tsd['Eprof'] = calc_Eprof(schedule_pro, bpr.internal_loads['Epro_Wm2'], bpr.rc_model['Aef'])  # in W
    else:
        tsd['Eprof'] = np.zeros(8760)
        tsd['Ecaf'] = np.zeros(8760) # not used in the current version but in the optimization part
    return tsd


def average_appliances_lighting_schedule(list_uses, schedules, building_uses):
    """
    Calculate the schedule to use for lighting and appliances based on the building uses from the schedules
    defined for the project unsing a weighted average.

    :param list_uses: the schedule names for the `schedules` parameter
    :type list_uses: List[str]
    :param schedules: the schedules, one for each name in `list_uses`. Each schedule is a list of 8760 floats...
    :type schedules: List[Tuple[List[float], List[float], List[float]]]
    :param building_uses: A set of weights for the schedules as they apply to this particular building.
    :type building_uses: Dict[str, float]

    :return: appliances lighting schedule as a weighted average of the schedules for a specific building.
    :rtype: numpy.ndarray[numpy.float64]
    """

    # weighted average of schedules
    def calc_average(last, current, share_of_use):
        return last + current * share_of_use

    el = np.zeros(8760)
    num_profiles = len(list_uses)
    for num in range(num_profiles):
        if list_uses[num] not in building_uses:
            current_share_of_use = 0
        else:
            current_share_of_use = building_uses[list_uses[num]]

        el = np.vectorize(calc_average)(el, schedules[num][1], current_share_of_use)
    return el


def calc_Edataf(schedule, Ed_Wm2, Aef):
    """
    Calculates the final electricity consumption in data centers.

    :param schedule: The data center schedule as calculated by `calc_Ea_El_Edata_Eref_schedule` but just for the
                     SERVERROOM portion of the occupancy.
    :type schedule: ndarray

    :param Ed_Wm2: The maximum electrical consumption due to servers per unit of gross floor area (as taken from the
                   building properties / internal loads file)
    :type Ed_Wm2: float64

    :param Aef: The floor area with electricity in [m2]
    :type Aef: float64

    :returns: final electricity consumption in data centers per hour in [W]
    :rtype: numpy.ndarray[numpy.float64]
    """
    Edataf = schedule * Ed_Wm2 * Aef   # in W
    return Edataf


def calc_Eref(schedule, Ere_Wm2, Aef):
    Eref = schedule * Ere_Wm2 * Aef  # in W
    return Eref


def calc_Eprof_schedule(list_uses, schedules, building_uses):
    """
    Calculate a weighted average of the schedules as defined in `list_uses` and `schedules`, using the weights
    in `building_uses` (which is taken from `bpr.occupancy`).

    :param list_uses: the schedule names for the `schedules` parameter
    :type list_uses: list of str
    :param schedules: the schedules, one for each name in `list_uses`. Each schedule is a list of 8760 floats...
    :type schedules: list of list of float
    :param building_uses: A set of weights for the schedules as they apply to this particular building.
    :type building_uses: dict of (str, float)

    :return: A weighted average of the schedules for a specific building.
    :rtype: numpy.ndarray[numpy.float64]
    """

    def calc_average(last, current, share_of_use):
        return last + current * share_of_use

    pro = np.zeros(8760)
    num_profiles = len(list_uses)
    for num in range(num_profiles):
        current_share_of_use = building_uses[list_uses[num]]
        epro = np.vectorize(calc_average)(pro, schedules[num][3], current_share_of_use)
    return epro


def calc_Eprof(schedule, Epro_Wm2, Aef):
    Eprof = schedule * Epro_Wm2 * Aef  # in W
    return Eprof


def calc_Eauxf(Ll, Lw, Mww, Qcsf, Qcsf_0, Qhsf, Qhsf_0, Qww, Qwwf, Qwwf_0, Tcs_re, Tcs_sup,
               Ths_re, Ths_sup, Vw, Year, fforma, gv, nf_ag, nfp, sys_e_cooling,
               sys_e_heating, Ehs_lat_aux, tsd):
    Eaux_cs = np.zeros(8760)
    Eaux_ve = np.zeros(8760)
    Eaux_fw = np.zeros(8760)
    Eaux_hs = np.zeros(8760)
    Imax = 2 * (Ll + Lw / 2 + gv.hf + (nf_ag * nfp) + 10) * fforma
    deltaP_des = Imax * gv.deltaP_l * (1 + gv.fsr)
    if Year >= 2000:
        b = 1
    else:
        b = 1.2
    Eaux_ww = np.vectorize(calc_Eauxf_ww)(Qww, Qwwf, Qwwf_0, Imax, deltaP_des, b, Mww)
    if sys_e_heating != "T0":
        Eaux_hs = np.vectorize(calc_Eauxf_hs_dis)(Qhsf, Qhsf_0, Imax, deltaP_des, b, Ths_sup, Ths_re, gv.Cpw)
    if sys_e_cooling != "T0":
        Eaux_cs = np.vectorize(calc_Eauxf_cs_dis)(Qcsf, Qcsf_0, Imax, deltaP_des, b, Tcs_sup, Tcs_re, gv.Cpw)
    if nf_ag > 5:  # up to 5th floor no pumping needs
        Eaux_fw = calc_Eauxf_fw(Vw, nf_ag, gv)

    Eaux_ve = np.vectorize(calc_Eauxf_ve)(tsd, gv)

    Eauxf = Eaux_hs + Eaux_cs + Eaux_ve + Eaux_ww + Eaux_fw + Ehs_lat_aux

    return Eauxf, Eaux_hs, Eaux_cs, Eaux_ve, Eaux_ww, Eaux_fw


def calc_Eauxf_hs_dis(Qhsf, Qhsf0, Imax, deltaP_des, b, ts, tr, cpw):
    # the power of the pump in Watts
    if Qhsf > 0 and (ts - tr) != 0:
        fctr = 1.05
        qV_des = Qhsf / ((ts - tr) * cpw * 1000)
        Phy_des = 0.2278 * deltaP_des * qV_des
        feff = (1.25 * (200 / Phy_des) ** 0.5) * fctr * b
        # Ppu_dis = Phy_des*feff
        if Qhsf / Qhsf0 > 0.67:
            Ppu_dis_hy_i = Phy_des
            feff = (1.25 * (200 / Ppu_dis_hy_i) ** 0.5) * fctr * b
            Eaux_hs = Ppu_dis_hy_i * feff
        else:
            Ppu_dis_hy_i = 0.0367 * Phy_des
            feff = (1.25 * (200 / Ppu_dis_hy_i) ** 0.5) * fctr * b
            Eaux_hs = Ppu_dis_hy_i * feff
    else:
        Eaux_hs = 0.0
    return Eaux_hs  # in #W


def calc_Eauxf_cs_dis(Qcsf, Qcsf0, Imax, deltaP_des, b, ts, tr, cpw):
    # refrigerant R-22 1200 kg/m3
    # for Cooling system
    # the power of the pump in Watts
    if Qcsf < 0 and (ts - tr) != 0:
        fctr = 1.10
        qV_des = Qcsf / ((ts - tr) * cpw * 1000)  # kg/s
        Phy_des = 0.2778 * deltaP_des * qV_des
        feff = (1.25 * (200 / Phy_des) ** 0.5) * fctr * b
        # Ppu_dis = Phy_des*feff
        # the power of the pump in Watts
        if Qcsf < 0:
            if Qcsf / Qcsf0 > 0.67:
                Ppu_dis_hy_i = Phy_des
                feff = (1.25 * (200 / Ppu_dis_hy_i) ** 0.5) * fctr * b
                Eaux_cs = Ppu_dis_hy_i * feff
            else:
                Ppu_dis_hy_i = 0.0367 * Phy_des
                feff = (1.25 * (200 / Ppu_dis_hy_i) ** 0.5) * fctr * b
                Eaux_cs = Ppu_dis_hy_i * feff
    else:
        Eaux_cs = 0.0
    return Eaux_cs  # in #W


def calc_Eauxf_ve(tsd, gv):
    """
    calculation of auxiliary electricity consumption of mechanical ventilation and AC fans
    
    :param tsd: Time series data of building
    :type tsd: dict
    :param gv: global variables
    :type gv: cea.globalvar.GlobalVariables
    :return: electrical energy for fans of mechanical ventilation in [Wh/h]
    :rtype: float
    """

    # TODO: DOCUMENTATION
    # FIXME: Why only energy demand for AC? Also other mechanical ventilation should have auxiliary energy demand
    # FIXME: What are the units

    # m_ve_mech is

    fan_power = gv.Pfan  # specific fan consumption in W/m3/h, see globalvar.py

    # mechanical ventilation system air flow [m3/s] = outdoor air + recirculation air
    q_ve_mech = tsd['m_ve_mech']/physics.calc_rho_air(tsd['theta_ve_mech']) \
        + tsd['m_ve_recirculation']/physics.calc_rho_air(tsd['theta_a'])

    Eve_aux = fan_power * q_ve_mech * 3600

    return Eve_aux


def calc_Eauxf_ww(Qww, Qwwf, Qwwf0, Imax, deltaP_des, b, qV_des):
    if Qww > 0:
        # for domestichotwater
        # the power of the pump in Watts
        Phy_des = 0.2778 * deltaP_des * qV_des
        feff = (1.25 * (200 / Phy_des) ** 0.5) * b
        # Ppu_dis = Phy_des*feff
        # the power of the pump in Watts
        if Qwwf / Qwwf0 > 0.67:
            Ppu_dis_hy_i = Phy_des
            feff = (1.25 * (200 / Ppu_dis_hy_i) ** 0.5) * b
            Eaux_ww = Ppu_dis_hy_i * feff
        else:
            Ppu_dis_hy_i = 0.0367 * Phy_des
            feff = (1.25 * (200 / Ppu_dis_hy_i) ** 0.5) * b
            Eaux_ww = Ppu_dis_hy_i * feff
    else:
        Eaux_ww = 0.0
    return Eaux_ww  # in #W


def calc_Eauxf_fw(freshw, nf, gv):
    Eaux_fw = np.zeros(8760)
    # for domesticFreshwater
    # the power of the pump in Watts Assuming the best performance of the pump of 0.6 and an accumulation tank
    for day in range(1, 366):
        balance = 0
        t0 = (day - 1) * 24
        t24 = day * 24
        for hour in range(t0, t24):
            balance = balance + freshw[hour]
        if balance > 0:
            flowday = balance / (3600)  # in m3/s
            Energy_hourWh = (gv.hf * (nf - 5)) / 0.6 * gv.Pwater * gv.gr * (flowday / gv.hoursop) / gv.effi
            for t in range(1, gv.hoursop + 1):
                time = t0 + 11 + t
                Eaux_fw[time] = Energy_hourWh
    return Eaux_fw
