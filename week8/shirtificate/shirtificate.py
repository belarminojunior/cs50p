from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image = ('week8\shirtificate\shirtificate.png', 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)


def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 213, f"{s} took CS50", align="C")
    pdf.output("week8\shirtificate\shirtificate.pdf")


def main():
    name = input('Name: ')
    shirt(name)


if __name__ == '__main__':
    main()
