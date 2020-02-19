from pgkb_hap_parser.parser import *

HAPLOTYPE_TABLE_DIR = path.join(path.dirname(__file__), '..', "definition", "xlsx")

GENE_ROW = 0
GENE_COL = 0

def test_parse_gene():
    files = filter(lambda f: f.endswith('.xlsx'), listdir(HAPLOTYPE_TABLE_DIR))
    files = sorted(files) # sorted str not int -> {0: CYP2C19, 1: CYP2C9}
    gene = []
    for file in files:
        definition_file = path.join(HAPLOTYPE_TABLE_DIR, file)
        definition_table = pd.read_excel(definition_file, header=None)
        
        gene.append(parse_gene(definition_table.iloc[GENE_ROW][GENE_COL]))
    actual = gene
    expect = ['CACNA1S', 'CFTR', 'CYP2B6', 'CYP2C19', 'CYP2C9', 'CYP3A5', 'CYP4F2', 'DPYD', 'G6PD', 'IFNL3', 'NUDT15', 'RYR1', 'SLCO1B1', 'TPMT', 'UGT1A1', 'VKORC1']
    assert actual == expect

def test_parse_chrome():
    files = filter(lambda f: f.endswith('.xlsx'), listdir(HAPLOTYPE_TABLE_DIR))
    files = sorted(files) # sorted str not int -> {0: CYP2C19, 1: CYP2C9}
    chrom = []
    for file in files:
        print(file)
        definition_file = path.join(HAPLOTYPE_TABLE_DIR, file)
        definition_table = pd.read_excel(definition_file, header=None)

        gene = parse_gene(definition_table.iloc[GENE_ROW][GENE_COL])

        if gene == 'G6PD':
            global CHROM_COL, VARIANT_COL, RSID_COL
            CHROM_COL = 1
            VARIANT_COL = 2
            RSID_COL = 2

        chrom.append(parse_chrom(definition_table.iloc[CHROM_ROW][CHROM_COL]))

        CHROM_COL = 0
        VARIANT_COL = 1
        RSID_COL = 1
    actual = chrom
    expect = ['chr1', 'chr7', 'chr19', 'chr10', 'chr10', 'chr7', 'chr19', 'chr1', 'chrX', 'chr19', 'chr13', 'chr19', 'chr12', 'chr6', 'chr2', 'chr16']
    assert actual == expect

# def test_parse_variants():


# def test_parse_rsid():


# def parse_alleles():

