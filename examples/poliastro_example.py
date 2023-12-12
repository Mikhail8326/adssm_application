from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
import matplotlib.pyplot as plt
from poliastro.plotting.static import StaticOrbitPlotter as SPlotter

r = [-6045, -3490, 2500] << u.km
v = [-3.457, 6.618, 2.533] << u.km / u.s

orb = Orbit.from_vectors(Earth, r, v)
orbPlot = SPlotter()
orbPlot.plot(orb)
plt.show()

