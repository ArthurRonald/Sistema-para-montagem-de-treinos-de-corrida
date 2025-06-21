import streamlit as st
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Times", "B", 25)
pdf.cell(0, 10, txt="MZRun", ln= True, align="C")

pdf.output("teste.pdf")

