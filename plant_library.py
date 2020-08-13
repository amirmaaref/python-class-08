valid_types = (
    'flower',
    'tree',
    'F',
    'T',
    'f',
    't'
)

ENTER_PLANT_TYPE_MESSAGE = '''Hello,
Enter Plant type:
Valid types (flower,F / tree,T): '''
plant_type = ''

def set_plant_type(input_plant_type):
    global plant_type
    if input_plant_type not in valid_types:
        raise ValueError('Wrong Plant type, valid params: (flower,F / tree,T), try again')
    if input_plant_type == 'flower' or input_plant_type.upper() == 'F':
        plant_type = 'flower'
    elif input_plant_type == 'tree' or input_plant_type.upper() == 'T':
        plant_type = 'tree'