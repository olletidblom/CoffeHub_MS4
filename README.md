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

<details><summary>1. As a user, I can register an account so that I can securely use the site </summary>
<img src="docs//userstory/1.png">
</details>

<details><summary>2. As a user, I can browse available products so I can choose what to buy.</summary>
<img src="docs//userstory/2.png">
</details>

<details><summary>3. As a user, I can add a product to my cart so I can buy it later. </summary>
<img src="docs//userstory/3.png">
</details>

<details><summary>4. As a user, I can update cart quantities or remove items</summary>
<img src="docs//userstory/4.png">
</details>

<details><summary>5. As a user, I can check out securely using Stripe</summary>
<img src="docs//userstory/5.png">
</details>

<details><summary>6. As a user, I can leave a comment and manage my own comments.</summary>
<img src="docs//userstory/6.png">
</details>

<details><summary>7. As a user, I can request a password reset in case I forget it.</summary>
<img src="docs//userstory/7.png">
</details>

<details><summary>8. As a user, I can navigate the site easily on any device</summary>
<img src="docs//userstory/8.png">
</details>



### Admin

<details><summary>9. As an admin, I can manage products so that I can keep the product catalog up to date.</summary>
<img src="docs/images/user_storys/9.png">
</details>

<details><summary>10. As an admin, I can moderate user comments so that I can ensure community guidelines are followed.</summary>
<img src="docs/images/user_storys/10.png">
</details>

<details><summary>11. As an admin, I can view user accounts and order history so that I can assist users or resolve disputes.</summary>
<img src="docs/images/user_storys/11.png">
</details>




<details><summary>12. As an admin, I can manage products and comments.</summary>
<img src="docs/images/user_storys/7.png">
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
<img src="docs/erd.png" alt="CoffeHub ERD">
</details>

> 💡 _All models are registered in the Django admin panel for easy access and management._

