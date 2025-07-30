# WIZR  

## Fund Manager Conversations - Meeting Files Feature  

This project is a **Django application** that allows you to manage meetings and upload/view related **PDF and Audio files**.  
It includes a web interface to list all meetings, view uploaded files, extract text from PDFs, and transcribe audio files using **Whisper**.  

---

## Steps Followed  

### 1. Project Setup  
- Used existing Django project `wiki` and app `fund_manager_conversations`.  
- Verified Django installation and existing project structure.  
- Installed dependencies: **Django**, **PyPDF2**, **OpenAI Whisper**.  

### 2. Models  
- Updated `Meeting` model:  
  - Added fields for `title`, `content`, `meeting_type`, `dates`, and `pdf_file` for file uploads.  
  - **New:** Added `audio_file` field for uploading meeting audio recordings.  
- Configured automatic extraction of text from PDFs and audio transcriptions using **Whisper**.  

### 3. Database Migrations  
- Ran `makemigrations` and `migrate` to update database schema.  

### 4. Admin & Superuser  
- Created a Django superuser to manage meetings via the admin panel.  
- Updated admin to allow uploading both **PDF and Audio files**.  

### 5. Templates & Views  
- Created a `templates/fund_manager_conversations/` folder.  
- Built an HTML template `meetings_list.html` to list all meetings, extracted content, and display file/audio links.  
- Updated `views.py` to fetch meetings and display:  
  - Extracted text  
  - PDF links  
  - Audio players  

### 6. URLs  
- Added a `urls.py` in the app and linked it in `wiki/urls.py` using `include()`.  

### 7. Static & Media Settings  
- Configured `MEDIA_URL` and `MEDIA_ROOT` in `settings.py`.  
- Updated `urls.py` to serve uploaded files (PDFs & audio) in development.  

### 8. File Upload, Extraction & Display  
- Added **PDF upload** option to meetings in the admin panel.  
- Added **Audio upload** option for meeting recordings.  
- Extracted text from PDFs using **PyPDF2** and appended it to the `content` field.  
- Transcribed audio files using **Whisper** and appended the transcription text to the `content` field.  
- Front-end now displays:  
  - Extracted meeting content (PDF + Audio)  
  - PDF download/view links  
  - Audio players for uploaded files  

### 9. Whisper & ffmpeg Setup  
- Installed **OpenAI Whisper** for audio transcription.  
- Installed **ffmpeg** (required by Whisper) and added it to the system path so Django can process audio files.  

---

## Approach  

- Extend the existing `Meeting` model to support both PDF and audio uploads.  
- Automate text extraction from PDFs and audio transcription using **Whisper**.  
- Use Django’s template system to display meetings, extracted content, and uploaded files.  
- Configure URLs and settings to handle media files correctly.  

### Test the flow:  
1. Create meetings in admin.  
2. Upload **PDF and/or audio files**.  
3. Verify extracted content and uploaded files display correctly in the front-end list.  

---

## Current Features  

- Add meetings with details and type (**Client, AMC, Internal**).  
- Upload and view meeting-related **PDF and Audio files**.  
- Automatically extract text from uploaded PDFs.  
- Automatically transcribe uploaded audio using **Whisper**.  
- User-friendly list of all meetings with:  
  - Extracted content  
  - PDF view/download links  
  - Audio players  

---

### TO DO LIST  
- An option for batch upload for files and in the content one should be able to extract content from the pdf uploaded  
