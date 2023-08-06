from sequana import fastq, sequana_data, FastQ
from easydev import TempFile
import os
from numpy import mean

datagz = sequana_data("test.fastq.gz", "testing")
data = sequana_data("test.fastq", "testing")


def test_fastq_unzipped():

    for thisdata in [data, datagz]:
        # isntanciation
        f = fastq.FastQ(thisdata)
        assert f.data_format == "Illumina_1.8+"
        # count lines
        # rune it twice because we want to make sure re-running count_lines
        # (decompression with zlib) works when run again.
        assert f.count_lines() == 1000
        assert f.count_lines() == 1000
        assert f.count_reads() == 250
        assert f.count_reads() == 250

        # extract head of the file into an unzipped file
        ft = TempFile()
        f.extract_head(100, ft.name)
        fcheck = fastq.FastQ(ft.name)
        assert fcheck.count_lines() == 100
        ft.delete()

        # extract head of the file and zip output
        ft = TempFile(suffix=".gz")
        f.extract_head(100, ft.name)
        fcheck = fastq.FastQ(ft.name)
        assert fcheck.count_lines() == 100
        ft.delete()

        with FastQ(thisdata) as ff:
            assert len(ff) == 250

        with TempFile() as fh:
            selection = f.select_random_reads(10, fh.name)
            f.select_random_reads(selection, fh.name)




def test_split():
    # general tests
    f = fastq.FastQ(data)
    try:
        f.split_lines(250) # not a multiple of 4
        assert False
    except:
        assert True

    #
    outputs = f.split_lines(500)
    assert len(outputs) == 2
    remove_files(outputs)
    outputs = f.split_lines(256)
    assert len(outputs) == 4
    remove_files(outputs)

    # Now tests the zip/unzip cases
    f = fastq.FastQ(data)
    outputs = f.split_lines(500, gzip=False)
    remove_files(outputs)
    outputs = f.split_lines(500, gzip=True)
    remove_files(outputs)

    f = fastq.FastQ(datagz)
    outputs = f.split_lines(500, gzip=False)
    remove_files(outputs)
    outputs = f.split_lines(500, gzip=True)
    remove_files(outputs)


def test_filter():
    f = fastq.FastQ(data)
    # keeps all

    with TempFile() as fh:
        f.filter(min_bp=80, max_bp=120, output_filename=fh.name,
            progressbar=False)
        assert len(f) == 250
        ff = FastQ(fh.name)
        assert len(ff) == 250


    # keeps nothing
    with TempFile() as fh:
        f.filter(min_bp=80, max_bp=90, output_filename=fh.name)
        assert len(f) == 250
        ff = FastQ(fh.name)
        assert len(ff) == 0

def remove_files(filenames):
    for filename in filenames:
        os.remove(filename)


def test_identifiers():
    f = fastq.FastQ(data)
    identifier = fastq.Identifier(f.next()["identifier"])
    assert identifier.version == 'Illumina_1.8+'

    identifier = fastq.Identifier(f.next()["identifier"], "Illumina_1.8+")
    assert identifier.version == 'Illumina_1.8+'


    identifier = fastq.Identifier("@prefix:1_13_573/1")
    assert identifier.version == "unknown"


    identifier = fastq.Identifier("@SEQ:1:1101:9010:3891#0/1")
    identifier = fastq.Identifier("@SEQ:1:1101:9010:3891#0/1", version="Illumina_1.4+")

    print(identifier)
    identifier.__repr__()


def test_fastqc():
    qc = fastq.FastQC(data, dotile=True)
    qc.boxplot_quality()
    qc.histogram_gc_content()
    GC = mean(qc.gc_list)
    assert GC>0 and GC<100
    qc.imshow_qualities()
    qc.histogram_sequence_lengths()
    qc.histogram_sequence_coordinates()
    qc.plot_acgt_content()

    stats = qc.get_stats()
    assert stats['A'][0] == 6952
    assert stats['T'][0] == 6400
    assert stats['C'][0] == 6129
    assert stats['G'][0] == 5768


