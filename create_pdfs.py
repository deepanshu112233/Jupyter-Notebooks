from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Create pdf_files directory if it doesn't exist
os.makedirs("notebook/pdf_files", exist_ok=True)

# Create first PDF
c1 = canvas.Canvas("notebook/pdf_files/document1.pdf", pagesize=letter)
c1.setFont("Helvetica-Bold", 16)
c1.drawString(50, 750, "Machine Learning Fundamentals")
c1.setFont("Helvetica", 12)
c1.drawString(50, 720, "This is the first dummy PDF document.")
c1.drawString(50, 700, "It contains information about machine learning basics.")
c1.drawString(50, 680, "Machine learning algorithms learn patterns from data.")
c1.drawString(50, 660, "Common types: Supervised, Unsupervised, Reinforcement Learning.")
c1.drawString(50, 640, "Applications include image recognition, NLP, and recommendations.")
c1.drawString(50, 620, "Deep learning uses neural networks for complex tasks.")
c1.save()
print("Created: notebook/pdf_files/document1.pdf")

# Create second PDF
c2 = canvas.Canvas("notebook/pdf_files/document2.pdf", pagesize=letter)
c2.setFont("Helvetica-Bold", 16)
c2.drawString(50, 750, "Advanced Data Science Techniques")
c2.setFont("Helvetica", 12)
c2.drawString(50, 720, "This is the second dummy PDF document.")
c2.drawString(50, 700, "It covers advanced topics in data science.")
c2.drawString(50, 680, "Feature engineering improves model performance.")
c2.drawString(50, 660, "Cross-validation prevents overfitting.")
c2.drawString(50, 640, "Hyperparameter tuning optimizes model accuracy.")
c2.drawString(50, 620, "Ensemble methods combine multiple models.")
c2.save()
print("Created: notebook/pdf_files/document2.pdf")
