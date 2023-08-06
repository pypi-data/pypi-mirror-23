"""Convert :term:`BAM` format to :term:`BED` formats"""
from biokit.converters.convbase import ConvBase

__all__ = ["Bam2Bed"]


class Bam2Bed(ConvBase):
    """Convert sorted :term:`BAM` file into :term:`BED` file

    ::

        samtools depth -aa INPUT > OUTPUT


    """
    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input BAM file. **It must be sorted**.
        :param str outfile: input BED file
        """
        super(Bam2Bed, self).__init__(infile, outfile, *args, **kargs)

    def convert(self):
        cmd = "samtools depth -aa {} > {}".format(self.infile, self.outfile)
        self.execute(cmd)



