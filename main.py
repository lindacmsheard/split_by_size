from lib.gen.gen1 import split_pdf_by_size
import os

input_pdf = "data/inputsample/sample.pdf"
mb=1048576

os.makdirs("data/output", exist_ok=True)
split_pdf_by_size(input_pdf, 0.1*mb , "data/output" )