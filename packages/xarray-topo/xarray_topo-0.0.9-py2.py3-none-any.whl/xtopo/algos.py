import numpy as np
import numba


@numba.njit
def compute_flow_receiver_d8(receiver, dist2receiver, elevation,
                             nx, ny, dx, dy):
    for i in range(1, ny - 1):
        for j in range(1, nx - 1):
            ij = i * nx + j
            slope_max = 1e-20

            for ii in (-1, 0, 1):
                for jj in (-1, 0, 1):
                    ni = i + ii
                    nj = j + jj
                    ijk = ni * nx + nj
                    if ijk == ij:
                        continue
                    length = np.sqrt((dx * ii)**2 + (dy * jj)**2)
                    slope = (elevation[ij] - elevation[ijk]) / length
                    if slope > slope_max:
                        slope_max = slope
                        receiver[ij] = ijk
                        dist2receiver[ij] = length


@numba.njit
def _find_stack(ij, donor, ndonor, nn, stack, nstack):
    for k in range(ndonor[ij]):
        ijk = donor[ij, k]
        stack[nstack] = ijk
        nstack += 1
        nstack = _find_stack(ijk, donor, ndonor, nn, stack, nstack)
    return nstack


@numba.njit
def compute_stack(stack, receiver, donor, ndonor, nn):
    # retrieve donors (invert receivers)
    ndonor[:] = 0
    for ij in range(nn):
        if receiver[ij] != ij:
            ijk = receiver[ij]
            ndonor[ijk] += 1
            donor[ijk, ndonor[ijk] - 1] = ij

    # build stack(s)
    nstack = 0
    for ij in range(nn):
        if receiver[ij] == ij:
            stack[nstack] = ij
            nstack += 1
            nstack = _find_stack(ij, donor, ndonor, nn, stack, nstack)


@numba.njit
def propagate_area(area, stack, receiver):
    for ijk in stack[-1::-1]:
        if receiver[ijk] != ijk:
            area[receiver[ijk]] += area[ijk]


@numba.njit
def compute_stream_power(erosion, elevation, stack, receiver, dist2receiver,
                         area, k, m, n, dt, tolerance, nn):
    for ij in range(nn):
        ijk = stack[ij]
        ijr = receiver[ijk]
        if ijr == ijk:
            continue

        factor = k * dt * area[ijk]**m / dist2receiver[ijk]**n
        elevation_0 = elevation[ijk]
        elevation_iter = elevation_0
        elevation_p = elevation_0

        while True:
            slope = elevation_iter - elevation[ijr]
            e_num = elevation_iter - elevation_0 + factor * (slope)**n
            e_den = 1. + factor * n * slope**(n-1)
            ers = e_num / e_den

            elevation_iter -= ers

            diff = elevation_iter - elevation_p
            elevation_p = elevation_iter
            if np.abs(diff) <= tolerance:
                break

        erosion[ijk] = elevation_0 - elevation_iter
