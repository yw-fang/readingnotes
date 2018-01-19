from aiida import load_dbenv
load_dbenv()

from aiida.orm import Code, DataFactory, load_node
StructureData = DataFactory('structure')
ParameterData = DataFactory('parameter')

import numpy as np
import os

codename = 'phono3py@boston-lab'
code = Code.get_from_string(codename)

###############
# Nitrogen structure
a = 5.7906907399999996
cell = [[a, 0, 0],
        [0, a, 0],
        [0, 0, a]]
symbols=['N'] * 8
scaled_positions = [(0.5554032500000000,  0.5554032500000000,  0.5554032500000000),
                    (0.9445967500000000,  0.4445967500000000,  0.0554032500000000),
                    (0.0554032500000000,  0.9445967500000000,  0.4445967500000000),
                    (0.4445967500000000,  0.0554032500000000,  0.9445967500000000),
                    (0.4445967500000000,  0.4445967500000000,  0.4445967500000000),
                    (0.0554032500000000,  0.5554032500000000,  0.9445967500000000),
                    (0.9445967500000000,  0.0554032500000000,  0.5554032500000000),
                    (0.5554032500000000,  0.9445967500000000,  0.0554032500000000)]

##############

structure = StructureData(cell=cell)
positions = np.dot(scaled_positions, cell)

for i, scaled_position in enumerate(scaled_positions):
    structure.append_atom(position=np.dot(scaled_position, cell).tolist(),
                          symbols=symbols[i])


# Machine
machine_dict = {'resources': {'num_machines': 1,
                              'parallel_env': 'mpi*',
                              'tot_num_mpiprocs': 16},
                'max_wallclock_seconds': 3600 * 10,
                }


# PHONOPY settings
parameters = ParameterData(dict={'supercell': [[2, 0, 0],
                                                [0, 2, 0],
                                                [0, 0, 2]],
                                  'primitive': [[0.0, 1.0, 1.0],
                                                [1.0, 0.0, 1.0],
                                                [1.0, 1.0, 0.0]],
                                  'distance': 0.01,
                                  'mesh': [20, 20, 20],
                                  'symmetry_precision': 1e-5,
                                  })

calc = code.new_calc(max_wallclock_seconds=3600,
                     resources={"num_machines": 1,
                                "parallel_env":"mpi*",
                                "tot_num_mpiprocs": 6})


calc.label = "test phono3py calculation"
calc.description = "A much longer description"

calc.use_structure(structure)
calc.use_code(code)
calc.use_parameters(parameters)

# Chose to use forces or force constants
if True:
    calc.use_data_sets(load_node(47616))  # This node should contain a ForceSetsData object
else:
    calc.use_force_constants(load_node(62098))
    calc.use_force_constants_3(load_node(62097))

if False:
    subfolder, script_filename = calc.submit_test()
    print "Test_submit for calculation (uuid='{}')".format(calc.uuid)
    print "Submit file in {}".format(os.path.join(
        os.path.relpath(subfolder.abspath),
        script_filename))
else:
    calc.store_all()
    print "created calculation with PK={}".format(calc.pk)
    calc.submit()
