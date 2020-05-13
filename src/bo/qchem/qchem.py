from __future__ import division
from bo.bo_calculator import BO_calculator

class QChem(BO_calculator):
    """ Class for common parts of QChem program

        :param string basis_set: basis set information
        :param string memory: allocatable memory in the calculations
        :param string qm_path: path for QM path
        :param integer nthreads: number of threads in the calculations
        :param double version: version of Molpro program
    """
    def __init__(self, basis_set, memory, qm_path, nthreads, version):

        # Save name of BO calculator and its method
        super().__init__()

        # Initialize QC5.2 common variables
        self.basis_set = basis_set

        self.memory = memory
        self.qm_path = qm_path
        self.nthreads = nthreads
        self.version = version

        if (self.version != 5.2):
            raise ValueError (f"( {self.qm_prog}.{call_name()} ) Other version not implemented! {self.version}")
