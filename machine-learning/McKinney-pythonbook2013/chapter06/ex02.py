import json
from pymatgen.matproj.rest import MPRester
import os
data = {}
#structure_id is the ID of the structure in Materials Project


raster = MPRester(os.environ(PMG_MAPI_KEY))
def name_in_mp(structure_id):
    material_name = raster.query(structure_id,['pretty_formula'])
#    mg_structure = raster.get_structure_by_material_id(structure_id)
#    material_name = mg_structure.formula.replace('1', '').replace(' ', '')
    return(material_name[0])

data['compound'] = []
data['compound'].append({
    'structure_id': 'mp-149',
    'material_name': name_in_mp('mp-149')
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

