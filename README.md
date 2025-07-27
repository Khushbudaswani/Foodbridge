# Food Bridge

Food Bridge is a Django-powered platform that connects food donors (restaurants, event organizers, individuals) with volunteers to deliver surplus food to people in need. Our mission is to reduce food waste and fight hunger by enabling easy food donations, volunteer signups, and community engagement.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Usage](#usage)
  - [Donating Food](#donating-food)
  - [Joining as a Volunteer](#joining-as-a-volunteer)
  - [Contacting the Team](#contacting-the-team)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Food Donation:** Donors can submit food donation details via a form ([donations/donate_food.html](templates/donations/donate_food.html)). Admins are notified by email.
- **Volunteer Signup:** Volunteers can join the team by filling out a form ([volunteers/join_team.html](templates/volunteers/join_team.html)). Admins are notified by email.
- **Contact Form:** Users can send messages to the team ([pages/contact.html](templates/pages/contact.html)).
- **Gallery:** Showcases images from donation drives and volunteer activities.
- **Events & Drives:** Lists upcoming donation drives and events ([pages/events.html](templates/pages/events.html)).
- **Impact & Partners:** Displays statistics, testimonials, and partner organizations ([pages/impact.html](templates/pages/impact.html), [pages/partners.html](templates/pages/partners.html)).
- **Admin Panel:** Manage donations, volunteers, and contact messages.
- **Responsive UI:** Modern, mobile-friendly design using Bootstrap 5, Animate.css, and AOS.
- **Email Notifications:** Sends emails to admins on new donations and volunteer signups.
- **Testimonials:** Carousel and stories from real beneficiaries and partners.
- **How We Operate:** Transparent workflow and impact metrics ([pages/about.html](templates/pages/about.html)).

---

## Project Structure

```
├── Foodbridge/
│   ├── db.sqlite3
│   ├── manage.py
│   ├── donations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── foodbridge/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── volunteers/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── donations/
│       │   └── donate_food.html
│       ├── pages/
│       │   ├── about.html
│       │   ├── contact.html
│       │   ├── events.html
│       │   ├── impact.html
│       │   └── partners.html
│       └── volunteers/
│           └── join_team.html
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (recommended)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Khushbudaswani/Foodbridge
   cd Foodbridge
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Collect static files (optional for production):**
   ```sh
   python manage.py collectstatic
   ```

### Running the Project

Start the development server:

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Usage

### Donating Food

- Click "Donate Food" in the navigation bar.
- Fill out the donation form with your details and food information.
- On submission, the admin is notified by email and you see a thank you message.

### Joining as a Volunteer

- Click "Join Us" in the navigation bar.
- Fill out the volunteer form.
- On submission, the admin is notified by email and you see a confirmation message.

### Contacting the Team

- Click "Contact" in the navigation bar.
- Fill out the contact form to send a message to the team.

---

## Configuration

- **Email Settings:**  
  Update email backend settings in `foodbridge/settings.py` for production use:
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.example.com'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = 'your-email@example.com'
  EMAIL_HOST_PASSWORD = 'your-password'
  EMAIL_USE_TLS =  True
  DEFAULT_FROM_EMAIL = 'Food Bridge <your-email@example.com>'
  ```
- **Static & Media Files:**  
  Place images in `static/images/` and CSS in `static/css/`.

- **Admin Panel:**  
  Access at `/admin/` with your superuser credentials.

---

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

---

## License

> This project is licensed under the MIT License.
---

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [AOS Animate on Scroll](https://michalsnik.github.io/aos/)
- [Animate.css](https://animate.style/)
- All contributors and volunteers!

---

## Contact

For questions, suggestions, or partnership inquiries, use the [Contact] page on the website.

---