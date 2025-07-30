import os
from django.db import models
from django.utils import timezone
import PyPDF2
import whisper
import tempfile

# 🔹 Add ffmpeg path so Whisper can use it
os.environ["PATH"] += os.pathsep + r"C:\Users\Poojitha\OneDrive - Manipal Academy of Higher Education\Desktop\Kshitija\bin"

class Meeting(models.Model):
    MEETING_TYPES = [
        ('client', 'Client'),
        ('amc', 'AMC'),
        ('internal', 'Internal'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)  # extracted text or manual input
    meeting_type = models.CharField(max_length=20, choices=MEETING_TYPES, default='client')
    last_modified_date = models.DateTimeField(auto_now=True)
    added_date = models.DateTimeField(auto_now_add=True)
    meeting_date = models.DateTimeField(default=timezone.now, editable=True)
    pdf_file = models.FileField(upload_to='meeting_files/', null=True, blank=True)
    audio_file = models.FileField(upload_to='meeting_audio/', null=True, blank=True)  # NEW

    def save(self, *args, **kwargs):
        # Extract from PDF if content is empty
        if self.pdf_file and not self.content:
            try:
                pdf_reader = PyPDF2.PdfReader(self.pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
                self.content = text
            except Exception as e:
                print(f"PDF extraction error: {e}")

        # Transcribe audio if content is still empty
        if self.audio_file:
            try:
                model = whisper.load_model("base")
                # Save temp file for whisper
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    for chunk in self.audio_file.chunks():
                        tmp.write(chunk)
                    tmp_path = tmp.name
                result = model.transcribe(tmp_path)
                self.content += result["text"]
                os.remove(tmp_path)
            except Exception as e:
                print(f"Whisper transcription error: {e}")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.meeting_type})"
