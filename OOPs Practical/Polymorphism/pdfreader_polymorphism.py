class PDFreader:
    def open(self):
        return "Read poem.pdf"
    
class ImageViewer:
    def open(self):
        return "View sky.png"

#polymorphism    
def view_pdf(view):
    print(view.open())

p = PDFreader()
i = ImageViewer()
view_pdf(p)
view_pdf(i)