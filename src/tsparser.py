from typing import Any, Dict, List, Tuple


def parse(path: str) -> Dict:
    """Parses any file from http://www.math.uwaterloo.ca/tsp/world/countries.html.

    The files are in a format where there are two sections. The first section has
    metadata about the country, including the name, number of cities and comments.
    The second section  has the points. If the type is EUC_2D (Euclidian Projection)
    it means that the points aren't latitudinal or longitudinal, they are already
    projected in a 2D surface, and the distance between any two points is equal to
    the euclidian distance.

    Parameters
    ----------
    path : str
        Path to the file to be parsed

    Returns
    -------
    Dict
        A dictionary containing the metadata as pairs key / value, and the point
        list in the key "point_list". The points are a tuple of three values, the
        id of the point, and the coordinates X and Y.
    """
    content: str

    with open(path, "rt") as f:
        content = f.read()

    # This phrase separates the two sections
    metadata, points = content.split("NODE_COORD_SECTION")

    problem = {}
    for field in metadata.strip().split("\n"):  # Strip to erase trailling spaces
        name, value = field.split(":")
        problem[name.lower().strip()] = value.strip()

    problem["point_list"] = []
    for point in points.strip().split("\n"):
        i, x, y = point.split(" ")
        problem["point_list"].append((int(i), float(x), float(y)))
    return problem
