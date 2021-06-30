
from grapher_new import *


if __name__ == '__main__':
	draw_parametric('r = 400*cos(t)', 'theta = tan(t)-t', plane_size=(1000,1000), continuity=0.0001)
