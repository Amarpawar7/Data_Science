# Duck typing : It is a concept where the type of an object is determined by its behaviour(function), not by it's class

class InkjetPrinter:
    def PrintDocument(self,document):
        print("Inkjet Printer Printing : ",document)

class LaserPrinter:
    def PrintDocument(self,document):
        print("Laser Printer Printing : ",document)

class PDFWriter:
    def PrintDocument(self,document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.PrintDocument("Marvellous notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())
    
main()
