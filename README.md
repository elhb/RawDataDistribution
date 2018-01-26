# RawDataDistribution
Small script to quickly plot the spatial distribution of raw data from fastq files.

## To install:
```
pip install -r requirements.txt
python setup.py build
python setup.py install
```

## To Run:
```
plotRawDataDistribution.py \
--barcode-file LP_Lot_number_x.txt \
--reads-file R1.fastq.gz \
--img-file raw_data_dist.pdf
```

# To get help:
```
$ plotRawDataDistribution.py --help
usage: plotRawDataDistribution.py [-h] -r <file> -b <file> -i <file>
                                  [-s <int>] [-p <int>] [-c <str>] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -r <file>, --reads-file <file>
                        barcode reads file/fwd read/first read/read one (must
                        be gzipped fastq format)
  -b <file>, --barcode-file <file>
                        ID file with barcodes and positions
  -i <file>, --img-file <file>
                        file name for the output image (pdf)
  -s <int>, --stop-after <int>
                        stop after this many reads
  -p <int>, --plot-every <int>
                        print plot to pdf after this many reads
  -c <str>, --color-map <str>
                        choose colormap for the plot ("red" or "heat", red is
                        default)
  -v, --verbose         print more stuff to stderr
```