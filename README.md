# ☕ CoffeHub - Online Coffee Shop

![Am I Responsive](docs/images/amiresponsive/amiresponsive.png)

**Developer: Olle**  
🌐 [Visit Live Website](https://your-live-site-link.com)

---

## 📖 Table of Contents
- [About](#about)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Design](#design)
  - [Colours](#colours)
  - [Fonts](#fonts)
  - [Structure](#structure)
  - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## 📝 About
CoffeHub is an eCommerce Django web app for coffee lovers. Users can browse, add to cart, and purchase coffee products. The site supports email verification, secure checkout via Stripe, and includes user authentication features.

---

## 🎯 User Goals
- Browse a wide selection of coffee products
- Add and remove products from a shopping cart
- Register and log in securely
- Make secure payments
- Receive email confirmations and account verification

## 🎯 Site Owner Goals
- Provide a reliable platform to sell coffee products
- Enable easy account creation and verification
- Allow secure Stripe-based payments
- Collect user data for order processing

---

## 🎨 User Experience

### 🎯 Target Audience
- Coffee enthusiasts
- Online shoppers
- Frequent users of specialty coffee products

### 🎯 User Requirements & Expectations
- Easy navigation and responsive design
- Quick access to cart and checkout
- Secure login and signup flow
- Product details with images and prices
- Order confirmation and email verification

---

## ✅ User Stories

### Users

<details><summary>1. As a user, I can register an account with email verification</summary>
<img src="docs/images/user_storys/1.png">
</details>

<details><summary>2. As a user, I can browse all available products</summary>
<img src="docs/images/user_storys/1.png">
</details>

<details><summary>3. As a user, I can add items to my cart</summary>
<img src="docs/images/user_storys/1.png">
</details>

<details><summary>4. As a user, I can view and manage my cart</summary>
<img src="docs/images/user_storys/1.png">
</details>

<details><summary>5. As a user, I can check out securely using Stripe</summary>
<img src="docs/images/user_storys/1.png">
</details>

<details><summary>6. As a user, I can view a success or cancellation message</summary>
<img src="docs/images/user_storys/1.png">
</details>

### Admin

<details><summary>7. As an admin, I can manage product inventory.</summary>
<img src="docs/images/user_storys/10.png">
</details>

<details><summary>8. As an admin, I can view orders and users.</summary>
<img src="docs/images/user_storys/10.png">
</details>

---

## 🎨 Design

### 🎨 Colours
- Earthy tones (brown, beige) to reflect coffee theme

### 🎨 Fonts
- Main font: Montserrat / Sans-serif (Google Fonts)

### 🎨 Structure
- Home > Products > Cart > Checkout > Success
- Navbar and Footer consistent across pages

## 🛢️ Database

The CoffeHub project uses Django’s ORM to manage a relational database structure. In development, it uses SQLite, while PostgreSQL is used for production.

---

### **🧾 Models Overview**

---

### **User Model**
This project uses Django’s built-in `User` model (`django.contrib.auth.models.User`) for authentication. No custom user model was created.

- `username`: User’s unique identifier.
- `email`: Used for registration and verification.
- `password`: Hashed and securely stored.
- `is_active`, `is_staff`, `date_joined`: Standard Django fields.
- Relationships: Linked via ForeignKey or OneToOneField in other models like `Cart` and `Comment`.

---

### **Product Model**
Located in: `products/models.py`

Represents a product available for purchase.

- `name`: `CharField` – Name of the product.
- `description`: `TextField` – Optional details.
- `price`: `DecimalField` – Cost of the product.
- `image_url`: `URLField` – Image of the product.

---

### **Comment Model**
Located in: `products/models.py`

Allows users to comment on products.

- `product`: `ForeignKey` to `Product`.
- `user`: `ForeignKey` to Django `User`.
- `text`: `TextField` – Content of the comment.
- `created_at`: `DateTimeField` – Timestamp.

---

### **Cart Model**
Located in: `checkout/models.py`

Each user has one associated cart.

- `user`: `OneToOneField` to `User`.
- `total_price()`: method – Calculates total cost of items.

---

### **CartItem Model**
Located in: `checkout/models.py`

Individual product added to a cart.

- `cart`: `ForeignKey` to `Cart`.
- `product`: `ForeignKey` to `Product`.
- `quantity`: `PositiveIntegerField` – Defaults to 1.
- `total_price()`: method – Line total for the product.

---

### **ERD Diagram**
<details><summary>View Diagram</summary>
<img src="docs/images/coffehub_erd.png" alt="CoffeHub ERD">
</details>

> 💡 _All models are registered in the Django admin panel for easy access and management._

### 🎨 Wireframes
- Mobile, tablet, and desktop wireframes created using Balsamiq or Figma *(insert screenshots)*

---

## 🚀 Features

### ✅ Authentication
- **User Registration** with email verification using SendGrid.
- **Login/Logout** functionality with feedback messages.
- **Only verified users can check out**, enhancing security and reliability.

<details><summary>🔍 Screenshots</summary>

![Register](docs/images/features/register.png)  
![Login](docs/images/features/login.png)  
![Verification](docs/images/features/verify-email.png)

</details>

---

### 🛒 Cart System
- Users can:
  - Add products to a cart.
  - Increase/decrease quantity or remove items.
  - View cart summary including item count and total price.
  - Cart is session-based for anonymous users and linked to accounts for authenticated users.
- Cart **empties automatically after successful checkout**.

<details><summary>🛒 Screenshots</summary>

![Cart View](docs/images/features/cart.png)  
![Cart Update](docs/images/features/cart-update.png)

</details>

---

### 💳 Stripe Checkout Integration
- Secure payment handling through Stripe.
- Redirects users to success or cancel page depending on payment outcome.
- Order summary and confirmation shown after payment.
- Works with **Stripe test cards** for development.

<details><summary>💳 Screenshots</summary>

![Stripe Checkout](docs/images/features/checkout.png)  
![Payment Success](docs/images/features/success.png)  
![Payment Cancelled](docs/images/features/cancel.png)

</details>

---

### 🛍️ Product Pages
- **Product List View**:
  - All coffee products displayed with name, image, price, and link to details.
- **Product Detail View**:
  - Includes image, detailed description, price, and "Add to Cart" button.
  - Users can leave comments after logging in.

<details><summary>☕ Screenshots</summary>

![Product List](docs/images/features/products.png)  
![Product Detail](docs/images/features/product-detail.png)

</details>

---

### 💬 Product Comments
- Authenticated users can:
  - Leave comments on product pages.
  - View all comments related to a product.
  - Delete their own comments.
- Admin can manage all comments through the admin panel.

<details><summary>💬 Screenshots</summary>

![Comments](docs/images/features/comments.png)  
![Add Comment](docs/images/features/add-comment.png)

</details>

---

### 📦 Admin Features
- Admin panel access to:
  - Manage all products (create, update, delete).
  - Review and delete inappropriate comments.
  - Monitor cart items and order-related data (if stored).

<details><summary>🔐 Screenshots</summary>

![Admin Dashboard](docs/images/features/admin-dashboard.png)  
![Manage Products](docs/images/features/manage-products.png)

</details>

---

### 📱 Responsive UI
- Mobile-friendly design using Bootstrap 5.
- Smooth navigation across desktop, tablet, and mobile devices.
- **Cart, navbar, and footer adapt to screen size.**

<details><summary>📱 Screenshots</summary>

![Mobile View](docs/images/features/mobile.png)  
![Tablet View](docs/images/features/tablet.png)

</details>

---

### 📧 Email Functionality
- SendGrid integration sends:
  - Account verification emails.
  - (Planned) Order confirmation emails after checkout.

<details><summary>📧 Screenshots</summary>

![Email Confirmation](docs/images/features/email-confirmation.png)

</details>

---

### ✨ Flash Messages
- Inform users of actions like login, logout, item added to cart, checkout success, etc.
- Shown using Django’s messages framework styled with Bootstrap alerts.

<details><summary>⚡ Screenshots</summary>

![Messages](docs/images/features/messages.png)

</details>

---

## 🧪 Testing
- Manual testing on Chrome, Firefox, Safari, mobile
- Validated HTML, CSS, and Python (PEP8)
- Lighthouse and WAVE accessibility tests

*(Include screenshots of test results and descriptions)*

---

## 🐞 Bugs

### Fixed
- Cart not clearing after checkout ➝ Fixed
- Email verification not blocking checkout ➝ Fixed

### Known
- Some iPhone SE responsiveness issues

---

## 🚀 Deployment

### Platform: Heroku
- Deployed using GitHub integration
- Env vars set for secret keys, SendGrid, Stripe

### To Deploy:
- Create app on Heroku
- Push code from GitHub repo
- Set environment variables
- Run migrations
- Collect static files

---

## 📜 Credits
- Icons: [FontAwesome](https://fontawesome.com/)
- Stripe & Django docs for guidance

---

## 💙 Acknowledgements
- Thanks to **Code Institute** for course content
- Inspiration from previous MS3 project

---

📌 Replace placeholders with screenshots and links where needed!
