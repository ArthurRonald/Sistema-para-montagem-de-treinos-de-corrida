import streamlit as st
from fpdf import FPDF

# Criar o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", "B", 25)
pdf.cell(0, 10, txt="MZRun", ln=True, align="C")

# Salvar PDF
pdf.output("pdf_de_treino.pdf")

# Exibir botão de download
with open("pdf_de_treino.pdf", "rb") as f:
    st.download_button("Baixar PDF", f, file_name="pdf de treino.pdf")