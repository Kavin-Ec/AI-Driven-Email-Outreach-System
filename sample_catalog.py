from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 10, txt="Sample Product Catalog", ln=True, align='C')

# Line break
pdf.ln(10)

# Table headers
pdf.set_font("Arial", size=12)
pdf.cell(40, 10, txt="SKU", border=1, align='C')
pdf.cell(80, 10, txt="Product Name", border=1, align='C')
pdf.cell(50, 10, txt="Description", border=1, align='C')
pdf.cell(20, 10, txt="Price", border=1, align='C')
pdf.ln()

# Table rows
products = [
    ("SKU001", "Widget A", "A high-quality widget", "$10.00"),
    ("SKU002", "Widget B", "Another great widget", "$15.00"),
    ("SKU003", "Gadget C", "A useful gadget", "$20.00"),
    ("SKU004", "Gadget D", "Another useful gadget", "$25.00")
]

for sku, name, description, price in products:
    pdf.cell(40, 10, txt=sku, border=1)
    pdf.cell(80, 10, txt=name, border=1)
    pdf.cell(50, 10, txt=description, border=1)
    pdf.cell(20, 10, txt=price, border=1)
    pdf.ln()

# Save the PDF
pdf_output_path = "sample_product_catalog.pdf"
pdf.output(pdf_output_path)

print(f"PDF generated and saved as {pdf_output_path}")
