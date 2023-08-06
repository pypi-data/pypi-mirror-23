"""Module containing cython functions, which generate first order Redfield kernel.
   For docstrings see documentation of module neumann1."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import itertools

from ..mytypes import doublenp
from ..mytypes import complexnp

from ..aprclass import Approach
from .c_neumann1 import c_generate_phi1fct

cimport numpy as np
cimport cython

ctypedef np.uint8_t bool_t
ctypedef np.int_t int_t
ctypedef np.int64_t long_t
ctypedef np.float64_t double_t
ctypedef np.complex128_t complex_t

#---------------------------------------------------------------------------------------------------
# Redfield approach
#---------------------------------------------------------------------------------------------------
@cython.boundscheck(False)
def c_generate_kern_redfield(sys):
    cdef np.ndarray[double_t, ndim=1] E = sys.qd.Ea
    cdef np.ndarray[complex_t, ndim=3] Tba = sys.leads.Tba
    cdef np.ndarray[complex_t, ndim=3] phi1fct = sys.phi1fct
    si = sys.si
    cdef bint symq = sys.funcp.symq
    cdef long_t norm_rowp = sys.funcp.norm_row
    #
    cdef bool_t bbp_bool, bbpi_bool
    cdef int_t charge, acharge, bcharge, ccharge, l, nleads, \
               aap_sgn, bppbp_sgn, bbpp_sgn, ccp_sgn
    cdef long_t b, bp, bbp, bbpi, bb, \
                a, ap, aap, aapi, \
                bpp, bppbp, bppbpi, bbpp, bbppi, \
                c, cp, ccp, ccpi, \
                bpap, ba, bppa, cbpp, cpbp, cb
    cdef long_t norm_row, last_row, ndm0, npauli,
    cdef complex_t fct_aap, fct_bppbp, fct_bbpp, fct_ccp
    #
    cdef np.ndarray[long_t, ndim=1] lenlst = si.lenlst
    cdef np.ndarray[long_t, ndim=1] dictdm = si.dictdm
    cdef np.ndarray[long_t, ndim=1] shiftlst0 = si.shiftlst0
    cdef np.ndarray[long_t, ndim=1] shiftlst1 = si.shiftlst1
    cdef np.ndarray[long_t, ndim=1] mapdm0 = si.mapdm0
    cdef np.ndarray[bool_t, ndim=1] booldm0 = si.booldm0
    cdef np.ndarray[bool_t, ndim=1] conjdm0 = si.conjdm0
    #
    norm_row = norm_rowp if symq else si.ndm0r
    last_row = si.ndm0r-1 if symq else si.ndm0r
    ndm0, npauli, nleads = si.ndm0, si.npauli, si.nleads
    #
    cdef np.ndarray[double_t, ndim=2] kern = np.zeros((last_row+1, si.ndm0r), dtype=doublenp)
    cdef np.ndarray[double_t, ndim=1] bvec = np.zeros(last_row+1, dtype=doublenp)
    bvec[norm_row] = 1
    for charge in range(si.ncharge):
        acharge = charge-1
        bcharge = charge
        ccharge = charge+1
        for b, bp in itertools.combinations_with_replacement(si.statesdm[bcharge], 2):
            bbp = mapdm0[lenlst[bcharge]*dictdm[b] + dictdm[bp] + shiftlst0[bcharge]]
            bbp_bool = booldm0[lenlst[bcharge]*dictdm[b] + dictdm[bp] + shiftlst0[bcharge]]
            if bbp != -1 and bbp_bool:
                bbpi = ndm0 + bbp - npauli
                bbpi_bool = True if bbpi >= ndm0 else False
                if bbpi_bool:
                    kern[bbp, bbpi] = kern[bbp, bbpi] + E[b]-E[bp]
                    kern[bbpi, bbp] = kern[bbpi, bbp] + E[bp]-E[b]
                #--------------------------------------------------
                for a, ap in itertools.product(si.statesdm[acharge], si.statesdm[acharge]):
                    aap = mapdm0[lenlst[acharge]*dictdm[a] + dictdm[ap] + shiftlst0[acharge]]
                    if aap != -1:
                        bpap = lenlst[acharge]*dictdm[bp] + dictdm[ap] + shiftlst1[acharge]
                        ba = lenlst[acharge]*dictdm[b] + dictdm[a] + shiftlst1[acharge]
                        fct_aap = 0
                        for l in range(nleads):
                            fct_aap += (+Tba[l, b, a]*Tba[l, ap, bp]*phi1fct[l, bpap, 0].conjugate()
                                        -Tba[l, b, a]*Tba[l, ap, bp]*phi1fct[l, ba, 0])
                        aapi = ndm0 + aap - npauli
                        aap_sgn = +1 if conjdm0[lenlst[acharge]*dictdm[a] + dictdm[ap] + shiftlst0[acharge]] else -1
                        kern[bbp, aap] = kern[bbp, aap] + fct_aap.imag                              # kern[bbp, aap]   += fct_aap.imag
                        if aapi >= ndm0:
                            kern[bbp, aapi] = kern[bbp, aapi] + fct_aap.real*aap_sgn                # kern[bbp, aapi]  += fct_aap.real*aap_sgn
                            if bbpi_bool:
                                kern[bbpi, aapi] = kern[bbpi, aapi] + fct_aap.imag*aap_sgn          # kern[bbpi, aapi] += fct_aap.imag*aap_sgn
                        if bbpi_bool:
                            kern[bbpi, aap] = kern[bbpi, aap] - fct_aap.real                        # kern[bbpi, aap]  -= fct_aap.real
                #--------------------------------------------------
                for bpp in si.statesdm[bcharge]:
                    bppbp = mapdm0[lenlst[bcharge]*dictdm[bpp] + dictdm[bp] + shiftlst0[bcharge]]
                    if bppbp != -1:
                        fct_bppbp = 0
                        for a in si.statesdm[acharge]:
                            bppa = lenlst[acharge]*dictdm[bpp] + dictdm[a] + shiftlst1[acharge]
                            for l in range(nleads):
                                fct_bppbp += +Tba[l, b, a]*Tba[l, a, bpp]*phi1fct[l, bppa, 1].conjugate()
                        for c in si.statesdm[ccharge]:
                            cbpp = lenlst[bcharge]*dictdm[c] + dictdm[bpp] + shiftlst1[bcharge]
                            for l in range(nleads):
                                fct_bppbp += +Tba[l, b, c]*Tba[l, c, bpp]*phi1fct[l, cbpp, 0]
                        bppbpi = ndm0 + bppbp - npauli
                        bppbp_sgn = +1 if conjdm0[lenlst[bcharge]*dictdm[bpp] + dictdm[bp] + shiftlst0[bcharge]] else -1
                        kern[bbp, bppbp] = kern[bbp, bppbp] + fct_bppbp.imag                        # kern[bbp, bppbp] += fct_bppbp.imag
                        if bppbpi >= ndm0:
                            kern[bbp, bppbpi] = kern[bbp, bppbpi] + fct_bppbp.real*bppbp_sgn        # kern[bbp, bppbpi] += fct_bppbp.real*bppbp_sgn
                            if bbpi_bool:
                                kern[bbpi, bppbpi] = kern[bbpi, bppbpi] + fct_bppbp.imag*bppbp_sgn  # kern[bbpi, bppbpi] += fct_bppbp.imag*bppbp_sgn
                        if bbpi_bool:
                            kern[bbpi, bppbp] = kern[bbpi, bppbp] - fct_bppbp.real                  # kern[bbpi, bppbp] -= fct_bppbp.real
                    #--------------------------------------------------
                    bbpp = mapdm0[lenlst[bcharge]*dictdm[b] + dictdm[bpp] + shiftlst0[bcharge]]
                    if bbpp != -1:
                        fct_bbpp = 0
                        for a in si.statesdm[acharge]:
                            bppa = lenlst[acharge]*dictdm[bpp] + dictdm[a] + shiftlst1[acharge]
                            for l in range(nleads):
                                fct_bbpp += -Tba[l, bpp, a]*Tba[l, a, bp]*phi1fct[l, bppa, 1]
                        for c in si.statesdm[ccharge]:
                            cbpp = lenlst[bcharge]*dictdm[c] + dictdm[bpp] + shiftlst1[bcharge]
                            for l in range(nleads):
                                fct_bbpp += -Tba[l, bpp, c]*Tba[l, c, bp]*phi1fct[l, cbpp, 0].conjugate()
                        bbppi = ndm0 + bbpp - npauli
                        bbpp_sgn = +1 if conjdm0[lenlst[bcharge]*dictdm[b] + dictdm[bpp] + shiftlst0[bcharge]] else -1
                        kern[bbp, bbpp] = kern[bbp, bbpp] + fct_bbpp.imag                           # kern[bbp, bbpp] += fct_bbpp.imag
                        if bbppi >= ndm0:
                            kern[bbp, bbppi] = kern[bbp, bbppi] + fct_bbpp.real*bbpp_sgn            # kern[bbp, bbppi] += fct_bbpp.real*bbpp_sgn
                            if bbpi_bool:
                                kern[bbpi, bbppi] = kern[bbpi, bbppi] + fct_bbpp.imag*bbpp_sgn      # kern[bbpi, bbppi] += fct_bbpp.imag*bbpp_sgn
                        if bbpi_bool:
                            kern[bbpi, bbpp] = kern[bbpi, bbpp] - fct_bbpp.real                     # kern[bbpi, bbpp] -= fct_bbpp.real
                #--------------------------------------------------
                for c, cp in itertools.product(si.statesdm[ccharge], si.statesdm[ccharge]):
                    ccp = mapdm0[lenlst[ccharge]*dictdm[c] + dictdm[cp] + shiftlst0[ccharge]]
                    if ccp != -1:
                        cpbp = lenlst[bcharge]*dictdm[cp] + dictdm[bp] + shiftlst1[bcharge]
                        cb = lenlst[bcharge]*dictdm[c] + dictdm[b] + shiftlst1[bcharge]
                        fct_ccp = 0
                        for l in range(nleads):
                            fct_ccp += (+Tba[l, b, c]*Tba[l, cp, bp]*phi1fct[l, cpbp, 1]
                                        -Tba[l, b, c]*Tba[l, cp, bp]*phi1fct[l, cb, 1].conjugate())
                        ccpi = ndm0 + ccp - npauli
                        ccp_sgn = +1 if conjdm0[lenlst[ccharge]*dictdm[c] + dictdm[cp] + shiftlst0[ccharge]] else -1
                        kern[bbp, ccp] = kern[bbp, ccp] + fct_ccp.imag                              # kern[bbp, ccp] += fct_ccp.imag
                        if ccpi >= ndm0:
                            kern[bbp, ccpi] = kern[bbp, ccpi] + fct_ccp.real*ccp_sgn                # kern[bbp, ccpi] += fct_ccp.real*ccp_sgn
                            if bbpi_bool:
                                kern[bbpi, ccpi] = kern[bbpi, ccpi] + fct_ccp.imag*ccp_sgn          # kern[bbpi, ccpi] += fct_ccp.imag*ccp_sgn
                        if bbpi_bool:
                            kern[bbpi, ccp] = kern[bbpi, ccp] - fct_ccp.real                        # kern[bbpi, ccp] -= fct_ccp.real
                #--------------------------------------------------
    # Normalisation condition
    kern[norm_row] = np.zeros(si.ndm0r, dtype=doublenp)
    for charge in range(si.ncharge):
        for b in si.statesdm[charge]:
            bb = mapdm0[lenlst[charge]*dictdm[b] + dictdm[b] + shiftlst0[charge]]
            kern[norm_row, bb] += 1
    sys.kern = kern
    sys.bvec = bvec
    return 0

@cython.boundscheck(False)
def c_generate_current_redfield(sys):
    cdef np.ndarray[double_t, ndim=1] phi0p = sys.phi0
    cdef np.ndarray[double_t, ndim=1] E = sys.qd.Ea
    cdef np.ndarray[complex_t, ndim=3] Tba = sys.leads.Tba
    cdef np.ndarray[complex_t, ndim=3] phi1fct = sys.phi1fct
    cdef np.ndarray[complex_t, ndim=3] phi1fct_energy = sys.phi1fct_energy
    si = sys.si
    #
    cdef bool_t bpb_conj, ccp_conj
    cdef int_t bcharge, ccharge, charge, l, nleads,
    cdef long_t c, b, cb, bp, bpb, cp, ccp, cbp, cpb
    cdef long_t ndm0, ndm1, npauli
    cdef complex_t fct1, fct2, fct1h, fct2h, phi0bpb, phi0ccp
    ndm0, ndm1, npauli, nleads = si.ndm0, si.ndm1, si.npauli, si.nleads
    #
    cdef np.ndarray[long_t, ndim=1] lenlst = si.lenlst
    cdef np.ndarray[long_t, ndim=1] dictdm = si.dictdm
    cdef np.ndarray[long_t, ndim=1] shiftlst0 = si.shiftlst0
    cdef np.ndarray[long_t, ndim=1] shiftlst1 = si.shiftlst1
    cdef np.ndarray[long_t, ndim=1] mapdm0 = si.mapdm0
    cdef np.ndarray[bool_t, ndim=1] booldm0 = si.booldm0
    cdef np.ndarray[bool_t, ndim=1] conjdm0 = si.conjdm0
    #
    cdef np.ndarray[complex_t, ndim=2] phi1 = np.zeros((nleads, ndm1), dtype=complexnp)
    cdef np.ndarray[complex_t, ndim=1] current = np.zeros(nleads, dtype=complexnp)
    cdef np.ndarray[complex_t, ndim=1] energy_current = np.zeros(nleads, dtype=complexnp)
    cdef np.ndarray[complex_t, ndim=1] phi0 = np.zeros(ndm0, dtype=complexnp)
    #
    phi0[0:npauli] = phi0p[0:npauli]
    phi0[npauli:ndm0] = phi0p[npauli:ndm0] + 1j*phi0p[ndm0:]
    #
    for charge in range(si.ncharge-1):
        ccharge = charge+1
        bcharge = charge
        for c, b in itertools.product(si.statesdm[ccharge], si.statesdm[bcharge]):
            cb = lenlst[bcharge]*dictdm[c] + dictdm[b] + shiftlst1[bcharge]
            for l in range(nleads):
                for bp in si.statesdm[bcharge]:
                    bpb = mapdm0[lenlst[bcharge]*dictdm[bp] + dictdm[b] + shiftlst0[bcharge]]
                    if bpb != -1:
                        cbp = lenlst[bcharge]*dictdm[c] + dictdm[bp] + shiftlst1[bcharge]
                        fct1 = phi1fct[l, cbp, 0]
                        fct1h = phi1fct_energy[l, cbp, 0]
                        bpb_conj = conjdm0[lenlst[bcharge]*dictdm[bp] + dictdm[b] + shiftlst0[bcharge]]
                        phi0bpb = phi0[bpb] if bpb_conj else phi0[bpb].conjugate()
                        phi1[l, cb] = phi1[l, cb] + Tba[l, c, bp]*phi0bpb*fct1
                        current[l] = current[l] + Tba[l, b, c]*Tba[l, c, bp]*phi0bpb*fct1
                        energy_current[l] = energy_current[l] + Tba[l, b, c]*Tba[l, c, bp]*phi0bpb*fct1h
                for cp in si.statesdm[ccharge]:
                    ccp = mapdm0[lenlst[ccharge]*dictdm[c] + dictdm[cp] + shiftlst0[ccharge]]
                    if ccp != -1:
                        cpb = lenlst[bcharge]*dictdm[cp] + dictdm[b] + shiftlst1[bcharge]
                        fct2 = phi1fct[l, cpb, 1]
                        fct2h = phi1fct_energy[l, cpb, 1]
                        ccp_conj = conjdm0[lenlst[ccharge]*dictdm[c] + dictdm[cp] + shiftlst0[ccharge]]
                        phi0ccp = phi0[ccp] if ccp_conj else phi0[ccp].conjugate()
                        phi1[l, cb] = phi1[l, cb] + Tba[l, cp, b]*phi0ccp*fct2
                        current[l] = current[l] + Tba[l, b, c]*phi0ccp*Tba[l, cp, b]*fct2
                        energy_current[l] = energy_current[l] + Tba[l, b, c]*phi0ccp*Tba[l, cp, b]*fct2h
    sys.phi1 = phi1
    sys.current = np.array(-2*current.imag, dtype=doublenp)
    sys.energy_current = np.array(-2*energy_current.imag, dtype=doublenp)
    sys.heat_current = sys.energy_current - sys.current*sys.leads.mulst
    return 0

@cython.boundscheck(False)
def c_generate_vec_redfield(np.ndarray[double_t, ndim=1] phi0p, sys):
    cdef np.ndarray[double_t, ndim=1] E = sys.qd.Ea
    cdef np.ndarray[complex_t, ndim=3] Tba = sys.leads.Tba
    cdef np.ndarray[complex_t, ndim=3] phi1fct = sys.phi1fct
    si = sys.si
    cdef long_t norm_row = sys.funcp.norm_row
    #
    cdef bool_t bbp_bool
    cdef int_t charge, acharge, bcharge, ccharge, l, nleads, \
               aap_sgn, bppbp_sgn, bbpp_sgn, ccp_sgn
    cdef long_t b, bp, bbp, bb, \
                a, ap, aap, \
                bpp, bppbp, bbpp, \
                c, cp, ccp, \
                bpap, ba, bppa, cbpp, cpbp, cb
    cdef long_t ndm0, npauli
    cdef complex_t fct_aap, fct_bppbp, fct_bbpp, fct_ccp, norm
    cdef complex_t phi0aap, phi0bppbp, phi0bbpp, phi0ccp
    ndm0, npauli, nleads = si.ndm0, si.npauli, si.nleads
    #
    cdef np.ndarray[long_t, ndim=1] lenlst = si.lenlst
    cdef np.ndarray[long_t, ndim=1] dictdm = si.dictdm
    cdef np.ndarray[long_t, ndim=1] shiftlst0 = si.shiftlst0
    cdef np.ndarray[long_t, ndim=1] shiftlst1 = si.shiftlst1
    cdef np.ndarray[long_t, ndim=1] mapdm0 = si.mapdm0
    cdef np.ndarray[bool_t, ndim=1] booldm0 = si.booldm0
    cdef np.ndarray[bool_t, ndim=1] conjdm0 = si.conjdm0
    #
    cdef np.ndarray[complex_t, ndim=1] phi0 = np.zeros(ndm0, dtype=complexnp)
    cdef np.ndarray[complex_t, ndim=1] i_dphi0_dt = np.zeros(ndm0, dtype=complexnp)
    #
    phi0[0:npauli] = phi0p[0:npauli]
    phi0[npauli:ndm0] = phi0p[npauli:ndm0] + 1j*phi0p[ndm0:]
    norm = 0
    for charge in range(si.ncharge):
        acharge = charge-1
        bcharge = charge
        ccharge = charge+1
        for b, bp in itertools.combinations_with_replacement(si.statesdm[charge], 2):
            bbp = mapdm0[lenlst[bcharge]*dictdm[b] + dictdm[bp] + shiftlst0[bcharge]]
            if bbp != -1:
                if b == bp: norm = norm + phi0[bbp]
                bbp_bool = booldm0[lenlst[bcharge]*dictdm[b] + dictdm[bp] + shiftlst0[bcharge]]
                if bbp_bool:
                    i_dphi0_dt[bbp] = i_dphi0_dt[bbp] + (E[b]-E[bp])*phi0[bbp]
                    #--------------------------------------------------
                    for a, ap in itertools.product(si.statesdm[charge-1], si.statesdm[charge-1]):
                        aap = mapdm0[lenlst[acharge]*dictdm[a] + dictdm[ap] + shiftlst0[acharge]]
                        if aap != -1:
                            bpap = lenlst[acharge]*dictdm[bp] + dictdm[ap] + shiftlst1[acharge]
                            ba = lenlst[acharge]*dictdm[b] + dictdm[a] + shiftlst1[acharge]
                            fct_aap = 0
                            for l in range(nleads):
                                fct_aap += (+Tba[l, b, a]*Tba[l, ap, bp]*phi1fct[l, bpap, 0].conjugate()
                                            -Tba[l, b, a]*Tba[l, ap, bp]*phi1fct[l, ba, 0])
                            phi0aap = phi0[aap] if conjdm0[lenlst[acharge]*dictdm[a] + dictdm[ap] + shiftlst0[acharge]] else phi0[aap].conjugate()
                            i_dphi0_dt[bbp] = i_dphi0_dt[bbp] + fct_aap*phi0aap
                    #--------------------------------------------------
                    for bpp in si.statesdm[charge]:
                        bppbp = mapdm0[lenlst[bcharge]*dictdm[bpp] + dictdm[bp] + shiftlst0[bcharge]]
                        if bppbp != -1:
                            fct_bppbp = 0
                            for a in si.statesdm[charge-1]:
                                bppa = lenlst[acharge]*dictdm[bpp] + dictdm[a] + shiftlst1[acharge]
                                for l in range(nleads):
                                    fct_bppbp += +Tba[l, b, a]*Tba[l, a, bpp]*phi1fct[l, bppa, 1].conjugate()
                            for c in si.statesdm[charge+1]:
                                cbpp = lenlst[bcharge]*dictdm[c] + dictdm[bpp] + shiftlst1[bcharge]
                                for l in range(nleads):
                                    fct_bppbp += +Tba[l, b, c]*Tba[l, c, bpp]*phi1fct[l, cbpp, 0]
                            phi0bppbp = phi0[bppbp] if conjdm0[lenlst[bcharge]*dictdm[bpp] + dictdm[bp] + shiftlst0[bcharge]] else phi0[bppbp].conjugate()
                            i_dphi0_dt[bbp] = i_dphi0_dt[bbp] + fct_bppbp*phi0bppbp
                        #--------------------------------------------------
                        bbpp = mapdm0[lenlst[bcharge]*dictdm[b] + dictdm[bpp] + shiftlst0[bcharge]]
                        if bbpp != -1:
                            fct_bbpp = 0
                            for a in si.statesdm[charge-1]:
                                bppa = lenlst[acharge]*dictdm[bpp] + dictdm[a] + shiftlst1[acharge]
                                for l in range(nleads):
                                    fct_bbpp += -Tba[l, bpp, a]*Tba[l, a, bp]*phi1fct[l, bppa, 1]
                            for c in si.statesdm[charge+1]:
                                cbpp = lenlst[bcharge]*dictdm[c] + dictdm[bpp] + shiftlst1[bcharge]
                                for l in range(nleads):
                                    fct_bbpp += -Tba[l, bpp, c]*Tba[l, c, bp]*phi1fct[l, cbpp, 0].conjugate()
                            phi0bbpp = phi0[bbpp] if conjdm0[lenlst[bcharge]*dictdm[b] + dictdm[bpp] + shiftlst0[bcharge]] else phi0[bbpp].conjugate()
                            i_dphi0_dt[bbp] = i_dphi0_dt[bbp] + fct_bbpp*phi0bbpp
                    #--------------------------------------------------
                    for c, cp in itertools.product(si.statesdm[charge+1], si.statesdm[charge+1]):
                        ccp = mapdm0[lenlst[ccharge]*dictdm[c] + dictdm[cp] + shiftlst0[ccharge]]
                        if ccp != -1:
                            cpbp = lenlst[bcharge]*dictdm[cp] + dictdm[bp] + shiftlst1[bcharge]
                            cb = lenlst[bcharge]*dictdm[c] + dictdm[b] + shiftlst1[bcharge]
                            fct_ccp = 0
                            for l in range(nleads):
                                fct_ccp += (+Tba[l, b, c]*Tba[l, cp, bp]*phi1fct[l, cpbp, 1]
                                            -Tba[l, b, c]*Tba[l, cp, bp]*phi1fct[l, cb, 1].conjugate())
                            phi0ccp = phi0[ccp] if conjdm0[lenlst[ccharge]*dictdm[c] + dictdm[cp] + shiftlst0[ccharge]] else phi0[ccp].conjugate()
                            i_dphi0_dt[bbp] = i_dphi0_dt[bbp] + fct_ccp*phi0ccp
                    #--------------------------------------------------
    i_dphi0_dt[norm_row] = 1j*(norm-1)
    return np.concatenate((i_dphi0_dt.imag, i_dphi0_dt[npauli:ndm0].real))

class Approach_Redfield(Approach):

    kerntype = 'Redfield'
    generate_fct = c_generate_phi1fct
    generate_kern = c_generate_kern_redfield
    generate_current = c_generate_current_redfield
    generate_vec = c_generate_vec_redfield
#---------------------------------------------------------------------------------------------------
