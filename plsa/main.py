
from pprocess import Pprocess as PP
from plsa import pLSA
import numpy as np
import logging
import time


def main():
  # Setup logging -------------------------
  logging.basicConfig(filename='plsa2.log', level=logging.INFO)
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  logging.getLogger('').addHandler(console)

  # Some basic configuration ---------------
  fname = './Collection.txt'
  fsw = './stopwords.txt'
  eps = 1000.0


  # Preprocess ------------------------plsa1-----
  pp = PP(fname, fsw)
  t_d = pp.get_t_d()

  V,D = t_d.shape
  logging.info("V = %d  D = %d" %(V,D))
  key_word_size = V

  # Train model and get result -------------
  pmodel = pLSA()
  # for z in range(3,(D+1), 10):
  z = 3
  t1 = time.clock()
  (l, p_d_z, p_w_z, p_z)  = pmodel.train(t_d, z, eps)
  t2 = time.clock()
  logging.info('z = %d eps = %f time = %f' %(z, l, t2-t1))
  for itz in range(z):
    logging.info('Topic %d' %itz)
    data = [(p_w_z[i][itz], i)  for i in range(len(p_w_z[:,itz])) ]
    data.sort(key=lambda tup:tup[0], reverse=True)
    for i in range(key_word_size):
      logging.info('%s : %.6f ' %(pp.get_word(data[i][1]), data[i][0] ))

if __name__ == '__main__':
  main()
