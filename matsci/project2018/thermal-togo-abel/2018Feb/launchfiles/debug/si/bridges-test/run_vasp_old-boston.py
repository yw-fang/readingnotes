import click
import numpy


@click.command()
@click.option('--paw-family', type=str, default='vasp-test')
@click.option('--import-from', type=click.Path(), default='.')
@click.option('--queue', type=str, default='')
@click.argument('code', type=str)
@click.argument('computer', type=str)
def test_vasp(paw_family, import_from, queue, code, computer):
    load_dbenv_if_not_loaded()
    from aiida.orm import CalculationFactory, Code
    if import_from:
        import_paws(import_from, paw_family)
  #  try:
    paw_si = get_paws(paw_family)
   # except ValueError as err:
   #     click.echo(err.msg, err=True)
   #     raise ValueError(
   #         'give a valid family or import a new one (run with --help)')

    vasp_calc = CalculationFactory('vasp.vasp')()
    vasp_calc.use_structure(create_structure2())
    vasp_calc.use_kpoints(create_kpoints())
    vasp_calc.use_parameters(create_params())
    code = Code.get_from_string('{}@{}'.format(code, computer))
    vasp_calc.use_code(code)
    # vasp_calc.use_paw(paw_in, 'In')
    # vasp_calc.use_paw(paw_as, 'As')
    vasp_calc.use_paw(paw_si, 'Si')
    vasp_calc.set_computer(code.get_computer())
    vasp_calc.set_queue_name(queue)
    vasp_calc.set_resources({
        'num_machines': 1,
#        'parallel_env': 'mpi*',
        'tot_num_mpiprocs': 28
    })
    vasp_calc.label = 'Test VASP run'
    vasp_calc.store_all()
    vasp_calc.submit()
    vasp_calc = CalculationFactory('vasp.vasp')

    #from aiida_vasp.parsers.pymatgen_vasp import PymatgenParser
    #vasp_calc.set_parser_cls(PymatgenParser)
    #vasp_calc.use_settings(DataFactory('parameter')(dict={
    #        'pymatgen_parser': {
    #            'exception_on_bad_xml': False,
    #            'parse_dos': False
    #        }
    #    }
    #))




def load_dbenv_if_not_loaded():
    from aiida import load_dbenv, is_dbenv_loaded
    if not is_dbenv_loaded():
        load_dbenv()


def get_data_cls(descriptor):
    load_dbenv_if_not_loaded()
    from aiida.orm import DataFactory
    return DataFactory(descriptor)


def create_structure():
    structure_cls = get_data_cls('structure')
    structure = structure_cls(
        cell=numpy.array([[0, .5, .5], [.5, 0, .5], [.5, .5, 0]]) * 6.058, )
    structure.append_atom(position=(0, 0, 0), symbols='In')
    structure.append_atom(position=(0.25, 0.25, 0.25), symbols='As')
    return structure

def create_structure2():
	import numpy as np
	from aiida.orm import DataFactory
	StructureData = DataFactory('structure')

	a = 5.404
	cell = [[a, 0, 0],
	        [0, a, 0],
	        [0, 0, a]]
	
	symbols=['Si'] * 8
	scaled_positions = [(0.875,  0.875,  0.875),
	                    (0.875,  0.375,  0.375),
	                    (0.375,  0.875,  0.375),
	                    (0.375,  0.375,  0.875),
	                    (0.125,  0.125,  0.125),
	                    (0.125,  0.625,  0.625),
	                    (0.625,  0.125,  0.625),
	                    (0.625,  0.625,  0.125)]
	
	structure = StructureData(cell=cell)
	positions = np.dot(scaled_positions, cell)

	for i, scaled_position in enumerate(scaled_positions):
	    structure.append_atom(position=np.dot(scaled_position, cell).tolist(),
	                          symbols=symbols[i])
	return structure
	

def create_kpoints():
    kpoints_cls = get_data_cls('array.kpoints')
    return kpoints_cls(kpoints_mesh=[8, 8, 8])


def create_params():
    param_cls = get_data_cls('parameter')
    return param_cls(dict={
        'SYSTEM': 'InAs',
        'EDIFF': 1e-5,
        'ISMEAR': 0,
        'SIGMA': 0.05,
        'ENCUT': '280.00 eV',
        'LEPSILON': '.TRUE.'
    })


def import_paws(folder_path, family_name):
    load_dbenv_if_not_loaded()
    from aiida.orm import DataFactory
    paw_cls = DataFactory('vasp.paw')
    paw_cls.import_family(
        folder_path, familyname=family_name, family_desc='Test family')


def get_paws(family_name):
    load_dbenv_if_not_loaded()
    from aiida.orm import DataFactory
    paw_cls = DataFactory('vasp.paw')
    #paw_in = paw_cls.load_paw(family=family_name, symbol='In')[0]
    #paw_as = paw_cls.load_paw(family=family_name, symbol='As')[0]
    paw_si = paw_cls.load_paw(family=family_name, symbol='Si')[0]

    return paw_si


if __name__ == '__main__':
    test_vasp()
