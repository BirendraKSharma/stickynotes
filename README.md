# StickyNotes

A feature-rich Django web application for creating, managing, and sharing notes and blog posts.

## Live Demo

Visit the live application: [StickyNotes on Render](https://stickynotes-zcme.onrender.com/profile/)

## Features

- 📝 Create, edit, and delete notes/blog posts
- 👤 User authentication and profiles
- 🖼️ Image upload with Cloudinary integration
- 🔍 Post search functionality
- 📱 Responsive design
- ✍️ Rich text editor (TinyMCE)

## Technologies Used

- **Backend**: Django 5.1
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (development) / PostgreSQL (production option)
- **Deployment**: Render with ASGI (Uvicorn)
- **Media Storage**: Cloudinary
- **Text Editor**: TinyMCE
- **Authentication**: Django built-in authentication

## Installation

### Prerequisites

- Python 3.8+
- Git
- Cloudinary account

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/stickynotes.git
   cd stickynotes
   ```

2. Create a virtual environment
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with the following variables
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   USER_EMAIL=your-email@example.com
   USER_PASS=your-email-password
   ```

5. Run migrations
   ```bash
   python manage.py migrate
   ```

6. Create a superuser
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` in your browser

## Usage

1. Register a new account or log in
2. Create posts via the "New Post" option
3. View, edit, or delete your posts from your profile
4. Upload a profile picture in your profile settings
5. Search for posts using the search bar

## Deployment

This application is deployed on Render using ASGI (Uvicorn). The live version can be accessed at:

[https://stickynotes-zcme.onrender.com/](https://stickynotes-zcme.onrender.com/)

### Deployment Instructions

1. Create a `build.sh` file in your project root:
   ```bash
   #!/usr/bin/env bash
   set -o errexit
   pip install -r requirements.txt
   python manage.py collectstatic --no-input
   python manage.py migrate
   ```

2. Set up environment variables on Render:
   - SECRET_KEY
   - DEBUG (set to False)
   - ALLOWED_HOSTS
   - CSRF_TRUSTED_ORIGINS
   - CLOUDINARY credentials
   - Email settings

3. Start command for Render:
   ```
   uvicorn stickynotes.asgi:application --host 0.0.0.0 --port $PORT
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django documentation and community
- Bootstrap for the frontend framework
- Cloudinary for media storage solution
- Render for the hosting platform

---

© 2025 StickyNotes. All rights reserved.
