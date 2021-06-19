from rpy2.robjects import r
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import ListVector
import numpy as np


def fpca(id_, tp_, y_):

    print len(id_)
    print len(tp_) 
    
    n = len(id_)
    x = np.array(range(1,n+1))
    t = len(tp_)
    id_= np.repeat(x,t)
    print len(id_)
    rid = robjects.FloatVector(id_)

    tp = np.tile(tp_,n)
    print len(tp)
    rtp = robjects.FloatVector(tp)
    print len(y_)
    ry = robjects.FloatVector(y_)


    base = importr('fdapace')

    rMakeFPCAInputs = r['MakeFPCAInputs']
    expr = rMakeFPCAInputs(rid,rtp,ry)
    Lt = expr.rx2('Lt')
    Ly = expr.rx2('Ly')
    rfpca = r['FPCA']
    FPCAdense = rfpca(Ly,Lt)
    
    return FPCAdense.rx2("phi")