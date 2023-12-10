import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

Lx = 200  # total width of the pool
Nx = 160   # amount of points in the x direction
Ly = 200  # total height of the pool
Ny = 160   # amount of points in the y direction

# Calculate the spacing between points in x and y directions
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

dt = 0.025  # the amount of time that will pass after every iteration
Nt = 700    # amount of iterations

c = 2

# defines a 2-dimensional array that corresponds to the value of u at every point in the mesh
u = numpy.zeros([Nt, Nx, Ny])

u[0, Nx // 2, Ny // 2] = numpy.sin(0)   # disturbance at t = 0
u[1, Nx // 2, Ny // 2] = numpy.sin(1 / 10)  # disturbance at t = 1

# iterating through time and plugging all the values into discretized equations
for t in range(1, Nt - 1):
    print(t / Nt)
    for x in range(1, Nx - 1):
        for y in range(1, Ny - 1):
            if t < 100:
                u[t, Nx // 2, Ny // 2] = numpy.sin(t / 10)

            u[t + 1, x, y] = (
                c ** 2 * dt ** 2
                * (
                    ((u[t, x + 1, y] - 2 * u[t, x, y] + u[t, x - 1, y]) / (dx ** 2))
                    + ((u[t, x, y + 1] - 2 * u[t, x, y] + u[t, x, y - 1]) / (dy ** 2))
                )
                + 2 * u[t, x, y] - u[t - 1, x, y]
            )

# plotting all the calculated values
fig = pyplot.figure()
ax = fig.add_subplot(111, projection="3d")
X, Y = numpy.meshgrid(numpy.linspace(0, Lx, Nx), numpy.linspace(0, Ly, Ny))
for t in range(0, Nt):
    surf = ax.plot_surface(
        X, Y, u[t], color="b", shade=True, linewidth=0, antialiased=False
    )

    ax.view_init(elev=45)
    ax.set_zlim(-0.0001, 2.4)
    pyplot.axis("off")

    pyplot.pause(0.0001)
    pyplot.cla()

pyplot.show()
