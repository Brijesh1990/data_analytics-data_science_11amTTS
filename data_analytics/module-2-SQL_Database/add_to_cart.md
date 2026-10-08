# E-commerce SQL Case Study: Add to Cart and Order Analysis

## Case

An online store, **Ecommerce App Demo**, wants to understand how customers browse products, add items to their carts, and place orders. The store keeps product categories and subcategories, customer details, active cart items, and order line items in a relational database.

Use the tables below to answer the business questions with SQL. The examples use **MySQL** syntax. Assume that each row in `orders` represents one product line; rows with the same `order_id` belong to the same order.

## Database and tables

```sql
CREATE DATABASE ecommerce_app_demo;
USE ecommerce_app_demo;

CREATE TABLE category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE subcategory (
    subcategory_id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT NOT NULL,
    subcategory_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    subcategory_id INT NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    city VARCHAR(100),
    signup_date DATE NOT NULL
);

CREATE TABLE cart (
    cart_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    added_at DATETIME NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE orders (
    order_line_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    order_date DATETIME NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

## Business questions

Write a SQL query for each requirement:

1. List all active products with their current prices and stock quantities, sorted from highest to lowest price.

2. Find all customers who live in a specified city. Return each customer's full name and email.

3. Show each product with its subcategory and category name.

4. Find products priced between `$25` and `$100`, inclusive.

5. Count the number of products in each category, including categories that currently have no products.

6. Show the number of customers who signed up in each year.

7. List each customer's cart items with the product name, quantity, current unit price, and total cart-item value.

8. Find customers who have at least one item in their cart.

9. Find active products that have never been added to a cart.

10. Show the total quantity of each product currently in all carts, from greatest to least.

11. Calculate the total value of each customer's cart using the current product prices.

12. Find cart items that have been waiting for more than seven days.

13. For each customer, calculate the number of distinct orders they have placed. Count an order once even if it contains multiple product lines.

14. Calculate total revenue by product using only orders with a status of `delivered`. Use the recorded `unit_price` in `orders`, not the current product price.

15. Find the five best-selling products by delivered quantity.

16. Calculate monthly delivered revenue for the current calendar year.

17. Find customers who have placed at least one delivered order but have no items currently in their cart.

18. Update the status of a specified order to `cancelled`.

19. Remove a specified product from a customer's cart without deleting the customer or product.

20. Add a new product to the appropriate subcategory, then verify that it appears with the correct category name.

For questions 18–20, use appropriate `UPDATE`, `DELETE`, and `INSERT` statements. For the remaining questions, write `SELECT` queries. Use joins, aggregate functions, `GROUP BY`, `HAVING`, subqueries, and date functions where appropriate.
