#gerar_pdf_treino.py
from fpdf import FPDF
import os

class PDFTreino(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Plano de Treinamento Personalizado", 0, 1, "C")

    def add_plano(self, texto):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, texto)

def gerar_pdf(texto_treino, nome_arquivo="treino_personalizado.pdf"):
    if not os.path.exists("pdfs"):
        os.makedirs("pdfs")

    pdf = PDFTreino()
    pdf.add_page()
    pdf.add_plano(texto_treino)
    caminho = f"pdfs/{nome_arquivo}"
    pdf.output(caminho)
    return caminho
