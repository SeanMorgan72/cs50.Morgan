from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, new_x="LMARGIN", new_y="NEXT", align="C")

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add shirt image
    pdf.image("shirtificate/shirtificate.png", x=0, y=60, w=210)

    # Add user's name
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 200, name, 0, new_x="LMARGIN", new_y="NEXT", align="C")

    # Output the PDF
    pdf.output("shirtificate/shirtificate.pdf")

def main():
    name = input("Enter your name: ")
    create_shirtificate(name)

if __name__ == "__main__":
    main()
