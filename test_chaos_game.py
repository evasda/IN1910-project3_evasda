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

@nt.raises(ValueError)
def test_savepng():
	T = ChaosGame(5, 0.5)
	T.iterate(50)
	T.savepng("outfile.pic")
	
def test_starting_point():
	""" Test that _starting_point returns array. """
	T = ChaosGame(5, 0.5)
	s = T._starting_point()
	nt.assert_equal(type(s), np.ndarray)

def test_generate_ngon():
	""" Test that _generate_ngon returns list. """
	T = ChaosGame(5, 0.5)
	s = T._generate_ngon(5)
	nt.assert_equal(type(s), list)

if __name__ == '__main__':
	import nose
	nose.run()