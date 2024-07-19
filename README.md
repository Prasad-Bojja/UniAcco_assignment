### Project Description: User Login API with Email and OTP Authentication

#### Project Overview
The goal of this project is to develop a secure and efficient API system for user authentication using email and One-Time Password (OTP). This system will enable users to log in by providing their email address, receiving an OTP, and verifying the OTP to gain access.

#### Objectives
1. **User Authentication**: Create a seamless authentication process that uses email and OTP.


#### Key Features
1. **Email Registration**:
   - Endpoint to register a new user with an email address.
   - Validate the email format and check for duplicates.

2. **OTP Generation and Sending**:
   - Endpoint to request an OTP.
   - Generate a secure OTP.
   - Send the OTP to the user's registered email address.

3. **OTP Verification**:
   - Endpoint to verify the OTP.
   - Authenticate the user if the OTP is valid and within the time limit.


4. **Security Measures**:
   - Implement rate limiting on OTP requests to prevent abuse.
   

#### Technologies Used
1. **Backend Framework**: Django.
2. **Database**:  SQLite 
3. **Email Service**: Integrate with a mock email service for sending OTPs.
4. **Token Management**: Use JWT (JSON Web Tokens).


## Setup Instructions

### Prerequisites
- Python 3.10 or higher


### Local Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Prasad-Bojja/UniAcco_assignment
   cd uniacco-backend

2. **Create and activate a virtual environment**:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:
    pip install -r requirements.txt

4. **Apply migrations**:
    python manage.py migrate

5. **Run the server**:
    python manage.py runserver

## Usage
   * Register a new user: Send a POST request to /api/register with the user's email.
   * Request an OTP: Send a POST request to /api/request-otp with the user's email.
   * Verify the OTP: Send a POST request to /api/verify-otp with the user's email and the received OTP.





