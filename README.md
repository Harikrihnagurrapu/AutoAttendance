# AutoAttendance

Automated Attendance Tracking System Using Face Recognition (OpenCV + Firebase)

## Overview

AutoAttendance is a Python-based system for automating student attendance using real-time face recognition. It uses OpenCV for image processing, the face_recognition library for identifying faces, and Firebase for storing student data and attendance records.

## Features

- Real-time face recognition from webcam
- Attendance marking and tracking
- Integration with Firebase Realtime Database and Cloud Storage
- GUI interface with live feedback
- Easy student data management

## How It Works

1. **Student Registration:** Admin adds student images and info to the database.
2. **Face Encoding:** The system generates encodings for all known faces.
3. **Attendance:** Students stand in front of the webcam; their faces are recognized, and attendance is marked and updated in Firebase.
4. **Feedback:** Student info and status are displayed on the GUI.

## Technologies Used

- Python
- OpenCV
- face_recognition (dlib ResNet model)
- Firebase Admin SDK (Realtime Database & Cloud Storage)
- cvzone (for GUI overlays)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Harikrihnagurrapu/AutoAttendance.git
   cd AutoAttendance
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Firebase:**
   - Create a Firebase project.
   - Download your `serviceAccountKey.json` and place it in the project directory.
   - Update the database URL and storage bucket in the code as per your project.

4. **Add Student Images:**
   - Place student face images in the `Images` folder, naming each image with the student’s ID.

5. **Run Encoding Script:**
   ```bash
   python EncodeGenerator.py
   ```

6. **Add Student Data to Database:**
   - Use `AddDataToDatabase.py` to populate student details in Firebase.

7. **Start Attendance System:**
   ```bash
   python main.py
   ```

## Project Structure

- `main.py` - Runs the real-time attendance GUI and logic
- `EncodeGenerator.py` - Generates and saves face encodings
- `AddDataToDatabase.py` - Populates Firebase with student info
- `Images/` - Folder for student face images
- `Resources/` - GUI backgrounds and mode images

## Contributing

Contributions are welcome! Please open issues or pull requests for feature requests, bug reports, or improvements.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [Firebase](https://firebase.google.com/)
