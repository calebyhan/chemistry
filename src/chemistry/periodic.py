import json
from pathlib import Path

def name(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic name.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["name"]
    elif type(ele) is str:
        data = json.load(open('periodic.json'))
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["name"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def number(ele):
    """
    Inputs atomic symbol to fetch atomic number.
    """

    if type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["atomicNumber"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic symbol.")

def symbol(ele):
    """
    Inputs an atomic number to fetch atomic symbol.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["atomicNumber"].lower() == ele.lower():
                return i["symbol"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number.")

def mass(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic mass.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["mass"][:-3]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["atomicMass"][:-3]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def elecConfig(ele):
    """
    Inputs either an atomic number or symbol to fetch electronic configuration.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["electronicConfiguration"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["electronicConfiguration"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def position(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic position (period, group).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return (data[ele - 1]["period"], data[ele - 1]["group"])
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return (i["period"], i["group"])
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def elecNeg(ele):
    """
    Inputs either an atomic number or symbol to fetch electron negativity.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["electronegativity"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["electronegativity"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def atomRadius(ele):
    """
    Inputs either an atomic number or symbol to fetch atomic radius (pm).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["atomicRadius"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["atomicRadius"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def ionRadius(ele):
    """
    Inputs either an atomic number or symbol to fetch ion radius (pm).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["ionRadius"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["ionRadius"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def standardState(ele):
    """
    Inputs either an atomic number or symbol to fetch state of matter at STP.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["standardState"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["standardState"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def ionEnergy(ele):
    """
    Inputs either an atomic number or symbol to fetch ionization energy (kJ/mol).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["ionizationEnergy"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["ionizationEnergy"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def elecAffinity(ele):
    """
    Inputs either an atomic number or symbol to fetch electron affinity (kJ/mol).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["electronAffinity"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["electronAffinity"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def meltingPoint(ele):
    """
    Inputs either an atomic number or symbol to fetch melting point (K).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["meltingPoint"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["meltingPoint"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def boilingPoint(ele):
    """
    Inputs either an atomic number or symbol to fetch boiling point (K).
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["boilingPoint"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["boilingPoint"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")

def block(ele):
    """
    Inputs either an atomic number or symbol to fetch the block.
    """

    if type(ele) is int:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        return data[ele - 1]["block"]
    elif type(ele) is str:
        folder = Path(__file__).parent
        with (folder / 'periodic.json').open('r') as f:
            data = json.load(f)
        for i in data:
            if i["symbol"].lower() == ele.lower():
                return i["block"]
        raise Exception("Inputted value is not an atomic number or symbol.")
    else:
        raise Exception("Inputted value is not an atomic number or symbol.")