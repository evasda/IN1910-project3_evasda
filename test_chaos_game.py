from chaos_game import ChaosGame
import numpy as np
import nose.tools as nt
np.random.seed(2345)

@nt.raises(ValueError)
def test__init__n():
	ChaosGame(2, 0.5)
	ChaosGame(3.5, 0.5)
	

@nt.raises(ValueError)
def test__init__():
	ChaosGame(5, 1.1)
	ChaosGame(4, 1)

# Need at least 4 unit tests here:	
def test_starting_point(self):
	something



if __name__ == '__main__':
	import nose
	nose.run()