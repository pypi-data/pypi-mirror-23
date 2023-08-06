from isatools import isatab, magetab
import logging
import isatools

logging.basicConfig(level=isatools.log_level)
LOG = logging.getLogger(__name__)


def convert(source_inv_fp, output_path):
    """ Converter for ISA-Tab to MAGE-TAB.
    :param source_inv_fp: File descriptor of input investigation file
    :param output_dir: Path to directory to write output MAGE-TAB files to
    """
    LOG.info("loading isatab %s", source_inv_fp.name)
    ISA = isatab.load(source_inv_fp)
    LOG.info("dumping magetab %s", output_path)
    magetab.dump(ISA, output_path)
