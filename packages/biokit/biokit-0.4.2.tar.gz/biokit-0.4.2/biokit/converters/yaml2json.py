"""Convert :term:`YAML` to :term`JSON` format"""
import yaml, json
from biokit.converters.convbase import ConvBase

__all__ = ["YAML2JSON"]


class YAML2JSON(ConvBase):
    """Convert :term:`YAML` file into :term:`JSON` file

    Conversion is based on yaml and json standard Python modules

    .. note:: YAML comments will be lost in JSON output


    """
    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input YAML file. 
        :param str outfile: input JSON file
        """
        super(YAML2JSON, self).__init__(infile, outfile, *args, **kargs)

    def get_json(self):
        """Return the JSON dictionary corresponding to the YAML input"""
        data = yaml.load(open(self.infile, "r"))
        return json.dumps(data, sort_keys=True, indent=4)

    def convert(self):
        with open(self.outfile, "w") as outfile:
            outfile.write(self.get_json())

