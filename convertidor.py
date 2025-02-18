import pypandoc

def convert_docx_to_pdf(docx_path, pdf_path):
    pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)

# Uso de la función
convert_docx_to_pdf("Hoja de vida jorge luis final cst.docx", "Hoja_de_vida_jorge_luis.pdf")

