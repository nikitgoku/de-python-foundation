-- Create database
CREATE DATABASE pizza_shop;

-- Create table
CREATE TABLE pizza_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    pizza_type VARCHAR(50),
    size VARCHAR(10),
    quantity INT,
    price NUMERIC(5,2),
    order_time TIMESTAMP,
    status VARCHAR(20)
);

INSERT INTO pizza_orders (customer_name, pizza_type, size, quantity, price, order_time, status) VALUES
('Alice', 'Margherita', 'Medium', 2, 8.50, '2025-12-08 12:15:00', 'Completed'),
('Bob', 'Pepperoni', 'Large', 1, 12.00, '2025-12-08 12:45:00', 'Completed'),
('Charlie', 'Veggie', 'Small', 3, 7.00, '2025-12-08 13:05:00', 'Pending'),
('David', 'BBQ Chicken', 'Large', 2, 13.50, '2025-12-08 13:30:00', 'Completed'),
('Eva', 'Hawaiian', 'Medium', 1, 9.00, '2025-12-08 14:00:00', 'Completed'),
('Frank', 'Margherita', 'Large', 4, 12.00, '2025-12-08 14:20:00', 'Completed'),
('Grace', 'Pepperoni', 'Medium', 2, 10.00, '2025-12-08 14:45:00', 'Completed'),
('Henry', 'Veggie', 'Small', 1, 7.00, '2025-12-08 15:00:00', 'Pending'),
('Ivy', 'BBQ Chicken', 'Large', 3, 13.50, '2025-12-08 15:20:00', 'Completed'),
('Jack', 'Hawaiian', 'Medium', 2, 9.00, '2025-12-08 15:45:00', 'Completed'),
('Kate', 'Margherita', 'Small', 1, 6.50, '2025-12-08 16:00:00', 'Completed'),
('Leo', 'Pepperoni', 'Large', 5, 12.00, '2025-12-08 16:20:00', 'Completed'),
('Mia', 'Veggie', 'Medium', 2, 8.50, '2025-12-08 16:45:00', 'Pending'),
('Nina', 'BBQ Chicken', 'Small', 1, 7.50, '2025-12-08 17:00:00', 'Completed'),
('Oscar', 'Hawaiian', 'Large', 2, 12.00, '2025-12-08 17:20:00', 'Completed'),
('Paul', 'Margherita', 'Medium', 3, 8.50, '2025-12-08 17:45:00', 'Completed'),
('Quinn', 'Pepperoni', 'Small', 2, 7.00, '2025-12-08 18:00:00', 'Pending'),
('Rita', 'Veggie', 'Large', 4, 11.00, '2025-12-08 18:20:00', 'Completed'),
('Sam', 'BBQ Chicken', 'Medium', 2, 10.00, '2025-12-08 18:45:00', 'Completed'),
('Tina', 'Hawaiian', 'Small', 1, 6.50, '2025-12-08 19:00:00', 'Completed'),
('Uma', 'Margherita', 'Large', 2, NULL, '2025-12-08 19:20:00', 'Completed'), -- Missing price
('Victor', 'Pepperoni', 'Medium', 3, 10.00, '2025-12-08 19:45:00', 'Completed'),
('Wendy', 'Veggie', 'Small', 2, 7.00, '2025-12-08 20:00:00', 'Pending'),
('Xavier', 'BBQ Chicken', 'Large', 1, 13.50, '2025-12-08 20:20:00', 'Completed'),
('Yara', 'Hawaiian', 'Medium', 2, 9.00, '2025-12-08 20:45:00', 'Completed');