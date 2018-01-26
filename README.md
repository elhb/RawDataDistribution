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