#!/usr/bin/env/ python3

"""
Lançamento de projéteis em duas dimensões usando o método de euler
"""
import time
import numpy as np
import matplotlib.pyplot as plt


M = float(input("Entre com a massa: "))
B = float(input("Entre com o arrasto: "))
DT = float(input("Entre com o diferencial de tempo: "))
SPEED = float(input("Entre com a velocidade inicial: "))


def launchwoar(G, DT, SPEED, THET, PSI):
    """Lançamento sem a resistência do ar"""
    # Variáveis
    velocity_x = SPEED * np.cos(PSI)*np.sin(THET)
    velocity_y = SPEED * np.sin(PSI)*np.sin(THET)
    velocity_z = SPEED * np.cos(PSI)

    # Cria as arrays necessárias
    x_axis = np.array([])
    y_axis = np.array([])
    z_axis = np.array([])
    vx_axis = np.array([])
    vy_axis = np.array([])
    vz_axis = np.array([])

    # Define o valor inicial
    vx_axis = np.append(vx_axis, velocity_x)
    vy_axis = np.append(vy_axis, velocity_y)
    vz_axis = np.append(vz_axis, velocity_z)
    x_axis = np.append(x_axis, 0)
    y_axis = np.append(y_axis, 0)
    z_axis = np.append(z_axis, 0)

    rev = 0

    while z_axis[rev] >= 0:
        x_axis = np.append(x_axis, x_axis[rev] + (vx_axis[rev] * DT))
        vx_axis = np.append(vx_axis, vx_axis[rev])

        y_axis = np.append(y_axis, y_axis[rev] + (vy_axis[rev] * DT))
        vy_axis = np.append(vy_axis, vy_axis[rev])

        z_axis = np.append(z_axis, z_axis[rev] + (vz_axis[rev] * DT))
        vz_axis = np.append(vz_axis, vz_axis[rev] - (G * DT))

        rev += 1
    return x_axis, y_axis, z_axis

def launchwog(G, M, B, DT, SPEED, THET, PSI):
    """Lançamento com a resistência do ar"""
    # Variáveis
    velocity_x = SPEED * np.cos(PSI)*np.sin(THET)
    velocity_y = SPEED * np.sin(PSI)*np.sin(THET)
    velocity_z = SPEED * np.cos(PSI)

    # Cria as arrays necessárias
    x_axis = np.array([])
    y_axis = np.array([])
    z_axis = np.array([])
    vx_axis = np.array([])
    vy_axis = np.array([])
    vz_axis = np.array([])

    # Define o valor inicial
    vx_axis = np.append(vx_axis, velocity_x)
    vy_axis = np.append(vy_axis, velocity_y)
    vz_axis = np.append(vz_axis, velocity_z)
    x_axis = np.append(x_axis, 0)
    y_axis = np.append(y_axis, 0)
    z_axis = np.append(z_axis, 0)

    rev = 0

    while z_axis[rev] >= 0:
        v = np.sqrt((vx_axis)**2 + (vy_axis)**2 + (vz_axis)**2)

        x_axis = np.append(x_axis, (x_axis[rev] + (vx_axis[rev] * DT)))
        vx_axis = np.append(vx_axis, (vx_axis[rev] - (B*vx_axis[rev]*vx_axis[rev])/M * DT))

        y_axis = np.append(y_axis, (y_axis[rev] + (vy_axis[rev] * DT)))
        vy_axis = np.append(vy_axis, (vy_axis[rev] - (B*vy_axis[rev]*vy_axis[rev])/M * DT))

        z_axis = np.append(z_axis, (z_axis[rev] + (vz_axis[rev] * DT)))
        vz_axis = np.append(vz_axis, (vz_axis[rev] - (G * DT)  - (B*vz_axis[rev]*vz_axis[rev])/M * DT))

        rev += 1
    return x_axis, y_axis, z_axis


def launch(M, B, DT, SPEED, THET, PSI):
    """Lançamento com a resistência do ar e campo gravitacional variável"""
    # Variáveis
    velocity_x = SPEED * np.cos(PSI)*np.sin(THET)
    velocity_y = SPEED * np.sin(PSI)*np.sin(THET)
    velocity_z = SPEED * np.cos(PSI)
    gravity = 9.81

    # Cria as arrays necessárias
    x_axis = np.array([])
    y_axis = np.array([])
    z_axis = np.array([])
    vx_axis = np.array([])
    vy_axis = np.array([])
    vz_axis = np.array([])

    # Define o valor inicial
    vx_axis = np.append(vx_axis, velocity_x)
    vy_axis = np.append(vy_axis, velocity_y)
    vz_axis = np.append(vz_axis, velocity_z)
    x_axis = np.append(x_axis, 0)
    y_axis = np.append(y_axis, 0)
    z_axis = np.append(z_axis, 0)

    rev = 0

    while z_axis[rev] >= 0:
        v = np.sqrt((vx_axis)**2 + (vy_axis)**2 + (vz_axis)**2)

        x_axis = np.append(x_axis, (x_axis[rev] + (vx_axis[rev] * DT)))
        vx_axis = np.append(vx_axis, (vx_axis[rev] - (B*vx_axis[rev]*vx_axis[rev])/M * DT))

        y_axis = np.append(y_axis, (y_axis[rev] + (vy_axis[rev] * DT)))
        vy_axis = np.append(vy_axis, (vy_axis[rev] - (B*vy_axis[rev]*vy_axis[rev])/M * DT))

        z_axis = np.append(z_axis, (z_axis[rev] + (vz_axis[rev] * DT)))
        vz_axis = np.append(vz_axis, (vz_axis[rev] - (gravity * DT)  - (B*vz_axis[rev]*vz_axis[rev])/M * DT))

        gravity = (3.98589196e14) / (6371000 + z_axis[rev])**2

        rev += 1
    return x_axis, y_axis, z_axis

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

i = 0
varp = np.linspace(-np.pi,np.pi,100)
vart = np.linspace(0,2*np.pi,100)
while i != 100:
    a, b, c = launch(M, B, DT, SPEED, np.pi, vart[i])
    ax.plot(a, b, c)
    fig.canvas.draw()
    plt.pause(0.05)
#    ax.clear()
    i += 1
    if i == 99:
        plt.pause(10)
