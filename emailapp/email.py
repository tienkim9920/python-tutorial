class Email:
  def __init__(self, title, description, time):
    self.title = title
    self.description = description
    self.time = time

def get_Email_list():
  return [
    Email('Cong ty ABC', 'Thong bao lich phong van', 'Hom qua'),
    Email('Cong ty Ninedev', 'Thong bao ket qua', '26/04/2025'),
    Email('Cong ty XYZ', 'Thong bao lich trinh', 'Hom qua'),
  ]
    