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

from django.db import models

## 🛢️ Database

The CoffeHub project uses a relational database powered by Django’s ORM, backed by PostgreSQL in production.

---

### **🧾 Models Overview**

---

### **`Product` Model**
Located in: `products/models.py`

Represents a product available for sale.

- `name`: `CharField` – Product name.
- `description`: `TextField` – Optional product details.
- `price`: `DecimalField` – Product price.
- `image_url`: `URLField` – Link to product image.

---

### **`Comment` Model**
Located in: `products/models.py`

Allows users to comment on products.

- `product`: `ForeignKey` to `Product`.
- `user`: `ForeignKey` to Django `User`.
- `text`: `TextField` – Comment content.
- `created_at`: `DateTimeField` – Auto timestamp.

---

### **`Cart` Model**
Located in: `checkout/models.py`

Stores each user’s active shopping cart.

- `user`: `OneToOneField` – Connected to a `User`.
- `total_price()`: method – Returns total value of all cart items.

---

### **`CartItem` Model**
Located in: `checkout/models.py`

Represents individual product entries in the user’s cart.

- `cart`: `ForeignKey` to `Cart`.
- `product`: `ForeignKey` to `Product`.
- `quantity`: `PositiveIntegerField` – Default is 1.
- `total_price()`: method – Returns line total for item.

---

### **ERD Diagram**
<details><summary>View Diagram</summary>
<img src="docs/images/coffehub_erd.png" alt="CoffeHub ERD">
</details>


> 💡 _All models are registered in the Django admin panel for easy access during development._



### 🎨 Wireframes
- Mobile, tablet, and desktop wireframes created using Balsamiq or Figma *(insert screenshots)*

---

## 🛠️ Technologies Used
- **HTML5**, **CSS3**, **JavaScript**, **Python3**
- **Django** - Python web framework
- **Django Allauth** - for user authentication
- **PostgreSQL** - production DB
- **SQLite** - development DB
- **Stripe** - for payment processing
- **SendGrid** - for email
- **Heroku** - for deployment
- **GitHub** - version control
- **Bootstrap 5**, **Crispy Forms**, **Widget Tweaks**

---

## 🚀 Features

### User Authentication
- Registration with email verification
- Login/logout flow with secure redirect

### Cart
- Add, update, and remove products
- Cart persists per user session

### Checkout
- Stripe integration with success/cancel handling
- Requires verified email to proceed
- Cart is cleared after successful checkout

### Product Pages
- List view with images, prices
- Detail view with descriptions

### Responsive Design
- Works across all screen sizes
- Flexbox and Bootstrap grid used

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

