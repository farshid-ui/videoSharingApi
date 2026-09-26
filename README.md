# Video Sharing API

A REST API for a video sharing platform built with Django and Django REST Framework.

Users can register and log in, subscribe to available plans, make payments, access videos based on their subscription, save watch progress, rate videos, and leave comments.

## Technologies

* Python
* Django
* Django REST Framework
* SQLite
* Git / GitHub

## Project Structure

```text
VideoSharingApi/
├── config/
├── documents/
│   └── Erd_VideoSharingApi.png
├── payment/
├── subscription/
├── user/
├── video/
├── manage.py
└── requirements.txt
```

## Main Features

### User

* User registration
* User login
* Authenticated profile
* Session-based authentication

### Subscription

* View active subscription plans
* Create a subscription
* Cancel a subscription
* Renew an active subscription
* Subscription start and end dates
* Active/inactive subscription status

### Payment

* Create a payment for a subscription
* Payment amount is taken from the selected subscription plan
* Payment status
* Payment history
* Simulated successful payment

A real bank gateway is not used in this project.

### Video

* List published videos
* Create videos
* View video details
* Update videos
* Delete videos
* Subscription-based video access

Videos can be public or require a specific subscription plan.

### Watch History

* Save video watching progress
* Update existing progress
* View personal watch history
* View a specific history record
* Delete a history record

### Rating

* Rate videos from 1 to 5
* A user can have one rating for each video
* Update an existing rating
* View ratings and average score for a video

### Comments

* Add comments to videos
* View video comments
* Edit own comments
* Delete own comments

### Live Update

A simple API endpoint is provided for live video information.

It returns:

* Average rating
* Number of ratings
* Number of comments
* Current comments

The project uses a normal API endpoint for this feature and does not use WebSockets.

## API Endpoints

### User

```text
POST /api/user/register/
POST /api/user/login/
GET  /api/user/profile/
```

### Subscription

```text
GET  /api/subscription/plans/
POST /api/subscription/create/
POST /api/subscription/<id>/cancel/
POST /api/subscription/<id>/renew/
```

### Payment

```text
POST /api/payment/create/
GET  /api/payment/history/
```

### Video

```text
GET    /api/video/
POST   /api/video/
GET    /api/video/<id>/
PUT    /api/video/<id>/
PATCH  /api/video/<id>/
DELETE /api/video/<id>/
```

### Watch History

```text
GET    /api/video/watch-history/
POST   /api/video/watch-history/
GET    /api/video/watch-history/<id>/
DELETE /api/video/watch-history/<id>/
```

### Rating

```text
POST /api/video/ratings/
GET  /api/video/ratings/<video_id>/
```

### Comments

```text
POST   /api/video/comments/
GET    /api/video/comments/<video_id>/
PUT    /api/video/comments/<id>/
PATCH  /api/video/comments/<id>/
DELETE /api/video/comments/<id>/
```

### Live Update

```text
GET /api/video/live-update/<video_id>/
```

## Permissions

The API uses Django REST Framework authentication and permissions.

Authenticated users can access protected endpoints.

Video access is checked based on the user's active subscription. If a video requires a specific subscription plan, the user must have an active subscription for that plan.

Users can only manage their own subscriptions, payments, watch history, ratings, and comments.

## Database Models

The main models in the project are:

* User
* SubscriptionPlan
* Subscription
* Payment
* Video
* WatchHistory
* Rating
* Comment

The ER diagram is available in:

```text
documents/Erd_VideoSharingApi.png
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd VideoSharingApi
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Authentication

The project uses Django session authentication.

After logging in, protected endpoints can be tested using Django REST Framework's Browsable API.

## API Testing

The APIs can be tested through the DRF Browsable API.

A typical flow is:

1. Register a user
2. Log in
3. Create or select a subscription plan
4. Create a subscription
5. Make a payment
6. Access a protected video
7. Add watch history
8. Rate the video
9. Add a comment
10. Check the live update endpoint

## Notes

This project was developed as a Django REST Framework backend project.

The main focus is the API, database relationships, authentication, permissions, subscriptions, payments, and video access control.

No frontend interface is included.