### 🎨 Wireframes
Wireframes were created using [Balsamiq](https://balsamiq.com/) to plan the UI structure.

<details><summary>Home</summary>
<img src="docs/wireframe/home.png">
</details>
<details><summary>Products</summary>
<img src="docs/wireframe/products.png">
<img src="docs/wireframe/productsdetail.png">
</details>
<details><summary>Cart</summary>
<img src="docs/wireframe/cart.png">
</details>
<details><summary>Account</summary>
<img src="docs/wireframe/login.png">
<img src="docs/wireframe/signup.png">
<img src="docs/wireframe/mail.png">
<img src="docs/wireframe/password.png">

</details>
---

## 🚀 Features

### ✅ Authentication
- **User Registration** with email verification using SendGrid.
- **Login/Logout** functionality with feedback messages.
- **Only verified users can check out**, enhancing security and reliability.

<details><summary>🔍 Screenshots</summary>

![Register](docs/features/signin.png)  
![Login](docs/features/signup.png)  
![Verification](docs/features/emailvali.png)

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

![Home View](docs/features/home.png)  
![Product View](docs/features/products.png)  
![Product Detail ](docs/features/productdetails.png)
![Cart View](docs/features/cart.png)  

</details>

---

### 💳 Stripe Checkout Integration
- Secure payment handling through Stripe.
- Redirects users to success or cancel page depending on payment outcome.
- Order summary and confirmation shown after payment.
- Works with **Stripe test cards** for development.

<details><summary>💳 Screenshots</summary>

![Stripe Checkout](docs/features/payment.png)  
![Payment Success](docs/features/paymentgood.png)  
![Payment Cancelled](docs/features/paymentbad.png)

</details>

---

### 🛍️ Product Pages
- **Product List View**:
  - All coffee products displayed with name, image, price, and link to details.
- **Product Detail View**:
  - Includes image, detailed description, price, and "Add to Cart" button.
  - Users can leave comments after logging in.

<details><summary>☕ Screenshots</summary>

![Product List](docs/features/products.png)  
![Product Detail](docs/features/productdetails.png)

</details>

---

### 💬 Product Comments
- Authenticated users can:
  - Leave comments on product pages.
  - View all comments related to a product.
  - Delete their own comments.
  - Edit their own comment.
- Admin can manage all comments through the admin panel.

<details><summary>💬 Screenshots</summary>

![Comments](docs/features/comment.png)  
![Add Comment](docs/features/editcomment.png)
![Delete Comment](docs/features/deletecomment.png)


</details>

---

### 📦 Admin Features
- Admin panel access to:
  - Manage all products (create, update, delete).
  - Review and delete inappropriate comments.
  - Monitor cart items and order-related data (if stored).

<details><summary>🔐 Screenshots</summary>

![Admin Dashboard](docs/features/adminpanel.png)  

</details>

---


---

### 📧 Email Functionality
- SendGrid integration sends:
  - Account verification emails.
  - (Planned) Order confirmation emails after checkout.

<details><summary>📧 Screenshots</summary>

![Email Confirmation](docs/features/emailvali.png)

</details>

---

### ✨ Flash Messages
- Inform users of actions like login, logout, item added to cart, checkout success, etc.
- Shown using Django’s messages framework styled with Bootstrap alerts.

<details><summary>⚡ Screenshots</summary>

![Messages](docs/features/messages.png)

</details>

## 🧪 Manual Testing

---

### ✅ 1. User Story: Register an Account  
_As a user, I can register an account so that I can securely use the site._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|---------|---------------------|-------------------|
| Click on 'Sign Up' | Signup form appears | Works as expected |
| Fill out the form and submit | Account is created and confirmation email sent | Works as expected |



---

### ✅ 2. User Story: Browse Products  
_As a user, I can browse available products so I can choose what to buy._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|---------|---------------------|-------------------|
| Visit products page | All products are displayed with info | Works as expected |
| Click on product | Product detail page loads | Works as expected |



---

### ✅ 3. User Story: Add Product to Cart  
_As a user, I can add a product to my cart so I can buy it later._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|---------|---------------------|-------------------|
| Click 'Add to Cart' | Product is added and message shows | Works as expected |
| Check cart | Product is visible in cart | Works as expected |



---

### ✅ 4. User Story: Edit or Remove Items from Cart  
_As a user, I can update cart quantities or remove items._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|---------|---------------------|-------------------|
| Increase/decrease quantity | Cart total updates accordingly | Works as expected |
| Click remove | Product is deleted from cart | Works as expected |



---

### ✅ 5. User Story: Checkout with Stripe  
_As a user, I can checkout securely using Stripe._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|---------|---------------------|-------------------|
| Click 'Checkout' | Redirected to Stripe | Works as expected |
| Complete payment | Redirected to success page | Works as expected |



---

### ✅ 6. User Story: Add and Manage Product Comments  
_As a user, I can leave a comment and manage my own comments._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|---------|---------------------|-------------------|
| Submit a comment | Comment is visible under product | Works as expected |
| Edit or delete own comment | Changes appear or comment is removed | Works as expected |



---

### ✅ 7. User Story: Reset Password  
_As a user, I can request a password reset in case I forget it._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|----------|---------------------|-------------------|
| Click on 'Forgot password' | Password reset form appears | Works as expected |
| Enter registered email and submit | Reset email is sent with instructions | Works as expected |
| Follow link in email | Password reset form loads | Works as expected |
| Enter new password and confirm | Password updated and redirected to login | Works as expected |



---


### ✅ 8. User Story: Responsive Navigation  
_As a user, I can navigate the site easily on any device._

#### Test Cases

| **Step** | **Expected Result** | **Actual Result** |
|----------|---------------------|-------------------|
| Open website on mobile device | Navbar collapses into hamburger menu | Works as expected |
| Tap hamburger icon | Navigation links expand | Works as expected |
| Tap link | Navigation menu closes and page loads | Works as expected |



---

### Admin

### ✅ 9. Admin: Manage Products
_As an admin, I can manage products so that I can keep the product catalog up to date._

#### Test Cases

| **Step**                   | **Expected Result**                            | **Actual Result**      |
|---------------------------|------------------------------------------------|------------------------|
| Log in to admin panel     | Admin dashboard loads                          | Works as expected      |
| Navigate to products list | Products are listed with options to edit/delete | Works as expected      |
| Edit a product            | Product form loads with existing data          | Works as expected      |
| Delete a product          | Product is removed from the product list       | Works as expected      |



----

### ✅ 10. Admin Story: Manage Comments  
_As an admin, I can moderate user comments so that I can ensure community guidelines are followed._

#### Test Cases

| **Step**                       | **Expected Result**                                | **Actual Result**      |
|-------------------------------|----------------------------------------------------|------------------------|
| Log in to admin panel         | Admin dashboard loads                              | Works as expected      |
| Navigate to comments section  | All product comments are listed                    | Works as expected      |
| Delete inappropriate comment  | Comment is removed and no longer visible           | Works as expected      |


---

### ✅ 11. Admin Story: Manage Accounts and Order History  
_As an admin, I can view user accounts and order history so that I can assist users or resolve disputes._

#### Test Cases

| **Step**                        | **Expected Result**                              | **Actual Result**      |
|--------------------------------|--------------------------------------------------|------------------------|
| Log in to admin panel          | Admin dashboard loads                            | Works as expected      |
| View user list                 | All registered users are listed                  | Works as expected      |
| View order history for a user  | Orders for that user are shown                   | Works as expected      |


---

## 🧪 Testing
- Manual testing on Chrome, Firefox, Safari, mobile
- Validated HTML, CSS, and Python (PEP8)
- Lighthouse and WAVE accessibility tests

## ✔️ Validation

- HTML and CSS validated using **W3C Validator**.
- Python code checked with **PEP8 compliance**.
- JavaScript validated using **JSHint**.
- Accessibility tested using **Lighthouse** and **WAVE**.

### HTML Validation
The W3C Markup Validation Service was used to validate the HTML of the website. All pages pass with exept signup woch has some error in the allauth code. Ive been trying to fix it in diffrent ways, but did not end upp succesful.
<details><summary>Home</summary>
<img src="docs/html/homepage.png">
</details>
<details><summary>Products</summary>
<img src="docs/html/products.png">
<img src="docs/html/detailproduct.png">
<img src="docs/html/editcomment.png">
<img src="docs/html/deletecomment.png">

</details>
<details><summary>Cart</summary>
<img src="docs/html/cart.png">
</details>
<details><summary>Account</summary>
<img src="docs/html/login.png">
<img src="docs/html/logout.png">
<img src="docs/html/signup.png">
<img src="docs/html/emails.png">
<img src="docs/html/changepassword.png">

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.
The style.css file was approved.
<details><summary>style.css</summary>
<img src="docs/css/css.png">
</details>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>
<img src="docs/js/js.png">
</details><hr>

### PEP8 Validation
Python code checked with **PEP8 compliance**


### Accessibility
The WAVE WebAIM web accessibility evaluation tool was used to ensure the website met high accessibility standards. All pages pass with 0 errors.
<details><summary>Home</summary>
<img src="docs/access/home.png">
</details>
<details><summary>Products</summary>
<img src="docs/access/products.png">
<img src="docs/access/productdetail.png">
</details>
<details><summary>Cart</summary>
<img src="docs/access/cart.png">
</details>
<details><summary>Account</summary>
<img src="docs/access/login.png">
<img src="docs/access/logout.png">
<img src="docs/access/signup.png">
<img src="docs/access/email.png">
<img src="docs/access/password.png">

</details>


### Performance 
Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 

<details><summary>Home</summary>
<img src="docs/lighthouse/home.png">
</details>
<details><summary>Products</summary>
<img src="docs/lighthouse/products.png">
<img src="docs/lighthouse/detailproduct.png">
</details>
<details><summary>Cart</summary>
<img src="docs/lighthouse/cart.png">
</details>
<details><summary>Account</summary>
<img src="docs/lighthouse/login.png">
<img src="docs/lighthouse/logout.png">
<img src="docs/lighthouse/signup.png">
<img src="docs/lighthouse/mail.png">
<img src="docs/lighthouse/password.png">



---


---

## 🐞 Bugs

### Fixed
- Cart not clearing after checkout ➝ Fixed
- Email verification not blocking checkout ➝ Fixed

### Known
- Some iPhone SE responsiveness issues

---

## 🚀 Heroku Deployment



# 🚀 **Heroku Deployment Guide**

## 🌐 **Deploying Through the Heroku Website**
[🔗 **Official Heroku Git Deployment Guide**](https://devcenter.heroku.com/articles/git)  

This guide will walk you through deploying your application from GitHub using **Heroku**.

---

### 📝 **1. Create a Heroku Account & Log In**
1. Visit [**Heroku**](https://heroku.com) and sign up/log in.
2. Once logged in, navigate to your **dashboard**.

<details>
<summary>📸 Screenshots</summary>
<img src="docs/heroku/dash.png">
</details>

---

### 🚀 **2. Create a Heroku App**
1. Click on **"New"** to create an app.
2. Enter a unique app name (e.g., `doitms3`).
3. Choose a region that suits you.

<details>
<summary>📸 Screenshots</summary>
<img src="docs/heroku/dash.png">
<img src="docs/heroku/new.png">
<img src="docs/heroku/create.png">
</details>

---

### 🔧 **3. Configure Settings**

1. In your Heroku **Dashboard**, go to your app's **Settings** tab.
2. Scroll down to **Config Vars** and click **Reveal Config Vars**.
3. Add the following environment variables:

```bash
heroku config:set SECRET_KEY='your-django-secret-key'
heroku config:set DATABASE_URL='your-database-url'
heroku config:set STRIPE_PUBLIC_KEY='your-stripe-public-key'
heroku config:set STRIPE_SECRET_KEY='your-stripe-secret-key'
heroku config:set STRIPE_WEBHOOK_SECRET='your-stripe-webhook-secret'
heroku config:set EMAIL_HOST_USER='your-sendgrid-email@example.com'
heroku config:set EMAIL_HOST_PASSWORD='your-sendgrid-api-key'


<details>
<summary>📸 Screenshots</summary>
<img src="docs/heroku/dash.png">
<img src="docs/heroku/settings.png">
<img src="docs/heroku/config.png">
</details>

---

### 💻 **4. Prepare Your Code in VS Code**
1. Install **Gunicorn**:
   ```sh
   pip3 install gunicorn
   pip3 freeze > requirements.txt
   ```
2. Create a **Procfile** in the same directory as `manage.py` with the following content:
   ```
   web: gunicorn doit.wsgi
   ```

<details>
<summary>📸 Screenshot</summary>
<img src="docs/images/heroku/procfile.png">
</details>

3. Update **settings.py**:
   - Add `'.herokuapp.com'` to `ALLOWED_HOSTS`.
   - Set `DEBUG = False`.

<details>
<summary>📸 Screenshots</summary>
<img src="docs/images/heroku/allowedhost.png">
<img src="docs/images/heroku/false.png">
</details>

---

### 🗃️ **5. Run Migrations**
1. Check migration status:
   ```sh
   python3 manage.py showmigrations
   ```
2. Apply migrations:
   ```sh
   python3 manage.py migrate
   ```

---

### 🔗 **6. Connect to GitHub & Deploy**
1. Go to **Deploy** tab in Heroku.
2. Connect your **GitHub** repository.
3. Enable **automatic deploys** from the `main` branch (optional).
4. Click **Deploy**.

<details>
<summary>📸 Screenshots</summary>
<img src="docs/images/heroku/main2.png">
<img src="docs/images/heroku/github.png">
<img src="docs/images/heroku/deploy.png">
</details>

---

### ⚡ **7. Manage Dynos**
1. Check your **dynos**.
2. Make sure you are using the **ECO** plan.

<details>
<summary>📸 Screenshots</summary>
<img src="docs/images/heroku/main3.png">
<img src="docs/images/heroku/dynos.png">
</details>

---

### 🌍 **8. Access Your Application**
1. Click the provided **Heroku link** to access your app.
2. If you encounter issues, check **Heroku build logs** for troubleshooting.

---

## 📟 **Heroku Deployment via Terminal**
If you prefer the **command-line approach**, here’s how to deploy **CoffeHub**:

### 1️⃣ **Create a New Heroku App**
```bash
heroku create coffehub-app
```

### 2️⃣ **Set Environment Variables**
Make sure you set your secret keys and database config:
```bash
heroku config:set SECRET_KEY='your-django-secret-key'
heroku config:set DATABASE_URL='your-database-url'
heroku config:set EMAIL_HOST_USER='your-sendgrid-email'
heroku config:set EMAIL_HOST_PASSWORD='your-sendgrid-password'
heroku config:set STRIPE_PUBLIC_KEY='your-stripe-public-key'
heroku config:set STRIPE_SECRET_KEY='your-stripe-secret-key'
heroku config:set STRIPE_WH_SECRET='your-stripe-webhook-secret'
heroku config:set USE_AWS=True
```

### 3️⃣ **Push to Heroku**
Make sure your `main` branch is up-to-date, then push:
```bash
git push heroku main
```

### 4️⃣ **Run Migrations and Collect Static Files**
```bash
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
```

### 5️⃣ **Create Superuser (Optional but Recommended)**
```bash
heroku run python manage.py createsuperuser
```

### 6️⃣ **Restart App**
```bash
heroku restart
```

---

### 🎉 **Your App is Now Live on Heroku!**  
Click the link provided by **Heroku** to see your deployed application in action. 🚀

---

## 📜 Credits

### 📷 Images
- Placeholder images sourced from **ChatGpt**, edited with GIMP.

### 📌 Code
- Bootstrap templates used for styling.
- Django documentation used for authentication and static file handling.

---

## 💙 Acknowledgements
- Special thanks to **Mo Shami** for guidance.
- Inspired by **Django tutorials and online resources**.
- Thanks to **Code Institute** for support.

##### Back to [top](#table-of-contents)