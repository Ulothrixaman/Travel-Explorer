# Travel Explorer

Explore the world with Travel Explorer, your ultimate travel booking companion. Plan your dream vacations, discover exciting destinations, and book flights, hotels, and activities seamlessly. Embark on a journey of a lifetime with our user-friendly full-stack travel booking app. Let the adventure begin!

## Features

- **Destination Discovery**: Browse and explore various travel destinations.
- **Flight Booking**: Search and book flights with ease.
- **Hotel Reservations**: Find and book hotels that suit your preferences.
- **Activity Booking**: Discover and book activities at your travel destination.
- **User Accounts**: Create and manage user accounts for personalized experiences.

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: Bootstrap
- **Containerization**: Docker

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Ulothrixaman/Travel-Explorer.git
    cd Travel-Explorer
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

### Using Docker

1. Build the Docker image:
    ```sh
    docker build -t travel-explorer .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8000:8000 travel-explorer
    ```

3. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [Your Email](mailto:youremail@example.com)

Project Link: [https://github.com/Ulothrixaman/Travel-Explorer](https://github.com/Ulothrixaman/Travel-Explorer)