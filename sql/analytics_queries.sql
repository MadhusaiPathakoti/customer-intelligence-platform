-- Top customers by revenue
SELECT c.customer_id, c.name, SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY revenue DESC;

-- Top selling products
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

-- Monthly revenue
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
SUM(total_amount) AS revenue
FROM orders
GROUP BY month;
