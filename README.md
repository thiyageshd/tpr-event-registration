## Tirupur Marathon Event Registration

# Technology Stack

## Backend - 
    - Python (Django/Flask/FastAPI) or Node.js.

## Database: 
    - PostgreSQL/MySQL for structured data, Redis for caching.

## Frontend: 
    - React.js/Next.js or Angular for a responsive user interface.

## Payment Gateway:
    - Stripe, Razorpay, or PayPal SDKs for secure transactions.

## Hosting:

     - Hostingr

## Deployment:

    - Use Docker for containerization.

     - CI/CD tools like GitHub Actions or Jenkins.

## Development Roadmap
## Phase 1: Core Features

    Build user registration and profile management.

    Develop the yearly subscription form.

## Phase 2: Payment Integration

    Integrate a payment gateway and test different scenarios.

## Phase 3: Notifications

    Set up automated email/SMS reminders using services like Twilio or SendGrid.

## Phase 4: Analytics and Admin Panel

    Create dashboards for the admin to view user and payment data.


## Frontend (Angular)
## Step 1: Set Up Angular Project
````shell
ng new running-event-registration
cd running-event-registration
ng generate component register
ng generate component admin
Step 2: Registration Form (Reactive Forms)
Use Angular Reactive Forms for dynamic form validation

Fields: dropdowns, inputs, etc.
````

Include a Coupon Code field


````shell
this.registerForm = this.fb.group({
  event_type: ['', Validators.required],
  name: ['', Validators.required],
  age: ['', Validators.required],
  sex: ['', Validators.required],
  address: ['', Validators.required],
  state: ['', Validators.required],
  city: ['', Validators.required],
  blood_group: ['', Validators.required],
  contact: ['', Validators.required],
  emergency_contact: ['', Validators.required],
  emergency_contact_name: ['', Validators.required],
  coupon_code: ['']
});
````
Step 3: Submit Form to Backend
````shell
this.http.post('/api/register', this.registerForm.value).subscribe(response => {
  // Handle success
});
````
Step 4: Admin Component
Fetch All Users
````shell
this.http.get<User[]>('/api/users').subscribe(data => {
  this.users = data;
});
````
Add Filters

Dropdown to select Event Type

Text input for name, contact, etc.

Send as a filter object to /users/filter

````shell
let filterPayload = { event_type: this.selectedEvent };
this.http.post<User[]>('/api/users/filter', filterPayload).subscribe(data => {
  this.users = data;
});
````