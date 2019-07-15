# Instruction
# 1. Convert data by running 'main.py'

import json


def convert(items):
    '''
        Converts minerals.py into a format compatible to django's data pre-loading feature
        @ input - list of dictionary
        @ output - list of dictionary

        Example
        Input -
        [
            {
                "name": "Abelsonite",
                "image_filename": "Abelsonite.jpg",
                "image_caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
                "category": "Organic",
                "formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
                "strunz_classification": "10.CA.20",
                "crystal_system": "Triclinic",
                "unit_cell": "a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
                "color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
                "crystal_symmetry": "Space group: P1 or P1Point group: 1 or 1",
                "cleavage": "Probable on {111}",
                "mohs_scale_hardness": "2\u20133",
                "luster": "Adamantine, sub-metallic",
                "streak": "Pink",
                "diaphaneity": "Semitransparent",
                "optical_properties": "Biaxial",
                "group": "Organic Minerals"
            }
            ...
        ]

        Output -
        [
            {
                "model": "website.Mineral",
                "pk": 1,
                "fields": {
                    "name": "Abelsonite",
                    "image_filename": "Abelsonite.jpg",
                    "image_caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
                    "category": "Organic",
                    "formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
                    "strunz_classification": "10.CA.20",
                    "crystal_system": "Triclinic",
                    "unit_cell": "a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
                    "color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
                    "crystal_symmetry": "Space group: P1 or P1Point group: 1 or 1",
                    "cleavage": "Probable on {111}",
                    "mohs_scale_hardness": "2\u20133",
                    "luster": "Adamantine, sub-metallic",
                    "streak": "Pink",
                    "diaphaneity": "Semitransparent",
                    "optical_properties": "Biaxial",
                    "group": "Organic Minerals"
                }
            }
        ]
    '''
    output = []
    model = 'website.Mineral'

    # edge case - if empty, then return empty
    if not isinstance(items, list) or len(items) == 0:
        return output

    # for each item, convert it as outlined above
    for (index, item) in enumerate(items):
        temp = {
            "model": model,
            "pk": (index+1),
            "fields": item
        }

        # append item to a new list
        output.append(temp)

    # return output
    return output

if __name__ == '__main__':
    data = None

    # import and parse json file
    with open('minerals.json') as json_file:
        data = json.load(json_file)

    # convert data
    output = convert(data)

    # store list into json file
    with open('output.json', 'wb') as outfile:
        json.dump(output, outfile)
