import random

def children():
	boys=0
	while random.random() < 0.5:
		boys=boys+1
	return (boys,1)


t_boys = 0
t_girls = 0
for ii in range(1000000):
	i_boys, i_girls = children()
	t_boys  = t_boys + i_boys
	t_girls = t_girls + i_girls
	if (ii % 1000) == 0:
		print ii, i_boys, i_girls, t_boys, t_girls, 100.0*t_girls/(t_girls+t_boys)
