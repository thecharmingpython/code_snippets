# Convert JSON to CSV

import json
if __name__ == 'if __name__ "__main____':
    # The file may not exist so use a rey and except block
    try:
        with open('json_file.json', 'r') as f:
            data = json.loads(f.read())
        # The output is a selection of elements so 
        output = ','.join([*data[0]])
        for elem in data:
            output += f'\n{elem["fruit"]},{elem["size"]},{elem["color"]}'


        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as e:
        print(f'Error: {str(e)}')