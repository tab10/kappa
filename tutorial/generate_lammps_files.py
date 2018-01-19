"""

@author: Alex Kerr
"""

import numpy as np
import kappa

amber = kappa.Amber(angles=True, lengths=True, dihs=False, imptors=False, lj=False)

# create stubby cnt
cnt = kappa.build(amber, "cnt", radius=1, length=10)

#kappa.plot.bonds(cnt, indices=True)
kappa.plot.faces(cnt)
indices = [2, 57]

for i in range(1,41):
    
    # generate polyethylene of lunit length
    teflon = kappa.build(amber, "teflon", count=i)
    func_cnt = kappa.attach(cnt, [teflon]*2, indices)
    type_list = np.ones(len(func_cnt.posList))  # ones are non-interface atoms
    for j in range(len(cnt.posList)):
       for k in range(len(func_cnt.posList)):
           if j <= k:
               temp_chk = (cnt.posList[j] == func_cnt.posList[k])
               if np.all(temp_chk, axis=0):
                   type_list[k] = 1     # part of CNT
               else:
                   type_list[k] = 2     # part of ends
    # counter = 0
    # for face in cnt.faces:
    #     if counter == 0:
    #         type_list[face.atoms[0]] = 2  # interface 1
    #         type_list[face.atoms[1]] = 2  # interface 1
    #         type_list[face.atoms[2]] = 2  # interface 1
    #         type_list[face.atoms[3]] = 2  # interface 1
    #         type_list[face.atoms[4]] = 2  # interface 1
    #         type_list[face.atoms[5]] = 2  # interface 1
    #     elif counter == 1:
    #         type_list[face.atoms[0]] = 3  # interface 2
    #         type_list[face.atoms[1]] = 3  # interface 2
    #         type_list[face.atoms[2]] = 3  # interface 2
    #         type_list[face.atoms[3]] = 3  # interface 2
    #         type_list[face.atoms[4]] = 3  # interface 2
    #         type_list[face.atoms[5]] = 3  # interface 2
    #     counter += 1


    kappa.pdb(func_cnt, fn='cnt{}.pdb'.format(i))
    kappa.lammps(func_cnt, fn='cnt{}.lammps'.format(i), type_list=type_list)
