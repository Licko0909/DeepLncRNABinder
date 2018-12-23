# DeepLncRNABinder
Prediction of Genome-wide binding of long noncoding RNAs using Deep Learning


Requirements
  - python > 3.0 (anaconda package)
  - Keras
  - Tensorflow


# Convert fasta files to one hot encoding. This will save one hot encoded matrices in <name>.h5 file
python fasta2OneHotEncoding.py <postrain.fa> <negtrain.fa> <postest.fa> <negtest.fa> <name>

# To run smallCNN Models (the best model in the paper)
python run_smallCNN.py <name>.h5 <name>

# Test example
Example Four fasta files are given

GSE31332_terc_peaks.pos.train.fa
GSE31332_terc_peaks.neg.train.fa
GSE31332_terc_peaks.pos.test.fa
GSE31332_terc_peaks.neg.test.fa

# For this example, convert to one hot encoding 
python fasta2OneHotEncoding.py GSE31332_terc_peaks.pos.train.fa GSE31332_terc_peaks.neg.train.fa GSE31332_terc_peaks.pos.test.fa GSE31332_terc_peaks.neg.test.fa TERC
# This will create TERC.h5 file
# To run smallCNN Models (the best model in the paper). This might take a while
python run_smallCNN.py TERC.h5 TERC

How to change learning rate of the optimization algorithm
  - Go to line no. 35 in 'Models.py' to change learning rate

